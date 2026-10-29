"""
Flask server for Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Endpoint to analyze emotion from user text.
    Extracts text from query parameters, calls emotion_detector,
    and returns a formatted string response.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the index.html page for user interaction.
    Supports optional text query parameter for initial state rendering.
    """
    text_to_analyze = request.args.get('text')
    initial_response = None
    if text_to_analyze is not None:
        if text_to_analyze == "":
            initial_response = "Invalid text! Please try again!"
        else:
            resp = emotion_detector(text_to_analyze)
            if resp.get('dominant_emotion') is None:
                initial_response = "Invalid text! Please try again!"
            else:
                initial_response = (
                    f"For the given statement, the system response is "
                    f"'anger': {resp['anger']}, 'disgust': {resp['disgust']}, "
                    f"'fear': {resp['fear']}, 'joy': {resp['joy']} and "
                    f"'sadness': {resp['sadness']}. "
                    f"The dominant emotion is {resp['dominant_emotion']}."
                )
    return render_template(
        'index.html',
        initial_text=text_to_analyze,
        initial_response=initial_response
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
