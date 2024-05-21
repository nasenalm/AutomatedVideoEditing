import dropbox


def upload_mp4_to_dropbox(local_file_path, remote_file_path, access_token):
    try:
        # Create a Dropbox object
        dbx = dropbox.Dropbox(access_token)

        # Open the MP4 file in binary mode
        with open(local_file_path, 'rb') as f:
            # Upload the file to Dropbox
            dbx.files_upload(f.read(), remote_file_path)

        print(f"File '{local_file_path}' uploaded to Dropbox as '{remote_file_path}'")
    except dropbox.exceptions.AuthError as e:
        print(f"Error connecting to Dropbox: {e}")
    except Exception as e:
        print(f"Error uploading file to Dropbox: {e}")

