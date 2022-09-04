title: Release v2.5.2
author: Johannes Demel
date: 09-04-2022
summary: VOLK release v2.5.2

Hi everyone!

We have a new VOLK release! We are happy to announce VOLK v2.5.2! We want to thank all contributors. This release wouldn't have been possible without them.

We are happy to announce that our re-licensing effort is complete. This has been a long and challenging journey. Being technical: There are 3 people left (out of 74) who we haven't been able to get in contact with (at all), for a total of 4 (out of 1092) commits, 13 (of 282822) additions, and 7 (of 170421) deletions. We have reviewed these commits and all are simple changes (e.g., 1 line change) and most are no longer relevant (e.g., to a file that no longer exists). VOLK maintainers are in agreement that the combination -- small numbers of changes per committer, simple changes per commit, commits no longer relevant -- means that we can proceed with re-licensing without the approval of the folks. We will try reaching out periodically to these folks, but we believe it unlikely we will get a reply.

This maintainance release is intended to be the last VOLK 2.x release. After we completed our re-licensing effort, we want to make a VOLK 3.0 release soon. VOLK 3.0 will be fully compatible with VOLK 2.x on a technical level. However, VOLK 3+ will be released under LGPL. We are convinced a license change justifies a major release.

### Contributors

* Aang23 <qwerty15@gmx.fr>
* Clayton Smith <argilo@gmail.com>
* Johannes Demel <demel@ant.uni-bremen.de>, <demel@uni-bremen.de>
* Michael Dickens <michael.dickens@ettus.com>
* Michael Roe <michael-roe@users.noreply.github.com>

### Changes

* Android
    - Add Android CI
    - Fix armeabi-v7a on Android
* CI
    - Update all test jobs to more recent actions
* volk_8u_x4_conv_k7_r2_8u
    - Add NEON implementation `neonspiral` via `sse2neon.h`
* Fixes
    - Fix out-of-bounds reads
    - Fix broken neon kernels
    - Fix float to int conversion
* CMake
    - Suppress superfluous warning
    - Fix Python install path calculation and documentation
* cpu_features
    - Update submodule pointer
* VOLK 3.0 release preparations
    - Use SPDX license identifiers everywhere
    - Re-arrange files in top-level folder
    - Update Doxygen and all Doxygen related tasks into `docs`
