from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    CASH = "cash"
    TRANSFER = "transfer"

    PAYMENT_METHOD = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод на счет"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pay_user",
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    payment_date = models.DateTimeField(
        verbose_name="Дата оплаты", null=True, blank=True
    )
    payment_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="pay_course",
        verbose_name="Оплаченный курс",
        null=True,
        blank=True,
    )
    payment_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="pay_lesson",
        verbose_name="Оплаченный урок",
        null=True,
        blank=True,
    )
    payment_amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD, verbose_name="Способ оплаты"
    )
    session_id = models.CharField(
        max_length=255, verbose_name="Id сессии", null=True, blank=True
    )
    link = models.URLField(
        max_length=400, verbose_name="Ссылка на оплату", null=True, blank=True
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Платеж пользователя {self.user} за {self.payment_course}-{self.payment_amount}"
