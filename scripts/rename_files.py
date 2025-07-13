import os
import shutil
from datetime import datetime

def get_target_folder():
    folder = input("🔍 Enter the full path to the folder containing files to rename: ").strip('"')
    if not os.path.isdir(folder):
        print("❌ Invalid folder path.")
        return None
    return folder

def get_output_folder(base_path, *subfolders):
    folder = os.path.join(base_path, *subfolders)
    os.makedirs(folder, exist_ok=True)
    return folder

def rename_files():
    # Get the target input folder
    folder = get_target_folder()
    if not folder:
        return

    prefix = input("🔠 Enter prefix for files (e.g. HR_Resume): ").strip()
    dry_run = input("🧪 Do a dry-run (y/n)? ").lower() == 'y'

    # Base project folder (where this script is located)
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Define output and log paths using safe relative logic
    output_folder = get_output_folder(base_path, "..", "output", "renamed")
    error_folder = get_output_folder(base_path, "..", "input", "errors")
    logs_folder = get_output_folder(base_path, "..", "logs")
    log_path = os.path.join(logs_folder, "rename_log.txt")

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    with open(log_path, "a", encoding="utf-8") as log_file:
        for i, file in enumerate(files, start=1):
            name, ext = os.path.splitext(file)

            if not ext:
                shutil.move(os.path.join(folder, file), os.path.join(error_folder, file))
                print(f"⚠️ No extension found: {file} → Moved to 'errors'")
                continue

            timestamp = datetime.now().strftime("%Y%m%d")
            new_name = f"{prefix}_{i}_{timestamp}{ext}"
            src_path = os.path.join(folder, file)
            dst_path = os.path.join(output_folder, new_name)

            if dry_run:
                print(f"💡 DRY-RUN: {file} → {new_name}")
            else:
                shutil.move(src_path, dst_path)
                print(f"✅ Renamed: {file} → {new_name}")
                log_file.write(f"{file} → {new_name}\n")

if __name__ == "__main__":
    rename_files()
