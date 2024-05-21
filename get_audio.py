from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio_from_video(video_file_path, output_audio_path):
    # Load the video clip
    video_clip = VideoFileClip(video_file_path)

    # Extract audio from the video clip
    audio_clip = video_clip.audio

    # Save the audio clip to a new file
    audio_clip.write_audiofile(output_audio_path)

    # Close the video clip
    video_clip.close()


