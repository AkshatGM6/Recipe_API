# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import MySerializer
# from .recipe_generator_func import recipe_generator

# class RecipeGeneratorAPIView(APIView):
#     def post(self, request, format=None):
#         serializer = MySerializer(data=request.data)
#         if serializer.is_valid():
#             preferred_ingredients = serializer.validated_data['preferred_ingredients']
#             result = recipe_generator(preferred_ingredients)
#             return Response(result, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MySerializer
from .recipe_generator_func import recipe_generator  # Import your recipe_generator function

class RecipeGeneratorAPIView(APIView):
    def post(self, request, format=None):
        serializer = MySerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.validated_data
            serialized_str = "\n".join([f"{field}: {value}" for field, value in serialized_data.items()])
            
            result = recipe_generator(serialized_str)
            print(result)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
