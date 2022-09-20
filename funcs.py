from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                                Schoolkid, Subject)
from django.core.exceptions import MultipleObjectsReturned, DoesNotExist

def find_kid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except MultipleObjectsReturned:
        print("Найдено несколько детей с таким именем!")
    except DoesNotExist:
        print("Не найдено детей с таким именем!")

def set_all_fives(kid):
     marks = Mark.objects.filter(schoolkid=kid)
     bad = marks.filter(points__lt=4)
     bad.update(points=5)

def remove_chastisements(kid):
    Chastisement.filter(schoolkid=kid).delete()

def create_commendation(kid, subject_name, text="Хвалю!"):
    maths_subject = Subject.objects.filter(title=subject_name, year_of_study=kid.year_of_study)
    lesson = Lesson.objects.get(subject__in=maths_subject, group_letter=kid.group_letter)
    Commendation.objects.create(text=text, created=lesson.date, schoolkid=kid, subject=lesson.subject, teacher=lesson.teacher)