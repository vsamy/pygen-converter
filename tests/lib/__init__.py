# MIT License

# Copyright (c) 2019 Vincent SAMY

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#### Matrix and vectors
# int
from .pygenTestLib import RandomDynamicSizeMatrixInt
from .pygenTestLib import RandomFixedSizeMatrixInt
from .pygenTestLib import RandomHalfDynamicSizeMatrixInt
from .pygenTestLib import RandomDynamicSizeVectorInt
from .pygenTestLib import RandomDynamicSizeRowVectorInt
from .pygenTestLib import RandomFixedSizeVectorInt
from .pygenTestLib import RandomFixedSizeRowVectorInt
# float32
from .pygenTestLib import RandomDynamicSizeMatrixFloat
from .pygenTestLib import RandomFixedSizeMatrixFloat
from .pygenTestLib import RandomHalfDynamicSizeMatrixFloat
from .pygenTestLib import RandomDynamicSizeVectorFloat
from .pygenTestLib import RandomDynamicSizeRowVectorFloat
from .pygenTestLib import RandomFixedSizeVectorFloat
from .pygenTestLib import RandomFixedSizeRowVectorFloat
# float
from .pygenTestLib import RandomDynamicSizeMatrixDouble
from .pygenTestLib import RandomFixedSizeMatrixDouble
from .pygenTestLib import RandomHalfDynamicSizeMatrixDouble
from .pygenTestLib import RandomDynamicSizeVectorDouble
from .pygenTestLib import RandomDynamicSizeRowVectorDouble
from .pygenTestLib import RandomFixedSizeVectorDouble
from .pygenTestLib import RandomFixedSizeRowVectorDouble
# complex float32
from .pygenTestLib import RandomDynamicSizeMatrixCFloat
from .pygenTestLib import RandomFixedSizeMatrixCFloat
from .pygenTestLib import RandomHalfDynamicSizeMatrixCFloat
from .pygenTestLib import RandomDynamicSizeVectorCFloat
from .pygenTestLib import RandomDynamicSizeRowVectorCFloat
from .pygenTestLib import RandomFixedSizeVectorCFloat
from .pygenTestLib import RandomFixedSizeRowVectorCFloat
# complex float
from .pygenTestLib import RandomDynamicSizeMatrixCDouble
from .pygenTestLib import RandomFixedSizeMatrixCDouble
from .pygenTestLib import RandomHalfDynamicSizeMatrixCDouble
from .pygenTestLib import RandomDynamicSizeVectorCDouble
from .pygenTestLib import RandomDynamicSizeRowVectorCDouble
from .pygenTestLib import RandomFixedSizeVectorCDouble
from .pygenTestLib import RandomFixedSizeRowVectorCDouble

#### Array
# int
from .pygenTestLib import RandomDynamicSizeArrayInt
from .pygenTestLib import RandomFixedSizeArrayInt
from .pygenTestLib import RandomHalfDynamicSizeArrayInt
from .pygenTestLib import RandomDynamicSizeColumnArrayInt
from .pygenTestLib import RandomDynamicSizeRowArrayInt
from .pygenTestLib import RandomFixedSizeColumnArrayInt
from .pygenTestLib import RandomFixedSizeRowArrayInt
# float32
from .pygenTestLib import RandomDynamicSizeArrayFloat
from .pygenTestLib import RandomFixedSizeArrayFloat
from .pygenTestLib import RandomHalfDynamicSizeArrayFloat
from .pygenTestLib import RandomDynamicSizeColumnArrayFloat
from .pygenTestLib import RandomDynamicSizeRowArrayFloat
from .pygenTestLib import RandomFixedSizeColumnArrayFloat
from .pygenTestLib import RandomFixedSizeRowArrayFloat
# float
from .pygenTestLib import RandomDynamicSizeArrayDouble
from .pygenTestLib import RandomFixedSizeArrayDouble
from .pygenTestLib import RandomHalfDynamicSizeArrayDouble
from .pygenTestLib import RandomDynamicSizeColumnArrayDouble
from .pygenTestLib import RandomDynamicSizeRowArrayDouble
from .pygenTestLib import RandomFixedSizeColumnArrayDouble
from .pygenTestLib import RandomFixedSizeRowArrayDouble
# complex float32
from .pygenTestLib import RandomDynamicSizeArrayCFloat
from .pygenTestLib import RandomFixedSizeArrayCFloat
from .pygenTestLib import RandomHalfDynamicSizeArrayCFloat
from .pygenTestLib import RandomDynamicSizeColumnArrayCFloat
from .pygenTestLib import RandomDynamicSizeRowArrayCFloat
from .pygenTestLib import RandomFixedSizeColumnArrayCFloat
from .pygenTestLib import RandomFixedSizeRowArrayCFloat
# complex float
from .pygenTestLib import RandomDynamicSizeArrayCDouble
from .pygenTestLib import RandomFixedSizeArrayCDouble
from .pygenTestLib import RandomHalfDynamicSizeArrayCDouble
from .pygenTestLib import RandomDynamicSizeColumnArrayCDouble
from .pygenTestLib import RandomDynamicSizeRowArrayCDouble
from .pygenTestLib import RandomFixedSizeColumnArrayCDouble
from .pygenTestLib import RandomFixedSizeRowArrayCDouble

