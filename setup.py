from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    description="Emotion Detection package using Watson NLP",
    author="Author",
    packages=find_packages(),
    install_requires=[
        "requests",
        "flask"
    ]
)
