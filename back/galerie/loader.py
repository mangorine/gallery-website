import os
import galerie.settings as settings
from api.models import File
from PIL import Image, ImageOps
import zipfile
from api.models import Gallery
from celery import shared_task

def load_zip_into_gallery(zip_dir, gal):
    unzip(zip_dir, gal.slug)
    generate_thumbnails.delay(gal.slug)
    load_folder_into_gallery.delay(gal.slug)


def unzip(zip_dir, folder_dir):
    file = zipfile.ZipFile(str(settings.BASE_DIR) + "/media/" + zip_dir)
    file.extractall(
        path=str(settings.BASE_DIR) + "/media/" + folder_dir + "/uploads/", pwd=None
    )


# folder_dir format has to be vap-2023/ if the gallery's folder in media folder is vap-2023 /!\ DONT FORGET THE SLASH AT THE END
@shared_task
def load_folder_into_gallery(folder_dir):
    gal = Gallery.objects.get(slug=folder_dir)
    for filename in os.listdir(
        str(settings.BASE_DIR) + "/media/" + folder_dir + "/uploads/"
    ):
        temp = filename.split(".")
        files = File.objects.filter(
            file_name=temp[0],
            file_extension=temp[1],
            file_full_name=filename,
            link="/media/" + folder_dir,
            gallery=gal,
        )
        if files.count() == 0:
            file = File(
                file_name=temp[0],
                file_extension=temp[1],
                file_full_name=filename,
                link="/media/" + folder_dir,
                gallery=gal,
            )
            file.save()


@shared_task
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
