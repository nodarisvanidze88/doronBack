
from django.urls import path
from rest_framework import routers
from .views import DynamicModelViewSet,DynamicModelView

router = routers.DefaultRouter()
router.register(r'dynamic_models', DynamicModelViewSet, basename='dynamic_models')
urlpatterns = [
    path('dynamic/', DynamicModelView.as_view(), name='dynamic_model_create'),
] + router.urls