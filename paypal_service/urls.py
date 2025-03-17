from django.urls import path, include
from . import views

urlpatterns = [
    path('paypal-ipn/', include('paypal.standard.ipn.urls')),
    path('payment/', views.payment_view, name='payment'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-cancelled/', views.payment_cancelled, name='payment-cancelled'),
]