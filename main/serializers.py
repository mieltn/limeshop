from rest_framework import serializers
from .models import Category, Cuisine, Recipe, Ingredient, Basket
from .fields import CategoryRelatedField, IngredientRelatedField, CuisineRelatedField


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')


class CuisineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuisine
        fields = ('__all__')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('__all__')


class RecipeSerializer(serializers.ModelSerializer):
    category = CategoryRelatedField(queryset=Category.objects.all())
    cuisine = CuisineRelatedField(queryset=Cuisine.objects.all())
    ingredients = IngredientRelatedField(queryset=Ingredient.objects.all(), required=False)

    class Meta:
        model = Recipe
        fields = ('name', 'description', 'category', 'cuisine', 'ingredients')
        

class RecipeReadSerializer(RecipeSerializer):
    category = serializers.StringRelatedField()
    cuisine = serializers.StringRelatedField()
    ingredients = serializers.StringRelatedField(many=True)


class BasketSerializer(serializers.ModelSerializer):

    ingredient = IngredientRelatedField(queryset=Ingredient.objects.all())

    class Meta:
        model = Basket
        fields = ('ingredient', 'user')

    


# class BasketSerializer(serializers.ModelSerializer):
    # ingredients = IngredientRelatedField(queryset=Ingredient.objects.all(), required=False)
    # total = serializers.DecimalField(decimal_places=2, max_digits=10, required=False)

    # class Meta:
    #     model = Basket
    #     fields = ('id', 'ingredients', 'total')

    # def create(self, validated_data):
    #     ingredients = validated_data.pop('ingredients')
    #     newBasket = Basket.objects.create(**validated_data)
    #     for ingredient in ingredients:
    #         newBasket.add_ingredient(ingredient)
    #     newBasket.total = newBasket.get_total()
    #     newBasket.save()
    #     return newBasket


# class BasketReadSerializer(BasketSerializer):
#     ingredients = serializers.StringRelatedField(many=True)
