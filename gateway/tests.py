"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
import logging
from django.utils import simplejson


from django.test import TestCase
from gateway.models import ExtractedPattern
from gateway.server_protocol import extract_patterns
from gateway.services import handle_message

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}


class ExtractPatternsTest(TestCase):
    def setUp(self):
        patterns = []
        patterns.append({'subject':'amazon','relation':'course_of_action_of_goal','object':'cloud'})
        patterns.append({'subject':'amazon','relation':'course_of_action_of_goal','object':'cloud'})
        patterns.append({'subject':'google','relation':'course_of_action_of_possible_result','object':'high_performence'})
        patterns.append({'subject':'webfaction','relation':'course_of_action_of_sibling','object':'amazon'})
        data = {'action' : 'extract_patterns','discussion_id': 10, 'patterns':patterns}


        json = simplejson.dumps(data)
        result = handle_message(json)
        logging.info("result %s" % result)

    def testBasic(self):
        query = ExtractedPattern.objects.all()
        logging.info("testBasic count %d"% query.count())
        self.failUnlessEqual(3, query.count())

    def testPatternsCount(self):
        patterns = []
        patterns.append({'subject':'amazon','relation':'course_of_action_of_goal','object':'cloud'})
        data = {'action' : 'extract_patterns','discussion_id': 10, 'patterns':patterns}
        json = simplejson.dumps(data)
        result = handle_message(json)
        logging.info("testPatternsCount result %s"% result)
        self.failUnlessEqual(2,len(result))
