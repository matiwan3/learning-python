import os
import sys
import datetime
import subprocess

# Specify the repository location
repo_location = r"C:\Users\mateu\Documents\GitHub\local_projects\python\2023.08\Auto git commit"
txt_file_path = os.path.join(repo_location, "autoCommit.txt")
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "ac.ico")
else:
    icon_path = "ac.ico"

def get_next_version(version):
    major, minor = version.split(".")
    next_minor = int(minor) + 1
    return f"{major}.{next_minor}"

def commit_changes(commit_message):
    subprocess.run(["git", "add", "autoCommit.txt"])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])

def main():
    # Specify the repository location
    repo_location = r"C:\Users\mateu\Documents\GitHub\local_projects\python\2023.08\Auto git commit"

    # Change the current working directory to the repository location
    os.chdir(repo_location)

    # Read the current version from the first line of the file
    txt_file_path = os.path.join(repo_location, "autoCommit.txt")
    current_version = ""
    if os.path.exists(txt_file_path):
        with open(txt_file_path, "r") as txt_file:
            lines = txt_file.readlines()
            if lines:
                current_version = lines[0].strip()

    # Get the next version
    next_version = get_next_version(current_version)

    # Read existing commit dates from the file
    existing_commit_dates = []
    if len(lines) > 1:
        existing_commit_dates = [line.strip() for line in lines[1:]]

    # Append the current date and time to the list of commit dates
    existing_commit_dates.append(datetime.datetime.now().strftime("%d.%m.%Y:%H:%M"))

    # Update the file with the new version and the concatenated commit dates
    with open(txt_file_path, "w") as txt_file:
        txt_file.write(next_version + "\n")
        txt_file.write(" / ".join(existing_commit_dates) + "\n")

    # Commit the change with the new version
    commit_message = f"{next_version}: Commit at {datetime.datetime.now().strftime('%d.%m.%Y:%H:%M')}"
    commit_changes(commit_message)

if __name__ == "__main__":
    main()