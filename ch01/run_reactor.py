"""
How to start a twisted reactor(Event loop).

- To start do reactor.run()
- To stop press ctrl-c
"""

from twisted.internet import reactor


print("Starting reactor...")
reactor.run()
