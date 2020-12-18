import tensorflow
import keras
import numpy as np
import tensorflow.keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#from tensorflow.keras.models import load_model
from tensorflow.keras import layers
from PIL import Image
from skimage import transform


class Olga:
    def __init__(self):
        self.path_to_model = 'C:\\AllMemes\\model_meme_predict.h5'
        self.model = tensorflow.keras.models.load_model(self.path_to_model)

    def predict_for_one(self, path_to_picture):
        """
        Мем или не мем для одной пикчи
        Если не мем - False
        Если мем - True
        """
        my_image = self.load(path_to_picture)
        my_prediction = self.model.predict(my_image)
        if my_prediction[0][0] > my_prediction[0][1]:
            return False
        else:
            return True

    def predict_for_some(self, count):
        """
        Мем или не мем для некоторого count мемов.
        Пока не понятно как брать названия этих мемов,
        поэтому оставляю заглушку
        :param count:
        :return:
        """
        pass

    def load(self, name):
        """
        Приведение одной фотографии для нейронки в удобоворимый для нейронки
        """
        np_image = Image.open(name)
        np_image = np.array(np_image).astype('float32') / 255
        np_image = transform.resize(np_image, (150, 150, 3))
        np_image = np.expand_dims(np_image, axis=0)
        return np_image

if __name__ == '__main__':
    my_path = 'dobriememes/photo_2560/0.jpg'
    my_predict = Olga()
    my_predict.predict_for_one(my_predict)

