# -*- coding: utf-8 -*-
"""Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2020, Caleb Bell <Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import division
import types
import numpy as np
import chemicals


'''Basic module which wraps all chemicals functions with numpy's vectorize.
All other object - dicts, classes, etc - are not wrapped. Supports star 
imports; so the same objects exported when importing from the main library
will be imported from here. 

>>> from chemicals.vectorized import *

Inputs do not need to be numpy arrays; they can be any iterable:

>>> import chemicals.vectorized
>>> chemicals.vectorized.Tc(['108-88-3', '7732-18-5'])
array([591.75, 647.14])

Note that because this needs to import chemicals itself, chemicals.vectorized
needs to be imported separately; the following will cause an error:
    
>>> import chemicals
>>> chemicals.vectorized # Won't work, has not been imported yet

The correct syntax is as follows:

>>> import chemicals.vectorized # Necessary
>>> from chemicals.vectorized import * # May be used without first importing chemicals
'''

__all__ = []


__funcs = {}

for name in dir(chemicals):
    obj = getattr(chemicals, name)
    if isinstance(obj, types.FunctionType):
        obj = np.vectorize(obj)
    elif isinstance(obj, str):
        continue
    __all__.append(name)
    __funcs.update({name: obj})
globals().update(__funcs)



        
