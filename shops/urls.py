from django.urls import path
from .views import customer, shop, vespa
urlpatterns = [
    path('', vespa, name='vespa'),
    path('shop/',  shop, name="shop"),
    path('customer/', customer, name="customer")
]