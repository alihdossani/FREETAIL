usereq= input(""" "ENC", "DEC" """)

if usereq == "ENC":
        plaintext = input("text:")
        print("sample string: ZRyQbAtHfsWKxNrEMndluJBTXocDkGzOYUaPmCjgFpwqLiISevVh")
        alphabet = input("string 1 must have all letters upper and lower case you can also have numbers: ")+" "
        alphabettwo = input("string 2 must have all letters upper and lower case you can also have numbers: ")+" "
        k = int(input("""key one:"""))
        k1 = int(input("""key two:"""))
        cipherone = ""
        ciphertwo = ""
        for c in plaintext:
            if c in alphabet:
                cipherone += alphabet[(alphabet.index(c)+k) % (len(alphabet))]
        for c in cipherone:
            if c in alphabettwo:
                ciphertwo += alphabettwo[(alphabettwo.index(c)+k1) % (len(alphabettwo))]
        print("message: "+ciphertwo)

if usereq == "DEC":
        plaintext = input("text:")
        print("sample string: ZRyQbAtHfsWKxNrEMndluJBTXocDkGzOYUaPmCjgFpwqLiISevVh")
        alphabet = input("string 1 must have all letters upper and lower case you can also have numbers: ")+" "
        alphabettwo = input("string 2 must have all letters upper and lower case you can also have numbers: ")+" "
        k = int(input("""key one:"""))
        k1 = int(input("""key two:"""))
        cipherone = ""
        ciphertwo = ""
        for c in plaintext:
            if c in alphabet:
                cipherone += alphabettwo[(alphabettwo.index(c)-k1) % (len(alphabettwo))]
        for c in cipherone:
            if c in alphabet:
                ciphertwo += alphabet[(alphabet.index(c)-k) % (len(alphabet))]
        print("message: "+ ciphertwo)