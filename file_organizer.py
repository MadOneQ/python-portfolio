import os
import shutil
downloads = os.path.expanduser("~/Downloads")
extensions = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".doc", ".docx", ".txt", ".pptx", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
}
for filename in os.listdir(downloads):
    filepath = os.path.join(downloads, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()

        for folder, exts in extensions.items():
            if ext in exts:
                dest_folder = os.path.join(downloads, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f"Moved {filename} --> {folder}")
                break
