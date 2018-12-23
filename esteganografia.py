from PIL import Image
import numpy as np
import sys

RED_LAYER = 0

"""
USAGE:
    pass the image path as the first argument 
    and the txt file with the message as the 
    second argument
"""
def read_file(file_name):
    """
    Read a text from a file
    """
    with open(file_name,'r') as f:
        file_message = f.read()

    return str(file_message)

def convert_user_message(user_text):
    """
    Read user input and convert
    to binary string
    """
    #user_text = input()
    #binary_text = ''.join( format(ord(char),'b') if char == 7 else '0'+format(ord(char),'b') for char in user_text )
    #binary_text= ''.join(x if len(x) ==7 else '0'+x for x in (format(ord(char),'b') for char in user_text)) sem acento
    binary_text = ''.join(x if len(x) == 8 else '0'+x if len(x) == 7 else '0000'+x if len(x) == 4 else '00'+x for x in (format(ord(char),'b') for char in user_text)) 
    return binary_text

def encode_message(message,image):
    """
    Encript the message in the image
    """
    image = Image.open(image)
    image_array = np.array(image)

    h,w,d = image_array.shape

    message += '00000000'
    if len(message) > h*w: return -1

    #TODO: use other layers
    for line in range(0,image_array.shape[0]-1):
        for column in range(0,image_array.shape[1]-1):
            value = image_array[line][column][RED_LAYER]
            binary_value = bin(value)[2:]
            
            binary_value = binary_value[:-1] + message[:1]
            message = message[1:]
            value = int(binary_value,2)
            image_array[line][column][RED_LAYER] = value

            if len(message) == 0: return image_array


out = read_file(sys.argv[2])
out = convert_user_message(out)
print(out)
image = sys.argv[1]
out = encode_message(out,image)
new_img = Image.fromarray(out,'RGB')
new_img.save("teste.png")
