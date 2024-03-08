import sys

"""
This module contains a function named "helloworld" that 
writes a message to the standard output stream. 
The message is "Hello world from python project! :)". 
The function takes an argument "out" which is a file-like 
object representing the output stream. 
The function uses the "write" method of the "out" 
object to write the message to the output stream.
"""

def helloworld(out):
    """ Uses sys out to write message """
    out.write("Hello world from python project! :)\n")

helloworld(sys.stdout)