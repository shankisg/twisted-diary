"""
Calling method with argument in twisted.
"""

from twisted.internet import reactor


def hello_word(msg):
    print("Hello world from {}.".format(msg))
    reactor.stop()

reactor.callWhenRunning(hello_word, "twisted")
reactor.run()
