from django.shortcuts import render, redirect
from django.views import View
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.contrib.auth import get_user_model
from .utils import account_activation_token

User = get_user_model()


# Create your views here.
class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login' + '?message=', 'User Already activated, Please login')

            if user.is_active:
                return redirect('Account Activated!')
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated Successfully')
            return redirect('AccountSuccess')
        except Exception as ex:
            return redirect('AccountSuccess')


def ActivateAccount(request):
    return render(request, 'activateAccount.html')
