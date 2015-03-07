title: home
save_as: index.html

<div class="row"> 
  <img class="img-responsive center-block" src="theme/assets/volk.png"> 
</div> 
<div class="row text-center"> 
  <p> 
    VOLK is the Vector-Optimized Library of Kernels. It is a free library, 
    currently offered under the GPLv3, that contains kernels of hand-written SIMD 
    code for different mathematical operations. Since each SIMD architecture can be 
    very different and no compiler has yet come along to handle vectorization 
    properly or highly efficiently, VOLK approaches the problem differently. 
</p> 

  <p> 
  For each architecture or platform that a developer wishes to vectorize for, a
  new proto-kernel is added to VOLK. At runtime, VOLK will select the correct 
  proto-kernel. In this way, the users of VOLK call a kernel for performing the
  operation that is platform/architecture agnostic. This allows us to write 
  portable SIMD code. 
  </p> 
</div> 
<div class="row text-center"> 
    <a href="https://github.com/gnuradio/volk.git" class="btn btn-primary btn-large"> 
        <i class="fa fa-code-fork"></i> Web Git 
    </a> 
    <a href="doxygen/" class="btn btn-primary btn-large"> 
        <i class="fa fa-book"></i> Documentation 
    </a> 
    <a href="javascript:void(0)" class="btn btn-primary btn-large"> 
        <i class="fa fa-bug"></i> Issues 
    </a> 
</div>
