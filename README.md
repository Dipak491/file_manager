# File Manager Application

A cross-platform desktop application built with Python and Tkinter that helps you organize and manage files based on their extensions. This tool makes it easy to browse directories and filter files by type.

## Features

- 🗂️ GUI-based file management interface
- 📂 Easy directory browsing
- 🔍 File filtering by type:
  - 🎵 Music (.mp3, .wav, .flac)
  - 🎥 Video (.mp4, .mkv, .avi)
  - 🖼️ Images (.jpg, .jpeg, .png, .gif)
  - 📦 Archives (.zip, .rar, .7z)
  - 📄 Documents (.pdf, .docx, .txt)
  - 📁 All files (*.*)
- 📊 File details (size and modified date)
- 💾 Export filtered file list to CSV/TXT
- 🖱️ Double-click to open files

## Installation

### Method 1: Running from Source

1. Ensure you have Python installed on your system
2. Clone the repository:
   ```bash
   git clone https://github.com/Dipak491/file_manager.git
   cd file_manager
   ```
3. Run the application:
   ```bash
   python file_manager.py
   ```

### Method 2: Using the Executable

1. Download the latest release from the releases page
2. Extract the zip file
3. Run `file_manager.exe`

## Usage

1. Launch the application
2. Click "Browse Folder" to select a directory
3. Use the dropdown menu to select file type filter
4. Click "Apply Filter" to show matching files
5. Double-click any file to open it
6. Use "Export List" to save the current file list as CSV/TXT

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.