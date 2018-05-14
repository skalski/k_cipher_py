password = "something"
text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr"

#funny logical site effect - if text binary and password binary the same - nothing happends
text_binary = ''.join(format(ord(x), 'b') for x in text)
password_binary = ''.join(format(ord(x), 'b') for x in password)

text_binary_enc = ''

def bit_shift_enc(password_bit, text_binary_string):
    if password_bit == 1:
        text_binary_string = text_binary_string[1:int(len(text_binary_string))] + text_binary_string[:1]
    else:
        text_binary_string = text_binary_string[:1] + text_binary_string[1:len(text_binary)]
    return text_binary_string


def bit_shift_dec(password_bit, text_binary_string):
    if password_bit == 0:
        text_binary_string = text_binary_string[1:len(text_binary_string)] + text_binary_string[:1]
    else:
        text_binary_string = text_binary_string[:1] + text_binary_string[1:len(text_binary)]
    return text_binary_string


print(text_binary)

##this is the encryption part
ii = 0
while ii < len(password_binary):
    i = 0
    while i < len(text_binary):
        text_binary_enc = text_binary_enc + str(int(password_binary[ii]) ^ int(text_binary[i]))
        i = i + 1
    text_binary = bit_shift_enc(password_binary[ii], text_binary_enc)
    text_binary_enc = ""
    ii = ii + 1

print(text_binary)

##this is the decryption part
ii = 0
while ii < len(password_binary):
    i = 0
    text_binary = bit_shift_dec(password_binary[ii], text_binary)
    while i < len(text_binary):
        text_binary_enc = text_binary_enc + str(int(password_binary[ii]) ^ int(text_binary[i]))
        i = i + 1
    text_binary = text_binary_enc
    text_binary_enc = ""
    ii = ii + 1

print(text_binary)
