This project was created to repurpose youtube videos as short form content for TikTok, Instagram Reels, or Youtube Shorts.

Functionality: this code will utilize the moviepy and pytube libraries, and gpt-3.5-turbo with the openai api to stack 30 second clips of a specified youtube video
(deemed interesting by chatgpt prompting) on top of a specified video downloaded locally to your computer. It will then save the completed videos to a local folder 
on your computer, and to a dropbox account for access on a variety of devices to upload from. 

Setup (files): 

Create a main folder locally on your computer with 6 subfolders.

example:
MainFolder
- completed videos
- audio
- 30 second clips (for yt video)
- pre downloaded 30 second clips
- subtitles
- uncut videos

folder pathnames must be then manually inserted in video_downloader.py, video_chop.py, and main.py

Setup (dropbox/openai): dropbox access token must be input in main.py line 73, and openai key must be inserted in content_analysis.py line 6

Note: Although there is a file and associated folder for subtitle creation, it is not actively being implemented as the Google Speech Recognition service is not a
great speech to text model for most use cases on youtube videos.
