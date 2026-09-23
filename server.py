"""Flask server for the emotion detection application."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector


APP = Flask(__name__)


@APP.route("/emotionDetector")
def detect_emotion():
    """Analyze text received from the web interface."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        "The dominant emotion is "
        f"<b>{result['dominant_emotion']}</b>."
    )


@APP.route("/")
def render_index_page():
    """Render the application's main page."""
    return render_template("index.html")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
