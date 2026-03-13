import sys
import subprocess

# Makes sure a log file is provided
if len(sys.argv) < 2:
    print("Error: log file name not provided")
    sys.exit(1)

logFile = sys.argv[1]

# Launch logger program
loggerProcess = subprocess.Popen(
    ['python', 'encryption.py'],
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
    print("Commands: password, encrypt, decrypt, history, quit\n")

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
