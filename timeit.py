import time
def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()        #start time, float datatype in second.
        result = method(*args, **kwargs)
        te = time.time()        #end time, float datatype in second.
        delta_time =  round((te - ts) * 100_000_000)//100   # delta time in ns.
        if 'log_time' in kwargs:
            name = kwargs.get('log_name', method.__name__) + " [nano_second]"    
            if name not in kwargs['log_time']:  
                kwargs['log_time'][name] = list()      
            kwargs['log_time'][name].append(   delta_time)
        else:
            print( '%r  %2.2f ns' % (method.__name__, delta_time))
        return result
    return timed