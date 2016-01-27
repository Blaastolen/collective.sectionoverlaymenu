import os
from setuptools import setup
from setuptools import find_packages

version = '0.1.dev0'

setup(
    name='collective.sectionoverlaymenu',
    version=version,
    description="A dropdown menu for the top menu populated with content from pages",
    long_description=open("README.rst").read() + "\n" +
    open("CHANGELOG.rst").read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.0',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone menu overlay megamenu dropdown',
    author='Martin Reistadbakk, Blåstolen AS',
    author_email='info@blaastolen.com',
    url='https://github.com/collective/collective.sectionoverlaymenu',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'test': ['plone.testing [zca, z2]', 'unittest2'],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
