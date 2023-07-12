import os
import galerie.settings as settings
from api.models import (
    Gallery, File
)

def load_folder_into_gallery(folder_dir, gal):
    for filename in os.listdir(str(settings.BASE_DIR) + folder_dir):
        temp = filename.split('.')
        file = File(file_name=temp[0], file_extension=temp[1], file_full_name=filename, link=folder_dir + filename, gallery=gal)
        file.save()