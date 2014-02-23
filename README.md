Tradewind
============
A sci-fi / future ship's company generator.

Running
------------

First, you'll need to clone the repo.

    $ git https://github.com/zleach/tradewind.git
    $ cd tradewind

We'll need to install the dependencies, with `pip`.
    
    $ pip install -r requirements.txt 

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages venv
    $ source venv/bin/activate
    
Finally, once it's running you can load tradewind in your browser.

    0.0.0.0:5000
    (Stop the server by pressing ctrl-c)
    
Running Tradewind
------------------------

Now, you can run the application locally with foreman.

    $ foreman start

Reactivating the Virtual Environment
------------------------------------

If you haven't worked with `virtualenv` before, you'll need to
reactivate the environment everytime you close or reload your terminal.

    $ source venv/bin/activate

If you don't reactivate the environment, then you'll probably receive a
screen full of errors when trying to run the application locally.