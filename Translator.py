from transformers import pipeline

translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-mul-en")

translator('Девочки, страдаю от учебы!!!!!')