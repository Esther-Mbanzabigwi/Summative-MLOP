# Save the TensorFlow model in the .tf format

def save_tf_model(model, path="models/trained_plant_disease_model.tf"):
    model.save(path)
    print(f"Model saved in TensorFlow format at: {path}")

# Load the TensorFlow model from the .tf format

def load_tf_model(path="models/trained_plant_disease_model.tf"):
    model = tf.keras.models.load_model(path)
    print(f"Model loaded from TensorFlow format at: {path}")
    return model
