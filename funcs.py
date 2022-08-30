from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                                Schoolkid, Subject)

def find_kid(name):
    return Schoolkid.objects.get(full_name__contains=name)

def set_all_fives(kid):
     marks = Mark.objects.filter(schoolkid=kid)
     bad = marks.filter(points__lt=4)
     bad.update(points=5)

def remove_chastisements(kid):
    Chastisement.filter(schoolkid=kid).delete()

def create_commendation(kid, subject_name, text="Хвалю!"):
    maths = Subject.objects.filter(title=subject_name, year_of_study=kid.year_of_study)
    lesson = Lesson.objects.get(subject__in=maths, group_letter=kid.group_letter)
    Commendation.objects.create(text=text, created=lesson.date, schoolkid=kid, subject=lesson.subject, teacher=lesson.teacher)