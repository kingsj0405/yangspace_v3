from django.test import TestCase
from blog.models import Page


class TestTest(TestCase):
    def test_add(self):
        self.assertEqual(1 + 2, 3)


class TestPage(TestCase):
    space_title = 'Hello World'
    space_url = 'hello-world_None'
    blanket_title = 'Hello World(1)'
    blanket_url = 'hello-world1_None'
    dummy_content = 'Content'

    def setUp(self):
        Page.objects.create(title=self.space_title, content=self.dummy_content)
        Page.objects.create(title=self.blanket_title,
                            content=self.dummy_content)

    def test_url__with_space(self):
        p = Page.objects.get(title=self.space_title)
        self.assertEqual(p.url, self.space_url)

    def test_url__with_blanket(self):
        p = Page.objects.get(title=self.blanket_title)
        self.assertEqual(p.url, self.blanket_url)
