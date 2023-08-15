import os
import shutil

def create_folders(base_folder):
    folders = ["Images", "Documents", "Executables", "Other Extensions", "Video", "Music"]
    for folder in folders:
        folder_path = os.path.join(base_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def sort_files(source_folder, base_folder):
    image_extensions = [".jpeg", ".jpg", ".img", ".png", ".gif"]
    doc_extensions = [".pdf", ".docx"]
    music_extensions = [".mp3", ".3gp"]
    video_extensions = [".mp4", ".mov"]

    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            if ext in image_extensions:
                destination_folder = "Images"
            elif ext in doc_extensions:
                destination_folder = "Documents"
            elif ext == ".exe":
                destination_folder = "Executables"
            elif ext in music_extensions:
                destination_folder = "Music"
            elif ext in video_extensions:
                destination_folder = "Video"
            else:
                destination_folder = "Other Extensions"

            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(base_folder, destination_folder, filename)

            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to '{destination_folder}'")

if __name__ == "__main__":
    downloads_folder = "C:\\Users\\mateu\\Downloads"

    create_folders(downloads_folder)
    sort_files(downloads_folder, downloads_folder)
