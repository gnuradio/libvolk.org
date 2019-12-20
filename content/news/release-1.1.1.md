title: Release v1.1.1
author: Nathan West <nathan.west@okstate.edu>
date:   Sat Oct 31 12:17:18 2015 -0400
summary: This is the first maintenance release with only bug fixes since v1.1

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
