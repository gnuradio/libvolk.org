tag v1.1.1
Tagger: Nathan West <nathan.west@okstate.edu>
Date:   Sat Oct 31 12:17:18 2015 -0400

Release v1.1.1

This is the first maintenance release with only bug fixes since v1.1

Contributors
============

The following authors have contributed code to this release:

 * Ben Hilburn <ben.hilburn@ettus.com>
 * Marcus Müller <marcus@hostalia.de>
 * Nathan West <nathan.west@okstate.edu>
 * Pascal Giard <pascal.giard@lacime.etsmtl.ca>

Changes
=======

Coverity
--------

Ben spent the post-GRcon hackfest fixing a few errors that the GNU Radio coverity
scan reported. The critical fix was a potential buffer overflow in the profiler while
reading existing results.

Builds
------

Based on feedback from packagers VOLK has made strides towards reproducible builds.
The latest effort is removing the builddate.

Several header includes and ifdef guards have been shuffled around to make VOLK
out of tree modules easier to work with and ARM builds more robust to compiler whims.

commit ff1933b1827c68c05c6edaa7e86fd25abe45051b
Author: Nathan West <nathan.west@okstate.edu>
Date:   Sat Oct 31 12:14:17 2015 -0400

    Update CMake for release v1.1.1

diff --git a/CMakeLists.txt b/CMakeLists.txt
index 77b96ef..612c9df 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -44,7 +44,7 @@ message(STATUS "Build type set to ${CMAKE_BUILD_TYPE}.")
 
 set(VERSION_INFO_MAJOR_VERSION 1)
 set(VERSION_INFO_MINOR_VERSION 1)
-set(VERSION_INFO_MAINT_VERSION 0)
+set(VERSION_INFO_MAINT_VERSION 1)
 include(VolkVersion) #setup version info
 
 
