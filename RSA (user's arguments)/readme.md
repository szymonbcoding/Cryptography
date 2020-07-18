Operations of RSA algorithm is described in link below:
https://simple.wikipedia.org/wiki/RSA_algorithm

It's version. which let user to choose arguments and check if they are correct with RSA algorithm. 

Program can be runned in three modes:

a) encryption - coding your sequence,

b) decryption - decoding coded sequence,

c) test - checking correctness of coding.


Arguments, that are needed to run program, are depended on program's mode.
Each mode of program needs:

1. argument - mode 

2,3,4. arguments - p,q,e - they are create public key

Later, each mode of program needs different data for next arguments.

a) encryption

5. argument - sequence (in quotes)

Example command:

python rsa.py encryption 29 19 5 "szymon"

b) decryption 

Coded sequence is represented as series of numbers, so you can put as many arguments as you need.

For exmaple, if your sequence has 6 characters, so your last arguments will be 10.

python rsa.py decryption 29 19 5 189 252 123 331 48 470

c) test 

Just like for encryption, exmaple command:

python rsa.py encryption 29 19 5 "szymon"

Remember about fact that your arguments p,q,e (public key) have to prime numbers
and e with phi (which equals to (p-1)*(q-1) ) have to be coprime numbers.

