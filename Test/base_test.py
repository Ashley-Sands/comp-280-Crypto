import unittest
import time


# Set up a timer for all test classes
class BaseTestClass( unittest.TestCase ):

    print_elapsed_time_threshold = 0.0001   # < 0 always print else print if > value (sec)

    def setUp(self):
        self.started_time = time.time()

    def tearDown(self):
        self.elapsed_time = time.time() - self.started_time
        if self.elapsed_time > self.print_elapsed_time_threshold:
            print( '.'.join('{} ( {}s )'.format( self.id(), round( self.elapsed_time, 3 ) ).split('.')[1:]) )