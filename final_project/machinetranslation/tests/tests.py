import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('apikey')
URL = os.getenv('url')

def english_to_french(english_text):
    """
    Translates English text to French using IBM Watson Language Translator API
    """
    if english_text is None:
        return None
    else:
        authenticator = IAMAuthenticator(API_KEY)
        translator = LanguageTranslatorV3(
            version='2021-09-01',
            authenticator=authenticator
        )
        translator.set_service_url(URL)

        translation = translator.translate(
            text=english_text,
            source='en',
            target='fr'
        ).get_result()

        french_text = translation['translations'][0]['translation']
        return french_text

def french_to_english(french_text):
    """
    Translates French text to English using IBM Watson Language Translator API
    """
    if french_text is None:
        return None
    else:
        authenticator = IAMAuthenticator(API_KEY)
        translator = LanguageTranslatorV3(
            version='2021-09-01',
            authenticator=authenticator
        )
        translator.set_service_url(URL)

        translation = translator.translate(
            text=french_text,
            source='fr',
            target='en'
        ).get_result()

        english_text = translation['translations'][0]['translation']
        return english_text
