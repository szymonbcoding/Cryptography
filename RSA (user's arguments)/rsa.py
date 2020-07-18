import sys
from math import gcd

def checkingCoprimeNumbers(a, b):
    #checking if numbers are coprime 
    return gcd(a, b) == 1

def checkingPrimeNumbers(num):

    prime = False

    if num > 1:
    # calculating factors
        for i in range(2,num):
            if (num % i) == 0:
                prime = False
                break
    #if number has not other factors than 1 is prime number
        else:
            prime = True
       
    #if number is equal or less than 1 is not prime number
    else:
        prime = False

    return prime

def encryption(text, e, n):

    code = []

    #coding letters to numbers
    for i in text:
        code.append(((ord(i)-97)**e)%n)
        
    return code 

def decryption(text, e, n, phi):

    d = 0

    #calculating d - secret key
    while True:
        d=d+1
        if e*d%phi==1:
            break
    
    print("Private key: d = ", d)
    decode = []

    #decoded numbers
    for i in text:
        decode.append(pow(i,d)%n)

    return decode

def test(text, e, n, phi):

    myCode = encryption(text, e, n)
    print("My coded sequence: ", end = '')

    for i in myCode:
        print(i, end = ' ')

    print('')

    myDecode = decryption(myCode, e, n, phi)
    print("My decoded sequence: ", end = '')
    DecodedText = ''

    for i in myDecode:
            i_char = chr(i+97)
            DecodedText += i_char
            print(i_char, end = '' )

    print('')
    
    if(text in DecodedText):
        print("Program correctly coded and decoded sequence.")
    else:
        print("Test failed. The sequences are not the same.")

def main():

    mode = sys.argv[1]

    #public keys - prime numbers
    for i in range(2,5):
        #checking if p,q,e arguments are prime numbers
        if(checkingPrimeNumbers(int(sys.argv[i]))):
            p = int(sys.argv[2])
            q = int(sys.argv[3])
            e = int(sys.argv[4])
        #if they are not, program will raise exception
        else:
            raise Exception ('Wrong ', i, 'program argument. You have to type prime number.')
    
    n = p*q
    #Euler function
    
    phi = (p-1)*(q-1)

    #e, phi have to be coprime numbers

    if(checkingCoprimeNumbers(phi, e)==False):
        raise Exception ('Wrong argument. Your phi and e have to be coprime numbers.')

    if mode == 'encryption':
    
        text = sys.argv[5]
        myCode = encryption(text, e, n)
        print("Coded sequence: ", end = '')

        #printing coded sequence
        for i in myCode:
            print(i, end = ' ')
        
    elif mode == 'decryption':

        #converting program aruments to array
        sequenceLen = len(sys.argv) 
        sequence = []

        for i in range(5, sequenceLen):
            sequence.append(int(sys.argv[i]))

        #decoding numbers 
        myDecode = decryption(sequence, e, n, phi)
        print("Decoded sequence: ", end = '') 

        #converting numbers to letters and printing decoded sequence
        for i in myDecode:
            print(chr(i+97), end='')

    elif mode == 'test':
        text = sys.argv[5]
        test(text, e, n, phi)
    else:
        raise Exception ('Wrong mode. Please use encryption, decryption or test.')

if __name__ == '__main__':
    main()
