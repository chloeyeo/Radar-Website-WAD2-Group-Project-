from django.test import TestCase
from radar.models import Post, Category
from django.contrib.auth.models import User
from django.urls import reverse
    
# Create your tests here.

class CategoryMethodTests(TestCase):
    def test_ensure_category_views_are_positive(self):
        '''Ensures the number of views received for a Category are positive or zero.'''
        category = Category(name='test', views=-1)
        category.save()
        self.assertEqual((category.views >= 0), True)

    def test_category_slug_line_creation(self):
        ''' Checks to make sure that when a category is created, an appropriate slug is created. Example: "Random Category String" should be "random-category-string". '''
        category = Category(name='Random Category String')
        category.save()
        self.assertEqual(category.slug, 'random-category-string')

class PostMethodTests(TestCase):
    def test_ensure_post_views_are_positive(self):
        '''Ensures the number of views received for a Post is positive or zero.'''
        User.posts=0
        post = Post(title='test', views=-1)
        category = Category(name='test')
        category.save()
        post.category_id = category.id
        post.save()
        self.assertEqual((post.views >= 0), True)

    def test_post_slug_line_creation(self):
        ''' Checks to make sure that when a post is created, an appropriate slug is created. Example: "Random Category String" should be "random-category-string". '''
        post = Post(title='Random Category String')
        category = Category(name='test')
        category.save()
        post.category_id = category.id
        post.save()
        self.assertEqual(post.slug, 'random-category-string')


#class HomepageViewTests(TestCase):
   # def test_homepage_view_with_no_posts(self):
      #  ''' If no posts exist, the appropriate message should be displayed. '''
        #response = self.client.get(reverse('radar:homepage'))
        #self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'There are no posts present in your data base.')
        #self.assertQuerysetEqual(response.context['posts'],[])
