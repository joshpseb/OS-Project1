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
                    # Prints numbered list form 1 to n
                    for i, savedString in enumerate(history):
                        print(f"{i + 1}. {savedString}")
                    
                    # User can exit history if they want
                    print("0. Exit history and enter a new string")
                    
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

    elif command == "decrypt":
        
        loggerProcess.stdin.write("CMD User selected decrypt command.\n")
        loggerProcess.stdin.flush()

    elif command == "history":
        
        loggerProcess.stdin.write("CMD User selected history command.\n")
        loggerProcess.stdin.flush()
    
    else:
        print("Invalid command")

