import cv2
import mediapipe as mp
import pyautogui
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Screen size
screen_w, screen_h = pyautogui.size()

# Load model
base_options = python.BaseOptions(
    model_asset_path="hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
# Force hd resolution for better viewing
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


pyautogui.FAILSAFE = True

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    h_cam, w_cam, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    if result.hand_landmarks:

        for hand in result.hand_landmarks:

            lm_list = []

            for lm in hand:
                x = int(lm.x * w_cam)
                y = int(lm.y * h_cam)

                lm_list.append((x, y))

                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            # index finger tip
            ix, iy = lm_list[8]

            # map camera screen
            screen_x = int(ix * screen_w / w_cam)
            screen_y = int(iy * screen_h / h_cam)

            # move mouse
            prev_x, prev_y = pyautogui.position()

            smooth_x = int(prev_x + (screen_x - prev_x) * 0.3)
            smooth_y = int(prev_y + (screen_y - prev_y) * 0.3)

            pyautogui.moveTo(smooth_x, smooth_y)


            # finger count
            fingers = 0
            tips = [8, 12, 16, 20]

            for tip in tips:
                if lm_list[tip][1] < lm_list[tip - 2][1]:
                    fingers += 1

            #thumb
            if lm_list[4][0] > lm_list[3][0]:
                fingers += 1

            #Click
            if fingers == 0:
                pyautogui.click()
                cv2.putText(frame, "Click", (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2)

            # Scroll
            if fingers == 2:
                pyautogui.scroll(20)
                cv2.putText(frame, "Scroll", (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0), 2)

            #show mode
            cv2.putText(frame, f"Fingers: {fingers}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 0), 2)

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
