from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

def payment_view(request):
    paypal_dict = {
        "business": "your-paypal-business-email@example.com",
        "amount": "10.00",
        "item_name": "Example Item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri('/paypal-ipn/'),
        "return_url": request.build_absolute_uri('/payment-success/'),
        "cancel_return": request.build_absolute_uri('/payment-cancelled/'),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "payment.html", {"form": form})


def payment_success(request):
    return render(request, "success.html")

def payment_cancelled(request):
    return render(request, "cancelled.html")