title: Release v1.2
author: Nathan West
date: 12-23-2015


Release v1.2

Contributors
============

 * Ben Hilburn <ben.hilburn@ettus.com>
 * Doug Geiger <doug.geiger@bioradiation.net>
 * Johannes Demel <ufcsy@student.kit.edu>
 * Marcus Müller <marcus@hostalia.de>
 * Michael Dickens <michael.dickens@ettus.com>
 * Nathan West <nathan.west@okstate.edu>
 * Pascal Giard <pascal.giard@lacime.etsmtl.ca>

Changes
=======

Kernels
-------

New kernels for doing polar codes are available with generic, SSE3, and AVX
implementations. This is the result of ESA SoC by Jannes Demel and used in
GNU Radio.

The rotator protokernels now normalize phase after every time finished through
the main for loop to guarantee normalization happens for a series of calls with
smaller vector lengths.

Some kernels now use inacc tolerances for QA. The kernels themselves are exactly
the same funcationality as before, but with the existing QA tolerance would fail
on NEON due to sqrt and inverse approximations in NEON.

