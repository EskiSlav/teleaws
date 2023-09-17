from __future__ import annotations

import logging

import boto3

logger = logging.getLogger(__name__)


class Translator:
    def __init__(self) -> None:
        self.translate = boto3.client(
            service_name='translate', region_name='eu-west-2',
        )
        logger.info('Translate is initialized')

    def translate_text(self, text, from_lang='en', to_lang='uk'):
        logger.debug(f"Translating {from_lang=} {to_lang=} text: {text}")
        result = self.translate.translate_text(
            Text=text, SourceLanguageCode=from_lang,
            TargetLanguageCode=to_lang,
        )
        logger.debug(f"Translated text: {result.get('TranslatedText')}")
        return result.get('TranslatedText')
