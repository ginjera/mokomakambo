Searching bash history
======================

:date: 2014-08-16 21:53
:tags: bash
:category: blog
:slug: bash-history

Recently I was helping my better half to download megabytes of image files from an ftp site. She was having trouble because the ftp connection kept breaking and messing up her workflow of right-click and downloading individual files in her browser. I got to show off the power of the command line with `wget` and its powerful features like `--no-clobber`, `--continue`, `--read-timeout=*seconds*`, `--tries=*number*`, `--recursive`, `--level=*depth*`, `--user=*username*`, and `password=*password*`.

When she made the same request a couple of days later, I wanted to retrieve thos `wget` commands from bash history to avoid retyping them esp. the long ftp urls.

Turns out it's pretty simple. Just run history through a grep filter

.. code-block:: bash
   
   $ history | grep wget

and out comes a list of commands containing `wget`.

From there it was just a simple cut and paste.
