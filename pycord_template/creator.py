import shutil

import os
import shutil
import subprocess

def download_from_git():
    """Gets the newest version from github, git is required"""

    subprocess.run(f"cd {os.getcwd()}", shell=True)
    subprocess.run("git clone https://github.com/Cryxyemi/Python-better-bot-Template.git", shell=True)

    print(f"Created template in {os.getcwd()}")