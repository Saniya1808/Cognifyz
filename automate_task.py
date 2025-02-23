import os
import shutil
from pathlib import Path

def organize_files(directory):
    """Organizes files in the given directory into categorized subfolders."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".tar", ".rar", ".7z"],
        "Scripts": [".py", ".sh", ".bat", ".js"]
    }
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_extension = Path(file).suffix.lower()
            
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    category_path = os.path.join(directory, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, file))
                    print(f"Moved '{file}' to '{category}/'")
                    break
    
    print("File organization complete.")

if __name__ == "__main__":
    directory = input("Enter the directory to organize: ")
    organize_files(directory)
