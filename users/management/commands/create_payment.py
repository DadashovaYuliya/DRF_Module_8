from django.core.management.base import BaseCommand
from django.utils import timezone

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Создание платежа"

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.get(pk=1)
            course = Course.objects.get(pk=1)
            lesson = Lesson.objects.get(pk=1)

            payment = Payment.objects.create(
                user=user,
                payment_date=timezone.now(),
                payment_course=course,
                payment_lesson=lesson,
                payment_amount=1000,
                payment_method=Payment.CASH,
            )
            self.stdout.write(self.style.SUCCESS("Платеж сохранен"))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Пользователь не найден"))
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("Курс не найден"))
        except Lesson.DoesNotExist:
            self.stdout.write(self.style.ERROR("Урок не найден"))
