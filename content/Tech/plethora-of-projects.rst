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

This is a newer project. Though currently in a working state, I'd like to finish
some features and release 1.0 as a stable product.

The next steps are basic features (already filed as issues on github), that
should be a minimal amount of hacking and result in something that doesn't
require much maintenance.

.. _pytmux: https://crate.io/packages/pytmux/

hackspots.net_
--------------

**Since it's new, maybe add information about what it is?**

This project is still `gathering data`_. It has potential to help Portlandians
discover new **places to go**, and to provide a place to send people who are new
to town.

**(Unclear what "places to go" actually means. (i.e. go do what? This could
benefit from context, as noted above.)**

Coding hasn't yet begun. In an effort to not polarize Pythonistas or Rubyists,
I'll likely use nodejs.

.. _hackspots.net: http://hackspots.net/
.. _`gathering data`: https://wraithan.etherpad.mozilla.org/cafe-hacking-pdx

`Django Debug Panel`_
---------------------

**Could also be helped by context, especially given the similar name to the
toolbar**

Though this project has great potential, it is an unfortunate amount of work.
I've put it on the back burner until I can clear other things off my plate.

.. _`Django Debug Panel`: https://github.com/wraithan/django-debug-panel

training.wraithan.net_
----------------------

This one is broken. In fact, it's throwing a 500 right now. As I get ready to do
more century rides this summer, I'll want to **(have a place to log training
rides?)**. I'd like to add integration for more than just DailyMile_. Other than
getting it functional again, there isn't a ton of work to do.

.. _training.wraithan.net: http://training.wraithan.net/
.. _DailyMile: http://www.dailymile.com/


Summary
-------

I have many projects to work on, some of which are higher priority than others.
When combined with other hobbies, work, and obligations, I'm feeling a bit
overwhelmed. Please be patient with me as I try to find the time to work on them
all.
