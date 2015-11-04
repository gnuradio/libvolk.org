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

commit 52f219294c2424b541739b28dd7296196067dba9
Author: Nathan West <nathan.west@okstate.edu>
Date:   Mon Aug 24 12:54:11 2015 -0400

    Update CMake for release v1.1

diff --git a/CMakeLists.txt b/CMakeLists.txt
index 44cbd52..77b96ef 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -44,7 +44,7 @@ message(STATUS "Build type set to ${CMAKE_BUILD_TYPE}.")

 set(VERSION_INFO_MAJOR_VERSION 1)
 set(VERSION_INFO_MINOR_VERSION 1)
-set(VERSION_INFO_MAINT_VERSION git)
+set(VERSION_INFO_MAINT_VERSION 0)
 include(VolkVersion) #setup version info


