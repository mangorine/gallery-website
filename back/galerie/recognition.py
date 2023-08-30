import os

import face_recognition
import galerie.settings as settings
import numpy as np
from api.models import Face, File, Gallery, Student
from celery import shared_task
from django.contrib.auth.models import User


@shared_task
def get_associated_pictures(username, face_path):
    encodings = []
    file = face_recognition.load_image_file(face_path)
    encoder = face_recognition.face_encodings(file)[0]
    encodings.append(encoder)
    student = Student.objects.get(user=User.objects.get(username=username))
    galleries = Gallery.objects.all()
    for gallery in galleries:
        # if gallery.year.id >= student.promo.first_year.id and gallery.year.id < (student.promo.first_year.id + 5):
        files = File.objects.filter(gallery=gallery)
        for file in files:
            file_ = face_recognition.load_image_file(
                str(settings.BASE_DIR)
                + file.link
                + "/thumbnails/"
                + file.file_full_name
            )
            face_locations = face_recognition.face_locations(file_)
            face_encodings = face_recognition.face_encodings(file_, face_locations)
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(encodings, face_encoding)
                face_distances = face_recognition.face_distance(
                    encodings, face_encoding
                )
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    Face.objects.create(file=file, student=student)
    os.remove(face_path)
