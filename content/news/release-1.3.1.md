title: Release v1.3.1
author: Nathan West
date: 03-25-2018

Contributors
===========

The following people had commits in this release. Thanks to them for making VOLK possible!

* Carles Fernandez <carlesfernandez@gmail.com>
* Damian Miralles <damian.miralles@colorado.edu>
* Josh Blum <josh@joshknows.com>
* Marcus Müller <marcus@hostalia.de>
* Michael Dickens <michael.dickens@ettus.com>
* Nathan West <nathan.west@gnuradio.org>
* Nick Foster <bistromath@gmail.com>
* Paul Cercueil <paul.cercueil@analog.com>

##Changes

This is an API-compatible support release that only includes bug fixes.

###Kernels

Fix GH issue #139 for 32fc_index_max_* kernels. Note that this is a minor API change that modern compilers should be OK with if they can handle the implicit type conversion.

Use 'powf' to match variables and avoid implicit type converstion.
Makes some older compilers happy, allowing 'make test' to pass.
kernels: Add AVX support to `32f_x2_divide_32f`,`32f_x2_dot_prod_16i`.

Fix bug 106 (volk_64u_popcnt bug in generic implementation)

Adds protokernels for AVX support. Modest speed improvements in some of the kernels, however, it seems to be related to the host architecture being used

Adds AVX support to `volk_32f_s32f_normalize`,`volk_32f_s32f_stddev_32f`, `volk_32f_sqrt_32f`, `volk_32f_x2_max_32f` and `volk_32f_x2_min_32f`. Some speed improvements can be seen with the new protokernel addition.

Adds unaligned protokernels to `32f_x2_s32f_interleave_16ic` and `32f_x2_subtract_32f`.

Adds unaligned versions to the afore mentioned kernels, relative speeds improvements shown in both cases.

Add NEON, AVX and unaligned versions of SSE4.1 and SSE.

Added `__VOLK_PREFETCH()` compatibility macro

`__VOLK_PREFETCH()` performs `__builtin_prefetch()` on GCC compilers and is otherwise a NOP for other systems. The use of `__builtin_prefetch` was replaced with `__VOLK_PREFETCH()` to make the kernels portable.

###Documentation

Fixing a minimal bug in the log2 docstring

###Build Support

Support relocated install with VOLK_PREFIX env var.

Some packaging systems such as snaps will install the volk library to a dynamically chosen location.  The install script can set an evironment variable so that the library reports the correct prefix.

cmake: support empty `CMAKE_INSTALL_PREFIX`

###QA and CI

qa: lower tolerance for 32fc_mag to fix issue #96
apps: fix profile update reading end of lines
Add a AppVeyor compatible YAML file for building on the AppVeyor CI

###Modtool

Update the cmake find module for volk mods and deconflict module include guards from main volk.

