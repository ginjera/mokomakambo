==============================
Colour settings for ls command
==============================

:date: 2014-08-11 17:53
:tags: ls, bash
:category: blog
:slug: Colour-settings-for-the-ls-command

I use CentOS 6.5 on my personal laptop. For the longest time, I lived with the awful colour defaults for the ls command. Certain directories default to blue text on green background.

.. image:: {filename}/images/Awful-default-dir-colour.png

Ugh, grosser than gross!

It occurred to me recently that there must be a text file somewhere that I could tweak to make this more readable. 

Lo and behold, here's the file that does the trick: /etc/DIR_COLORS. And there are nice helpful comments, which tell us that we can adjust 3 elements:

.. code-block:: bash

    # Below are the color init strings for the basic file types. A color init
    # string consists of one or more of the following numeric codes:
    # Attribute codes:
    # 00=none 01=bold 04=underscore 05=blink 07=reverse 08=concealed
    # Text color codes:
    # 30=black 31=red 32=green 33=yellow 34=blue 35=magenta 36=cyan 37=white
    # Background color codes:
    # 40=black 41=red 42=green 43=yellow 44=blue 45=magenta 46=cyan 47=white

Scanning through that file, I found the blue (34) on green (42) culprit:

.. code-block:: bash
   
    OTHER_WRITABLE 34;42 # dir that is other-writable (o+w) and not sticky

Rather than mess around with /etc/DIR_COLORS, I made a copy at ~/.dircolors and changed the settings for OTHER_WRITABLE to 01;35: 

.. image:: {filename}/images/Ahh-much-better.png

Ahhh, much, much better...

For a full list of available colours, this `site <http://linux-sxs.org/housekeeping/lscolors.html>`_ gives the full low down.

