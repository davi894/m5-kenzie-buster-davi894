from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Movie, MovieChoices, MovieOrder
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(required=False)
    duration = serializers.CharField(max_length=10)
    rating = serializers.ChoiceField(
        choices=MovieChoices.choices,
        default=MovieChoices.G,
    )
    duration = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, dict):
        return dict.user.email

    def create(self, validated_data):

        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, dict):
        return dict.movie.title

    def get_buyed_by(self, dict):
        return dict.user_movie.email

    def create(self, validated_date):

        return MovieOrder.objects.create(**validated_date)
