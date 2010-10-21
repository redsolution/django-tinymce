Welcome to the tinymce documentation
====================================

tinymce is a Django_ application that contains a widget to render a form field
as a TinyMCE_ editor.

Features:
- Use as a form widget or with a view.
- Enhanced support for content languages.
- Integration with the TinyMCE spellchecker.
- Enables predefined link and image lists for dialogs.
- Can compress the TinyMCE Javascript code.
- Integration with `django-filebrowser`_.

The tinymce code is licensed under the `MIT License`_. See the ``LICENSE.txt``
file in the distribution. Note that the TinyMCE editor is distributed under
`its own license`_.

.. _Django: http://www.djangoproject.com/
.. _TinyMCE: http://tinymce.moxiecode.com/
.. _`django-filebrowser`: http://code.google.com/p/django-filebrowser/
.. _`MIT License`: http://www.opensource.org/licenses/mit-license.php
.. _`its own license`: http://tinymce.moxiecode.com/license.php


Installation
------------

1. Place the ``tinymce`` module in your Python path. You can put it into your
Django project directory or run ``python setup.py install`` from a shell.
2. Copy the ``jscripts/tiny_mce`` directory from the TinyMCE distribution into
a directory named ``js`` in your media root. You can override the location in
your settings (see below).
3. If you want to use any of the views add tinymce your installed applications
list and URLconf:

``settings.py``::

  INSTALLED_APPS = (
      ...
      'tinymce',
      ...
  )

``urls.py``::

  urlpatterns = patterns('',
      ...
      (r'^tinymce/', include('tinymce.urls')),
      ...
  )


.. _configuration:

Configuration
-------------

The application can be configured by editing the project's ``settings.py``
file.

``TINYMCE_JS_URL`` (default: ``settings.MEDIA_URL + 'js/tiny_mce/tiny_mce.js'``)
  The URL of the TinyMCE javascript file.

``TINYMCE_JS_ROOT`` (default: ``settings.MEDIA_ROOT + 'js/tiny_mce'``)
  The filesystem location of the TinyMCE files.

``TINYMCE_DEFAULT_CONFIG`` (default: ``{'theme': "simple", 'relative_urls': False}``)
  The default TinyMCE configuration to use. See `the TinyMCE manual`_ for all
  options. To set the configuration for a specific TinyMCE editor, see the
  ``mce_attrs`` parameter for the ``widget``.

``TINYMCE_SPELLCHECKER`` (default: ``False``)
  Whether to use the spell checker through the supplied view. You must add
  ``spellchecker`` to the TinyMCE plugin list yourself, it is not added
  automatically.

``TINYMCE_COMPRESSOR`` (default: ``False``)
  Whether to use the TinyMCE compressor, which gzips all Javascript files into
  a single stream.  This makes the overall download size 75% smaller and also
  reduces the number of requests. The overall initialization time for TinyMCE
  will be reduced dramatically if you use this option.

``TINYMCE_FILEBROWSER`` (default: ``True`` if ``'filebrowser'`` is in ``INSTALLED_APPS``, else ``False``)
  Whether to use `django-filebrowser`_ as a custom filebrowser for media
  inclusion. See the `official TinyMCE documentation on custom filebrowsers`_.

Example::

  TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
  TINYMCE_DEFAULT_CONFIG = {
      'plugins': "table,spellchecker,paste,searchreplace",
      'theme': "advanced",
  }
  TINYMCE_SPELLCHECKER = True
  TINYMCE_COMPRESSOR = True

REdsolution CMS classifiers:
----------------------------

`Content plugins`_


.. _`the TinyMCE manual`: http://wiki.moxiecode.com/index.php/TinyMCE:Configuration
.. _`official TinyMCE documentation on custom filebrowsers`: http://wiki.moxiecode.com/index.php/TinyMCE:Custom_filebrowser
.. _`Content plugins`: http://www.redsolutioncms.org/classifiers/content

Copyright (C) 2008 Joost Cassee
This program is licensed under the MIT License (see LICENSE.txt)

See http://django-tinymce.googlecode.com for docs.

-- 
Joost Cassee
joost@cassee.net
