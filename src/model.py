import tensorflow as tf

def create_model(input_shape=(128, 128, 3), num_classes=38):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation='relu', padding='same', input_shape=input_shape),
        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        # Add more layers as per your current architecture...
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1500, activation='relu'),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model
