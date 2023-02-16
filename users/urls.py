from .views import UserView, LoginView, UserViewId
from django.urls import path


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", LoginView.as_view()),
    path("users/<int:user_id>/", UserViewId.as_view()),
]