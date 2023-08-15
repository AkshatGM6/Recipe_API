# from rest_framework import serializers

# class MySerializer(serializers.Serializer):
#     preferred_ingredients = serializers.CharField(max_length=500)



from rest_framework import serializers

class MySerializer(serializers.Serializer):
    preferred_ingredients = serializers.CharField(max_length=500)
    calorie_limit = serializers.IntegerField()
    allergic_ingredients = serializers.CharField(max_length=500)
    meal_type = serializers.CharField(max_length=20)
    cooking_time = serializers.IntegerField()
    serving_size = serializers.IntegerField()
    dietary_preference = serializers.CharField(max_length=20)
    nutrition_needs = serializers.CharField(max_length=20)
    cuisine_type = serializers.CharField(max_length=20)
    skill_level = serializers.CharField(max_length=20)
    # Add more fields as needed
