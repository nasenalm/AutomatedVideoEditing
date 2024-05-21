import os

import content_analysis
import video_chop
import video_downloader
import video_editor
import get_audio
import text
import save_dropbox
import random_file
import subtitle_creation

# main.py
def main():
    print("main is running...")

    # Ask for link.
    # Code will create and save to dropbox for every 30 second increment of video.
    link_test = "" # youtube video to be repurposed
    video_downloader.video_download(link_test)

    # Chops videos into 30 second clips
    video_chop.chop_and_save()

    # Speech to text --> analysis
    # loop through mp4 files in 30 second clips folder

    file_list = os.listdir("chopped-video-dir") # local directory where chopped video is saved (must be manually created)

    for file_name in file_list:
        # You can perform any actions on the file here
        # For example, print the file name
        print(file_name)
        video_file_path = "chopped-video-dir" + file_name

        # Specify the desired output audio file path (send to audio folder)
        output_audio_path = "audio-file-folder-dir" + file_name + ".wav"

        # Call the function to extract audio from the video
        get_audio.extract_audio_from_video(video_file_path, output_audio_path)
        print(f"Audio extracted and saved to: {output_audio_path}")

        # Call the function to convert speech to text (result is a string with text from video)
        result = text.convert_wav_to_text(output_audio_path)
        os.remove(output_audio_path) # remove used audio file from computer


        # Analyze text content to see if it invokes any emotional response from the viewer videos with analizer
        yes_no = content_analysis.text_analyzer(result)
        print(yes_no)
        if str(yes_no) == "ChatCompletionMessage(content='Yes.', role='assistant', function_call=None, tool_calls=None)":
            # should stack each 30 second clip with a random gameplay video pre-downloaded. Once used, the 30 second
            # videos should be deleted from folder.

            # find random gameplay video:
            folder_path = "video-game-30sec-dir"
            random_filename = random_file.get_random_file(folder_path)

            if random_filename:
                print(f"Randomly selected file: {random_filename}")
            else:
                print("No files found in the specified folder or the folder does not exist.")

            video_editor.stack_videos_with_audio(
                video_file_path,
                "" + folder_path + "/" + random_filename,
                "completed-video-dir", "ready_" + file_name + ".mp4")
            print("A video has been saved to folder: ready")
            os.remove(video_file_path)
            # save video to dropbox from ready (for future it may be smart to remove ready folder and save direct
            # to dropbox) for now videos will be saved to folder and dropbox to avoid losing videos if space fills in
            # dropbox account
            save_dropbox.upload_mp4_to_dropbox("completed-video-dir" + "ready_" + file_name + ".mp4",
                                               "/Completed TikTok/ready_" + file_name + ".mp4",
                                                'dropbox-access-token'
                                               )

        elif str(yes_no) == "ChatCompletionMessage(content='No.', role='assistant', function_call=None, tool_calls=None)":
            # remove 30 second clip
            os.remove(video_file_path)
            print("bad video deleted")
        else:
            print("Sorry, there was an error analyzing audio as text.")
        print(file_name, " finished.")
    print("Program finished running successfully!")

# main.py
if __name__ == "__main__":
    print("Program Starting...")
    main()
