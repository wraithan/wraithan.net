:title: Server Time
:date: 2013-02-17

About a year ago, some friend and I were talking about each getting
servers then going to a local data center and getting a third of a
rack. There was lots of excitement but unfortunately most of us
weren't in a position to purchase the needed hardware at the
time. Fast forward a year and now the topic has come up again but this
time things are looking a lot more feasible.

Now, why would someone need or even want a hardware server in these
days of fluffy cloud servers floating everywhere? Isn't managing a
server pretty lack luster now that we have these wonderful solutions
like Heroku? It's true, running a server isn't glamorous, but it is
cost effective depending on your skill level, needs, and willingness
to put in a little bit of effort. 

The cost is where it really shines. The up front cost of ~$1800 that I
am looking at for the server I'd like is pretty steep, it doesn't say,
"I'm saving money!" when you look at it. But, how I like to look at it
is how the cost breaks down over the course of a year or two. $150/mo
if you put it over a year, $75/mo if you put it over two. Which still
looks pretty hefty, but consider the amount of hardware you get for
that. This is a dual Xeon system, each 4x2.4GHz, 64GB of RAM (easily
able ramp that up to 256GB) and I'll be running 1TB of redundant
storage to start with and have the ability to expand that if needed.

This gives me the ability to replace a couple of my Rackspace VPSs as
well as build sites that require out of band work to be done without
paying $36/mo per dyno on Heroku. This is where my savings will start
to kick in. Considering over 2 years I am looking at $75/mo for the
hardware and $50/mo (likely closer to $40) for the hosting for a total
of $125/mo. If I am able to take down my VPSs which total out to
~$35/mo, and replace 3 Heroku worker dynos, I am able to break
even. If I use it more than that, then I am saving money. And with the
level of hardware I am getting, it wont be hard to use it for more
things.

All of this said, I'll still be using Heroku to host my sites. Their
deployment, add-on management, and databases are pretty
great. Especially since I don't want to have to deal with things like
changing my nginx config every time I add a server, writing/modifying
a deployment script for each new service, etc. I just get some extra
things I've been wanting, and the ability to consolidate some of my
servers and costs. Overall I am pretty stoked.

If you are a friend of mine, especially in the Portland area, and
interested in joining us, let me know. I'll gladly give you more
information. We are keeping it to people we know and trust since
people will potentially have hardware access.
