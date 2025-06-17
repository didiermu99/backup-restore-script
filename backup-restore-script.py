import os
import tarfile
import datetime

def create_backup(source_path, backup_dir):
    """
    Creates a timestamped .tar.gz backup of the source_path in backup_dir.
    """
    # Step 1: Check if the source path exists (file or folder to back up)
    if not os.path.exists(source_path):
        print("Source path does not exist.")
        return None

    # Step 2: Ensure the backup directory exists; create it if it doesn't
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Step 3: Generate a unique backup file name using the current date and time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.tar.gz"
    backup_path = os.path.join(backup_dir, backup_name)

    # Step 4: Open a new tar.gz file and add the source file/folder to it
    with tarfile.open(backup_path, "w:gz") as tar:
        # arcname sets the root name inside the archive to just the file/folder name
        tar.add(source_path, arcname=os.path.basename(source_path))

    print(f"Backup created at: {backup_path}")
    return backup_path

def restore_backup(backup_path, restore_dir):
    """
    Restores the backup archive to the restore_dir.
    """
    # Step 1: Check if the backup archive exists
    if not os.path.exists(backup_path):
        print("Backup file does not exist.")
        return

    # Step 2: Extract all contents of the archive to the restore directory
    with tarfile.open(backup_path, "r:gz") as tar:
        tar.extractall(path=restore_dir)

    print(f"Backup restored to: {restore_dir}")

if __name__ == "__main__":
    print("Automated Backup & Restore Script")
    print("1. Create Backup")
    print("2. Restore Backup")
    # Step 1: Ask the user what they want to do
    choice = input("Select option (1/2): ")

    if choice == "1":
        # Step 2a: If creating a backup, ask for the source and destination
        source = input("Enter file/folder to back up: ").strip()
        backup_dir = input("Enter backup directory: ").strip()
        create_backup(source, backup_dir)
    elif choice == "2":
        # Step 2b: If restoring, ask for the archive and restore location
        backup_file = input("Enter path to backup archive (.tar.gz): ").strip()
        restore_dir = input("Enter restore directory: ").strip()
        restore_backup(backup_file, restore_dir)
    else:
        print("Invalid option.")
