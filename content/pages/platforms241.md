title: Kernels per platform
save_as: platforms.html

# Kernels per platform

Here we present a snapshot of currently available VOLK kernels and their implementations in [VOLK version 2.4.1](release-v421.html).
An [overview for VOLK version 1.0.0](platforms100.html) is also available.
Most, if not all kernels in the SSE/AVX/AVX512 columns offer aligned and unaligned versions.


## Exact SIMD extension versions

Each column contains the exact SIMD extension that is required for that kernel, e.g. `sse` or `sse4_1`.
The columns represent the SIMD register width and archictecture such as x86 128bit SSE or ARM 128bit NEON.
The ORC column indicates if a [liborc](https://gstreamer.freedesktop.org/projects/orc.html) implementation for this kernel is available.
Only kernels that benefit from newer instruction set versions should receive specialized implementations.

| Kernel name | generic | SSE | AVX | AVX512 | NEON | ORC | Other |
|:----------- | ------- | --- | --- | ------ | ---- | --- | ----- |
| volk_16i_32fc_dot_prod_32fc | generic|sse|avx2, avx2_fma|-|neon|-|- |
| volk_16i_branch_4_state_8 | generic|ssse3|-|-|-|-|- |
| volk_16i_convert_8i | generic|sse2|avx2|-|neon|-|- |
| volk_16i_max_star_16i | generic|ssse3|-|-|neon|-|- |
| volk_16i_max_star_horizontal_16i | generic|ssse3|-|-|neonasm, neon|-|- |
| volk_16i_permute_and_scalar_add | generic|sse2|-|-|-|-|- |
| volk_16i_s32f_convert_32f | generic|sse4_1, sse|avx, avx2|-|neon|-|- |
| volk_16i_x4_quad_max_star_16i | generic|sse2|-|-|neon|-|- |
| volk_16i_x5_add_quad_16i_x4 | generic|sse2|-|-|neon|-|- |
| volk_16ic_convert_32fc | generic|sse2|avx, avx2|-|neon|-|- |
| volk_16ic_deinterleave_16i_x2 | generic|ssse3, sse2|avx2|-|-|orc|- |
| volk_16ic_deinterleave_real_16i | generic|sse2, ssse3|avx2|-|-|-|- |
| volk_16ic_deinterleave_real_8i | generic|ssse3|avx2|-|neon|orc|- |
| volk_16ic_magnitude_16i | generic|sse, sse3|avx2|-|neonv7|orc|- |
| volk_16ic_s32f_deinterleave_32f_x2 | generic|sse|avx2|-|neon|orc|- |
| volk_16ic_s32f_deinterleave_real_32f | generic|sse, sse4_1|avx2|-|-|-|- |
| volk_16ic_s32f_magnitude_32f | generic|sse, sse3|avx2|-|-|orc|- |
| volk_16ic_x2_dot_prod_16ic | generic|sse2|avx2|-|neon_vma, neon_optvma, neon|-|- |
| volk_16ic_x2_multiply_16ic | generic|sse2|avx2|-|neon|-|- |
| volk_16u_byteswap | generic|sse2|avx2|-|neon_table, neon|orc|- |
| volk_32f_64f_add_64f | generic|-|avx|-|neon|-|- |
| volk_32f_64f_multiply_64f | generic|-|avx|-|-|-|- |
| volk_32f_8u_polarbutterfly_32f | generic|-|avx2, avx|-|-|-|- |
| volk_32f_accumulator_s32f | generic|sse|avx|-|-|-|- |
| volk_32f_acos_32f | generic|sse4_1|avx, avx2_fma|-|-|-|- |
| volk_32f_asin_32f | generic|sse4_1|avx, avx2_fma|-|-|-|- |
| volk_32f_atan_32f | generic|sse4_1|avx, avx2_fma|-|-|-|- |
| volk_32f_binary_slicer_32i | generic_branchless, generic|sse2|avx|-|-|-|- |
| volk_32f_binary_slicer_8i | generic_branchless, generic|sse2|avx2|-|neon|-|- |
| volk_32f_convert_64f | generic|sse2|avx|-|-|-|- |
| volk_32f_cos_32f | generic_fast, generic|sse4_1|avx2, avx2_fma|-|neon|-|- |
| volk_32f_exp_32f | generic|sse2|-|-|-|-|- |
| volk_32f_expfast_32f | generic|sse4_1|avx, avx_fma|-|-|-|- |
| volk_32f_index_max_16u | generic|sse, sse4_1|avx|-|-|-|- |
| volk_32f_index_max_32u | generic|sse4_1, sse|avx|-|neon|-|- |
| volk_32f_invsqrt_32f | generic|sse|avx|-|neon|-|- |
| volk_32f_log2_32f | generic|sse4_1|avx2, avx2_fma|-|neon|-|- |
| volk_32f_null_32f | generic|-|-|-|-|-|- |
| volk_32f_s32f_32f_fm_detect_32f | generic|sse|avx|-|-|-|- |
| volk_32f_s32f_add_32f | -|sse|avx|-|neon|orc|- |
| volk_32f_s32f_calc_spectral_noise_floor_32f | generic|sse|avx|-|-|-|- |
| volk_32f_s32f_convert_16i | generic|sse2, sse|avx, avx2|-|-|-|- |
| volk_32f_s32f_convert_32i | generic|sse2, sse|avx|-|-|-|- |
| volk_32f_s32f_convert_8i | generic|sse2, sse|avx2|-|-|-|- |
| volk_32f_s32f_multiply_32f | generic|sse|avx|-|neon|orc|- |
| volk_32f_s32f_normalize | generic|sse|avx|-|-|orc|- |
| volk_32f_s32f_power_32f | generic|sse, sse4_1|-|-|-|-|- |
| volk_32f_s32f_s32f_mod_range_32f | generic|sse2, sse|avx|-|-|-|- |
| volk_32f_s32f_stddev_32f | generic|sse, sse4_1|avx|-|-|-|- |
| volk_32f_sin_32f | generic|sse4_1|avx2, avx2_fma|-|neon|-|- |
| volk_32f_sqrt_32f | generic|sse|avx|-|neon|orc|- |
| volk_32f_stddev_and_mean_32f_x2 | generic|sse, sse4_1|avx|-|-|-|- |
| volk_32f_tan_32f | generic|sse4_1|avx2, avx2_fma|-|neon|-|- |
| volk_32f_tanh_32f | generic|sse|avx, avx_fma|-|-|-|series |
| volk_32f_x2_add_32f | generic|sse|avx|avx512f|neonpipeline, neonasm, neon|orc|- |
| volk_32f_x2_divide_32f | generic|sse|avx|avx512f|neon|orc|- |
| volk_32f_x2_dot_prod_16i | generic|sse|avx, avx2_fma|avx512f|-|-|- |
| volk_32f_x2_dot_prod_32f | generic|sse4_1, sse3, sse|avx, avx2_fma|avx512f|neonasm, neonasm_opts, neonopts, neon|-|- |
| volk_32f_x2_interleave_32fc | generic|sse|avx|-|neon|-|- |
| volk_32f_x2_max_32f | generic|sse|avx|avx512f|neon|orc|- |
| volk_32f_x2_min_32f | generic|sse|avx|avx512f|neon|orc|- |
| volk_32f_x2_multiply_32f | generic|sse|avx|avx512f|neon|orc|- |
| volk_32f_x2_pow_32f | generic|sse4_1|avx2, avx2_fma|-|-|-|- |
| volk_32f_x2_s32f_interleave_16ic | generic|sse2, sse|avx2|-|-|-|- |
| volk_32f_x2_subtract_32f | generic|sse|avx|avx512f|neon|orc|- |
| volk_32f_x3_sum_of_poly_32f | generic|sse3|avx, avx2_fma, avx_fma|-|neon, neonvert|-|- |
| volk_32fc_32f_add_32fc | generic|-|avx|-|neon|-|- |
| volk_32fc_32f_dot_prod_32fc | generic|sse|avx, avx2_fma|-|neon_unroll, neonpipeline, neonasm, neon, neonasmvmla|-|- |
| volk_32fc_32f_multiply_32fc | generic|sse|avx|-|neon|orc|- |
| volk_32fc_conjugate_32fc | generic|sse3|avx|-|neon|-|- |
| volk_32fc_convert_16ic | generic|sse2|avx2|-|neonv8, neon|-|- |
| volk_32fc_deinterleave_32f_x2 | generic|sse|avx|-|neon|-|- |
| volk_32fc_deinterleave_64f_x2 | generic|sse2|avx|-|neon|-|- |
| volk_32fc_deinterleave_imag_32f | generic|sse|avx|-|neon|-|- |
| volk_32fc_deinterleave_real_32f | generic|sse|avx2|-|neon|-|- |
| volk_32fc_deinterleave_real_64f | generic|sse2|avx2|-|neon|-|- |
| volk_32fc_index_max_16u | generic|sse3|avx2_variant_1, avx2_variant_0|-|-|-|- |
| volk_32fc_index_max_32u | generic|sse3|avx2_variant_1, avx2_variant_0|-|neon|-|- |
| volk_32fc_magnitude_32f | generic|sse3, sse|avx|-|neon_fancy_sweet, neon|orc|- |
| volk_32fc_magnitude_squared_32f | generic|sse3, sse|avx|-|neon|-|- |
| volk_32fc_s32f_atan2_32f | generic|sse, sse4_1|-|-|-|-|- |
| volk_32fc_s32f_deinterleave_real_16i | generic|sse|avx2|-|-|-|- |
| volk_32fc_s32f_magnitude_16i | -|sse, sse3|avx2|-|-|-|- |
| volk_32fc_s32f_power_32fc | generic|sse|-|-|-|-|- |
| volk_32fc_s32f_power_spectrum_32f | generic|sse3|-|-|neon|-|- |
| volk_32fc_s32f_x2_power_spectral_density_32f | generic|sse3|avx|-|-|-|- |
| volk_32fc_s32fc_multiply_32fc | generic|sse3|avx, avx_fma|-|neon|-|- |
| volk_32fc_s32fc_x2_rotator_32fc | generic|sse4_1|avx, avx_fma|-|neon|-|- |
| volk_32fc_x2_add_32fc | generic|sse|avx|-|neon|-|- |
| volk_32fc_x2_conjugate_dot_prod_32fc | generic|sse3, sse, sse_32|avx|-|neon|-|- |
| volk_32fc_x2_divide_32fc | generic|sse3|avx|-|neon|-|- |
| volk_32fc_x2_dot_prod_32fc | generic|sse3, sse_64, sse_32|avx, avx_fma|-|neon_opttests, neon_optfmaunroll, neon_optfma, neon|-|- |
| volk_32fc_x2_multiply_32fc | generic|sse3|avx, avx2_fma|-|neon_opttests, neonasm, neon|orc|- |
| volk_32fc_x2_multiply_conjugate_32fc | generic|sse3|avx|-|neon|-|- |
| volk_32fc_x2_s32f_square_dist_scalar_mult_32f | generic|sse3, sse|avx, avx2|-|-|-|- |
| volk_32fc_x2_s32fc_multiply_conjugate_add_32fc | generic|sse3|avx|-|neon|-|- |
| volk_32fc_x2_square_dist_32f | generic|sse3|avx2|-|neon|-|- |
| volk_32i_s32f_convert_32f | generic|sse2|avx2|avx512f|-|-|- |
| volk_32i_x2_and_32i | generic|sse|avx2|avx512f|neon|orc|- |
| volk_32i_x2_or_32i | generic|sse|avx2|avx512f|neon|orc|- |
| volk_32u_byteswap | generic|sse2|avx2|-|neonv8, neon|-|- |
| volk_32u_popcnt | generic|sse4_2|-|-|-|-|- |
| volk_32u_reverse_32u | -|-|-|-|neonv8|-|dword_shuffle, lut, 2001magic, byte_shuffle, bintree_permute_top_down, bintree_permute_bottom_up, 1972magic |
| volk_64f_convert_32f | generic|sse2|avx|avx512f|-|-|- |
| volk_64f_x2_add_64f | generic|sse2|avx|-|-|-|- |
| volk_64f_x2_max_64f | generic|sse2|avx|avx512f|-|-|- |
| volk_64f_x2_min_64f | generic|sse2|avx|avx512f|-|-|- |
| volk_64f_x2_multiply_64f | generic|sse2|avx|-|-|-|- |
| volk_64u_byteswap | generic|sse2, ssse3|avx2|-|neonv8|-|- |
| volk_64u_popcnt | generic|sse4_2|-|-|neon|-|- |
| volk_8i_convert_16i | generic|sse4_1|avx2|-|neon|orc|- |
| volk_8i_s32f_convert_32f | generic|sse4_1|avx2|-|neon|orc|- |
| volk_8ic_deinterleave_16i_x2 | generic|sse4_1|avx, avx2|-|-|-|- |
| volk_8ic_deinterleave_real_16i | generic|sse4_1|avx, avx2|-|-|-|- |
| volk_8ic_deinterleave_real_8i | generic|ssse3|avx, avx2|-|neon|-|- |
| volk_8ic_s32f_deinterleave_32f_x2 | generic|sse4_1, sse|avx2|-|-|-|- |
| volk_8ic_s32f_deinterleave_real_32f | generic|sse, sse4_1|avx2|-|-|-|- |
| volk_8ic_x2_multiply_conjugate_16ic | generic|sse4_1|avx2|-|-|-|- |
| volk_8ic_x2_s32f_multiply_conjugate_32fc | generic|sse4_1|avx2|-|-|-|- |
| volk_8u_x2_encodeframepolar_8u | generic|ssse3|avx2|-|-|-|- |
| volk_8u_x3_encodepolar_8u_x2 | generic|ssse3|avx2|-|-|-|- |
| volk_8u_x4_conv_k7_r2_8u | generic|-|avx2|-|-|-|spiral |
