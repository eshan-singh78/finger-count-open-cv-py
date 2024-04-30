import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=2, detectionCon=0.8)
video = cv2.VideoCapture(0)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True)

    if hands:
        for hand in hands:
            fingers_up = detector.fingersUp(hand)
            num_fingers_up = fingers_up.count(1)
            
            hand_side = "Right" if hand["type"] == "Right" else "Left"
            
            text = f"Hand: {hand_side} Finger-{num_fingers_up}"
            cv2.putText(img, text, (50, img.shape[0] - 50 * (2 - hands.index(hand))), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
