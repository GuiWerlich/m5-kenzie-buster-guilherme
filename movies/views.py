from rest_framework.views import APIView, Response, status
from .persmissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.pagination import PageNumberPagination

class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MovieSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        movie = serializer.save()
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def get(self, request, movie_id=None):
        if movie_id != None:
            found_movie = Movie.objects.filter(id=movie_id)
            if not found_movie.exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            movies = Movie.objects.all()
            result_page = self.paginate_queryset(movies, request, view=self)
            serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


    def delete (self, request, movie_id):

        found_movie = Movie.objects.filter(id=movie_id)
        if not found_movie.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        movie = Movie.objects.get(id=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        

