import cv2
from deepface import DeepFace

def analyze_emotion(frame):
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    return result[0]['dominant_emotion']

def process_image(image_path):
    frame = cv2.imread(image_path)
    emotion = analyze_emotion(frame)
    # Only return 'happy' or 'neutral'
    if emotion == 'happy':
        return 'happy'
    else:
        return 'neutral'