Publishing New Content
######################
:date: 2012-12-28

I am currently debating between two different ways of dealing with publishing
new posts. On one side I have a really simple fabric_ file that lets me publish
from any of my OS X or Linux systems. On the other side I am considering
setting up my weblistener_ from ZenIRCBot_ and using that to listen for call
back from GitHub saying there is new content.

The fabric solution is an already working solution that doesn't require much
upkeep and because it does the push as well as going to the server and
publishing it is the same amount of commands. It doesn't have a server side
component might crash (other than the sshd which I trust.) But it restricts me
from posting from certain devices of mine.

The automatic publishing solution has two daemon scripts and the redis daemon
to get working. I could cut this down to a single script but that requires
writing more code which hasn't been tested. On the other hand it just requires
me to push my new posts and other changes and see them on the site rather
rapidly. This allows me to use GitHub for windows or mobile applications. I
game from windows and one of my blogs is about gaming which makes this solution
pretty ideal.

I think I am going to setup the automatic publishing and see how it goes. I
don't have to remove my fabric setup because I add the automatic publishing
which lets me fall back on it. When I have the whole thing working I'll do a
full write-up on it including source.

.. _fabric: http://fabfile.com
.. _weblistener: http://example.com
.. _ZenIRCBot: http://example.com
