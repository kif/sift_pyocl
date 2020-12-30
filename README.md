sift_pyocl
==========

An implementation of SIFT on GPU with OpenCL

This code is no more maintained in this repository and has been merged into the `silx` project:
https://github.com/silx-kit/silx/tree/master/silx/opencl/sift

Once `silx` installed, it can be used as previously:

```
from silx.opencl import sift
sift_ocl = sift.SiftPlan(template=image)
keypoints = sift_ocl.keypoints(image)
```
