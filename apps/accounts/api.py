from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import account_activation_token
from django.core.mail import EmailMessage, EmailMultiAlternatives
from rest_framework.exceptions import MethodNotAllowed
from apps.QLA.models import School as XS
from apps.QLA.models import Country

User = get_user_model()
emailfilterlist = settings.EMAIL_FILTER


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        country = Country.objects.get(id=request.data['Country'])
        y = XS.objects.get(id=request.data['School'])
        for x in emailfilterlist:
            x = x.lower()
            email_filter = request.data['email'].lower().find(x)
            if email_filter == -1:
                email = request.data['email']
                firstname = request.data['firstname']
                lastname = request.data['lastname']
                password = request.data['password']
                serializer = self.get_serializer(data=request.data)
                if not User.objects.filter(email=email):
                    if serializer.is_valid():
                        user = User.objects.create_user(email=email, firstname=firstname, lastname=lastname, School=y,
                                                        Country=country)
                        user.set_password(password)
                        user.is_active = False
                        user.save()
                        # Email function
                        current_site = get_current_site(request)
                        email_body = {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(user),
                        }
                        link = reverse('activate', kwargs={
                            'uidb64': email_body['uid'], 'token': email_body['token'],
                        })
                        # TODO:HTTPS in deployment
                        activate_url = 'http://' + current_site.domain + link
                        htmly = get_template('Email.html')
                        data = {'firstname': firstname, 'lastname': lastname, 'activate_url': activate_url}
                        subject, from_email, to = 'Welcome Dear' + " " + firstname.capitalize() + " " + lastname.capitalize() + " " + "Please Activate your account", 'your_email@gmail.com', email
                        html_content = htmly.render(data)
                        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        return Response({
                            "message": "Please Check your Email and Activate Account"
                        }, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                else:
                    error_message = "Account Already Exist"
                    return Response(
                        {"message": error_message}, status=status.HTTP_403_FORBIDDEN
                    )
            else:
                error_message = "Domain not Allowed"
                return Response(
                    {"message": error_message}, status=status.HTTP_403_FORBIDDEN
                )


class LoginAPI(generics.GenericAPIView):
    serializer_class = loginSerializer
    def post(self, request, *args, **kwargs):
        print(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializers(user, context=self.get_serializer_context()).data,
            "token": token
        })


class UpdateUserAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpdateSerializers

    def get_queryset(self):
        queryset = User.objects.filter(id=self.kwargs['pk'])
        return queryset


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializers

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePassword
    model = User

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': 'Wrong Password'},
                                status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'message': 'Password Updated Successfully'
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
