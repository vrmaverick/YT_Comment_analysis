# 🎯 Intent Classification & Sentiment Analysis on YouTube Comments

This project combines a **Bi-directional RNN**-based **Intent Classification** model with **TextBlob-based sentiment analysis** on **YouTube video comments**. It demonstrates an end-to-end NLP pipeline — from training a deep learning model to extracting and analyzing real-world data via the YouTube Data API.

---

## 🚀 Features

- Trained Bi-directional RNN (GRU + LSTM) model for intent detection  
- Pre-trained model reused from [Intent Classification Project](https://github.com/your-username/previous-intent-repo)  
- Extracts comments using YouTube Data API (given a `video_id`)  
- Analyzes sentiment (positive/negative/neutral) using `TextBlob`  
- Visualizes prediction and sentiment outcomes  
- Includes sample results and model architecture screenshots

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- TextBlob
- Pandas, NumPy
- YouTube Data API (v3)

---

## 🧠 Model Overview

The core of the intent classification is a **Bi-directional Recurrent Neural Network**, composed of:
- `TextVectorization` for input preprocessing
- `Embedding` layer for word representation
- `BiGRU` + `BiLSTM` layers for sequential understanding
- `Dense` layers for classification over 27 intent classes

<p float="left">
  <img src="images/Screenshot 2025-05-31 181304.png" width="45%" />
  <img src="images/Screenshot 2025-05-31 181323.png" />
</p>

---

## 📊 Sample Results

After extracting comments via the YouTube API of Grammarly video about AI, the following are the results:

<p float="left">
  <img src="images/Screenshot 2025-05-31 184818.png" width="45%" />
  <img src="images/Screenshot 2025-05-31 184852.png" width="45%" />
</p>

---

## 📁 Project Structure
```
├── main.py # Main pipeline
├── BI_RNN.keras # .keras model used for intent detection (reviews)(27 classes)
├── video.py # Extract the video comments and sentiment analysis function
├── vectorize.py # Text vectorization and embedding setup
├── model.py # All model handling functions
├── images/ # Images of model & results (for README)
├── README.md
```
---
## 📩 Contact

- ✉️ Email: [vedantranade2612@gmail.com](mailto:vedantranade2612@gmail.com)  
- 🌐 Portfolio: [My_portfolio]([https://yourportfolio.com](https://vedant-ranade.netlify.app/))

---

