import unittest
import SimpleRest as app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, 'Home Page')

    def test_hello_greet(self):
        rv = self.app.get('/greet')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, 'Greetings from Flask Server')

    def test_hello_name(self):
        name = 'Simon'
        rv = self.app.get('/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn("{name}", rv.data)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
