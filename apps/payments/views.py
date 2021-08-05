import stripe

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from apps.Subscription.models import Subscription
from django.contrib.auth import get_user_model

from apps.bundle.models import Bundle
from apps.QLA.models import School, Subject

User = get_user_model()

stripe.api_key = 'sk_test_51J8lHoGGgwsNAb9x7KYjVcuJ2qitfv5kS8fDTiPuesRTtP1dQffkDKdJ8oBN221dezBWlt1M4nUcLx2n5fsGQ5PX00BRUWcVEK'  # your real key will be much longer


@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1000,
        currency='GBP',
        payment_method_types=['card'],
        receipt_email='test@example.com',
    )

    return Response(status=status.HTTP_200_OK, data=test_payment_intent)


@api_view(['POST'])
def confirm_payment_intent(request):
    data = request.data
    payment_intent_id = data['payment_intent_id']

    stripe.PaymentIntent.confirm(payment_intent_id)

    return Response(status=status.HTTP_200_OK, data={"message": "Success"})


@api_view(['POST'])
def save_stripe_info(request):
    print(request.data)
    global extra_msg
    data = request.data
    price = data['x']['Price']
    price = price * 100
    email = data['x']['email']
    user_here = data['x']['user']
    user = User.objects.get(pk=user_here)
    firstName = data['x']['firstName']
    lastName = data['x']['lastName']
    phone = data['x']['phone']
    PackageID_here = data['x']['PackageID']
    PackageID = Bundle.objects.get(pk=PackageID_here)
    payment_method_id = data['payment_method_id']
    checkout = data['x']['checkout']
    Citi_data = data['x']['Citi_data']
    Country_state = data['x']['Country_state']
    stateName = data['x']['stateName']
    School_here = data['x']['School']
    School_data = School.objects.get(pk=School_here)
    Subject_here = data['x']['Subject']
    Subject_data = Subject.objects.get(pk=Subject_here)

    # checking if customer with provided email already exists
    customer_data = stripe.Customer.list(email=email).data
    if len(customer_data) == 0:
        # creating customer
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
    else:
        customer = customer_data[0]
        extra_msg = "Customer already existed."

    # creating paymentIntent

    stripe.PaymentIntent.create(customer=customer,
                                payment_method=payment_method_id,
                                currency='GBP', amount=price,
                                confirm=True)
    Subscription.objects.create(
        user=user,
        firstName=firstName,
        lastName=lastName,
        email=email,
        phone=phone,
        Country_state=Country_state,
        stateName=stateName,
        Citi_data=Citi_data,
        Price=data['x']['Price'],
        Transaction_ID=payment_method_id,
        bundle=PackageID,
        Subject=Subject_data,
        School=School_data,
        PaymentMethod=checkout,
    )
    return Response(status=status.HTTP_200_OK,
                    data={'message': 'Success', 'data': {'customer_id': customer.id}})
