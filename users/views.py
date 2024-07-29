from rest_framework.views import APIView, Response, status
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        serializer = UserSerializer(user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

