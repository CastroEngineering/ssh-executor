import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("SSH_HOST")
user = os.getenv("SSH_USER")

try: 
    command = ["ssh", user + "@" + host, "echo hello"]
    result = subprocess.run(command, capture_output=True, text=True, timeout=4)

    if result.returncode == 0:
        print ("Success")
        print (result.stdout)
    else:
        print ("Command failed")
        print (result.stderr)

except subprocess.TimeoutExpired:
    print("Command timed out")

except Exception:
    print("Something else went wrong")

