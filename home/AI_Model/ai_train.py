import cv2
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)

# Load the pre-trained model
model = load_model('home/AI_Model/fire_detection_model.h5')

def predict_fire(image_path):
    """
    Predict whether the image contains fire or not.

    Parameters:
    image_path (str): The path to the input image.

    Returns:
    str: 'Fire' if fire is detected, 'No Fire' otherwise.
    """
    # Load and preprocess the image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (256, 256))
    img = img.reshape((1, 256, 256, 3))

    # Make a prediction
    prediction = model.predict(img)

    # Determine the result
    result = 'Fire' if prediction[0][0] > 0.5 else 'No Fire'

    return result

