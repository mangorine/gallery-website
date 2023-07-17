import os
import galerie.settings as settings
from api.models import File
from PIL import Image, ImageOps


# TODO: function that transform a zip file into a gallery
def load_zip_into_gallery(zip_dir, folder_dir):
    pass


# folder_dir format has to be vap-2023/ if the gallery's folder in media folder is vap-2023 /!\ DONT FORGET THE SLASH AT THE END
def load_folder_into_gallery(folder_dir, gal):
    for filename in os.listdir(
        str(settings.BASE_DIR) + "/media/" + folder_dir + "/uploads/"
    ):
        temp = filename.split(".")
        file = File(
            file_name=temp[0],
            file_extension=temp[1],
            file_full_name=filename,
            link="/media/" + folder_dir,
            gallery=gal,
        )
        file.save()


def generate_thumbnails(folder_name):
    for filename in os.listdir(
        str(settings.BASE_DIR) + "/media/" + folder_name + "/uploads/"
    ):
        temp = filename.split(".")
        if (
            temp[1] == "jpg"
            or temp[1] == "png"
            or temp[1] == "jpeg"
            or temp[1] == "JPG"
            or temp[1] == "PNG"
            or temp[1] == "JPEG"
        ):
            im = Image.open(
                str(settings.BASE_DIR)
                + "/media/"
                + folder_name
                + "/uploads/"
                + filename
            )
            im = ImageOps.exif_transpose(im)
            if im.size[0] > im.size[1]:
                im.thumbnail((510 * im.size[0] / im.size[1], 200))
            else:
                im.thumbnail((600, 600 * im.size[1] / im.size[0]))
            im.save(
                str(settings.BASE_DIR)
                + "/media/"
                + folder_name
                + "/thumbnails/"
                + filename
            )
