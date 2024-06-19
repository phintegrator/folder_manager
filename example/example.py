from folder_manager import Folder, FolderError

def main():
    # Use a Windows-style path (ensure the path is suitable for your system)
    folder_path = r"C:\test"

    # Create a Folder instance
    folder = Folder(folder_path)

    # 1. Create a Folder
    try:
        result = folder.create_folder()
        print(f"Folder created: {result}")  # Returns True if the folder was created successfully
    except FolderError as e:
        print(f"Error: {e}")

    # 2. List Files in the Folder
    try:
        files = folder.list_files()
        print(f"Files in folder: {files}")  # Returns a list of filenames in the folder
    except FolderError as e:
        print(f"Error: {e}")

    # 3. Count Files in the Folder
    try:
        file_count = folder.count_files()
        print(f"Number of files: {file_count}")  # Returns the number of files in the folder
    except FolderError as e:
        print(f"Error: {e}")

    # 4. Create a File
    file_name = "example_file.txt"
    file_content = "Hello, World!"
    try:
        result = folder.create_file(file_name, file_content)
        print(f"File created: {result}")  # Returns True if the file was created successfully
    except FolderError as e:
        print(f"Error: {e}")

    # 5. Check if the File Exists
    if folder.file_exists(file_name):
        print(f"File '{file_name}' exists.")
    else:
        print(f"File '{file_name}' does not exist.")

    # 6. List Files again to see the new file
    try:
        files = folder.list_files()
        print(f"Files in folder after creating file: {files}")  # Returns a list of filenames in the folder
    except FolderError as e:
        print(f"Error: {e}")

    # 7. Count Files again to see the new count
    try:
        file_count = folder.count_files()
        print(f"Number of files after creating file: {file_count}")  # Returns the number of files in the folder
    except FolderError as e:
        print(f"Error: {e}")

    # 8. Delete the File
    try:
        result = folder.delete_file(file_name)
        print(f"File deleted: {result}")  # Returns True if the file was deleted successfully
    except FolderError as e:
        print(f"Error: {e}")

    # 9. List Files again to see the remaining files
    try:
        files = folder.list_files()
        print(f"Files in folder after deleting file: {files}")  # Returns a list of filenames in the folder
    except FolderError as e:
        print(f"Error: {e}")

    # 10. Delete the Folder
    try:
        result = folder.delete_folder()
        print(f"Folder deleted: {result}")  # Returns True if the folder was deleted successfully
    except FolderError as e:
        print(f"Error: {e}")

    # 11. Check if the Folder Exists
    if folder.folder_exists():
        print(f"Folder '{folder_path}' exists.")
    else:
        print(f"Folder '{folder_path}' does not exist.")

if __name__ == "__main__":
    main()
