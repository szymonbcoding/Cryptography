import sys

M_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
            'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 
            'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 
            'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 
            'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
            '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', 
            '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '!':'-.-.--', '/':'-..-.', '-':'-....-', 
            '(':'-.--.', ')':'-.--.-'} 

def encryption(text):
    code = ''
    for i in text:
        if (i != ' '):
            #changing character for morse code with space to seprate characters
            code += M_DICT[i] + ' ' 
        else:
            #if character is space, give extra space to signalize new word
            code += ' '

    return code

def decryption(text):
    #without this extra space, last mark would not be decoded
    text += ' '
    decode = ''
    supportText = ''
    spaceCounter = 0
    for i in text:
        if (i != ' '):
            spaceCounter = 0
            #creating supportText to gather dots and dashes for current mark decoding
            supportText += i
        else:
            #incrementing spaceCounter to find out when current sequence is over
            spaceCounter += 1

            if (spaceCounter == 2):
                decode += ' '
            else:
        
                #converting dictionary to list to find specific symbol by specific set of dots and dashes
                decode += list(M_DICT.keys())[list(M_DICT.values()).index(supportText)]
                #clearing supportText for new mark 
                supportText = ''

    return decode

def test(text):

    #encryption
    codedText = encryption(text.upper())
    print("This is my coded sequence: " + codedText)

    #decryption
    decodedText = decryption(codedText)
    print("This is my decoded sequence: " + decodedText)
    
    #checking if firstly coded and then decoded sequence is the same as in the beginning
    if(text.upper() in decodedText):
        print("Program correctly coded and decoded sequence.")
    else:
        print("Test failed. The sequences are not the same.")


def main():

    mode = sys.argv[1]
    text = sys.argv[2]

    if mode == 'encryption':
        print(encryption(text.upper()))
    elif mode == 'decryption':
        print(decryption(text))
    elif mode == 'test':
        test(text)
    else:
        raise Exception ('Wrong mode. Please use encryption, decryption or test.')

if __name__ == '__main__':
    main()