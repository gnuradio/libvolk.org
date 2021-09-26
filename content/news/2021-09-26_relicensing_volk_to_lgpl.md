title: Help us relicense VOLK under LGPL
author: Johannes Demel
date: 26-09-2021
summary: We started the process to relicense VOLK under LGPLv3+. We ask all contributors to support us.


Dear VOLK community,

we are writing to let you know that we are working towards a new major
release of VOLK. The possibly biggest change will be that we intend to
use a different license for this release: VOLK 3.0 shall be licensed
under the LGPL 3.0 (or later).
To do this effectively, we will need your help, should you agree. If you
are already aware of this effort and are in support, you can skip to
"What are you asking from contributors?" below, but we recommend you
read this letter in its entirety to make sure you understand our
intentions and process.

Thanks for your support!


# Why are we doing this?

In retrospect, LGPL would probably have been the better choice for VOLK
from the get-go. The FSF recommendations on libraries states that ["If
developers are already using an established alternative library released
under a nonfree license or a lax pushover license, then we recommend
using the GNU Lesser General Public License (LGPL)."](https://www.gnu.org/licenses/license-recommendations.html).

We agree with this recommendation, and want to avoid VOLK being a SIMD
library exclusively used by GNU Radio (and a few others), while other
software packages rally behind other SIMD libraries, that are more
liberally licensed.

We could have chosen an even less restrictive license, but we are
believers in copyleft, and believe the LGPL strikes the right balance
between not restricting users in which types of software they may use
VOLK, and requiring users to continue upstreaming their modifications to
VOLK.


# How are we going to do this?

Relicensing codebases is a complex process, full of potential pitfalls.
To avoid any misconceptions, ambiguities, or legal issues, we have
decided to go for the nuclear option: We will delete all of VOLK, and
start from scratch, using the LGPL from the beginning of VOLK 3.0.
It would be a futile attempt to try and recreate the decades of work
that went into previous versions of VOLK without violating the VOLK 2.0
license. We are therefore asking all contributors to re-grant us
permission to include their code, previously submitted into VOLK
versions 1 and 2, into the newly licensed VOLK 3. The process for
contributors is simple (see below), but first, we want to explain how
this works.

For contributing to VOLK 2.0, most of you signed a CLA, granting the
copyright to the FSF. This CLA includes a paragraph stating that the FSF
grants back to the developer the rights to use their contributions as
they see fit.

We cannot copy code from VOLK 2.0, since that is GPL licensed. But we
can ask you to resubmit your contributions to VOLK 3.0, which is LGPL
licensed. And that's what we're asking you to do in this letter. The
process to do so is really simple and will be explained shortly.

Once your previous contributions are re-submitted, the copyright will
fall back onto the original authors.


# What's going to happen to VOLK 2?

VOLK 2 will remain GPL-licensed. We may choose to continue supporting it
with bug fixes, but the main development focus will lie on VOLK 3 going
forward.

# Will there be other changes in VOLK 3.0 other than the license change?
The roadmap for VOLK 3.0 is not yet fully laid out, but we are
considering making some API-breaking changes in VOLK 3 along with the
relicensing.
At the moment, we consider approaches to fix complex data type
incompatibilities between C and C++.


# What are you asking from contributors?

To grant us permission to use your contributions under the LGPLv3+ license
for VOLK 3.0, we ask that you sign the paragraph [HERE](https://github.com/gnuradio/volk/blob/main/AUTHORS_RESUBMITTING_UNDER_LGPL_LICENSE.md). You
can do this either by submitting a pull request against [THIS FiLE](https://github.com/gnuradio/volk/blob/main/AUTHORS_RESUBMITTING_UNDER_LGPL_LICENSE.md),
adding your name and email address as they appear in previous
commits. Alternatively, you can send us an email, in which you state
that you've read and understood the following paragraph, and we will add
your name on your behalf. You should have received an email asking for code re-submissions.

There is *no need to submit pull requests with your previous
submissions*. Once you have agreed to re-submit your code to VOLK 3, we
will pull your submissions out of git history and apply them to the VOLK
3 branch under the new license on your behalf.

Should you not wish to re-use your contributions for VOLK 3, we
understand and respect that, and will not include your code in future
versions of VOLK. For logistical purposes, it would be very helpful if
you still respond and let us know about your decision, so
we can more easily track how many contributors are in agreement with
this change.


# Relicensing Agreement (this goes into the repo)
This statement goes into the commit message.

> I, {contributor name}, hereby resubmit all my contributions to the VOLK project and repository under the terms of the LGPL-3.0-or-later.
> 
> My GitHub handle is {github handle}.
> 
> My email addresses used for contributions are: {email address}, ... .
> 
> I hereby agree that contributions made by me in the past, to previous versions of VOLK, may be re-used for inclusion in VOLK 3. I understand that VOLK 3 will be relicensed under LGPL-3.0-or-later.
