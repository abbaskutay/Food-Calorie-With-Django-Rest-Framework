from django.db import models

from PIL import Image
# Create your models here.


class ImageModel(models.Model):

    photo = models.ImageField(upload_to='images')


class DetailFromReact(models.Model):
    idOfFood = models.OneToOneField(
        ImageModel,
        on_delete=models.CASCADE,
        primary_key=True,
        db_constraint=False,


    )

    main_food = models.CharField(max_length=32)
    sub_food = models.CharField(max_length=32,null=True,blank=True)


class ValueFromMl(models.Model):
    idOfImage = models.OneToOneField(
        DetailFromReact,
        on_delete=models.CASCADE,
        primary_key=True,
        db_constraint=False,
    )
    carbohydrate = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    sugars = models.FloatField()
    calorie = models.FloatField()

"""
{'Carbohydrate (g)': 21.0,
 'Fat (g)': 4.0,
 'Protein (g)': '2',
 'Sugars (g)': 1.0,
 'calorie (kcal)': 130.0}
"""