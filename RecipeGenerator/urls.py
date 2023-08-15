from django.urls import path
from .views import RecipeGeneratorAPIView

app_name = 'RecipeGenerator'

urlpatterns = [
    path('recipe-generator/', RecipeGeneratorAPIView.as_view(), name='recipe-generator'),
]
