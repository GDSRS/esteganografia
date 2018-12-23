from PIL import Image
import numpy as np
import sys
    
RED_LAYER = 0
def decode_message(image):
    """
    Retrieve message inside the image
    """
    image = Image.open(image)
    #print(image.size)
    image_array = np.array(image)
    #print(image_array.shape)
    phrase = ''
    #print('image to decode',image_array.shape)
    for line in range(0,image_array.shape[0]-1):
        for column in range(0,image_array.shape[1]-1):
            value = image_array[line][column][RED_LAYER]
            binary_value = bin(value)[2:]

            lsb = binary_value[-1]
            phrase+=lsb
            #print(phrase)
            if len(phrase) > 8 and phrase[-8:] == '00000000': return phrase


def convert_binary_to_string(string):
    """
    Convert binary string to char
    string
    """
    final_string = ''
    while len(string) > 0:
        word = string[:8]
        string = string[8:]
        final_string += ''.join(chr(int(word,2)))
    return final_string

image_path = sys.argv[1]
out = decode_message(image_path)
print(out)
print('-----------------')
print(convert_binary_to_string(out))#[:-2]
