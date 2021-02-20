from PIL import Image

path_to_img = 'test.png'

img = Image.open(path_to_img)

# Width and Height
width, height = img.size

ratio = width/height/1.65

new_width = 200
new_height = new_width*ratio

# Resizing the img
img = img.resize((new_width, new_height)).convert('L')

# getting pixels' data
pixels = img.getdata()

# ascii art for dense
art = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". '
