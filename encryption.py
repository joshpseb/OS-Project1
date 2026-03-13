import sys

def vigenereEncrypt(text, key):
    res = []

    for i, char in enumerate(text):
        # Convert letters to numbers 0-25
        plain = ord(char) - ord('A')
        shift = ord(key[i % len(key)]) - ord('A')

        cipher = (plain + shift + 26) % 26
        res.append(chr(cipher + ord('A')))

    return "".join(res)

def vigenereDecrypt(text, key):
    res = []

    for i, char in enumerate(text):
        # Convert letters to numbers 0-25
        cipher = ord(char) - ord('A')
        shift = ord(key[i % len(key)]) - ord('A')
        
        # Reverse the cipher math and convert back to a letter
        plain = (cipher - shift + 26) % 26
        res.append(chr(plain + ord('A')))
        
    return "".join(res)

def main():
    passkey = None

    for line in sys.stdin:

        # gets rid of whitespace
        line = line.strip()

        # only splits once based on first space
        parts = line.split(maxsplit=1)
        command = parts[0]

        if len(parts) > 1:
            argument = parts[1]
        else:
            argument = ""

        if command == "QUIT":
            break

        elif command == "PASS":
            passkey = argument
            print("RESULT: New passkey set")
        
        elif command == "ENCRYPT":
            if not passkey:
                print("ERROR: Passkey not set")
            else:
                res = vigenereEncrypt(argument, passkey)
                print("RESULT: ", res)

        
        elif command == "DECRYPT":
            if not passkey:
                print("ERROR: Passkey not set")
            else:
                res = vigenereDecrypt(argument, passkey)
                print("RESULT: ", res)
        
        else:
            print("ERROR: Invalid command")

if __name__ == "__main__":
    main()