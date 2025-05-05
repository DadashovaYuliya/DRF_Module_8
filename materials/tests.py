from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(
            title="Курс 3", description="Это третий курс"
        )
        self.lesson = Lesson.objects.create(
            title="Урок 1",
            video_url="https://youtube.com/c3/l1/",
            description="Первый урок третьего курса",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тестирование получения урока."""
        url = reverse("materials:lesson-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        """Тестирование создания урока."""
        url = reverse("materials:lesson-create")
        data = {
            "title": "Урок 2",
            "video_url": "https://youtube.com/c3/l2/",
            "description": "Второй урок третьего курса",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """Тестирование изменения урока."""
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {
            "title": "Урок 10",
        }
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Урок 10")

    def test_lesson_delete(self):
        """Тестирование удаления урока."""
        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        """Тестирование списка уроков."""
        url = reverse("materials:lesson-list")

        response = self.client.get(url)
        data = response.json()

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_url": self.lesson.video_url,
                    "title": self.lesson.title,
                    "description": self.lesson.description,
                    "preview": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(
            title="Курс 5", description="Это пятый курс", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        """Тестирование получения курса."""
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.course.title)

    def test_course_create(self):
        """Тестирование создания курса."""
        url = reverse("materials:course-list")
        data = {
            "title": "Курс 4",
            "description": "Это четвертый курс",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        """Тестирование изменения курса."""
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {
            "title": "Курс 10",
        }
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Курс 10")

    def test_course_delete(self):
        """Тестирование удаления курса."""
        url = reverse("materials:course-detail", args=(self.course.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        """Тестирование списка курсов."""
        url = reverse("materials:course-list")

        response = self.client.get(url)
        data = response.json()

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "title": self.course.title,
                    "preview": None,
                    "description": self.course.description,
                    "lesson_count": 0,
                    "lessons": [],
                    "owner": self.user.pk,
                    "is_signed": False,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
