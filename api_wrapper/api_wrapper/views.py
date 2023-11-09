from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageUploadSerializer, ResponseSerializer

class AnimateDrawingView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            
            # Process image to generate GIF URLs

            response_data = {
                'gif_urls': [
                    {'type': 'DAB', 'url': 'http://example.com/dab.gif'},
                    {'type': 'JESSE_DANCE', 'url': 'http://example.com/dab.gif'},
                    {'type': 'JUMPING_JACKS', 'url': 'http://example.com/dab.gif'},
                    {'type': 'JUMPING', 'url': 'http://example.com/dab.gif'},
                    {'type': 'WAVE_HELLO', 'url': 'http://example.com/dab.gif'},
                ]
            }
            response_serializer = ResponseSerializer(data=response_data)
            if response_serializer.is_valid():
                return Response(response_serializer.data)
            return Response(response_serializer.errors, status=400)
        return Response(serializer.errors, status=400)
