from random import choice

import clarifai
from clarifai.rest import ClarifaiApp

import settings


def is_cat(file_name):
    image_has_cat = False
    try:
        app = ClarifaiApp(api_key=settings.CLARIFAI_API)
        model = app.public_models.general_model
        response = model.predict_by_filename(file_name, max_concepts=200)
        if response['status']['code'] == 10000:
            for concept in response['outputs'][0]['data']['concepts']:
                if concept['name'] == 'cat':
                    print(concept['value'])
                    image_has_cat = True
    except clarifai.errors.ApiError as e:
        print('Ошибка опять')
    return image_has_cat


if __name__ == '__main__':
    print(is_cat('images/catwoman.jpg'))
