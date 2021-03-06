from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

from ML.food_list import food_list

model_best = load_model('ML/model_trained_101class_v1.hdf5', compile=False)


def predict_class(model, n, images, show=True):
    for img in images:
        img = image.load_img(img, target_size=(299, 299))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img /= 255.

        pred_list = []
        pred = model.predict(img)
        pred = np.argsort(pred, axis=1)[:, -n:]
        food_list.sort()
        for p in pred:
            for index in p:
                pred_value = food_list[index]
                pred_list.append(pred_value)
        return pred_list


