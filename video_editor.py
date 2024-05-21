import os
from moviepy.editor import VideoFileClip, clips_array

def stack_videos_with_audio(video_path1, video_path2, output_folder, output_filename):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load video clips
    clip1 = VideoFileClip(video_path1)
    clip2 = VideoFileClip(video_path2)

    # Ensure both clips have the same duration
    min_duration = min(clip1.duration, clip2.duration)
    clip1 = clip1.subclip(0, min_duration)
    clip2 = clip2.subclip(0, min_duration)

    # Extract audio from the first video
    audio_clip1 = clip1.audio

    # Mute the audio in the second video
    clip2 = clip2.set_audio(None)

    # Stack videos vertically
    stacked_clips = clips_array([[clip1.set_audio(audio_clip1)], [clip2]])

    # Set the output file path
    output_path = os.path.join(output_folder, output_filename)

    # Write the result to the output file
    stacked_clips.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close the video clips
    clip1.close()
    clip2.close()
