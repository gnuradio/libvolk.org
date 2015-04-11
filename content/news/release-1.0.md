title: Initial Release
author: Nathan West
date: 04-11-2015

VOLK 1.0 is available. This is the first release of VOLK as an independently
tracked sub-project of GNU Radio.

## Contributors

VOLK has been tracked separetly from GNU Radio since 2014 Dec 23. Contributors
between the split and the initial release are

 * Albert Holguin <aholguin_77@yahoo.com>
 * Doug Geiger <doug.geiger@bioradiation.net>
 * Elliot Briggs <elliot.briggs@gmail.com>
 * Julien Olivain <julien.olivain@lsv.ens-cachan.fr>
 * Michael Dickens <michael.dickens@ettus.com>
 * Nathan West <nathan.west@okstate.edu>
 * Tom Rondeau <tom@trondeau.com>

## Changes

### QA

The test and profiler have significantly changed. The profiler supports run-time
changes to vlen and iters to help kernel development and provide more
flexibility on embedded systems. Additionally there is a new option to update an
existing volk_profile results file with only new kernels which will save time
when updating to newer versions of VOLK

The QA system creates a static list of kernels and test cases. The QA testing
and profiler iterate over this static list rather than each source file keeping
its own list. The QA also emits XML results to lib/.unittest/kernels.xml which
is formatted similarly to JUnit results.

### Modtool

Modtool was updated to support the QA and profiler changes.

### Kernels

New proto-kernels:

 * 16ic_deinterleave_real_8i_neon
 * 16ic_s32f_deinterleave_32f_neon
 * fix preprocessor errors for some compilers on byteswap and popcount puppets

ORC was moved to the asm kernels directory.

### volk_malloc

The posix_memalign implementation of Volk_malloc now falls back to a standard
malloc if alignment is 1.

### Miscellaneous

Several build system and cmake changes have made it possible to build VOLK both
independently with proper soname versions and in-tree for projects such as GNU
Radio.

The static builds take advantage of cmake object libraries to speed up builds.

Finally, there are a number of changes to satisfy compiler warnings and make QA
work on multiple machines.
