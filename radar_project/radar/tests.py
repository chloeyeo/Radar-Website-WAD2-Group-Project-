from django.test import TestCase
from radar.models import Post, Category
from django.contrib.auth.models import User

# Create your tests here.

class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        '''Ensures the number of views received for a Category are positive or zero.'''
        category = Category(name='test', views=-1)
        category.save()
        self.assertEqual((category.views >= 0), True)

    def test_slug_line_creation(self):
        ''' Checks to make sure that when a category is created, an appropriate slug is created. Example: "Random Category String" should be "random-category-string". '''
        category = Category(name='Random Category String')
        category.save()
        self.assertEqual(category.slug, 'random-category-string')

class PostMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        '''Ensures the number of views received for a Post is positive or zero.'''
        User.posts=0
        post = Post(title='test', views=-1)
        category = Category(name='test', views=-1)
        category.save()
        post.category_id = category.id
        post.save()
        self.assertEqual((post.views >= 0), True)
        
