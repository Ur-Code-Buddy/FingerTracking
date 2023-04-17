import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Reduce image size to 640x480
width, height = 640, 480

webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.6) as hands:
    while webcam.isOpened():
        success, img = webcam.read()

        if not success:
            break

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (width, height))

        results = hands.process(img)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for idx, landmark in enumerate(hand_landmarks.landmark):
                    print(f"Landmark {idx}: ({landmark.x}, {landmark.y}, {landmark.z})")
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=3, circle_radius=3))

        cv2.imshow('HandDetector', img)

        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()
