import sys

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