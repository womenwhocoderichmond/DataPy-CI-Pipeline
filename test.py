import unittest
import simple_rest as app


class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data.decode(), 'Home Page')

    def test_hello_greet(self):
        rv = self.app.get('/greet')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data.decode(), 'Greetings from Flask Server')

    def test_hello_name(self):
        name = 'Simon'
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(name, rv.data.decode())


if __name__ == '__main__':
    import xmlrunner

    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
