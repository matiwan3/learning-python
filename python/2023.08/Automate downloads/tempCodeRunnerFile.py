
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
