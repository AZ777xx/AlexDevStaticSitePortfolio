import subprocess

def git_subtree_pull():
    # Pull the latest changes from the remote gh-pages branch into the site folder
    pull_command = ["git", "subtree", "pull", "--prefix", "site", "origin", "gh-pages"]
    subprocess.run(pull_command)


def git_subtree_push():
    # Call the pull function before pushing
   # git_subtree_pull()

    # Push the changes to the remote repository

    push_command = ["git", "subtree", "push", "--prefix", "site", "origin", "gh-pages"]
    push_result = subprocess.run(push_command, capture_output=True, text=True)

    # Print the push command output
    print("Push Command Output:")
    print(push_result.stdout)

    # Print the error output if there's any
    if push_result.stderr:
        print("Error Output:")
        print(push_result.stderr)


def git_subtree_force_push():
    # Split the 'site' folder into a new branch
    split_command = ["git", "subtree", "split", "--prefix=site", "origin", "gh-pages"]
    split_result = subprocess.run(split_command, capture_output=True, text=True)
    if split_result.returncode != 0:
        print("Error splitting subtree:")
        print(split_result.stdout)
        print(split_result.stderr)
        return

    # Extract the commit hash from the split result
    commit_hash = split_result.stdout.strip()

    # Force push the subtree split to the remote gh-pages branch
    force_push_command = ["git", "push", "origin", f"{commit_hash}:gh-pages", "--force"]
    force_push_result = subprocess.run(force_push_command, capture_output=True, text=True)

    # Check the results and print them out
    print("Force Push Command Output:")
    print(force_push_result.stdout)
    if force_push_result.stderr:
        print("Error Output:")
        print(force_push_result.stderr)
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
    git_subtree_force_push()
    print("https://github.com/AZ777xx/AlexDevStaticSitePortfolio/settings/pages")
    print("Use this site: alexanderzhx.is-a.dev")