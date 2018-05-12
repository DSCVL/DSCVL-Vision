import threading
import collections
from rplidar import RPLidar

try:
    import Queue
except ImportError:
    import queue as Queue

class AsynchronousGenerator:
    """
    The AsynchronousGenerator class is used to buffer output of a
    generator between iterable.__next__ or iterable.next calls. This
    allows the generator to continue producing output even if the
    previous output has not yet been consumed. The buffered structure is
    particularly useful when a process that consumes data from a
    generator is unable to finish its task at a rate comparable to which
    data is produced such as writing a large amount of data to a
    low-bandwidth I/O stream at the same time the data is produced.

        >>> for chunk in AsynchronousGenerator(function=makes_lots_of_data):
        ...     really_slow_iostream.write(chunk)
    source: https://www.reddit.com/r/Python/comments/ew9is/buffered_asynchronous_generators_for_parallel/
    """
    def __init__(self, function, args=(), kwargs={}, start=True, maxsize=1):
        self.generator = iter(function(*args, **kwargs))
        self.thread = threading.Thread(target=self._generatorcall)
        self.q = Queue.Queue(maxsize=maxsize)
        self.next = self.__next__
        if start:
            self.thread.start()

    def __iter__(self):
        return self

    def __next__(self):
        done, item = self.q.get()
        if done:
            raise StopIteration
        else:
            return item

    def _generatorcall(self):
        try:
            for output in self.generator:
                self.q.put((False, output))
        finally:
            self.q.put((True, None))

class wrapper(object):

    def __init__(self, generator):
        self.__gen = generator()

    def __iter__(self):
        return self

    def __next__(self):
        self.current = None
        while self.current == None:
            try:
                self.current = next(self.__gen)
            except:
                print("Lidar init failed. Please restart. (Common issue)")
                quit()
        return self.current

    def __call__(self):
        return self

PORT_NAME = 'COM15'
@wrapper
def gen():
    lidar = RPLidar(PORT_NAME)
    return lidar.iter_scans()