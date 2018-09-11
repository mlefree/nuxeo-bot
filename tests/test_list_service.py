# coding: utf8
from __future__ import unicode_literals

import unittest

from flask_api import FlaskAPI

from src.list.service import ListService

app = FlaskAPI(__name__)


class ListServiceTests(unittest.TestCase):
    def test_launch(self):
        service = ListService()
        output, outputStatus = service.launch({'data': [
            {'value': 3, 'comments': ['my comment']},
            {'value': 4, 'comments': ['my comment', 'my comment 2']},
            {'value': 5, 'comments': ['my comment']}]})
        self.assertEqual(output, 'List max found: 4 - 2')
        self.assertEqual(outputStatus, 200)
