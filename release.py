import subprocess

def git_subtree_pull():
    # Pull the latest changes from the remote gh-pages branch into the site folder
    pull_command = ["git", "subtree", "pull", "--prefix", "site", "origin", "gh-pages"]
    subprocess.run(pull_command)


def git_subtree_push():
    # Call the pull function before pushing
   # git_subtree_pull()

    # Push the changes to the remote repository
    push_command = ["git", "subtree", "commit", "--prefix", "site", "origin", "gh-pages"]
    subprocess.run(push_command)
    push_command = ["git", "subtree", "push", "--prefix", "site", "origin", "gh-pages"]
    push_result = subprocess.run(push_command, capture_output=True, text=True)

    # Print the push command output
    print("Push Command Output:")
    print(push_result.stdout)

    # Print the error output if there's any
    if push_result.stderr:
        print("Error Output:")
        print(push_result.stderr)
def mkdocs_build():
    command = ["mkdocs", "build"]
    try:
        # Run the command using subprocess
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Check the command output and handle it as needed
        if result.stdout:
            print("Command Output:")
            print(result.stdout)

        if result.stderr:
            print("Error Output:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print("Error occurred while executing the command:")
        print(e.stderr)
if __name__ == "__main__":
    mkdocs_build()
    git_subtree_push()