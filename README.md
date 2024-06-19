# folder_manager

`folder_manager` is a Python package designed to manage folders and files. It provides functionalities to create, list, count, and delete files and folders, making it a versatile tool for file management. The package is designed to be OS-independent, ensuring compatibility with both Windows and Unix-based systems.

## Features

- **Create Folder:** Create a new folder at a specified path.
- **List Files:** List all files in a specified folder.
- **Count Files:** Count the number of files in a specified folder.
- **Create File:** Create a new file with optional content.
- **Delete File:** Delete a specified file.
- **Delete Folder:** Delete a specified folder and all its contents.
- **Check Folder Exists:** Check if a specified folder exists.
- **Check File Exists:** Check if a specified file exists.

## Requirements

- Python 3.x

## Installation

Install the package via PyPI using pip:

```python
pip install folder_manager
```

## Usage

### Importing the Package

To use the `folder_manager` package, import it into your Python script:

```python
from folder_manager import Folder
```

### Creating an Instance

To create an instance of the `Folder` class, provide the path to the folder you want to manage.

```python
folder = Folder("/path/to/folder")
```

### Examples

1. **Create a Folder:**
    
    ```python
    folder = Folder("/path/to/folder")
    try:
        result = folder.create_folder()
        print(result)  # Returns True if the folder was created successfully
    except FolderError as e:
        print(e)
    ```
    
2. **List Files in a Folder:**
    
    ```python
    folder = Folder("/path/to/folder")
    try:
        files = folder.list_files()
        print(files)  # Returns a list of filenames in the folder
    except FolderError as e:
        print(e)
    ```
    
3. **Count Files in a Folder:**
    
    ```python
    folder = Folder("/path/to/folder")
    try:
        file_count = folder.count_files()
        print(f"Number of files: {file_count}")  # Returns the number of files in the folder
    except FolderError as e:
        print(e)
    ```
    
4. **Create a File:**
    
    ```python
    folder = Folder("/path/to/folder")
    try:
        result = folder.create_file("file.txt", "Hello, World!")
        print(result)  # Returns True if the file was created successfully
    except FolderError as e:
        print(e)
    ```
    
5. **Delete a File:**
    
    ```python
    folder = Folder("/path/to/folder")
    try:
        result = folder.delete_file("file.txt")
        print(result)  # Returns True if the file was deleted successfully
    except FolderError as e:
        print(e)
    ```
    
6. **Delete a Folder:**
    
    ```python
    folder = Folder("/path/to/folder")
    try:
        result = folder.delete_folder()
        print(result)  # Returns True if the folder was deleted successfully
    except FolderError as e:
        print(e)
    ```
    
7. **Check if a Folder Exists:**
    
    ```python
    folder = Folder("/path/to/folder")
    if folder.folder_exists():
        print("Folder exists.")
    else:
        print("Folder does not exist.")
    ```
    
8. **Check if a File Exists:**
    
    ```python
    folder = Folder("/path/to/folder")
    if folder.file_exists("file.txt"):
        print("File exists.")
    else:
        print("File does not exist.")
    ```
    

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

[Javer Valino](https://github.com/phintegrator)

## Acknowledgments

- Thanks to the open-source community for providing the tools and inspiration for this project.
- Special thanks to all contributors and users of the package.