# timeit
Python decorator/wrapper to measure execution time (in nanosecond) of a function call.
To use it, call the decorator @timeit.

See example below:

@timeit
def print_hello_world(  *args, **kwargs):
  print('hello world!')
  pass  
print_hello_world()

Output:
print_hello_world 12.34 ns
