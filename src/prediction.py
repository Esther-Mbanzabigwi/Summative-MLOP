import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def predict_image(model, image_path, class_names, target_size=(128, 128)):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0)
    predictions = model.predict(input_arr)
    result_index = np.argmax(predictions)
    return class_names[result_index], predictions[0]

def evaluate_model(model, dataset):
    y_pred = model.predict(dataset)
    predicted_categories = tf.argmax(y_pred, axis=1)
    true_categories = tf.concat([y for _, y in dataset], axis=0)
    true_categories = tf.argmax(true_categories, axis=1)
    cm = confusion_matrix(true_categories, predicted_categories)
    report = classification_report(true_categories, predicted_categories)
    return cm, report

def plot_confusion_matrix(cm, class_names):
    plt.figure(figsize=(10, 10))
    sns.heatmap(cm, annot=True, fmt="d", xticklabels=class_names, yticklabels=class_names, cmap="Blues")
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()
