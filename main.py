import subprocess
import os

m3u8_url = str(input("url : "))
output_file = "video_output4.mp4"

command = [
    "ffmpeg",
    "-i", m3u8_url,
    "-c", "copy",
    "-bsf:a", "aac_adtstoasc",
    output_file
]

try:
    print("Starting video download...")
    subprocess.run(command, check=True)
    print(f"Video downloaded successfully as {output_file}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while downloading the video: {e}")
except FileNotFoundError:
    print("ffmpeg is not installed or not in the PATH.")
