import sys,types,os
import sre
import unittest
from optparse import OptionParser

sys.path[:0]=[".."]

testMatch = sre.compile(r'^[Tt]est')

class TestSuite(unittest.TestSuite):
    loader = unittest.defaultTestLoader

    def __init__(self, names=[]):
        self.names=names
        super(TestSuite,self).__init__()
        tests=self.collectTests()
        self.addTests(tests)

    def _import(self,name):
        mod = __import__(name,{},{})
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod,comp)
        return mod

    def collectTests(self):
        if self.names:
           entries=self.names
        else:
           entries = [ item for item in os.listdir(os.getcwd())
                        if item.lower().find('test') >= 0 ]

        tests=[]
        for item in entries:
            path=os.path.abspath(os.path.join(os.getcwd(),item))
            if os.path.isfile(item):
                root, ext = os.path.splitext(item)
                if ext == '.py':
                    if root.find('/') >= 0:
                       dirname, file = os.path.split(path)
                       root, ext = os.path.splitext(file)
                       sys.path.insert(0,dirname)
                       mod=self._import(root)
                       sys.path.remove(dirname)
                    else:
                       mod=self._import(root)
                    tests.append(ModuleTestSuite(mod))
            elif os.path.isdir(item):
                init = os.path.abspath(os.path.join(item,'__init__.py'))
                if os.path.isfile(init):
                   package=self._import(item)
                   if package:
                      tests.append(TestPackageSuite(package))
                else:
                   tests.append(TestDirectorySuite(path))
        return tests

class TestDirectorySuite(TestSuite):
    ignore=[]
    def __init__(self,path):
        self.path=path
        super(TestDirectorySuite,self).__init__()

    def collectTests(self):
        tests=[]
        if self.path:
            sys.path.insert(0,self.path)
            entries = os.listdir(self.path)
            entries.sort()
            for item in entries:
                if (item[0] == '.'
                    or item in self.ignore
                    or not testMatch.search(item)):
                    continue
                item_path = os.path.abspath(os.path.join(self.path,item))
                if os.path.isfile(item_path):
                    root, ext = os.path.splitext(item)
                    if ext != '.py':
                        continue
                    if root.find('/') >= 0:
                       dirname, file = os.path.split(item_path)
                       root, ext = os.path.splitext(file)
                       sys.path.insert(0,dirname)
                       mod=self._import(root)
                       sys.path.remove(dirname)
                    else:
                       mod=self._import(root)
                    tests.append(ModuleTestSuite(mod))
                elif os.path.isdir(item_path):
                    init = os.path.abspath(os.path.join(item_path,'__init__.py'))
                    if os.path.isfile(init):
                        package=self._import(item)
                        if package:
                           tests.append(TestPackageSuite(package))
                    else:
                        tests.append(TestDirectorySuite(item_path))
            sys.path.remove(self.path)
        return tests

class TestPackageSuite(TestDirectorySuite):
    def __init__(self,package):
        self.package=package
        path=os.path.abspath(os.path.dirname(self.package.__file__))
        super(TestPackageSuite,self).__init__(path)

    def collectTests(self):
        tests=[]
        if self.path:
            sys.path.insert(0,self.path)
            entries = os.listdir(self.path)
            entries.sort()
            for item in entries:
                if (item[0] == '.'
                    or item in self.ignore
                    or not testMatch.search(item)):
                    continue
                item_path = os.path.abspath(os.path.join(self.path,item))
                if os.path.isfile(item_path):
                    root, ext = os.path.splitext(item)
                    if ext != '.py':
                        continue
                    name="%s.%s" % (self.package.__name__,root)
                    mod=self._import(name)
                    tests.append(ModuleTestSuite(mod))
                elif os.path.isdir(item_path):
                    init = os.path.abspath(os.path.join(item_path,'__init__.py'))
                    if os.path.isfile(init):
                        name="%s.%s" % (self.package.__name__,item)
                        package=self._import(name)
                        if package:
                           tests.append(TestPackageSuite(package))
                    else:
                        tests.append(TestDirectorySuite(item_path))
            sys.path.remove(self.path)
        return tests


class ModuleTestSuite(TestSuite):

    def __init__(self, module):
        self.module = module
        super(ModuleTestSuite,self).__init__()

    def collectTests(self):
        def cmpLineNo(a,b):
            a_ln = a.func_code.co_firstlineno
            b_ln = b.func_code.co_firstlineno
            return cmp(a_ln,b_ln)

        entries = dir(self.module)
        tests = []
        func_tests = []
        for item in entries:
            test = getattr(self.module,item)
            if (isinstance(test, (type, types.ClassType))
                and issubclass(test,unittest.TestCase)):
                if testMatch.search(item):
                    [ tests.append(case) for case in
                      self.loader.loadTestsFromTestCase(test)._tests ]
            elif callable(test) and testMatch.search(item):
                # simple functional test
                func_tests.append(test)

        # run functional tests in the order in which they are defined
        func_tests.sort(cmpLineNo)
        [ tests.append(unittest.FunctionTestCase(test))
          for test in func_tests ]
        return tests

class TestProgram(unittest.TestProgram):
    USAGE="""
"""
    def __init__(self,testRunner=None):
        self.testRunner = testRunner
        self.verbosity = 1
        self.parseArgs(sys.argv)
        self.createTests()
        self.runTests()

    def parseArgs(self,argv):
        parser = OptionParser(usage=self.USAGE)
        parser.add_option("-v","--verbose",action="count",
                          dest="verbosity",default=1,
                          help="Be more verbose. ")

        options, args = parser.parse_args(argv)
        self.verbosity = options.verbosity

        if args:
            self.names = list(args)
            if self.names[0] == 'run.py':
                self.names = self.names[1:]

    def createTests(self):
        self.test = TestSuite(self.names)


main = TestProgram

if __name__ == "__main__":
    main()

