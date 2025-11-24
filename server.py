from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return jsonify('Invalid text! Please try again!')
    
    response = emotion_detector(text_to_analyse)

    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)