import unittest

from ..migrations import reset_db
from ..models import User

class TestUserModel(unittest.TestCase):

    def setUp(self):
        reset_db()


    def test_password_hashing(self):
        u = User(username='vilmibm', password='foobar')
        u.hash_password()
        self.assertIsNotNone(u.password)
        self.assertNotEquals(u.password, 'foobar')
        u.save()
        u = User.select()[0]
        self.assertTrue(u.check_password('foobar'))

    def test_can_create(self):
        u = User(username='vilmibm', password='foobar')
        u.hash_password()
        u.save()
        self.assertEqual(u.display_name, 'a gaseous cloud')
        u.display_name = 'vil'
        u.save()

    # validation stuff

    def test_username_taken(self):
        User.create(username='vilmibm', password='foo')
        u = User(username='vilmibm', password='bar')
        with self.assertRaises(
                Exception,
                msg='username taken: vilmibm'):
            u.validate()

    def test_username_invalid(self):
        # TODO
        self.assertTrue(False)

    def test_password_insecure(self):
        # TODO
        self.assertTrue(False)
