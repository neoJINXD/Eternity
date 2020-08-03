import subprocess
import os

path = os.path.dirname(os.path.abspath(__file__))
cmd = "pip install -r " + path + "/requirements.txt"
print(cmd)
subprocess.run(cmd)
