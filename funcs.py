from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                                Schoolkid, Subject)

def find_kid(name):
    kids = Schoolkid.objects.filter(full_name__contains=name)
    if len(kids) == 1:
        return kids[0]
    elif len(kids) > 1:
        raise Exception("Multiple kids found")
    else:
        raise Exception("No kids found")

def all_fives(kid):
     marks = Mark.objects.filter(schoolkid=kid)
     bad = marks.filter(points__lt=5)
     bad.update(points=5)

def remove_chastisements(kid):
    Chastisement.filter(schoolkid=kid).delete()

def create_commendation(kid, subject_name, text="Хвалю!"):
    maths = Subject.objects.filter(title=subject_name, year_of_study=kid.year_of_study)
    lesson = Lesson.objects.filter(subject__in=maths, group_letter=kid.group_letter)[0]
    Commendation.objects.create(text=text, created=lesson.date, schoolkid=kid, subject=lesson.subject, teacher=lesson.teacher)