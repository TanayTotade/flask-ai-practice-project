import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        
    emotion_data = formatted_response["emotionPredictions"][0]["emotion"]

    anger = emotion_data["anger"]
    disgust = emotion_data["disgust"]
    fear = emotion_data["fear"]
    joy = emotion_data["joy"]
    sadness = emotion_data["sadness"]

    scores = emotion_data
    dominant_emotion = max(scores, key=scores.get)

    result = (
        f"For the given statement, the system response is "
        f"'anger' : {anger}, 'disgust' : {disgust}, 'fear' : {fear}, "
        f"'joy' : {joy} and 'sadness' : {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result 