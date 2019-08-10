title: Release v1.4
author: Nathan West
date: 03-26-2018

# VOLK v1.4

A lot of really good changes came to VOLK with v1.4. It wouldn't have been possible without the following contributors:

## Contributors

 * Andrej Rode <mail@andrejro.de>
 * Bernhard M. Wiedemann <bwiedemann@suse.de>
 * Carles Fernandez <carles.fernandez@gmail.com>
 * Christoph Mayer <Christoph.Mayer@cern.ch>
 * Damian Miralles <damian.miralles@colorado.edu>
 * Douglas Anderson <douglas.j.anderson@gmail.com>
 * hcab14 <hcab14@gmail.com>
 * Johannes Demel <ufcsy@student.kit.edu>
 * Josh Blum <josh@joshknows.com>
 * luz.paz <luzpaz@users.noreply.github.com>
 * Magnus Lundmark <magnus@skysense.io>
 * Marcus Müller <marcus@hostalia.de>
 * Michael Dickens <michael.dickens@ettus.com>
 * Nathan West <nwest@deepsig.io>
 * Nick Foster <bistromath@gmail.com>
 * Paul Cercueil <paul.cercueil@analog.com>
 * Stefan Wunsch <stefan.wunsch@student.kit.edu>

##Changes

Generally, there are a lot of kernel changes and some minor dependency changes. I'm trying to remove boost as a dependency and we've introduced mako templates rather than the old Cheetah-templates to keep in line with GNU Radio. There are also several new CI files that support appveyor, travis-ci, and gitlab. Right now all pull requests must pass travis-ci.

###Kernels

The easiest way to show these changes is simply with two lists:

New kernels

 * `32 bit reversal`
 * `32f_s32f_s32f_mod_range_32f`
 * double precision (`64f_XXX`...)
     * multiply
     * add
 * `32f_64f_multiply_64f`
 * `add 32f_64f_add_64f`
 * `32fc_x2_add_32fc`

New proto-kernels by architecture

AVX(2):

Note that in some cases an unaligned version was added where an aligned version already existed

 * `volk_64f_convert_32f`
 * `volk_64f_x2_max_64f`
 * `volk_64f_x2_min_64f`
 * `volk_32f_x2_add_32f`
 * `32i_x2_and_32i`
 * `32i_x2_or_32i`
 * conjugate dot products
 * `32f_accumulator_32f`
 * `stddev_and_mean`
 * `volk_32f_*` kernels
 * `32f_x2_divide_32f`
 * `32f_x2_dot_prod_16i`
 * `volk_32f_s32f_normalize`
 * `volk_32f_s32f_stddev_32f`
 * `volk_32f_sqrt_32f`
 * `volk_32f_x2_max_32f`
 * `volk_32f_x2_min_32f`
 * `32f_x2_s32f_interleave_16ic`
 * `32f_x2_subtract_32f`
 * `32f_x2_s32f_interleave_16ic`
 * `32f_x2_subtract_32f`
 * `32f_x2_subtract_32f`
 * `32f_x2_s32f_interleave_16ic`
 * `volk_8ic_s32f_deinterleave_*`
 * `32f_log2_32f`
 * `volk_32f_s32f_convert_8i` and `16i`

NEON:

 * move all neonasm to aligned protokernels
 * added ARM version of volk_32u_reverse_32u (RBIT)
 * `volk_32fc_x2_divide_32fc`
 * `volk_32fc_32f_add_32fc`
 * `volk_32f_x2_divide_32f`
 * `volk_8i_s32f_convert_32f`

Additionally, there are new protokernel intrinsics available for use in writing new kernels.

Then, we also had some general kernel and protokernel bug fixes and using proper type-named C functions which happened to increase performance:

The polarbutterfly went through some heavy refactoring and bug fixes as well as adding an AVX version.
Fix GH issue #139 for `32fc_index_max_*` kernels resulting in a slightly wrong index being returned.
Fix bug 106 (volk_64u_popcnt bug in generic implementation)

###CI and Builds

As previously mentioned there are appveyor, travis-ci, and gitlab CI files available. There is a travis-ci instance checking all pull requests at https://travis-ci.org/gnuradio/volk/ and a gitlab mirror running CI checks at https://gitlab.com/n-west/volk.

While working on these CI files the kernel tests were split in to individual ctest targets so that each kernel is its own test rather than running them as a monolithic binary. This allows parallel testing, but mostly enables easier diagnostics when a test fails. The readme is now a markdown file that renders well on GitHub and Gitlab along with the travis-ci status as a badge.

Within this release two tools were run that reorganized includes and fixed a bunch of typos within code.

As part of the attempt to build VOLK without boost a bunch of app and build utilities were written to replace boost-code. This shouldnt be visible to the user, but will hopefully make future builds easier and smaller with fewer build and run-time dependencies. Builds with python 2.7 and 3 should work-- although six is required for python2.7 support.

Some build changes make it easier to do a relocatable build and order all files before building so that building from a particular revision (from now on) should be reproducible across machines building the same architectures. To use a relocatable install use the VOLK_PREFIX environment variable. This should support snaps (Canonical packaging environment).

###Modtool

    modtool: update the cmake find module for volk mods
    modtool: deconflict module include guards from main volk
 
