#!/usr/bin/python
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
there = os.path.join(here, "..", "build")
lib = [os.path.abspath(os.path.join(there, i)) for i in os.listdir(there) if "lib" in i][0]
sys.path.insert(0, lib)
import sift
import numpy
import scipy.misc

lena = scipy.misc.lena()
s = sift.SiftPlan(template=lena, profile=False, device=(1, 0))
kp = s.keypoints(lena)
