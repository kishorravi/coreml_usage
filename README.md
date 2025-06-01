# 🧠🔁 CoreML Model Converter

Convert your trained Keras `.h5` model into Apple Core ML `.mlmodel` format, ready to use in iOS/macOS apps!

## 📌 Overview

This project includes a simple script to:
- ✅ Load a TensorFlow/Keras `.h5` model
- ✅ Convert it into Core ML format using `coremltools`
- ✅ Save the `.mlmodel` file for use in Xcode/Swift

---

## 📂 Files Included

| File                    | Description                                      |
|-------------------------|--------------------------------------------------|
| `convert_to_coreml.py`  | Python script to perform the model conversion    |
| `my_model.h5`           | Placeholder for your trained Keras model         |
| `MyImageClassifier.mlmodel` | Output Core ML model (generated)           |

---

## ⚙️ Requirements

Install dependencies using pip:

```bash
pip install tensorflow coremltools
