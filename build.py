import PyInstaller.__main__
import os

if __name__ == "__main__":
    PyInstaller.__main__.run([
        "main.py",
        "--onefile",
        "--name", "regex-engine",
        "--add-data", f"regex_engine{os.pathsep}regex_engine",
    ])
