import shutil


BACKUP_FOLDER = "backup_data"
FORMAT = "zip"

# make archive

shutil.make_archive(base_name=BACKUP_FOLDER, format=FORMAT, root_dir="data")
print("Backup successfull")

# unpack rchive

shutil.unpack_archive(filename=f"{BACKUP_FOLDER}.{FORMAT}",
                      extract_dir='data2',
                      format=FORMAT)  # backup_data.zip
print("Archive unpacked succesfully")