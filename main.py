import subprocess
def run_mkdocs_serve():
    subprocess.run(["mkdocs", "serve"])

if __name__ == "__main__":
    run_mkdocs_serve()