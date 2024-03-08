import sys

'''
 A simple module to print 'Hello world' 
'''

def helloworld(out):
    """ Uses sys out to write message """
    out.write("Hello world from python project! :)\n")

helloworld(sys.stdout)
