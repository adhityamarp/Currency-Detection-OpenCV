# 💵 Indian Currency Detection & Counter (YOLO + OpenCV)

A real-time **Indian currency recognition system** built using **YOLO classification** and **OpenCV**.  
The system detects currency notes from a webcam and calculates the **total amount automatically**.

This project demonstrates how computer vision can be used for **currency identification and real-time financial counting systems**.

---

# 🚀 Features

✔ Real-time currency note detection using webcam  
✔ Deep learning model trained with YOLO classification  
✔ Confidence threshold filtering for reliable predictions  
✔ Manual confirmation system to prevent duplicate counting  
✔ Live display of detected note and running total amount  
✔ Simple and lightweight OpenCV interface  

---

# 🧠 How It Works

1️⃣ The webcam captures real-time frames.  
2️⃣ The trained YOLO model predicts the **currency denomination**.  
3️⃣ If prediction confidence is above the threshold, the note is detected.  
4️⃣ The user presses **'A'** to add the detected note value to the total amount.  
5️⃣ The total amount is displayed on the screen.

---

# 🛠 Tech Stack

- Python  
- OpenCV  
- YOLO (Ultralytics)  
- Deep Learning (CNN-based classification)

Libraries used:

- cv2
- ultralytics
- numpy

---

# 📦 Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Indian-Currency-Counter.git
cd Indian-Currency-Counter
```

---

## 2️⃣ Install dependencies

```bash
pip install opencv-python ultralytics
```

---

## 3️⃣ Ensure model weights exist

Make sure the trained model is located at:

```
runs/classify/train/weights/best.pt
```

This file is generated after training your YOLO classification model.

---

# ▶️ Run the Project

```bash
python currency_counter.py
```

Your webcam will open and start detecting currency notes.

---

# 🎮 Controls

| Key | Action |
|----|------|
| A | Add detected currency to total |
| ESC | Exit application |

---

# 📷 Output Display

The system displays:

- Detected currency denomination
- Prediction confidence score
- Total calculated amount

Example output:

```
Detected: Rs.500 (0.92)
TOTAL AMOUNT: Rs.1500
```

---

# 📂 Project Structure

```
currency-counter
│
├── currency_counter.py
├── runs
│   └── classify
│       └── train
│           └── weights
│               └── best.pt
│
├── README.md
└── requirements.txt
```

---

# ⚠️ Limitations

- Requires good lighting conditions  
- Works best when the currency note is clearly visible  
- Only detects denominations present in the training dataset  

---

# 🔮 Future Improvements

- Automatic counting without manual confirmation  
- Mobile camera support  
- Currency detection for multiple countries  
- GUI interface  
- Integration with payment systems  

---

# 👨‍💻 Author

Marpu Adhitya  
AI / ML Engineer  
Email: adhimarpu@gmail.com  

---

# ⭐ Support

If you like this project, consider giving it a **star on GitHub** ⭐
