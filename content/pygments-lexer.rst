============================
Lexical analysis in pygments
============================

:date: 2014-08-13 21:24
:category: blog
:tags: pelican, pygments
:slug: pygments-lexer

Lexicadelicalicious-what?! According to `wikipedia, lexical analysis`_  is the process of converting a sequence of characters into a sequence of tokens, i.e. meaningful character strings. In the case of pelican, the `pygments`_ module does this job. In restructured text, a `.. code-blocks::` directive tells pygments what to do:

.. code-block:: rst

   .. code-block:: lexer
   
      <bunch of code>

Trouble is what are the avaiable lexers? Surely there must be a list somewhere. Indeed there is. And we find it at the pygments documentation site. It's a long list. We find languages (`python`, `ruby`), markup (`css`, `html`), 'non-source code file types' (`latex`, `yaml`, `restructuredtext`) but strangely no `markdown`. Hmm, I wonder how folks highlight markdown syntax with pygments. Or don't they?


.. _wikipedia, lexical analysis: http://en.wikipedia.org/wiki/Lexical_analysis
.. _pygments: http://pygments.org/docs/lexers/ 
