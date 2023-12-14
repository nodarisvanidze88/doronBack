from django.apps import apps
from django.db import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import DynamicModel
from .serializers import DynamicModelSerializer

class DynamicModelView(APIView):
    def post(self, request):
        model = request.data.get('model')
        fields = request.data.get('fields', [])

        attrs = {'__module__': 'tablecreator.models'}
        for field in fields:
            attrs[field['name']] = models.CharField(max_length=255, default=field['default'])

        dynamic_model = type(model, (DynamicModel,), attrs)

        # Register the dynamic model with Django
        apps.all_models['tablecreator'][model] = dynamic_model

        return Response({'message': f'Dynamic model {model} created successfully'}, status=status.HTTP_201_CREATED)
    
class DynamicModelViewSet(viewsets.ModelViewSet):
    queryset = DynamicModel.objects.all()
    serializer_class = DynamicModelSerializer