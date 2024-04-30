
# Hand Tracking and Finger Counting using OpenCV

This Python script uses OpenCV and the cvzone library to detect hands in a live video stream from a webcam and count the number of fingers held up by each hand.

## Requirements

- Python 3.x
- OpenCV
- cvzone (HandTrackingModule)

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install OpenCV by running:
   ```
   pip install opencv-python
   ```
3. Install cvzone by running:
   ```
   pip install cvzone
   ```

## Usage

1. Run the Python script `hand_tracking_finger_count.py`.
2. The script will open a live video feed from your webcam.
3. Hold up your hands in front of the camera.
4. The script will detect your hands and count the number of fingers held up by each hand.
5. The count will be displayed on the video feed, with information about which hand (right/left) is detected and how many fingers are raised.

## Controls

- Press `q` or `Ctrl+C` in terminal to quit the program.

## Customization

You can customize the behavior of the script by adjusting parameters such as the maximum number of hands to detect and the detection confidence threshold. These parameters can be modified in the `HandDetector` initialization.

```python
detector = HandDetector(maxHands=2, detectionCon=0.8)
```

You can also customize the text displayed on the video feed by modifying the `text` variable in the script.

```python
text = f"Hand: {hand_side} Finger-{num_fingers_up}"
```
