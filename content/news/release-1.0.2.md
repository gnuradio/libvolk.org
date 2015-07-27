title: Maintenance Release v1.0.2
author: Nathan West
date: 2015-07-24

Release v1.0.2

This is a relatively minor maintenance release with bug fixes since v1.0.1.

Contributors
===========

The following have contributed code to this release:

 * Nathan West <nathan.west@okstate.edu>

Changes
=======

The major change is the CMake logic to add ASM protokernels.  Rather than
depending on CFLAGS and ASMFLAGS we use the results of VOLK's built in has_ARCH
tests. All configurations should work the same as before, but manually
specifying CFLAGS and ASMFLAGS on the cmake call for ARM native builds should
no longer be necessary.

The 32fc_s32fc_x2_rotator_32fc generic protokernel now includes a previously
implied header.

Finally, there is a fix to return the "best" protokernel to the dispatcher when
no volk_config exists. Thanks to Alexandre Raymond for pointing this out.

