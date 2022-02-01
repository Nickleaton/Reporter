from PIL import Image, ImageFont, ImageDraw
import cv2
from datetime import datetime, timedelta

cam = cv2.VideoCapture("sample.mp4")
frames_per_second = cam.get(cv2.CAP_PROP_FPS)
frame_count = cam.get(cv2.CAP_PROP_FRAME_COUNT)
seconds = int(frame_count / frames_per_second)
print(frame_count, frames_per_second, seconds)

frames = [t * frames_per_second for t in range(0, seconds, 5)]
print(frames)
i = 0
now = datetime.now()
while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break
    if i in frames:
        offset = timedelta(seconds=i*frames_per_second)
        timestamp = datetime.strftime(now+offset, '%Y-%m-%d %H:%M:%S')
        file_name = f'snap_{i:03d}.jpg'
        cv2.imwrite(file_name, frame)
        img = Image.open(file_name)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 30)
        draw.text((0, 0), timestamp, fill=(255, 255, 255), font=font)
        img.save(file_name)


    i += 1

cam.release()
cv2.destroyAllWindows()
