import os
import pandas as pd

def get_folder_path(prompt):
    folder = input(prompt).strip('"')
    if not os.path.isdir(folder):
        print("❌ Invalid folder path.")
        return None
    return folder

def convert_documents():
    input_folder = get_folder_path("📁 Enter the folder path containing documents to convert: ")
    if not input_folder:
        return

    # Base path of current script
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Output and logs folders
    output_folder = os.path.join(base_path, "..", "output", "converted")
    logs_folder = os.path.join(base_path, "..", "logs")
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(logs_folder, exist_ok=True)

    # Ask for file types and target format
    file_types = input("📎 Enter file types to convert (e.g. .csv .xlsx): ").split()
    target_format = input("🔁 Convert to format (.json/.csv/.txt): ").strip()
    dry_run = input("🧪 Do a dry-run (y/n)? ").lower() == 'y'

    log_path = os.path.join(logs_folder, "conversion_log.txt")

    files = [f for f in os.listdir(input_folder) if os.path.splitext(f)[1] in file_types]

    if not files:
        print("ℹ️ No matching files found to convert.")
        return

    with open(log_path, "a", encoding="utf-8") as log_file:
        for file in files:
            input_path = os.path.join(input_folder, file)
            name, ext = os.path.splitext(file)

            try:
                # Read file based on input type
                if ext == ".csv":
                    df = pd.read_csv(input_path)
                elif ext == ".xlsx":
                    df = pd.read_excel(input_path)
                else:
                    print(f"❌ Unsupported file type for reading: {file}")
                    continue

                output_path = os.path.join(output_folder, f"{name}{target_format}")

                if dry_run:
                    print(f"💡 DRY-RUN: {file} → {output_path}")
                else:
                    if target_format == ".json":
                        df.to_json(output_path, orient="records", lines=True)
                    elif target_format == ".csv":
                        df.to_csv(output_path, index=False)
                    elif target_format == ".txt":
                        df.to_csv(output_path, index=False, sep='\t')
                    else:
                        print(f"⚠️ Unsupported target format: {target_format}")
                        continue

                    print(f"✅ Converted: {file} → {output_path}")
                    log_file.write(f"{file} → {output_path}\n")

            except Exception as e:
                print(f"⚠️ Error converting {file}: {e}")

if __name__ == "__main__":
    convert_documents()
