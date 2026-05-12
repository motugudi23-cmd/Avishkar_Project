from flask import Flask, render_template, request, jsonify
import os
from gtts import gTTS
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Ensure the static folder exists for audio files
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    # 1. Handle File Upload
    file = request.files['image']
    lang = request.form.get('language', 'en')
    
    # 2. Mock AI Logic (Replace this with your OpenCV/YOLO model)
    
    violation_text = "No Helmet Detected. Please wear a helmet for your safety."
    fine_amount = 500
    
    # 3. Translation Logic
    translated = translator.translate(violation_text, dest=lang)
    translated_text = translated.text
    
    # 4. Text-to-Speech Logic
    tts = gTTS(text=translated_text, lang=lang)
    audio_path = "static/announcement.mp3"
    tts.save(audio_path)
    
    return jsonify({
        "violation": translated_text,
        "fine": fine_amount,
        "audio_url": audio_path
    })

if __name__ == '__main__':
    app.run(debug=True)