from PIL import Image
from transformers import Pipeline

CANDIDATE_LABELS = ["porcupine", "wild boar", "fox", "marten", "hare", "deer", "badger", "wolf", "horse", "dog", "cat", "buzzard", "heron", "mallard", "squirrel"]

def classify(image: Image, detector: Pipeline):
    """Classify the image using the zero-shot image classification pipeline."""
    try:
        result = detector(image, candidate_labels=CANDIDATE_LABELS)
        return result[0]['label']
    except Exception as e:
        print(f"Error classifying image: {e}")
        return None