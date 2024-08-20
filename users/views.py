from rest_framework.views import APIView, Response, status
from rest_framework.generics import get_object_or_404
from .serializers import UserSerializer, CustomJWTSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrEmployee
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User

class UserView(APIView):
    permission_classes = [IsOwnerOrEmployee]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        self.permission_classes = []
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, user_id):

        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, user_id):

        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
