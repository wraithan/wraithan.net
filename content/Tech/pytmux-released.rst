:title: pytmux Released
:date: 2013-03-07

So this last weekend I wrote a tool named pytmux_. It is a basic session
builder/wrapper around tmux so you can get going faster when you start up your
system. It uses a JSON based config files, is pretty minimal right now, but I
hope to make it better in the future as I use it more.

The idea is you specify what you want a session to look like in JSON, like so::

  {
      "name": "wraithan.net",
      "windows": [
          {
              "name": "editor",
              "command": "workon wraithan.net && emacs"
          },
          {
              "command": "workon wraithan.net && make regenerate"
          },
          {
              "command": "workon wraithan.net && git pull"
          }
      ]
  }

Then you run::

  pytmux run wraithan.net  # This is keyed off of file name.

And blamo! It builds a as well as it can. It also has convenience commands like
``pytmux list``, ``pytmux edit <config>``, and ``pytmux doctor``. Which you can
learn about in the README_ currently. Better docs (such as sphinx on RTD) in
the future if that is really needed.

Anyway, I hope y'all like it. Feel free to open issues on the tracker on GitHub
if there are any features missing that you'd like.

.. _pytmux: https://github.com/wraithan/pytmux
.. _README: https://github.com/wraithan/pytmux/blob/master/README.rst
