import sys

def vigenereEncrypt(text, key):
    res = []

    for i, char in enumerate(text):
        # Convert letters to numbers 0-25
        plain = ord(char) - ord('A')
        shift = ord(key[i % len(key)]) - ord('A')

        # Add the shift for each number and convert back to char
        cipher = (plain + shift + 26) % 26
        res.append(chr(cipher + ord('A')))

    return "".join(res)

def vigenereDecrypt(text, key):
    res = []

    for i, char in enumerate(text):
        # Convert letters to numbers 0-25
        cipher = ord(char) - ord('A')
        shift = ord(key[i % len(key)]) - ord('A')
        
        # Subtract the shift for each number and convert back to char
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
            if not argument:
                print("ERROR Passkey argument missing")
            else:
                passkey = argument
                print("RESULT")
        
        elif command == "ENCRYPT":
            if not passkey:
                print("ERROR Passkey not set")
            elif not argument:
                print("ERROR Nothing to encrypt")
            else:
                res = vigenereEncrypt(argument, passkey)
                print("RESULT", res)

        
        elif command == "DECRYPT":
            if not passkey:
                print("ERROR Passkey not set")
            elif not argument:
                print("ERROR Nothing to decrypt")
            else:
                res = vigenereDecrypt(argument, passkey)
                print("RESULT", res)
        
        else:
            print("ERROR Invalid command")

        # Makes sure every response is outputted from the pipe instantly.
        sys.stdout.flush()


if __name__ == "__main__":
    main()