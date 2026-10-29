"""
Emotion Detection Module using Watson NLP Library.
"""
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the input text using Watson NLP Emotion Predict service
    and returns a dictionary with emotion scores and the dominant emotion.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    try:
        formatted_response = response.json()
        if 'emotionPredictions' in formatted_response and formatted_response['emotionPredictions']:
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
            return {
                'anger': emotions.get('anger'),
                'disgust': emotions.get('disgust'),
                'fear': emotions.get('fear'),
                'joy': emotions.get('joy'),
                'sadness': emotions.get('sadness'),
                'dominant_emotion': dominant_emotion
            }
    except (ValueError, KeyError, IndexError):
        pass

    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
