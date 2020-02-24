title: Release v2.2.1
author: Johannes Demel
date: 02-24-2020
summary: VOLK bugfix release v2.2.1

Hi everyone,

with VOLK 2.2.0, we introduced another AVX rotator bug which is fixed with this release.
In the process 2 more bugs were identified and fixed. Further, we saw some documentation improvements.


### Contributors

*  Clayton Smith <argilo@gmail.com>
*  Michael Dickens <michael.dickens@ettus.com>


### Changes


* Fix loop bound in AVX rotator
* Fix out-of-bounds read in AVX2 square dist kernel
* Fix length checks in AVX2 index max kernels
* includes: rearrange attributes to simplify macros Whitespace
* kernels: fix usage in header comments
