:title: Uncomfortable and Unsatisfied
:date: 2013-05-30

I want to build a small website. Django feels a bit heavy for what I want to do, and I would like to give node more of an honest shot for building websites. I need to store some user data (name, email, notification settings). Also I need to store some topics and opinions on those topics. I'd like my users to be able to log in using Mozilla Persona.

The first thing that pops up when one goes to do websites using node is Express. You start using it, maybe asking a couple questions, and you find out noisy parts of the node world hate express and think you should use something else. Unfortunately, they may list one or two alternatives, likely those are things they wrote themselves or a friend of theirs wrote. They are probably especially young, which means there is unlikely to be drop in support for anything.

Once you get past that part, you are told there isn't support for the 10 things you actually wanted to do, but don't worry there are 100 modules for each of those things, you'll have to learn everything about the web package you are using, as well as the packages you want to glue together, praying there is some sort of common api. Sorry though, this one is streams based, but not those streams you are used to, you have to write a compatibility layer. And this one isn't stream based but doesn't like the request object you handed it, etc etc.

I get that a lot of this is a matter of comfort. I feel better in django/python because I've been here for a long time. I know what modules are good and which ones to avoid. Maybe, if I can get over this uncomfortable feeling, I can make something satisfying. As it stands though, I am unable to find anything that makes me happy when it comes to building websites in node.