__all__ = ["RandomDynamicSizeMatrixInt",
           "RandomFixedSizeMatrixInt",
           "RandomHalfDynamicSizeMatrixInt",
           "RandomDynamicSizeVectorInt",
           "RandomDynamicSizeRowVectorInt",
           "RandomFixedSizeVectorInt",
           "RandomFixedSizeRowVectorInt",

           "RandomDynamicSizeMatrixFloat",
           "RandomFixedSizeMatrixFloat",
           "RandomHalfDynamicSizeMatrixFloat",
           "RandomDynamicSizeVectorFloat",
           "RandomDynamicSizeRowVectorFloat",
           "RandomFixedSizeVectorFloat",
           "RandomFixedSizeRowVectorFloat",

           "RandomDynamicSizeMatrixDouble",
           "RandomFixedSizeMatrixDouble",
           "RandomHalfDynamicSizeMatrixDouble",
           "RandomDynamicSizeVectorDouble",
           "RandomDynamicSizeRowVectorDouble",
           "RandomFixedSizeVectorDouble",
           "RandomFixedSizeRowVectorDouble",

           "RandomDynamicSizeMatrixCFloat",
           "RandomFixedSizeMatrixCFloat",
           "RandomHalfDynamicSizeMatrixCFloat",
           "RandomDynamicSizeVectorCFloat",
           "RandomDynamicSizeRowVectorCFloat",
           "RandomFixedSizeVectorCFloat",
           "RandomFixedSizeRowVectorCFloat",

           "RandomDynamicSizeMatrixCDouble",
           "RandomFixedSizeMatrixCDouble",
           "RandomHalfDynamicSizeMatrixCDouble",
           "RandomDynamicSizeVectorCDouble",
           "RandomDynamicSizeRowVectorCDouble",
           "RandomFixedSizeVectorCDouble",
           "RandomFixedSizeRowVectorCDouble",


           "RandomDynamicSizeArrayInt",
           "RandomFixedSizeArrayInt",
           "RandomHalfDynamicSizeArrayInt",
           "RandomDynamicSizeColumnArrayInt",
           "RandomDynamicSizeRowArrayInt",
           "RandomFixedSizeColumnArrayInt",
           "RandomFixedSizeRowArrayInt",

           "RandomDynamicSizeArrayFloat",
           "RandomFixedSizeArrayFloat",
           "RandomHalfDynamicSizeArrayFloat",
           "RandomDynamicSizeColumnArrayFloat",
           "RandomDynamicSizeRowArrayFloat",
           "RandomFixedSizeColumnArrayFloat",
           "RandomFixedSizeRowArrayFloat",

           "RandomDynamicSizeArrayDouble",
           "RandomFixedSizeArrayDouble",
           "RandomHalfDynamicSizeArrayDouble",
           "RandomDynamicSizeColumnArrayDouble",
           "RandomDynamicSizeRowArrayDouble",
           "RandomFixedSizeColumnArrayDouble",
           "RandomFixedSizeRowArrayDouble",

           "RandomDynamicSizeArrayCFloat",
           "RandomFixedSizeArrayCFloat",
           "RandomHalfDynamicSizeArrayCFloat",
           "RandomDynamicSizeColumnArrayCFloat",
           "RandomDynamicSizeRowArrayCFloat",
           "RandomFixedSizeColumnArrayCFloat",
           "RandomFixedSizeRowArrayCFloat",

           "RandomDynamicSizeArrayCDouble",
           "RandomFixedSizeArrayCDouble",
           "RandomHalfDynamicSizeArrayCDouble",
           "RandomDynamicSizeColumnArrayCDouble",
           "RandomDynamicSizeRowArrayCDouble",
           "RandomFixedSizeColumnArrayCDouble",
           "RandomFixedSizeRowArrayCDouble"]
