from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    preview = models.ImageField(
        upload_to="materials/preview_course/",
        verbose_name="Превью курса",
        blank=True,
        null=True,
    )
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(
        upload_to="materials/preview_lesson/",
        verbose_name="Превью урока",
        blank=True,
        null=True,
    )
    video_url = models.URLField(max_length=150, verbose_name="Ссылка на видео")
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Курс",
    )
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
