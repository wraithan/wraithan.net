:title: Plethora of Projects
:date: 2013-04-11

I find myself in a place where I have many of projects that people ping me about
regularly. I enjoy each of them and would love to dedicate the time to each that
they deserve. This post is an enumeration of those projects and my goals.

`Read the Docs`_
----------------

This is definitely my highest priority project. It has the most users and with
my friend `Eric Holscher`_ soon leaving on a `long hike`_, I'll become its
primary caretaker.

First, I'd like to clean up the code base. I've already gotten all the files to
comply with flake8_; a big step forward. Next, I will refactor closer to what we
use at work, giving us a style guide to cite. During that work, I'll change the
log in system to `Mozilla Persona`_, eliminating the need for passwords. I'll
also work to increase our scant unit and integration test coverage. Lastly,
there are moderately boring and security-related architectural issues that I
won't go into.

.. _`Read the Docs`: https://readthedocs.org/
.. _`Eric Holscher`: http://ericholscher.com/
.. _`long hike`: http://ericholscher.com/blog/2013/jan/10/walk-woods/
.. _flake8: http://flake8.rtfd.org/
.. _`Mozilla Persona`: https://login.persona.org/

ZenIRCBot_
----------

Though this project has gatehred more users and contributors, it has also been a
victim of bitrot. To remedy, I will try to take over part of the May PDXNode_
hack night as a ZenIRCBot_ hack night. **<If you're interested in contributing,
ehere are details>.**

This code base is also in dire need of a cleanup. 3.0 is coming out soon, and
we'll be moving it under a `GitHub Organization`_ and splitting various parts
into their own repos. Once that is done, I'll add backwards-compatible changes
like multiple server support. The nodejs_ version will be**(-come?)** the
officially-blessed version, and though I'll try to keep the python_ and clojure_
versions up-to-date, I don't want them to hold back the project.

Finally, I've added `Aaron Parecki`_ as a contributor. We'll be reviewing each
other's patches as well as sharing the burden of project maintenance.

.. _ZenIRCBot: http://docs.zenircbot.net/
.. _PDXNode: http://www.pdxnode.com/
.. _`GitHub Organization`: https://github.com/blog/674-introducing-organizations
.. _nodejs: http://nodejs.org/
.. _python: https://python.org
.. _clojure: http://clojure.org/
.. _`Aaron Parecki`: http://aaronparecki.com/

pytmux_
-------

This is a newer project that is currently in a working state but I'd like
finish some features so can release 1.0 and leave the project in a stable
state.

The next steps for this are some more of the basic features (which are already
filed as issues on github) as well as taking some time looking at the other
projects in this space and determine what a 1.0 release should look like. This
should be a minimal amount of hacking and should result in something that
doesn't require much maintenance.

.. _pytmux: https://crate.io/packages/pytmux/

hackspots.net_
--------------

This project hasn't even started other than `gathering data`_. There is lots of
hope in it though, and I really want it to exist. It has a lot of potential for
those of us in town to discover new places to go, and to provide a place to
send people who are new to town.

The project needs to be inited, in an effort to not polarize to one of the two
bigger server side web languages (Python/Ruby) I'll likely be going with
nodejs. Theoretically there is a code base that was already started but it
isn't open source yet and rather than wait/force it to go open, I can just
build it myself.

.. _hackspots.net: http://hackspots.net/
.. _`gathering data`: https://wraithan.etherpad.mozilla.org/cafe-hacking-pdx

`Django Debug Panel`_
---------------------

This project has wonderful potential and high aspirations. Unfortunately it is
also quite a bit of work. I have lots of prior art to sort through, issues to
create, then finally I have to build it and document the protocol. This project
is on the back burner for now until I can clear some other things off my plate.

.. _`Django Debug Panel`: https://github.com/wraithan/django-debug-panel

training.wraithan.net_
----------------------

This one is in fact just throwing a 500 right now. I upgraded some stuff and it
is all broken. As I get ready to do more century rides this summer I will want
to have this around. Also I'd like to add integration for more than just
DailyMile_. There isn't a ton of work to do, other than getting it working
again.

.. _training.wraithan.net: http://training.wraithan.net/
.. _DailyMile: http://www.dailymile.com/


Summary
-------

I have a lot of projects to work on, some of which are higher priority than
others. I am feeling rather overwhelmed when you combine this list with my
hobbies, work, and other obligations. Hopefully, if you are using any of these
projects, you'll be patient with me as I try to find the time to improve them
all.
