"""
Calling a method in twisted.
"""

from twisted.internet import reactor


def hello_word():
    print("Hello world")
    reactor.stop()

reactor.callWhenRunning(hello_word)
reactor.run()
