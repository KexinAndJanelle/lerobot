import subprocess

def get_hf_user():
    HF_USER = ""
    try:
        # Execute the commands in a shell
        # The 'shell=True' argument is crucial for shell features like parameter expansion
        # The 'check=True' argument will raise an exception if the command fails
        # The 'capture_output=True' will capture stdout and stderr
        HF_USER = subprocess.run(
            "HF_USER=$(hf auth whoami | head -n 1); echo $HF_USER",
            shell=True,
            check=True,
            capture_output=True,
            text=True  # Decode output as text
        ).stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"HF_USER - Error executing shell command: {e}")
        print(f"Stderr: {e.stderr}")
    return HF_USER
