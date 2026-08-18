
import sys
import site
import os

def venv_detect() -> None:

    if sys.base_prefix == sys.prefix:
        status: tuple = ("You're still plugged in", False)
    else:
        status = ("Welcome to the construct", True)
    
    print(f"\nMATRIX STATUS: {status[0]}\n")
    print(f"Current Python: {sys.executable}")

    if status[1]:
        print(f"Virtual Environment: \
{os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment! \
Safe to install packages without affecting the global system\n")
        print(f"Package instalation path:\n\
{site.getsitepackages()[0]}")
    else:
        print(f"Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!\n\
The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")


    



if __name__ == "__main__":
    venv_detect()