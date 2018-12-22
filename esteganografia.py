from PIL import Image
import numpy as np

        #print(bin(image_array[x][0][0])[2:])
        #print(int(bin(image_array[x][0][0])[2:],2))

RED_LAYER = 0
def read_convert_user_input():
    """
    Read user input and convert
    to binary string
    """
    user_text = input()
    #binary_text = ''.join( format(ord(char),'b') if char == 7 else '0'+format(ord(char),'b') for char in user_text )
    #binary_text= ''.join(x if len(x) ==7 else '0'+x for x in (format(ord(char),'b') for char in user_text)) sem acento
    binary_text = ''.join(x if len(x) == 8 else '0'+x if len(x) == 7 else '00'+x for x in (format(ord(char),'b') for char in user_text)) 
    return binary_text

def convert_binary_to_string(string):
    """
    Convert binary string to char
    string
    """
    final_string = ''
    while len(string) > 0:
        word = string[:7]
        string = string[7:]
        final_string += ''.join(chr(int(word,2)))
    return final_string


#print(len(non_zero))
def encode_message(message):
    """
    Encript the message in the image
    """
    image = Image.open('img.jpg')
    #print(image.getpixel((23,23)))
    print(image.size)
    image_array = np.array(image)

    print(image_array.shape)
    h,w,d = image_array.shape

    message += '00000000'
    print('newMessage',message)
    if len(message) > h*w: return -1

    for line in range(0,image_array.shape[0]-1):
        for column in range(0,image_array.shape[1]-1):
            value = image_array[line][column][RED_LAYER]
            binary_value = bin(value)[2:]
            
            binary_value = binary_value[:-1] + message[:1]
            message = message[1:]
            value = int(binary_value,2)
            image_array[line][column][RED_LAYER] = value

            if len(message) == 0: return image_array

def decode_message(image):
    """
    Retrieve message inside the image
    """
    image = Image.open(image)
    #print(image.size)
    image_array = np.array(image)
    print(image_array.shape)
    phrase = ''
    #print('image to decode',image_array.shape)
    for line in range(0,image_array.shape[0]-1):
        for column in range(0,image_array.shape[1]-1):
            value = image_array[line][column][RED_LAYER]
            binary_value = bin(value)[2:]

            lsb = binary_value[-1]
            phrase+=lsb
            #print(phrase)
            if len(phrase) > 7 and phrase[-7:] == '0000000': return phrase



#def get_image_byte_value(mode,message_or_phrase):
#    if mode == DECODE:
#        def function(binary_value):
#            retrieve_lsb(binary_value)
#    else:
#        def function(binary_value):
#            replace_lsb(binary_value)
#
#    for line in range(0,image_array.shape[0]-1):
#        for column in range(0,image_array.shape[1]-1):
#            value = image_array[line][column][RED_LAYER]
#            binary_value = bin(value)[2:]
#            response = function()
#            if response is not None: return response
#
#
#def replace_lsb(binary_value,message):
#    binary_value = binary_value[:-1] + message[:1]
#    message = message[1:]
#    value = int(binary_value,2)
#    image_array[line][column][RED_LAYER] = value
#
#    if len(message) == 0: return image_array
#
#def retrieve_lsb(binary_value,phrase):
#    lsb = binary_value[-1]
#    phrase+=lsb
#    if len(phrase) > 7 and phrase[-7:] == '0000000': return phrase



out = read_convert_user_input()
print(out)
#out = convert_binary_to_string(out)
#print(out)

out = encode_message(out)
new_img = Image.fromarray(out,'RGB')
new_img.save("teste.png")
#out = decode_message("teste.png")
#print(out)
#print(convert_binary_to_string(out))
