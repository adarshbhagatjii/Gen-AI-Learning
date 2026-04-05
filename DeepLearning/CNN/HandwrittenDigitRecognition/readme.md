# ✍️ Smart Digit Recognizer (CNN + Streamlit)

🚀 A modern AI-powered web application that recognizes handwritten digits (0–9) using a **Convolutional Neural Network (CNN)** with an interactive **drawing canvas + image upload** interface.

---

## 🌟 Features

🎨 Draw digits in real-time (like a whiteboard)
📤 Upload handwritten digit images
🧠 CNN-based prediction (MNIST trained model)
📊 Probability distribution for all digits (0–9)
🎯 Confidence score display
🧹 Clear canvas & re-draw support
🌐 Deployable on Streamlit Cloud

---

## 🧠 Model Architecture

* Conv2D (32 filters) + MaxPooling
* Conv2D (64 filters) + MaxPooling
* Flatten
* Dense (128, ReLU)
* Output Layer (Softmax - 10 classes)

📌 Dataset: MNIST (60,000 training + 10,000 test images)

---

## 📊 Demo Preview

👉 Draw or upload a digit → Model predicts instantly with confidence and probability chart.

---

## ⚙️ Tech Stack

| Layer            | Technology                |
| ---------------- | ------------------------- |
| Frontend         | Streamlit                 |
| Backend          | Python                    |
| Deep Learning    | TensorFlow / Keras        |
| Visualization    | Matplotlib                |
| Image Processing | NumPy, Pillow             |
| UI Canvas        | streamlit-drawable-canvas |

---

## 📁 Project Structure

```id="zjhy4g"
smart-digit-recognizer/
│
├── train.py
├── app.py
├── model.h5
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash id="0kgt3t"
git clone https://github.com/your-username/smart-digit-recognizer.git
cd smart-digit-recognizer
```

---

### 2️⃣ Install Dependencies

```bash id="5fg6sx"
pip install -r requirements.txt
```

---

### 3️⃣ Train Model

```bash id="rxlr86"
python train.py
```

---

### 4️⃣ Run App

```bash id="tj8x06"
streamlit run app.py
```

---

## 📷 Usage

1. Draw a digit using canvas OR upload an image
2. Click **Predict**
3. View:

   * Predicted digit
   * Confidence score
   * Probability graph

---

## 📊 Model Performance

* Accuracy: ~98% on MNIST
* Loss Function: Categorical Crossentropy
* Optimizer: Adam

---

## 💡 Future Enhancements

* 🔥 Grad-CAM visualization
* 🌍 Multi-digit recognition
* 📱 Mobile-friendly UI
* 🎙️ Voice input support
* 🤖 Integration with LLM for explanations

---

## 🏆 Resume Highlight

> Developed a CNN-based handwritten digit recognition system with an interactive Streamlit UI supporting real-time drawing and image uploads, achieving ~98% accuracy on MNIST dataset.

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first.

---



## ⭐ Support

If you like this project:

👉 Star ⭐ the repo
👉 Share it with others

---

**Built with ❤️ using Deep Learning & Streamlit**
