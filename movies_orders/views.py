from rest_framework.views import APIView, Response, status
from .serializers import MovieOrderSerializer
from .permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        serializer = MovieOrderSerializer(data=request.data, context={'view': self, 'request': request})
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        order = serializer.save()

        if not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)