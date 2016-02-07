title: Release v1.2.1
author: Nathan West
date: 02-7-2016

Release v1.2.1

Contributors
============

 * Geof Nieboer <gnieboer@corpcomm.net>
 * Johannes Demel <ufcsy@student.kit.edu>
 * Marcus Müller <marcus@hostalia.de>
 * Nathan West <nathan.west@okstate.edu>

Changes
=======

Profiler
--------

 * Fixed a segfault in the polar butterfly puppet
 * Reverted back to input values in range [-1, 1] rather than [-pi, pi].

Builds (all windows related)
------

 * Add MSVC 14 to processor detection
 * Minor tweaks to fix builds on MSVC 2015

Kernels
-------

Small performance improvement in log2 by switching to log2f,
which is explicitly for floats.

Add reusable intrinsics for NEON. This continues the push for
creating an internal library of intrinsics that will make
composing more complex kernels from simpler reusable building
blocks without going back to memory.
