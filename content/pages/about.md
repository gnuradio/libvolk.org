title: about
save_as: about.html

# Overview

VOLK is the Vector-Optimized Library of Kernels. It is a free library,
currently offered under the LGPLv3, that contains kernels of hand-written SIMD
code for different mathematical operations. Since each SIMD architecture can be
very different and no compiler has yet come along to handle vectorization
properly or highly efficiently, VOLK approaches the problem differently.

For each architecture or platform that a developer wishes to vectorize for, a
new proto-kernel is added to VOLK. At runtime, VOLK will select the correct
proto-kernel. In this way, the users of VOLK call a kernel for performing the
operation that is platform/architecture agnostic. This allows us to write
portable SIMD code that is optimized for a variety of platforms.


# History

VOLK was introduced as a part of GNU Radio in late 2010 based on code released
in the public domain. In 2015 it was released as an independent library for use
by a wider audience. In 2023 the process to re-license VOLK under LGPLv3+ was
finalized.
