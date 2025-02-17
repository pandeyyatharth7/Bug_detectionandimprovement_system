import git
import os
import shutil

def clone_repo(repo_url, local_path):
    if os.path.exists(local_path):
        if os.listdir(local_path):
            print(f"Directory {local_path} is not empty. Please choose an empty directory or remove its contents.")
            return
    else:
        os.makedirs(local_path)
    
    git.Repo.clone_from(repo_url, local_path)
    print(f"Cloned {repo_url} to {local_path}")

repo_url = 'https://github.com/Vdv26/codebert-bug-finder.git'
local_path = "C:/Users/Asus/Desktop/Hackathons/Makethon' 25/blabla"
clone_repo(repo_url, local_path)