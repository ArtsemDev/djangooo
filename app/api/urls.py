from django.urls import path

from .views import RegistrationApiView, CustomViewSet


urlpatterns = [
    path("registration/", RegistrationApiView.as_view({"post": "post"})),
    path("profile/", CustomViewSet.as_view({"get": "get"})),
]
