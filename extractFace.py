import os
from object_extractor import Extractor, FRONTALFACE_ALT2

CURRENT_PATH = os.path.dirname(__file__)
extensions = ['jpeg', 'png','jpg']

directory = './input'
out_src = './test'

# Create the output directory if it doesn't exist
output_dir_path = os.path.join(CURRENT_PATH, out_src)
if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)

index = 1

for dir_path, _, file_names in os.walk(directory):
    for filename in file_names:
        if not filename.split('.')[-1] in extensions: 
            continue
        print("Processing:", filename)
        path = os.path.join(dir_path, filename)
        Extractor.extract(path, cascade_file=FRONTALFACE_ALT2,
                          output_directory=output_dir_path, 
                          output_prefix="face_" + str(index),
                          start_count=1)
        index += 1

