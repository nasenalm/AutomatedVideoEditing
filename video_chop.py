from moviepy.editor import *

import os


def chop_and_save():
    def get_video_length(video_path):
        """
        Get the length (duration) of a video file.
        Returns:
        - float: The length of the video in seconds.
        """
        try:
            video_clip = VideoFileClip(video_path)
            duration = video_clip.duration
            video_clip.close()
            return duration
        except Exception as e:
            print(f"Error: {e}")
            return None

    def find_any_file(folder_path):
        """
        Find the filename of any file within a specified folder.

        Returns:
        - str or None: The filename of the found file, or None if no file is found.
        """
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                return file
        return None

    def save_video_to_folder():

        """
        Save a video to a specified output folder.

        Parameters:
        - input_path (str): The path to the input video file.
        - output_folder (str): The path to the output folder.
        """
        output_folder = "chopped-video-dir" # this same directory will be accessed in main.py
        try:
            for i in range(30, duration + 1, 30):
                print(f"Processing subclip {i - 30} to {i}")

                # Ensure the subclip range is within the valid bounds
                start_time = max(0, i - 30)
                end_time = min(i, duration)

                video = VideoFileClip(video_path).subclip(start_time, end_time)

                output_path = f"{output_folder}/output_video_{i}.mp4"
                video.write_videofile(output_path, codec="libx264", audio_codec="aac")
                video.close()
                print(f"Video saved to: {output_path}")
        except Exception as e:
            print(f"Error: {e}")

    folder_path = "full-video-download-folder-dir" #created in video_downloader.py
    any_file = find_any_file(folder_path)

    if any_file:
        print(f"A file was found: {any_file}")
    else:
        print("No file found in the specified folder.")

    video_path = "full-video-download-folder-dir/" + any_file
    duration = int(get_video_length(video_path))
    print(duration)
    save_video_to_folder()