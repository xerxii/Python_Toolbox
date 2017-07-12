#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

__author__ = 'xerxii'
__email__ = 'xerx@tutanota.com'
__license__ = 'AGPLv3'

# Many of these modules are *not* in the standard lib.
# If you're in an interpreter, the 'imported' list object can help you view imported modules.
# Yes, I've read PEP8.
imported =  '''
asyncio asyncoro access_points abc aiohttp
aiodns async_timeout
base64 binascii binhex bs4 ctypes
collections concurrent configparser
cryptography django enum email flask io
hashlib multiprocessing netifaces pstats psutil
rtlsdr sys subprocess signal secrets smtplib ssl
math os tkinter uuid urllib
'''.split()

# This will import the modules in imported
try:
    for each in imported:
        exec(f"import {each.replace(',','').replace('.','')}")
except(ImportError) as e:
    print(f"The following occured: {e!s}")

from asyncio import iscoroutinefunction    
from math import ceil
from hashlib import sha3_512

###################
# General Purpose #
###################

loop = asyncio.get_event_loop()
sysc = subprocess.os.system

def to_binary(item):
    
    if isinstance(item, int):
        return bin(item)[2::]
    
    elif isinstance(item, str):
        return ' '.join(format(ord(x), 'b') for x in item)
    else:
        raise TypeError("to_binary converts Strings and Ints")
        
def fragmenter(item_given, step):
    item = item_given
    if len(item) <= step:
        raise ValueError("Too small to fragment")
    else:
        segments = [ [ item [index:index + step] ] for index in range(0, len(item_given), step) ]
        return segments

def padder(item, size):
    i = str(item)
    if len(i) < size:
        while len(i) < size:
            i = i.__add__(' ')
    else:
        raise ValueError("Larger or equal to size given")        
    return i
    
def hasher(item):
  return sha3_512(bytes( str(item), 'utf-8' )).hexdigest()
      
# Intended to assist those who are used to 'for' loops in C, Java, etc.
# Needs more versatility, especially when dividing.
def for_loop(i, limit, increment, logic):
    if logic is 'add':
        while (i < limit):
            i += increment
        return i
    elif logic is 'sub':
        while (i < limit):
            i -= increment
        return i
    elif logic is 'mul':
        while (i < limit)
            i *= increment
        return i
    elif logic is 'div':
        while (i > limit):
            i = i / increment
        return
      
#######################
# Coroutine Handeling #
#######################


# All coroutines use 'async' def instead of the @coroutine decorator, for return type purposes

# Uses wait() function to await. Could not [await coro for coro in coros] because exe is not async
async def waits(*coros): return [await each for each in coros]

async def wait(coro): return await coro

def execute(coro): return loop.run_until_complete(wait(coro))

def executes(*coros): 
    for each in  [waits(coro) for coro in coros]: return loop.run_until_complete(each)
    
def executes_if_true(*coros, condition):
    if condition: 
        for each in  [waits(coro) for coro in coros]: return loop.run_until_complete(each)
        
def executes_if_false(*coros, condition):
    if not condition: 
        for each in  [waits(coro) for coro in coros]: return loop.run_until_complete(each)

def run_safely(coro, loop):
    return asyncio.run_coroutine_threadsafe(coro,loop)
#needs work
def diagnose_coro(coro):
    if not iscoroutinefunction(coro):
        raise ValueError("Can only diagnose coroutine objects")
    else:  
        return f"The coro has the following code: {coro.cr_code!s}\nThe stacksize of this coro is: {coro.cr_code.co_stacksize!s}"
        
def coro_flags(coro) : return f"The flags are: {coro.cr_code.co_flags!s}"

def coro_stacksize(coro): return f"The stacksize of this coro is: {coro.cr_code.co_stacksize!s}"

def coro_frame(coro): return f"The frame of this coro is: {coro.cr_frame!s} "

# David Beazely made called_from_coro
def called_from_coro(obj):  return bool(sys._getframe(obj).f_code.co_flags & 0x80)

def coro_to_task(future):  future = Task(future) ; return future




##################
# Task Handeling #
##################

def task_stack(task_obj): return "The stack is: {task_obj.get_stack()!s}"

#def task_cancel(task_obj): return "Task cancelled" if task_obj.cancel() else raise RuntimeError("Cancelling Task failed")

def task_cancel(task_obj): raise RuntimError("Cancelling Task failed") if (task_obj.cancel() == False) else "Task cancelled"

# turns _asyncio.Task type into coroutine type. converts datatypes.
# task = to_coroutine(task)
def to_coroutine(task): task = task._coro; return task

def taskinfo(task_obj):  return task_obj._repr_info(), task_obj._state, task._loop

def set_task_result(task_obj, result): return task_obj.set_result(result)

def wakeup_task_with_coro(task_obj, coro): return task._wakeup(coro)    
    
    

##################
# Frame Handling #
##################
def show_frame(num, frame):
    print("Frame = {0} \nFunction_Called = {1} \nFile/Line = {2}:{3}".format(sys._getframe(num), frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno))

def frames_of_funcs(count_of_funcs):
    for num in range(0, count_of_funcs):
        frame = sys._getframe(count_of_funcs)
        show_frame(num, frame)



def callframes(num_of_calls):
    for num in range(0, num_of_calls):
        frame = sys._getframe(num)
        show_frame(num, frame)
