import sys
import subprocess

# Makes sure a log file is provided
if len(sys.argv) < 2:
    print("Error: log file name not provided")
    sys.exit(1)

logFile = sys.argv[1]

# Launch logger program
loggerProcess = subprocess.Popen(
    ['python', 'logger.py', logFile],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
    text = True
)

# Launch encryption program
encryptionProcess = subprocess.Popen(
    ['python', 'encryption.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
    text = True
)

# Log start of the driver program
loggerProcess.stdin.write("START Driver program started.\n")

history = []

while True:
    print("\n---Main Menu---")
    print("Commands: password, encrypt, decrypt, history, quit")

    command = input("Enter a command: ").strip().lower()

    if command == "quit":
        # Log driver program exit
        loggerProcess.stdin.write("EXIT Stopping driver program.\n")
        loggerProcess.stdin.flush()
            
        # 2. Send QUIT to the encryption program 
        encryptionProcess.stdin.write("QUIT\n")
        encryptionProcess.stdin.flush()
            
        # 3. Send QUIT to the logger program 
        loggerProcess.stdin.write("QUIT\n")
        loggerProcess.stdin.flush()
            
        # Clean up: wait for the subprocesses to actually finish closing
        encryptionProcess.wait()
        loggerProcess.wait()
            
        print("Exiting...")
        break

    elif command == "password":

        loggerProcess.stdin.write("CMD User selected password command.\n")
        loggerProcess.stdin.flush()

        choice = ""
        while choice not in ['1', '2']:
            print("\n1. Use a string from history")
            print("2. Enter a new string")
            choice = input("Select an option (1 or 2): ").strip()

        password = ""

        # Select string from history
        if choice == '1':
            if len(history) == 0:
                print("History is empty, must use new string.")
                choice = '2'
            else:
                while True:
                    print("\n---History---")
                    # User can exit history if they want
                    print("0. Exit history and enter a new string")
                    # Prints numbered list form 1 to n
                    for i, savedString in enumerate(history):
                        print(f"{i + 1}. {savedString}")
                    
                    histNum = input("Select a number: ")
                    
                    if histNum == '0':
                        choice = '2'
                        break
                    elif histNum.isdigit() and 1 <= int(histNum) <= len(history):
                        password = history[int(histNum) - 1]
                        break
                    else:
                        print("Invalid number, try again.")

        # New string 
        if choice == '2':
            while True:
                password = input("Enter a new password (letters only): ").strip()
                
                # Make sure only letters used 
                if password.isalpha():
                    break
                else:
                    print("Error: Password must only have letters.")

        # Make input case insensitive
        password = password.upper()

        # Send command to encryption program
        encryptionProcess.stdin.write(f"PASS {password}\n")
        encryptionProcess.stdin.flush()

        # Read the response back from the encryption program
        result = encryptionProcess.stdout.readline().strip()
        print("New password set.")

        # Log the result without logging the password
        loggerProcess.stdin.write(f"RESULT Password set process completed with: {result}\n")
        loggerProcess.stdin.flush()

    elif command == "encrypt":
        
        loggerProcess.stdin.write("CMD User selected encrypt command.\n")
        loggerProcess.stdin.flush()

        choice = ""
        while choice not in ['1', '2']:
            print("\n1. Use a string from history")
            print("2. Enter a new string")
            choice = input("Select an option (1 or 2): ").strip()

        text = ""

        # Select string from history
        if choice == '1':
            if len(history) == 0:
                print("History is empty, must use new string.")
                choice = '2'
            else:
                while True:
                    print("\n---History---")
                    # User can exit history if they want
                    print("0. Exit history and enter a new string")
                    # Prints numbered list form 1 to n
                    for i, savedString in enumerate(history):
                        print(f"{i + 1}. {savedString}")
                    
                    histNum = input("Select a number: ").strip()
                    
                    if histNum == '0':
                        choice = '2'
                        break
                    elif histNum.isdigit() and 1 <= int(histNum) <= len(history):
                        text = history[int(histNum) - 1]
                        break
                    else:
                        print("Invalid number, try again.")

        # New string 
        if choice == '2':
            while True:
                text = input("Enter a string to encrypt (letters only): ").strip()
                
                # Make sure only letters used 
                if text.isalpha():
                    # Save the entered string to history
                    history.append(text.upper())
                    break
                else:
                    print("Error: Input must only have letters.")

        # Make input case insensitive
        text = text.upper()

        # Send command to encryption program
        encryptionProcess.stdin.write(f"ENCRYPT {text}\n")
        encryptionProcess.stdin.flush()

        # Read the response back
        result = encryptionProcess.stdout.readline().strip()
        print(result)

        # If it encrypts, get the cipher and save it to history
        if result.startswith("RESULT") and len(result.split()) > 1:
            cipher = result.split(maxsplit=1)[1]
            history.append(cipher)

        # Log the result
        loggerProcess.stdin.write(f"RESULT Encrypt process completed with: {result}\n")
        loggerProcess.stdin.flush()

    elif command == "decrypt":
        
        loggerProcess.stdin.write("CMD User selected decrypt command.\n")
        loggerProcess.stdin.flush()

        choice = ""
        while choice not in ['1', '2']:
            print("\n1. Use a string from history")
            print("2. Enter a new string")
            choice = input("Select an option (1 or 2): ").strip()

        text = ""

        # Select string from history
        if choice == '1':
            if len(history) == 0:
                print("History is empty, must use new string.")
                choice = '2'
            else:
                while True:
                    print("\n---History---")
                    # User can exit history if they want
                    print("0. Exit history and enter a new string")
                    # Prints numbered list form 1 to n
                    for i, savedString in enumerate(history):
                        print(f"{i + 1}. {savedString}")
                    
                    histNum = input("Select a number: ").strip()
                    
                    if histNum == '0':
                        choice = '2'
                        break
                    elif histNum.isdigit() and 1 <= int(histNum) <= len(history):
                        text = history[int(histNum) - 1]
                        break
                    else:
                        print("Invalid number, try again.")

        # New string 
        if choice == '2':
            while True:
                text = input("Enter a string to decrypt (letters only): ").strip()
                
                # Make sure only letters used 
                if text.isalpha():
                    # Save the entered string to history
                    history.append(text.upper())
                    break
                else:
                    print("Error: Input must only have letters.")

        # Make input case insensitive
        text = text.upper()

        # Send command to encryption program
        encryptionProcess.stdin.write(f"DECRYPT {text}\n")
        encryptionProcess.stdin.flush()

        # Read the response back
        result = encryptionProcess.stdout.readline().strip()
        print(result)

        # If decrypts, get the plain text and save it to history
        if result.startswith("RESULT") and len(result.split()) > 1:
            plainText = result.split(maxsplit=1)[1]
            history.append(plainText)

        # Log the result
        loggerProcess.stdin.write(f"RESULT Decrypt process completed with: {result}\n")
        loggerProcess.stdin.flush()

    elif command == "history":
        
        loggerProcess.stdin.write("CMD User selected history command.\n")
        loggerProcess.stdin.flush()

        print("\n---Session History---")
        if len(history) == 0:
            print("History is currently empty.")
        else:
            for i, savedString in enumerate(history):
                print(f"{i + 1}. {savedString}")
                
        loggerProcess.stdin.write("RESULT History displayed successfully.\n")
        loggerProcess.stdin.flush()
    
    else:
        print("Invalid command")

