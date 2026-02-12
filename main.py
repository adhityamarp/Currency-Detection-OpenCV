import cv2
from ultralytics import YOLO

# 1. Load your newly trained classification model
model = YOLO('runs/classify/train/weights/best.pt') 

# 2. Configuration for Real-time calculation
# We use a threshold to ignore low-confidence detections
CONFIDENCE_THRESHOLD = 0.8 

def get_prediction(frame):
    results = model(frame)
    
    # Classification results provide probabilities for each class
    for r in results:
        # Get the top class name and its confidence
        top_class_idx = r.probs.top1
        conf = r.probs.top1conf.item()
        label = r.names[top_class_idx]
        
        if conf > CONFIDENCE_THRESHOLD:
            return label, conf
    return None, 0

# 3. Main Loop (Webcam)
cap = cv2.VideoCapture(0)
total_sum = 0
last_detected = ""
print("🇮🇳 Indian Currency Counter - running in OpenCV window")

while True:
    ret, frame = cap.read()
    if not ret: break

    label, confidence = get_prediction(frame)

    if label:
        # Visual Feedback
        color = (0, 255, 0)
        cv2.putText(frame, f"Detected: Rs.{label} ({confidence:.2f})", 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        
        # Simple Logic to add to total (Wait for user to press 'A' to add)
        # This prevents the same note from adding 1000 times per second
        cv2.putText(frame, "Press 'A' to add to Total", (50, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        key = cv2.waitKey(1)
        if key == ord('a'):
            total_sum += int(label)
            print(f"Added {label}. Current Total: {total_sum}")

    # Display Total Amount on screen
    cv2.rectangle(frame, (0, 400), (640, 480), (0, 0, 0), -1)
    cv2.putText(frame, f"TOTAL AMOUNT: Rs.{total_sum}", (150, 450), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)

    cv2.imshow("Currency Identifier", frame)
    
    if cv2.waitKey(1) == 27: # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()