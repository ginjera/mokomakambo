Inserting images in restructured text
=====================================

:date: 2014-08-10 19:03 
:tags: pelican, ReST
:category: blog
:slug: inserting-images-in-restructuredtext

I was struggling to figure out how to insert an image into a post. The example from the pelican docs simply rendered as text. 

.. code-block:: Markup
   ![Alt Text]({filename}/images/han.jpg)

Until I realised that the example was for Markdown. I was writing in restructuredtext. The equivalent in restructuredtext is:

.. code-block:: Markup
   .. image:: {filename}/images/han.jpg
      :alt: Alt Text

So there it is.
