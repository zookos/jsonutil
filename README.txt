This was originally part of jsonutil
http://tahoe-lafs.org/trac/jsonutil
http://pypi.python.org/pypi/jsonutil


python ./setup.py test

Some modules have self-benchmarks provided.  For example, to benchmark
the cache module, do

python -OOu -c 'from jsonutil.test import test_cache; test_cache.quick_bench()'

or for more complete and time-consuming results:

python -OOu -c 'from jsonutil.test import test_cache; test_cache.slow_bench()'

(The "-O" is important when benchmarking, since cache has extensive
self-tests that are optimized out when -O is included.)


LICENCE

You may use this package under the GNU General Public License, version 2 or, at
your option, any later version.  You may use this package under the Transitive
Grace Period Public Licence, version 1.0, or at your option, any later version.
(You may choose to use this package under the terms of either licence, at your
option.)  You may use this package under the Simple Permissive Licence, version
1 or, at your option, any later version.  See the file COPYING.GPL for the
terms of the GNU General Public License, version 2.  See the file
COPYING.TGPPL.html for the terms of the Transitive Grace Period Public Licence,
version 1.0.  See the file COPYING.SPL.txt for the terms of the Simple
Permissive Licence, version 1.
