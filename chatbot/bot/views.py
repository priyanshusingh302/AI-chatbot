# views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StringInputSerializer

@api_view(['POST'])
def remove_spaces(request):
    if request.method == 'POST':
        serializer = StringInputSerializer(data=request.data)
        if serializer.is_valid():
            input_string = serializer.validated_data['promt']
            processed_string = input_string.replace(' ', '')
            return Response({'response': processed_string}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
