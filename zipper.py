import os
import shutil

from ftp_connector import name_von_backup, bindir

#Compress Folder
if not os.path.exists("Backups"):
    os.makedirs("Backups")
os.chdir("Backups")

shutil.make_archive(name_von_backup, 'zip', bindir / name_von_backup)
#Delete Folder
os.chdir(bindir)

shutil.rmtree(name_von_backup)
