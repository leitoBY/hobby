import unittest
from unittest.mock import patch, MagicMock, Mock
from backend.api.users.user_service import UserService
from backend.api.users.user_repository import UserRepository

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.request_data = {
            "email": "test@test.com",
            "username": "test",
            "password": "password",
        }

    user = Mock(username="test", email="test.test.com", password="secret_test")
    @patch.object(UserRepository, 'get_all', MagicMock(return_value=[user]))
    def test_get_all_users(self):
        returned_user_list = UserService.get_all_users()
        self.assertTrue(returned_user_list)

    @patch.object(UserService, 'find_user_by_email', MagicMock(return_value=user))
    def test_add_new_user_when_user_was_found(self):
        with self.assertRaises(Exception):
            UserService.add_new_user(data=self.request_data)

    @patch.object(UserService, 'find_user_by_email', MagicMock(return_value=None))
    @patch.object(UserRepository, 'add', MagicMock(return_value=None))
    @patch.object(UserRepository, 'commit', MagicMock(return_value=None))
    def test_add_new_user_when_user_was_not_found(self):
        new_user = UserService.add_new_user(data=self.request_data)
        self.assertTrue(new_user)
        self.assertTrue(UserRepository.add.called)
        self.assertTrue(UserRepository.commit.called)

    @patch.object(UserRepository, 'find_user_by_email', MagicMock(return_value=user))
    def test_find_user_by_email(self):
        found_user = UserService.find_user_by_email(email=self.user.email)
        self.assertTrue(found_user)
        self.assertEqual(found_user.email, self.user.email)