import logging
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
                    logging.info(concept['value'])
                    image_has_cat = True
        else:
            print(response['status']['code'])
    except clarifai.errors.ApiError:
        logging.info('clarifai.errors.ApiError')
    return image_has_cat
