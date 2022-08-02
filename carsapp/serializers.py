from .models import Cars, Callback
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    shots = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='image'
    )

    class Meta:
        model = Cars
        fields = ["title", "description", "image", "amount", "shots"]


class CallbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Callback
        fields = ["name", "email", "message"]
