# compares the running time of a list to a generator
import time

def oddGen(n, m) -> None:
    '''
    generator function creates an iterator of odd numbers
    between n and m
    '''

    while n < m:
        yield n
        n += 2

def oddLst(n, m) -> None:
    '''
    builds a list of odd numbers between n and m
    '''

    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

# time it takes to perform sum on an generator
t1 = time.time()
sum(oddGen(1, 1000000))
print('time to sum a generator: %f' % (time.time() - t1))

# time it takes to build and sum a list
t1=time.time()
sum(oddLst(1, 1000000))
print('time to build and sum a list: %f' % (time.time() - t1))

'''
Building a list to do this calculation takes significantly longer.
The performance improvement as a result of using generators is 
because the values are generated on demand, rather than saved as 
a list in memory.
'''
