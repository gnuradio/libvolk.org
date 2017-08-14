title: Release v1.2.3
author: Nathan West
date: 07-2-2016

Release v1.2.3

Contributors
===========

 * Albert Holguin <aholguin_77@yahoo.com>
 * Geof Nieboer <gnieboer@gcndevelopment.com>
 * Marcus Müller <marcus@hostalia.de>
 * Nathan West <nate.ewest@gmail.com>
 * Nathan West <nathan.west@gnuradio.org>
 * Paul Cercueil <paul.cercueil@analog.com>
 * Tom Rondeau <tom@trondeau.com>
 * Vanya Sergeev <vsergeev@gmail.com>

Changes
=======

The index_max kernels were named with the wrong output datatype. To fix this there are new kernels that return a 32u (int32_t) and the existing kernels had their signatures changed to return 16u (int16_t).

The output to stdout and stderr has been shuffled around. There is no longer a message that prints what VOLK machine is being used and the warning messages go to stderr rather than stdout.

MSVC builds without explicitly set flags.

VolkConfig.cmake includes a hardcoded install path so that VOLK is easier to find in non-standard prefixes. Similarly the BOOST_ROOT environment variable is no longer overridden so that it is easier to find BOOST in non-standard prefixes.

The 32fc_index_max kernels previously were only accurate to the SSE register width (4 points). This was a pretty serious and long-lived bug that's been fixed and the QA updated appropriately.
