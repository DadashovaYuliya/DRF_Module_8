from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User


class Command(BaseCommand):
    help = 'Создает группу модераторов и пользователей'

    def handle(self, *args, **kwargs):
        moderator_group = Group.objects.create(name='Moderator')

        users = [
            {
                'email': 'moder1@example.com',
                'password': 'qwe123'
            },
            {
                'email': 'moder2@example.com',
                'password': '123qwe'
            },
        ]

        for u in users:
            user = User.objects.create(email=u['email'])
            user.set_password(u['password'])
            user.save()
            user.groups.add(moderator_group)







