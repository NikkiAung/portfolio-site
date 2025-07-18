import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)
    
    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        # Test creation of posts through database
        first_post = TimelinePost.create(name='William', email='william@example.com', content='Hello world, I\'m William!')
        assert first_post.id == 1

        second_post = TimelinePost.create(name='Aung', email='aung@example.com', content='Hello world, I\'m Aung!')
        assert second_post.id == 2

        # Test posts successfully added to database
        retrieved_first_post = TimelinePost.get_by_id(1)
        assert retrieved_first_post.name == 'William'
        assert retrieved_first_post.email == 'william@example.com'
        assert retrieved_first_post.content == 'Hello world, I\'m William!'

        retrieved_second_post = TimelinePost.get_by_id(2)
        assert retrieved_second_post.name == 'Aung'
        assert retrieved_second_post.email == 'aung@example.com'
        assert retrieved_second_post.content == 'Hello world, I\'m Aung!'