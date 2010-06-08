#!/usr/bin/env python

# jsonutil -- wrapper around simplejson that de-serializes decimals to Decimal
# instead of to float
#
# Author: Zooko Wilcox-O'Hearn
#
# See README.txt for licensing information.

import os, re, sys

from setuptools import find_packages, setup

trove_classifiers=[
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "License :: DFSG approved",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
    ]

PKG='jsonutil'
VERSIONFILE = os.path.join(PKG, "_version.py")
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^verstr = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        print "unable to find version in %s" % (VERSIONFILE,)
        raise RuntimeError("if %s.py exists, it must be well-formed" % (VERSIONFILE,))

setup_requires = []

# setuptools_trial is needed if you want "./setup.py trial" or
# "./setup.py test" to execute the tests.
# http://pypi.python.org/pypi/setuptools_trial
setup_requires.extend(['setuptools_trial >= 0.5'])

# darcsver is needed only if you want "./setup.py darcsver" to write a new
# version stamp in jsonutil/_version.py, with a version number derived from
# darcs history.  http://pypi.python.org/pypi/darcsver
if 'darcsver' in sys.argv[1:]:
    setup_requires.append('darcsver >= 1.0.0')

# setuptools_darcs is required to produce complete distributions (such as with
# "sdist" or "bdist_egg"), unless there is a jsonutil.egg-info/SOURCE.txt file
# present which contains a complete list of files that should be included.
# http://pypi.python.org/pypi/setuptools_darcs
setup_requires.append('setuptools_darcs >= 1.1.0')

data_fnames=[ 'COPYING.GPL', 'COPYING.TGPPL.html', 'COPYING.SPL.txt', 'README.txt', 'CREDITS' ]

# In case we are building for a .deb with stdeb's sdist_dsc command, we put the
# docs in "share/doc/python-$PKG".
doc_loc = "share/doc/" + PKG
data_files = [(doc_loc, data_fnames)]

setup(name=PKG,
      version=verstr,
      description='a wrapper around simplejson which deserializes decimals to Decimal instead of to float',
      author='Zooko O\'Whielacronx',
      author_email='zooko@simplegeo.com',
      url='http://tahoe-lafs.org/trac/' + PKG,
      license='Transitive Grace Period Public Licence', # see README.txt for details -- there are also alternative licences
      packages=find_packages(),
      include_package_data=True,
      setup_requires=setup_requires,
      install_requires=['simplejson >= 2.1.0',],
      classifiers=trove_classifiers,
      test_suite='jsonutil.test',
      zip_safe=False, # I prefer unzipped for easier access.
      )
