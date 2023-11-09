from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()

class GifUrlSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=['DAB', 'JESSE_DANCE', 'JUMPING_JACKS', 'JUMPING', 'WAVE_HELLO'])
    url = serializers.URLField()

class ResponseSerializer(serializers.Serializer):
    gif_urls = GifUrlSerializer(many=True)
