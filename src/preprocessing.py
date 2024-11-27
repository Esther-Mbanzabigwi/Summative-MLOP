import tensorflow as tf

def load_data(data_dir, image_size=(128, 128), batch_size=32):
    return tf.keras.utils.image_dataset_from_directory(
        data_dir,
        labels="inferred",
        label_mode="categorical",
        color_mode="rgb",
        batch_size=batch_size,
        image_size=image_size,
        shuffle=True,
        interpolation="bilinear",
    )
