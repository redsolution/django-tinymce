#!/usr/bin/env python

from setuptools import setup, find_packages
import metadata

app_name = metadata.name
version = metadata.version

setup(
    name="redsolutioncms.django-tinymce",
    version=version,
    description="Fork of django application that contains a widget to render a" \
            " form field as a TinyMCE editor.",
    license="MIT License",
    keywords="django widget tinymce",

    author="Joost Cassee",
    author_email="joost@cassee.net",

    maintainer='Ivan Gromov',
    maintainer_email='src@redsolution.ru',

    url="http://code.google.com/p/django-%s/" % app_name,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=\
"""
Use the TinyMCE editor for your form textareas.

Features:

* Use as a form widget or with a view.
* Enhanced support for content languages.
* Integration with the TinyMCE spellchecker.
* Enables predefined link and image lists for dialogs.
* Can compress the TinyMCE javascript files.
* Integration with django-filebrowser.
""",
    platforms=['any'],
    download_url="http://code.google.com/p/django-%s/downloads/list" \
            % app_name,
    entry_points={
        'redsolutioncms': ['tinymce = tinymce.redsolution_setup', ],
    }
)
