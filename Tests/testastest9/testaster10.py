import basetest

files="z*.comm"
TestCase=basetest.make_tests(files)
class TestCase(TestCase):pass
