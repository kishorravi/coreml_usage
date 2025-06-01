import tensorflow as tf
import coremltools as ct

# === CONFIGURATION ===
keras_model_path = "my_model.h5"           # Path to your trained Keras model
coreml_model_path = "MyImageClassifier.mlmodel"  # Desired output path
input_shape = (224, 224, 3)                # Input shape without batch size

# === STEP 1: Load the Keras model ===
print("Loading Keras model...")
model = tf.keras.models.load_model(keras_model_path)

# === STEP 2: Convert to CoreML ===
print("Converting to Core ML format...")
coreml_model = ct.convert(
    model,
    inputs=[ct.ImageType(name="input_1", shape=input_shape, scale=1/127.5, bias=[-1, -1, -1])],
)

# === STEP 3: Save CoreML model ===
coreml_model.save(coreml_model_path)
print(f"Core ML model saved as: {coreml_model_path}")
