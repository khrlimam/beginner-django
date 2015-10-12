import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Questions

# Create your tests here.

class QuestionMethodTests(TestCase):
	def test_method_was_published_recently_with_future_question(self):
		# return false if pub_date in the future
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Questions(pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)