import random
from datacenter.models import Schoolkid, Subject, Lesson, Mark, Commendation,
Сhastisement


COMMENDATIONS = [
    "Так держать!",
    "Я тобой горжусь!",
    "Ты сегодня прыгнул выше головы!",
    "Очень хороший ответ!"
]


def fix_marks(schoolkid_name):
    child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    for mark in marks:
        mark.points = random.choice([4, 5])
        mark.save()


def remove_chastisements(schoolkid_name):
    child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    chastisements = Сhastisement.objects.filter(schoolkid=child)
    chastisements.delete()


def create_commendation(schoolkid_name, subject_name):
    child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    subject = Subject.objects.get(title__contains=subject_name,
                                  year_of_study=child.year_of_study)
    lesson = Lesson.objects.filter(group_letter=child.group_letter,
                                   subject=subject).order_by('?')[0]
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
