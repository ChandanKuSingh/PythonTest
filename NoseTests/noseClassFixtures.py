import nose
from nose.tools import with_setup

"""A test class is a class defined in a test module that matches test_Match or is a subclass of unittest.
    TestCase. The respective setup and teardown functions are run at the beginning and the end of the class
    of test methods. Here is the nomenclature for the class-level setup fixtures:
    
    Setup - setup_class, setupClass, setUpClass, setupAll (or setUpAll)
    TearDown -  teardown_class, teardownClass, tearDownClass, teardownAll (or tearDownAll)
    
    To demonstrate the usage of fixtures, we use Nose fixtures in different levels – class, module, and 
    method.
    """

# Can also be setup, setup_module, setUp or setUpModule
def setUpModule(module):
    print("")
    print("%s" % (setUpModule.__name__,))


# Can also be teardown, teardown_module, or tearDownModule
def tearDownModule(module):
    print("%s" % (tearDownModule.__name__,))


def setup_func():
    print("%s" % (setup_func.__name__,))


def teardown_func():
    print("%s" % (teardown_func.__name__,))


@with_setup(setup_func, teardown_func)
def test_case_1():
    print("%s" % (test_case_1.__name__,))


class test_class_1:

    def setup(self):
        print("%s called before each test method" % (test_class_1.setup.__name__,))

    def teardown(self):
        print("%s called after each test method" % (test_class_1.teardown.__name__,))

    @classmethod
    def setup_class(cls):
        print("%s called before any method in this class is executed" % (test_class_1.setup_class.__name__,))

    @classmethod
    def teardown_class(cls):
        print("%s called after methods in this class is executed" % (test_class_1.teardown_class.__name__,))

    def test_case_2(self):
        print("%s" % (test_class_1.test_case_2.__name__,))

    """OUTPUT:
    1. setup - called before each test method > setUpModule
    2. setup class called before any method in this class is executed
    3. setup called before any method in this class is executed
    4. teardown - called after each test method in this class is executed
    5. teardown class called after methods in this class is executed
    6. teardown - called after each test method > tearDownModule
    """