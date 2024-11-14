from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        if highest_res_stream:
            highest_res_stream.download(output_path=save_path)
            print("Video downloaded successfully!")
        else:
            print("No suitable video stream found.")
    except pytube.exceptions.RegexMatchError:
        print("Error: Unable to match YouTube URL structure.")
    except pytube.exceptions.VideoUnavailable:
        print("Error: Video is unavailable or restricted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    else:
        print("No folder selected.")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
