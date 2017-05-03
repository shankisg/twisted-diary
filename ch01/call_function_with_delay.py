"""
Calling a method with delay in twisted.
"""

from twisted.internet import reactor


def hello_word():
    print("Hello world with delay.")
    reactor.stop()

# first argument for callLater is delay in seconds.
reactor.callLater(2, hello_word)
reactor.run()
