from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_video_url


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    is_signed = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
            return instance.lessons.count()

    def get_lessons(self, course):
            return [lesson.title for lesson in Lesson.objects.filter(course=course)]

    def get_is_signed(self, course):
            request = self.context.get('request')
            if request and request.user:
                return Subscription.objects.filter(user=request.user, course=course).exists()
            return False

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview', 'description', 'lesson_count', 'lessons', 'owner', 'is_signed']


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validate_video_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"
