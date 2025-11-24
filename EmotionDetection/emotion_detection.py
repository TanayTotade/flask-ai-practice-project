import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_data = formatted_response["emotionPredictions"][0]["emotion"]

    anger_score = emotion_data["anger"]
    disgust_score = emotion_data["disgust"]
    fear_score = emotion_data["fear"]
    joy_score = emotion_data["joy"]
    sadness_score = emotion_data["sadness"]

    scores = emotion_data
    dominant_emotion = max(scores, key=scores.get)
    emotion_value = scores[dominant_emotion]

    return "The given text has the emotion '{}' with a score of {}.".format(dominant_emotion, emotion_value)  