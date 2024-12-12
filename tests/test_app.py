import unittest
from flasked import app

class FlaskTestCase(unittest.TestCase):

    # config le client de test
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    # test route index
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Page index")

    # test route hello
    def test_hello_world(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn("coucou ça va", response.data.decode())

    # test route hello/<name>
    def test_hello(self):
        response = self.client.get('/hello/fabrice')
        self.assertEqual(response.status_code, 200)
        self.assertIn("fabrice", response.data.decode())

    #test route /<name>
    def test_coucou(self):
        response = self.client.get('/john')
        self.assertEqual(response.status_code, 200)
        self.assertIn("coucou, john!", response.data.decode())

    # test route /user/<name>
    def test_showUserProfile(self):
        response = self.client.get('/user/kevin')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Utilisateur : kevin", response.data.decode())

    # test route /post/<post_id>
    def test_showPost(self):
        response = self.client.get('/post/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Publication avec l'id : 1", response.data.decode())

    #   test route /login avec la méthode get
    def test_login_get(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Va sur le site", response.data.decode())

    #   test route /login avec la méthode post   
    def test_login_post(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Connecte toi", response.data.decode())

if __name__ == '__main__':
    unittest.main()