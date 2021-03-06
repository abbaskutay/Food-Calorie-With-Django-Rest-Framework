from rest_framework import serializers

from .models import ImageModel, DetailFromReact, ValueFromMl


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel

        fields = "__all__"



class DetailFromReactSeri(serializers.ModelSerializer):
    class Meta:
        model = DetailFromReact

        fields = ('main_food', 'sub_food',)


class ValueFromMlSeri(serializers.ModelSerializer):
    class Meta:
        model = ValueFromMl
        fields = ('carbohydrate', 'fat', 'protein', 'sugars', 'calorie',)

