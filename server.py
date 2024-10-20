"""
This module provides a Flask-based web application for emotion detection.
It includes endpoints for analyzing emotions in a given text and rendering an index page.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_analyser():
    """Analyzes the emotion in the provided text."""
    text_to_analyse = request.args.get('textToAnalyze')
    results_of_analysis = emotion_detector(text_to_analyse)

    if not results_of_analysis or not results_of_analysis.get('dominant_emotion'):
        return "Invalid input! Try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {results_of_analysis['anger']}, "
        f"'disgust': {results_of_analysis['disgust']}, "
        f"'fear': {results_of_analysis['fear']}, "
        f"'joy': {results_of_analysis['joy']}, "
        f"and 'sadness': {results_of_analysis['sadness']}. "
        f"The dominant emotion is {results_of_analysis['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """Renders the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
