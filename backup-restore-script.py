import os
import tarfile
import datetime
import shutil

def create_backup(source_path, backup_dir):
    """
    Creates a timestamped .tar.gz backup of the source_path in backup_dir.
    """
    if not os.path.exists(source_path):
        print("Source path does not exist.")
        return None

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.tar.gz"
    backup_path = os.path.join(backup_dir, backup_name)

    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(source_path, arcname=os.path.basename(source_path))

    print(f"Backup created at: {backup_path}")
    return backup_path

def restore_backup(backup_path, restore_dir):
    """
    Restores the backup archive to the restore_dir.
    """
    if not os.path.exists(backup_path):
        print("Backup file does not exist.")
        return

    with tarfile.open(backup_path, "r:gz") as tar:
        tar.extractall(path=restore_dir)

    print(f"Backup restored to: {restore_dir}")

if __name__ == "__main__":
    print("Automated Backup & Restore Script")
    print("1. Create Backup")
    print("2. Restore Backup")
    choice = input("Select option (1/2): ")

    if choice == "1":
        source = input("Enter file/folder to back up: ").strip()
        backup_dir = input("Enter backup directory: ").strip()
        create_backup(source, backup_dir)
    elif choice == "2":
        backup_file = input("Enter path to backup archive (.tar.gz): ").strip()
        restore_dir = input("Enter restore directory: ").strip()
        restore_backup(backup_file, restore_dir)
    else:
        print("Invalid option.")
