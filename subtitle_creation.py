import speech_recognition as sr
from moviepy.video.io.VideoFileClip import VideoFileClip

# this sucks
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            transcription = recognizer.recognize_google(audio)
            return transcription
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def create_srt_file(subtitles, output_path):
    with open(output_path, 'w') as f:
        for i, subtitle in enumerate(subtitles, start=1):
            f.write(f"{i}\n")
            f.write(f"{subtitle['start_time']} --> {subtitle['end_time']}\n")
            f.write(f"{subtitle['text']}\n\n")

def process_video(input_path, srt_output_path, clip_duration=2):
    print("starting function: process_video")
    video_clip = VideoFileClip(input_path)
    total_duration = video_clip.duration

    subtitles = []
    for start_time in range(0, int(total_duration), clip_duration):
        end_time = min(start_time + clip_duration, total_duration)
        clip_path = f"temp_clip_{start_time}_{end_time}.mp4"

        # Extract 3-second clip
        video_clip.subclip(start_time, end_time).write_videofile(clip_path, codec='libx264', audio_codec='aac')
        print("3 second clip created")
        # Transcribe the audio of the clip
        audio_path = f"temp_audio_{start_time}_{end_time}.wav"
        clip_audio = video_clip.audio.subclip(start_time, end_time)
        clip_audio.write_audiofile(audio_path, codec='pcm_s16le')

        transcription = transcribe_audio(audio_path)
        subtitles.append({
            'start_time': start_time,
            'end_time': end_time,
            'text': transcription
        })
        print("subtitle section appended")

    # Save the transcriptions as an SRT file
    create_srt_file(subtitles, srt_output_path)
