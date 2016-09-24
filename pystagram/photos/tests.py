from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.

user_model_class = get_user_model()

class PostTest(TestCase):
    def setUp(self):
        self.user = user_model_class()
        self.user.username = 'hello1'
        self.user.save()

    def test_add_op(self):
        self.assertEqual(1, 1)

    def test_create_post_by_model(self):
        post = Post()
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                post.save()
            self.assertIsNone(post.pk)

        user = user_model_class.objects.last()
        post.user = user
        post.save()
        self.assertIsNotNone(post.pk)
