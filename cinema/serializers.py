from django.template.context_processors import request
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Movie


class CinemaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
