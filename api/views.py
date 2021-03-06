from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImageSerializer, DetailFromReactSeri, ValueFromMlSeri
from .models import ImageModel, DetailFromReact, ValueFromMl
import pandas as pd
from ML.predict_image import *
from ML.predict_calorie import calorie
from ML.weight_food import weight

data = pd.read_csv("ML/final.csv")


@api_view(['POST'])
def image_response(request):
    serializer = ImageSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_main(request):
    if request.method == 'GET':
        result = ImageModel.objects.last()
        serializer = ImageSerializer(result)
        path_image = serializer.data['photo']
        print(path_image)
        images = [path_image]
        pred_classes = predict_class(model_best, 3, images, True)

        response = Response(pred_classes, status=status.HTTP_200_OK)
        print(pred_classes)

        return response


@api_view(['POST'])
def post_main(request):
    serializer = DetailFromReactSeri(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_sub(request):
    one = DetailFromReact.objects.last()
    serializer = DetailFromReactSeri(one)

    choice = serializer.data['main_food']

    new_df = data[data['Food_type'].str.contains(choice, na=False)]

    sub_food = new_df["food_category"].to_list()

    response = Response(sub_food, status=status.HTTP_200_OK)
    print(sub_food)

    return response


@api_view(['GET'])
def get_weight(request):
    one = DetailFromReact.objects.last()
    serializer = DetailFromReactSeri(one)

    choice = serializer.data['main_food']

    new_df = data[data['food_category'].str.contains(choice, na=False)]

    sub_food = new_df["food_category"].to_list()

    weight_food = weight(data, sub_food)

    response = Response(weight_food, status=status.HTTP_200_OK)

    return response


@api_view(['PUT'])
def put_sub(request):
    one = DetailFromReact.objects.last()
    serializer = DetailFromReactSeri(one, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_calorie(request):
    one = DetailFromReact.objects.last()
    serializer = DetailFromReactSeri(one)

    choice = serializer.data['sub_food']
    print(type(choice))

    result = calorie(data, choice)

    return Response(result, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def post_calorie(request):
    serializer = ValueFromMlSeri(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
