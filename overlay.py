from PIL import Image
import os

print('Processing...')

img_folder = "./frames/"
base_img_path = "oak.png"
output_folder = "./overlay/"

base_img = Image.open(base_img_path)

for filename in os.listdir(img_folder):
    img_path = os.path.join(img_folder, filename)
    img = Image.open(img_path)
    alpha_mask = img.split()[-1]

    base_img.paste(img, (0, 0), alpha_mask)

    output_path = os.path.join(output_folder, filename)
    base_img.save(output_path)

    base_img = Image.open(base_img_path)

print('Done!')
