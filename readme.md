# 🔒 Secure Data Hiding in Images Using Steganography

This project is part of the **AICTE IBM Skills Build Cyber Security Internship**. It provides an online **Steganography** tool that allows users to **hide and retrieve secret messages** within images securely.  

## 📌 Project Overview

Steganography is the practice of concealing secret information within digital media. This project implements **image-based steganography** using **Flask and OpenCV**, enabling users to encode and decode messages within images.

## ✨ Features

- 🔹 **Encode Secret Messages**: Hide a text message inside an image.
- 🔹 **Decode Messages**: Extract hidden messages from an encoded image.
- 🔹 **Simple Web Interface**: User-friendly UI for easy interaction.
- 🔹 **Supports PNG, JPG, and JPEG formats**.

## 🖥️ Tech Stack

- **Frontend**: HTML, CSS  
- **Backend**: Flask (Python)  
- **Image Processing**: OpenCV  
- **Storage**: Local File System  

## 📂 Directory Structure

```
aicte-ibm-internship/
├── app.py                   # Main Flask application
├── requirements.txt         # Dependencies list
├── static/
│   └── styles.css           # CSS file for styling
└── templates/
    └── index.html           # Frontend UI
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/akshay0611/aicte-ibm-internship.git
```

### 2️⃣ Install Dependencies

Make sure you have **Python** installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server

```bash
python3 app.py
```

### 4️⃣ Open in Browser

Visit: **http://127.0.0.1:5000/**

## 📜 Usage Guide

### 🔹 Encoding a Message:

1. Upload an image (**PNG/JPG/JPEG**).
2. Enter the secret message you want to hide.
3. Click **Encode** to download the encoded image.

### 🔹 Decoding a Message:

1. Upload the encoded image.
2. Click **Decode** to reveal the hidden message.


## 🛡️ Disclaimer

This project is for **educational purposes only**. Please use it ethically and responsibly.

---

