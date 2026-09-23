import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("SSH_HOST")
user = os.getenv("SSH_USER")

command = ["ssh", user + "@" + host, "echo hello"]
result = subprocess.run(command, capture_output=True, text=True)

if result.returncode == 0:
    print ("Success")
    print (result.stdout)
else:
    print ("Command failed")
    print (result.stderr)

