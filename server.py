"""
Flask server for the Emotion Detector application.
Provides web routes for emotion analysis.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint that receives user text through query parameters
    and returns emotion analysis results.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return jsonify('Invalid text! Please try again!')

    response = emotion_detector(text_to_analyse)

    return response

@app.route("/")
def render_index_page():
    """
    Renders the main HTML page for the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
