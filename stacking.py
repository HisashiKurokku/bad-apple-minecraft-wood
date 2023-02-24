from PIL import Image
import os

print('Processing...)

input_folder = "./overlay/"
output_folder = "./"

filename = os.listdir(input_folder)[0]
img_path = os.path.join(input_folder, filename)
base_img = Image.open(img_path)
output_size = base_img.size
output_mode = base_img.mode

output_img = Image.new(output_mode, (output_size[0], output_size[1] * len(os.listdir(input_folder))))

y_offset = 0
for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)
    input_img = Image.open(img_path)
    canvas = Image.new(output_mode, (output_size[0], output_size[1]))
    canvas.paste(input_img, (0, 0))
    output_img.paste(canvas, (0, y_offset))
    y_offset += output_size[1]

output_img.save(os.path.join(output_folder, "oak_planks.png"))
      
print('Done!')
