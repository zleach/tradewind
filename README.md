Tradewind
============

Running
------------

First, you'll need to clone the repo.

    $ git https://github.com/zleach/tradewind.git
    $ cd tradewind

Second, let's download `pip`, `virtualenv`, `foreman`, and the [`heroku`
Ruby gem](http://devcenter.heroku.com/articles/using-the-cli).

    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ sudo gem install foreman heroku

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate

Running Tradewind
------------------------

Now, you can run the application locally.

    $ foreman start

Reactivating the Virtual Environment
------------------------------------

If you haven't worked with `virtualenv` before, you'll need to
reactivate the environment everytime you close or reload your terminal.

    $ source env/bin/activate

If you don't reactivate the environment, then you'll probably receive a
screen full of errors when trying to run the application locally.