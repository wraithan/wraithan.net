Categories as Subdomains
########################
:date: 2012-12-27

So one of the things I wanted to do with my blog is to have Tech_, Life_, and
SC2_ under their own domains so I can link to just that domain when things are
specific. It was actually surprising easy to do this, just a simple nginx
rewrite rule and some modifications of the theme templates.

This is the entry for SC2::

    server {
        listen       80;
        server_name  sc2.wraithan.net;

        location / {
            root   /srv/http/wraithan.net/output/;
            index  category/sc2.html;
        }

        #error_page  404              /404.html;                                               

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
    }

Then I changed the places that linked to the category in the template to look
like::

    <li {% if cat == category %}class="active"{% endif %}><a href="http://{{ cat.name.lower() }}.wraithan.net/">{{ cat }}</a></li>
  
I could (should) probably generalize it a bit better, but this is better than
nothing!

.. _Life: http://life.wraithan.net/
.. _SC2: http://sc2.wraithan.net/
.. _Tech: http://tech.wraithan.net/
