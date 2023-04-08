"""
This module provides functions to translate text between English and French
using the IBM Watson Language Translator API
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('apikey')
URL = os.getenv('url')


def english_to_french(english_text):
    """
    Translates English text to French using IBM Watson Language Translator API
    """
    if not english_text:
        return "Error: No text to translate"
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
    if not french_text:
        return "Error: No text to translate"
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
