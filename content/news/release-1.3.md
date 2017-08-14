title: Release v1.3
author: Nathan West
date: 07-2-2016

Release v1.3

Contributors
===========

 * Albert Holguin <aholguin_77@yahoo.com>
 * Carles Fernandez <carles.fernandez@gmail.com>
 * git-artes <flarroca@fing.edu.uy>
 * Marcus Müller <marcus@hostalia.de>
 * Nathan West <nathan.west@gnuradio.org>
 * Stefan Wunsch <stefan.wunsch@student.kit.edu>

Changes
=======

Several new kernels are available. These include several type conversions, some
fixed point complex operations, and a complex float divide.

Volk_config functions are now overloaded to be able to read and write to a
custom volk_config path which can be controlled with a new `--path` option in
volk_profile.

Volk-config-info can now tell you the alignment VOLK is using for your CPU and
malloc implementation used in volk_profile.

Builds define the Dual ABI macro `_GLIBCXX_USE_CXX11_ABI` to 1, which should
allow builds with GCC 4 when linking against C++ libraries that are built with
GCC 5.

