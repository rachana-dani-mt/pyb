import sys

""" Prints message """

def helloworld(out):

    """ Uses sys out to write message """

    out.write("Hello world from python project! :)\n")

helloworld(sys.stdout)