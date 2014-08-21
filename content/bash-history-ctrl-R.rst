Searching bash history with ctrl-R
==================================

:date: 2014-08-20 21:53
:tags: bash
:category: blog
:slug: bash-history-ctrl-R

Wow, bash is cool. A couple of days ago I discovered a simple way to search through bash history by piping the `history` command through `grep` for a favourite old command and then follow through with a copy-n-paste. Turns out there's an even simpler way to achieve that. Bash has a built in search function!

Simply press `ctrl-R` and start typing the first characters of that command you're looking for. Bash will start matching it with the most recent occurence. Pressing `ctrl-R` again and bash will scroll backwards to the next most recent one. When you find it, press `Enter` to re-execute that command or use left- or right-arrow keys to start editing the command.

Check out this `tutorial`_ courtesy of the folks at Digital Ocean for the full dirt on bash history features.

Very. Very. Cool.

.. _tutorial: https://www.digitalocean.com/community/tutorials/how-to-use-bash-history-commands-and-expansions-on-a-linux-vps

