from flask import Flask, request, jsonify, render_template
import json
import os
from machinetranslation import translator

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('index.html')

@app.post('/englishToFrench')
def english_to_french():
    '''
    This function translates english to french
    '''
    text = request.get_json()['text']
    return jsonify(translator.english_to_french(text))

@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english():
    '''
    This function translates french to english
    '''
    text = request.get_json()['text']
    return jsonify(translator.french_to_english(text))

if __name__ == "__main__":
    app.run(debug=True)