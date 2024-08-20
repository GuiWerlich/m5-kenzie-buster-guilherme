from rest_framework import serializers
from .models import Movie, MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source='movie.title', read_only=True)
    purchased_by = serializers.EmailField(source='user.email', read_only=True)
    purchased_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data):
        movie_id = self.context['view'].kwargs['movie_id']

        found_movie = Movie.objects.filter(id=movie_id)
        if not found_movie.exists():
            return False
        
        movie = Movie.objects.get(id=movie_id)
        
        user = self.context['request'].user

        movie_order = MovieOrder.objects.create(movie=movie, user=user, **validated_data)

        return movie_order
