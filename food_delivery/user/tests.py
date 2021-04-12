from django.test import TestCase

from django.contrib.auth import get_user_model
# Create your tests here.

class ClientAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@email.com', 'username', 'firstname', 'password'
        )

        self.assertEqual(super_user.email, 'testuser@email.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertEqual(str(super_user), 'username')


        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username', first_name='first_name', 
                password='password', is_superuser=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username', first_name='first_name', 
                password='password', is_staff=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', user_name='username', first_name='first_name', 
                password='password', is_staff=True
            )
    
    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@email.com', 'username', 'firstname', 'password'
        )

        self.assertEqual(user.email, 'testuser@email.com')
        self.assertEqual(user.user_name, 'username')
        self.assertEqual(user.first_name, 'firstname')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', user_name='a', first_name='first_name', password='password'
            )
