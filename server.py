"""Flask server for the emotion detection application."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the text received from the web interface."""
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )


@app.route("/")
def render_index_page():
    """Render the application's main page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)