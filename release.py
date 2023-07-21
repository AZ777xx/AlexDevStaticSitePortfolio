import subprocess

def git_subtree_push():
    command = ["git", "subtree", "push", "--prefix", "site", "origin", "gh-pages"]
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