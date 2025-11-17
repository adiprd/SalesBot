
#!/usr/bin/env python3
import subprocess
import sys
import os

def install_requirements():
    print("📦 Installing Python requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "backend/app/requirements.txt"])
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False
    return True

def start_backend():
    print("🚀 Starting FastAPI backend...")
    os.chdir("backend/app")
    try:
        subprocess.call([sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])
    except KeyboardInterrupt:
        print("\n⏹️  Backend stopped")

if __name__ == "__main__":
    if install_requirements():
        start_backend()
