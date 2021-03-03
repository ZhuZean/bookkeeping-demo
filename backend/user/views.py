from django.shortcuts import render
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework import mixins, viewsets, status
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from user.serializers import UserRegisterSerializer

User = get_user_model()


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Bill endpoint to get the list of bills (current month)
    """
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        # serializer and validate data, raise Exception if invalid
        req_serializer = self.get_serializer(data=request.data)
        req_serializer.is_valid(raise_exception=True)
        user = self.perform_create(req_serializer)

        payload = jwt_payload_handler(user)
        response = {
            'token': jwt_encode_handler(payload),
            'username': user.username
        }

        return Response(response, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()
