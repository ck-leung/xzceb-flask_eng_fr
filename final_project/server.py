from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/englishToFrench")
def english_to_french_route():
    """
    Translates English text to French using the machinetranslation package
    """
    english_text = request.args.get('textToTranslate', '').strip()
    if not english_text:
        return "Error: No text to translate"
    else:
        french_text = english_to_french(english_text)
        return french_text


@app.route("/frenchToEnglish")
def french_to_english_route():
    """
    Translates French text to English using the machine_translation package
    """
    french_text = request.args.get('textToTranslate', '').strip()
    if not french_text:
        return "Error: No text to translate"
    else:
        english_text = french_to_english(french_text)
        return english_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
