Switching to Pelican
####################
:date: 2012-12-24

So, I haven't been blogging lately because I've been meaning to scrap my
Blogger setup and move to using Pelican_. Part of the battle was getting a
theme that made me happy, the other part of the battle was sitting down to
actually make things happen.

First off, let me just say that Pelican is a pretty great platform. And I am
not saying that because I have the pleasure of working with Alexis_, but
because it lets me use reST_ to write my entries and I can heavily customize
everything about its display.

One of the things I knew I wanted was the ability to use bootstrap_
themes. Luckily someone else had already made that possible, two someones in
fact! I found both of them in the `pelican-themes`_ repo which houses a number
of themes for Pelican. `themes/bootstrap`_ and `themes/bootstrap2`_ are the two
that are included in this aggregation and I found I liked the layout of
themes/bootstrap a bit more.

Unfortunately, I found that themes/bootstrap was built for a much older version
of bootstrap and that I'd have to modify things to make it work. Also, I found
a couple stylistic nits with it (especially when I changed to a darker theme)
that needed addressing as well. Fortunately for me, it wasn't very hard to
update it to the newest bootstrap and I'll be sending a pull request to
`pelican-themes`_ with the fixes needed once I am pretty sure I have ironed
everything out.

.. _Pelican: http://blog.getpelican.com/
.. _Alexis: http://blog.notmyidea.org/
.. _reST: http://docutils.sourceforge.net/rst.html
.. _`pelican-themes`: https://github.com/getpelican/pelican-themes
.. _bootstrap: http://twitter.github.com/bootstrap/
.. _`themes/bootstrap`: https://github.com/getpelican/pelican-themes/tree/master/bootstrap
.. _`themes/bootstrap2`: https://github.com/getpelican/pelican-themes/tree/master/bootstrap2
