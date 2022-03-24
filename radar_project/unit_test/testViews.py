import unittest
from django.views import View
from radar import views

class testViews(unittest.TestCase):

    def test_likes(self):
        # create post and like, and check that the like went up
        likePostView = LikePostView(View)
        #likePostView.get
        

if __name__ == '__main__':
    unittest.main()
    
