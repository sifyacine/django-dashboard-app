from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from param.models import School
from param.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            school = serializer.save()
            # Get the URL of the uploaded logo
            logo_url = request.build_absolute_uri(school.logo.url)
            # Include the logo URL in the response data
            response_data = serializer.data
            response_data['logo'] = logo_url
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
