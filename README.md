# Signature-text-voice
# 🖐️ Sign Language to Voice Conversion using Python

This project converts hand gestures (sign language) into spoken voice output using a webcam.  
It uses MediaPipe for hand detection, OpenCV for video processing, and pyttsx3 for text-to-speech conversion.

The system currently recognizes basic hand gestures and speaks the corresponding alphabet letters.

---

## 🚀 Features

- Real-time hand gesture detection using webcam  
- Converts sign language gestures into voice output  
- AI-based hand landmark detection  
- Cooldown mechanism to avoid repeated voice output  
- Simple and beginner-friendly Python code  

---

## 🛠️ Technologies Used

- Python  
- OpenCV  
- MediaPipe  
- pyttsx3  

---

## ✋ Supported Gestures

| Gesture | Description | Output |
|--------|------------|--------|
| 👍 Thumbs Up | Thumb up, other fingers down | A |
| 👎 Thumbs Down | Thumb down, other fingers up | B |
| ✌️ Peace Sign | Index and middle fingers up | C |

---

## 📁 Project Structure

sign-language-to-voice/
├── sign_language_to_voice.py  
├── README.md  
└── requirements.txt  

---

## 📦 Installation

1. Clone the repository:
git clone https://github.com/your-username/sign-language-to-voice.git
cd sign-language-to-voice

csharp
Copy code

2. Install required libraries:
pip install opencv-python mediapipe pyttsx3

yaml
Copy code

---

## 🧩 Environment Setup (VS Code)

Before running this program, the Python environment must be properly set up in Visual Studio Code (VS Code).

- Install Python and configure it in VS Code  
- Select the correct Python interpreter  
- Install the required libraries: OpenCV, MediaPipe, and pyttsx3  

After completing the environment setup, the program can be executed successfully.  
When the program runs, the webcam opens automatically, detects hand gestures in real time, and converts the detected sign language into voice output.


## ▶️ How to Run

python sign_language_to_voice.py

yaml
Copy code

- Webcam opens automatically  
- Show hand gestures in front of the camera  
- Detected letter will be spoken aloud  
- Press `q` to exit  

---

## 🧠 Working Principle

1. Webcam captures live video  
2. MediaPipe detects hand landmarks  
3. Finger positions are analyzed  
4. Corresponding letter is identified  
5. pyttsx3 converts the letter into voice output  

---

## 📌 Applications

- Assistive technology for speech-impaired people  
- Human–computer interaction  
- Educational projects  
- College mini and final year projects  

---

## 🔮 Future Enhancements

- Support for complete A–Z sign language  
- Word and sentence formation  
- Improved gesture accuracy  
- GUI-based interface  

---

## 👩‍💻 Author

Nandhika Sri  
Electronics and Communication Engineering (ECE)  

---

## 📜 License

This project is open-source and available under the MIT License.
