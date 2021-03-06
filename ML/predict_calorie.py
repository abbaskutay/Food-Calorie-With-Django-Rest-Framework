from collections import OrderedDict
import pandas as pd


def calorie(data, choice):
    dict_1 = data[data['food_category'].str.contains(choice, na=False)]
    a = dict_1.drop(columns=["Food_type", "Serving Weight (g)"])
    a.set_index('food_category', inplace=True)
    a.to_dict('dict')
    dict_2 = {}
    for i in a:
        for key in a[i]:
            dict_2[i] = key
    ordered_dict = OrderedDict()
    ordered_dict["carbohydrate"] = dict_2["Carbohydrate (g)"]
    ordered_dict["fat"] = dict_2["Fat (g)"]
    ordered_dict["protein"] = dict_2["Protein (g)"]
    ordered_dict["sugars"] = dict_2["Sugars (g)"]
    ordered_dict["calorie"] = dict_2["calorie (kcal)"]

    ordered_dict = dict(ordered_dict)

    print(ordered_dict)

    return ordered_dict



