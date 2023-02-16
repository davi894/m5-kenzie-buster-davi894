from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .pemissions import UserPermission, UserEmployeeVerify
from rest_framework.views import APIView, status
from .serializers import CustomJWTSerializer
from rest_framework.response import Response
from .serializers import UserSerializer
from django.shortcuts import render
from .models import User
import json
import ipdb

# Create your views here.


class LoginView(TokenObtainPairView):
    serializer = CustomJWTSerializer


class UserView(APIView):
    def post(self, req):
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserViewId(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserEmployeeVerify]

    def get(self, req, user_id):

        user = User.objects.get(id=user_id)
        self.check_object_permissions(req, user)
        data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "birthdate": user.birthdate,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_employee": user.is_employee,
            "is_superuser": user.is_superuser,
        }

        return Response(data, status.HTTP_200_OK)

    def patch(self, req, user_id):

        user = User.objects.get(id=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(user, req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
