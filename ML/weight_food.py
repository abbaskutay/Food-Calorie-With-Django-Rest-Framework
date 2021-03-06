

def weight(data, subfood):
    weight_list = []
    for choice in subfood:
        dict_1 = data[data['food_category'].str.contains(choice, na=False)]
        dict_1.set_index('food_category', inplace=True)
        a = dict_1.drop(
            columns=["Food_type", "Carbohydrate (g)", "Fat (g)", "Protein (g)", "Sugars (g)", "calorie (kcal)"])
        a.to_dict('dict')
        dict_2 = {}
        for i in a:
            for key in a[i]:
                dict_2[i] = key

            weight_list.append((dict_2["Serving Weight (g)"]))

    return weight_list
