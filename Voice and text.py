import cv2
import mediapipe as mp
import pyttsx3
import time

# Initialize mediapipe hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Initialize pyttsx3 for voice
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speech rate

# Start webcam
cap = cv2.VideoCapture(0)

previous_letter = ""  # store last detected letter
letter_cooldown = 1.0  # seconds to wait before speaking same letter again
last_time = 0

def detect_letter(hand_landmarks):
    # Get coordinates (y for vertical position)
    thumb_tip = hand_landmarks.landmark[4].y
    index_tip = hand_landmarks.landmark[8].y
    middle_tip = hand_landmarks.landmark[12].y
    ring_tip = hand_landmarks.landmark[16].y
    pinky_tip = hand_landmarks.landmark[20].y
    wrist_y = hand_landmarks.landmark[0].y  # wrist base position

    # A → 👍 (Thumbs up)
    # thumb above wrist (lower y value), all fingers closed (tips below wrist)
    if thumb_tip < wrist_y and all(
        tip > wrist_y for tip in [index_tip, middle_tip, ring_tip, pinky_tip]
    ):
        return "A"

    # B → 👎 (Thumbs down)
    # thumb below wrist (higher y value), all fingers closed
    elif thumb_tip > wrist_y and all(
        tip < wrist_y for tip in [index_tip, middle_tip, ring_tip, pinky_tip]
    ):
        return "B"

    # C → ✌️ (Peace sign)
    # index and middle fingers up, others down
    elif (
        index_tip < wrist_y and middle_tip < wrist_y
        and ring_tip > wrist_y and pinky_tip > wrist_y
    ):
        return "C"

    else:
        return None


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # mirror view
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    detected_letter = None
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            detected_letter = detect_letter(handLms)

    # Only speak if a letter is detected and cooldown passed
    current_time = time.time()
    if detected_letter and (detected_letter != previous_letter or current_time - last_time >= letter_cooldown):
        print(f"Detected Letter: {detected_letter}")
        engine.say(detected_letter)
        engine.runAndWait()
        previous_letter = detected_letter
        last_time = current_time

    # Display on webcam
    if detected_letter:
        cv2.putText(img, f'Letter: {detected_letter}', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Sign Language Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
