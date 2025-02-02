from ultralytics import YOLO
import cv2

# Load YOLOv11 model
model = YOLO("weights/yolo11n.pt")

# Open webcam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)

    # Annotate and display results
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv11 Detection", annotated_frame)

    # Quit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
