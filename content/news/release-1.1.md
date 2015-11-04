title: Release v1.1
author: Nathan West
date: 08-24-2015

Release v1.1

Contributors
============

The following authors have contributed code to this release:

 * Doug Geiger <doug.geiger@bioradiation.net>
 * Elliot Briggs <elliot.briggs@gmail.com>
 * Marcus Mueller <marcus@hostalia.de>
 * Nathan West <nathan.west@okstate.edu>
 * Pascal Giard <evilynux@gmail.com>
 * Tom Rondeau <tom@trondeau.com>

Changes
=======

This release contains all of the bug fixes from v1.0.1
and v1.0.2 as well as new features and other changes that
didn't belong on maint. The following is a summary of
non-maint changes.

Architectures
-------------

New architectures exist for the AVX2 and FMA ISAs. Along
with the build-system support the following kernels have
no proto-kernels taking advantage of these architectures:

 * 32f_x2_dot_prod_32f
 * 32fc_x2_multiply_32fc
 * 64_byteswap
 * 32f_binary_slicer_8i
 * 16u_byteswap
 * 32u_byteswap

QA/profiler
-----------

The profiler now generates buffers that are vlen + a tiny
amount and generates random data to fill buffers. This is
intended to catch bugs in protokernels that write beyond
num_points.

Miscellaneous
-------------

 * All builds now use '-Wall'
 * Removed stray references to PCC and Altivec
