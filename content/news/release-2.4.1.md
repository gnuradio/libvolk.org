title: Release v2.4.1
author: Johannes Demel
date: 17-12-2020
summary: VOLK release v2.4.1

Hi everyone!

We have a new VOLK bugfix release! We are happy to announce VOLK v2.4.1! We want to thank all contributors. This release wouldn't have been possible without them.

Our v2.4.0 release introduced quite a lot of changes under the hood. With this bugfix release, we want to make sure that everything works as expected again.


### Contributors

* A. Maitland Bottoms <bottoms@debian.org>
* Johannes Demel <demel@uni-bremen.de>
* Michael Dickens <michael.dickens@ettus.com>
* Philip Balister <philip@balister.org>
* Ron Economos <w6rz@comcast.net>
* Ryan Volz <ryan.volz@gmail.com>


### Changes

* Build
    - cpu_features CMake option
    - Add cpu_features to static library build.
    - Use static liborc-0.4 library for static library build.
    - cmake: Detect if cpu_features submodule is present.

* Install
    - Check for lib64 versus lib and set LIB_SUFFIX accordingly.

* CI
    - Add CI test for static library build.

* Releases
    - project: Include git submodules (i.e. cpu_features) in release tarball.
    - scripts: Add GPG signature to release script

* Other
    - readme: Update TravisCI status badge
