python-libcps
=============

Cryptographic Persistent Storage is a library for accessing your choice of
persistent key:value storage database through a layer of encryption that keeps
your data safe. Once created, it exposes the DB through the familiar dict
interface, meaning you don't really have to learn a lot of new stuff to take
advantage of this library.

If you want to see support for a specific backend, open up a ticket for it and
I'll invest an afternoon in adding support to the library. Polyfills are not
built all in a day, after all, but incrementally and adapting to demand.

This software will eventually be LGPL-licensed, when I actually get around to
adding license preambles and such everywhere. The author appreciates your
patience, and capacity to tolerate general laziness/other priorities.


Dependencies
============

 * Python 2.X
 * [python-libejtp](https://github.com/campadrenalin/EJTP-lib-python)


Backends supported
==================

 * [anydbm](http://docs.python.org/library/anydbm.html)
 * ramdict - Dummy db interface that stores all data in RAM, with no persistence.
