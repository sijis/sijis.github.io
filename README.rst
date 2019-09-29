My Blog
=======

My [infrequently updated] blog. Nothing more, nothing less.

Local
-----

This is what I need to do to validate my changes locally

Build image and run it

.. code-block:: sh

    $ docker build -t mywebsite .
    $ docker run --rm -v $(pwd):/app -p 4000:4000 mywebsite
