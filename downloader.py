import sys
import os

def run_downloader():
    print("Media Downloader Utility v1.0")
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(f"Processing stream from: {target}")
    else:
        print("Status: Ready. Pass target URL as argument.")

if __name__ == "__main__":
    run_downloader()
