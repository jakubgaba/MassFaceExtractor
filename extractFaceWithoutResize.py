import cv2
import os

CURRENT_PATH = os.path.dirname(__file__)
extensions = ['jpeg', 'png', 'jpg']


#Change here directories for input and output
directory = './input'
out_src = './test'

# Load OpenCV's pre-trained face detection models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
profile_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

# Create the output directory if it doesn't exist
output_dir_path = os.path.join(CURRENT_PATH, out_src)
if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)

index = 1

for dir_path, _, file_names in os.walk(directory):
    for filename in file_names:
        if filename.split('.')[-1].lower() not in extensions:
            continue
        print("Processing:", filename)
        path = os.path.join(dir_path, filename)
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect frontal faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5,)

        # Detect profile faces
        profile_faces = profile_face_cascade.detectMultiScale(gray, 1.3, 5)

        # Combine detected faces
        all_faces = list(faces) + list(profile_faces)

        for (x, y, w, h) in all_faces:
            margin = 50
            x_start = max(x - margin, 0)
            y_start = max(y - margin, 0)
            x_end = min(x + w + margin, img.shape[1])
            y_end = min(y + h + margin, img.shape[0])

            face = img[y_start:y_end, x_start:x_end]
            cv2.imwrite(os.path.join(output_dir_path, f"face_{index}.jpg"), face)
            index += 1

