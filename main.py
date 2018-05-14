password = "test"
text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr";

#todo: add a good random binary number generator
passwordBinary = ''.join(format(ord(x), 'b') for x in password)
textBinary = ''.join(format(ord(x), 'b') for x in text)
encryptedText = ''
textBinaryEnc = ''


def bitShiftEnc(passwordBit, textBinaryString):
    if passwordBit == 1:
        textBinaryString = textBinaryString[1:int(len(textBinaryString))] + textBinaryString[:1]
    else:
        textBinaryString = textBinaryString[:1] + textBinaryString[1:len(textBinary)]
    return textBinaryString


def bitShiftDec(passwordBit, textBinaryString):
    if passwordBit == 0:
        textBinaryString = textBinaryString[1:len(textBinaryString)] + textBinaryString[:1]
    else:
        textBinaryString = textBinaryString[:1] + textBinaryString[1:len(textBinary)]
    return textBinaryString

print(textBinary)

##this is the encryption part
ii = 0
while ii < len(passwordBinary):
    i = 0
    while i < len(textBinary):
        textBinaryEnc = textBinaryEnc + str(int(passwordBinary[ii]) ^ int(textBinary[i]))
        i = i + 1
    textBinary = bitShiftEnc(passwordBinary[ii], textBinaryEnc)
    textBinaryEnc = ""
    ii = ii + 1

print(textBinary)

##this is the decryption part
ii = 0
while ii < len(passwordBinary):
    i = 0
    textBinary = bitShiftDec(passwordBinary[ii], textBinary)
    while i < len(textBinary):
        textBinaryEnc = textBinaryEnc + str(int(passwordBinary[ii]) ^ int(textBinary[i]))
        i = i + 1
    textBinary = textBinaryEnc
    textBinaryEnc = ""
    ii = ii + 1

print(textBinary)