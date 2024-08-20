from rest_framework import serializers
from .models import CategoryRating, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(
        choices=CategoryRating.choices,
        default=CategoryRating.G
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.CharField(source='user.email', read_only=True)


    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        return Movie.objects.create(user=user, **validated_data)