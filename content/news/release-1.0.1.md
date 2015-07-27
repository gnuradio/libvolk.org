title: Maintenance Release v1.0.1
author: Nathan West
date: 2015-07-08

This is a maintenance release with bug fixes since the initial release of v1.0
in April.

Contributors
============

The following authors have contributed code to this release:

 * Doug Geiger <doug.geiger@bioradiation.net>
 * Elliot Briggs <elliot.briggs@gmail.com>
 * Marcus Mueller <marcus@hostalia.de>
 * Nathan West <nathan.west@okstate.edu>
 * Tom Rondeau <tom@trondeau.com>

Changes
=======

Kernels
-------

Several bug fixes in different kernels. The NEON implementations of the
following kernels have been fixed:

 * 32f_x2_add_32f
 * 32f_x2_dot_prod_32f
 * 32fc_s32fc_multiply_32fc
 * 32fc_x2_multiply_32fc

Additionally the NEON asm based 32f_x2_add_32f protokernels were not being used
and are now included and available for use via the dispatcher.

The 32f_s32f_x2_fm_detect_32f kernel now has a puppet. This solves QA seg
faults on 32-bit machines and provide a better test for this kernel.

The 32fc_s32fc_x2_rotator_32fc generic protokernel replaced cabsf with hypotf
for better Android support.

Building
--------

Static builds now trigger the applications (volk_profile and volk-config-info)
to be statically linked.

The file gcc_x86_cpuid.h has been removed since it was no longer being used.
Previously it provided cpuid functionality for ancient compilers that we do
not support.

All build types now use -Wall.

QA and Testing
--------------

The documentation around the --update option to volk_profile now makes it clear
that the option will only profile kernels without entries in volk_profile. The
signature of run_volk_tests with expanded args changed signed types to unsigned
types to reflect the actual input.

The remaining changes are all non-functional changes to address issues from
Coverity.
