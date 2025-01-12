import random

from django.core.exceptions import ObjectDoesNotExist

from datacenter.models import (
    Schoolkid,
    Subject,
    Lesson,
    Mark,
    Commendation,
    Сhastisement
)


COMMENDATIONS = [
    "Так держать!",
    "Я тобой горжусь!",
    "Ты сегодня прыгнул выше головы!",
    "Очень хороший ответ!"
]


def get_child(schoolkid_name):
    try:
        child = Schoolkid.objects.filter(
            full_name__contains=schoolkid_name
            ).first()
        return child
    except ObjectDoesNotExist:
        print('Does Not Exist!')


def fix_marks(schoolkid_name):
    child = get_child(schoolkid_name)
    if child:
        marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
        for mark in marks:
            mark.points = random.choice([4, 5])
            mark.save()


def remove_chastisements(schoolkid_name):
    child = get_child(schoolkid_name)
    if child:
        chastisements = Сhastisement.objects.filter(schoolkid=child)
        chastisements.delete()


def create_commendation(schoolkid_name, subject_name):
    child = get_child(schoolkid_name)
    if child:
        try:
            subject = Subject.objects.get(title__contains=subject_name,
                                      year_of_study=child.year_of_study)
        except ObjectDoesNotExist:
            print('Does Not Exist!')
        lesson = Lesson.objects.filter(group_letter=child.group_letter,
                                   subject=subject).order_by('?').first()
        teacher = lesson.teacher
        subject = lesson.subject
        date = lesson.date

Commendation.objects.create(
        text=random.choice(COMMENDATIONS),
        created=date,
        schoolkid=child,
        subject=subject,
        teacher=teacher
)
