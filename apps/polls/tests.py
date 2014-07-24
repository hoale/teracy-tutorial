import datetime

from django.test import TestCase
from django.utils import timezone

from apps.polls.models import Poll


class PollMethoTests(TestCase):
	def test_was_published_recently_with_future_poll(self):
		"""
		was_published_recently() should return False for polls whose
		pub_date is in the future
		"""
		future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(),False)
		
