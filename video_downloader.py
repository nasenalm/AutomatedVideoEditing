import pytube

link_test = "https://www.youtube.com/watch?v=2pMsYSR7g78"


def video_download(link):
    yt = pytube.YouTube(link)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Specify the folder path where you want to save the video
    download_folder = "full-video-download-folder-dir" # this folder will be accessed in video_chop.py

    # Download the video to the specified folder
    print("downloading...")
    stream.download(download_folder)
    print("video finished downloading.")
