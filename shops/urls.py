from django.urls import path
from .views import customer, shop, vespa,  object_predict, upload_image
urlpatterns = [
    path('', vespa, name='vespa'),
    path('shop/',  shop, name="shop"),
    path('customer/', customer, name="customer"),
    path('upload-image/', upload_image, name="upload_image"),
    path('predict/',  object_predict, name="predict")
]