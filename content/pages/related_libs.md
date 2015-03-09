title: Related Libraries
save_as: comparisons.html

There are several libraries and tools leveraging SIMD processors with different
techniques. The table below is an attempt to list similar libraries that are
known to the authors of VOLK and provide a high-level comparison of libraries.
This is not meant to be an authoritative list of SIMD-optimizing projects as
much as a resource to begin the decision making process.

| Library | License | Brief Description | Hardware Targets
|---------|---------|-------------------|------------------
| [VOLK](http://libvolk.org) | GPLv3 | Hand-tuned routines with a generic CPU dispatcher | SSE*, AVX, NEON
| [Yeppp!](http://www.yeppp.info) | 3-clause BSD | GTRI research project | SSE*, AVX, AVX2, FMA, NEON, NEONv2
| [Vc](https://compeng.uni-frankfurt.de/index.php?id=vc) | LGPLv3 | SIMD Vector classes for C++ | SSE*, AVX
| [libsimdpp](https://github.com/p12tic/libsimdpp/wiki) | Boost License | C++ wrapper for SIMD intrinsics | SSE2+, AVX, AVX2, FMA, AVX-512, NEON
| [Ne10](http://projectne10.github.io/Ne10/) | 3-clause BSD | Math functions optimized for ARM | NEON
| [Intel IPP](https://software.intel.com/en-us/intel-ipp) | proprietary | Math routines optimized for Intel processors | SSE*, AVX, AVX2, AVX-512
| [Libm](http://developer.amd.com/tools-and-sdks/cpu-development/libm/) | AMD License | Extended libm with vectorized routines for AMD processors |
