import cv2
import numpy as np

# Read the video
video_path = 'hiron.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define a codec and create a VideoWriter object to save the modified video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_path = 'output_video.mp4'
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Read and process frames
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

# Play the frames in reverse order and write to the output video
for frame in reversed(frames):
    out.write(frame)
    cv2.imshow('Reversed Video', frame)
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()
cv2.destroyAllWindows()
