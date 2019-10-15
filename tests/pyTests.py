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

import numpy
from pygenTestLib import *
import unittest

#######################################
#        Matrix
#######################################

## Of type int
class MatrixConversionCheckInt(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size matrix")
        structure = RandomDynamicSizeMatrixInt(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size matrix")
        structure = RandomFixedSizeMatrixInt()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size matrix")
        structure = RandomHalfDynamicSizeMatrixInt(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size vector")
        structure = RandomDynamicSizeVectorInt(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size vector")
        structure = RandomFixedSizeVectorInt()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowVectorInt(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowVectorInt()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size matrix list")
        structure = RandomDynamicSizeMatrixInt(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size vector list")
        structure = RandomDynamicSizeVectorInt(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowVectorInt(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

## Of type float32
class MatrixConversionCheckFloat(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size matrix")
        structure = RandomDynamicSizeMatrixFloat(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size matrix")
        structure = RandomFixedSizeMatrixFloat()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size matrix")
        structure = RandomHalfDynamicSizeMatrixFloat(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size vector")
        structure = RandomDynamicSizeVectorFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size vector")
        structure = RandomFixedSizeVectorFloat()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowVectorFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowVectorFloat()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size matrix list")
        structure = RandomDynamicSizeMatrixFloat(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size vector list")
        structure = RandomDynamicSizeVectorFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowVectorFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

## Of type float
class MatrixConversionCheckDouble(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size matrix")
        structure = RandomDynamicSizeMatrixDouble(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size matrix")
        structure = RandomFixedSizeMatrixDouble()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size matrix")
        structure = RandomHalfDynamicSizeMatrixDouble(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size vector")
        structure = RandomDynamicSizeVectorDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size vector")
        structure = RandomFixedSizeVectorDouble()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowVectorDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowVectorDouble()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size matrix list")
        structure = RandomDynamicSizeMatrixDouble(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size vector list")
        structure = RandomDynamicSizeVectorDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowVectorDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

## Of type complex float32
class MatrixConversionCheckCFloat(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size matrix")
        structure = RandomDynamicSizeMatrixCFloat(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size matrix")
        structure = RandomFixedSizeMatrixCFloat()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size matrix")
        structure = RandomHalfDynamicSizeMatrixCFloat(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size vector")
        structure = RandomDynamicSizeVectorCFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size vector")
        structure = RandomFixedSizeVectorCFloat()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowVectorCFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowVectorCFloat()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size matrix list")
        structure = RandomDynamicSizeMatrixCFloat(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size vector list")
        structure = RandomDynamicSizeVectorCFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowVectorCFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

## Of type complex float
class MatrixConversionCheckCDouble(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size matrix")
        structure = RandomDynamicSizeMatrixCDouble(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size matrix")
        structure = RandomFixedSizeMatrixCDouble()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size matrix")
        structure = RandomHalfDynamicSizeMatrixCDouble(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size vector")
        structure = RandomDynamicSizeVectorCDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size vector")
        structure = RandomFixedSizeVectorCDouble()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowVectorCDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowVectorCDouble()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size matrix list")
        structure = RandomDynamicSizeMatrixCDouble(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size vector list")
        structure = RandomDynamicSizeVectorCDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowVectorCDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

#######################################
#        Array
#######################################

## Of type int
class ArrayConversionCheckInt(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size array")
        structure = RandomDynamicSizeArrayInt(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size array")
        structure = RandomFixedSizeArrayInt()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size array")
        structure = RandomHalfDynamicSizeArrayInt(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size column array")
        structure = RandomDynamicSizeColumnArrayInt(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size column array")
        structure = RandomFixedSizeColumnArrayInt()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowArrayInt(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowArrayInt()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size array list")
        structure = RandomDynamicSizeArrayInt(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size column array list")
        structure = RandomDynamicSizeColumnArrayInt(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowArrayInt(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

## Of type float32
class ArrayConversionCheckFloat(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size array")
        structure = RandomDynamicSizeArrayFloat(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size array")
        structure = RandomFixedSizeArrayFloat()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size array")
        structure = RandomHalfDynamicSizeArrayFloat(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size column array")
        structure = RandomDynamicSizeColumnArrayFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size column array")
        structure = RandomFixedSizeColumnArrayFloat()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowArrayFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowArrayFloat()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size array list")
        structure = RandomDynamicSizeArrayFloat(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size column array list")
        structure = RandomDynamicSizeColumnArrayFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowArrayFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

## Of type float
class ArrayConversionCheckDouble(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size array")
        structure = RandomDynamicSizeArrayDouble(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size array")
        structure = RandomFixedSizeArrayDouble()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size array")
        structure = RandomHalfDynamicSizeArrayDouble(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size column array")
        structure = RandomDynamicSizeColumnArrayDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size column array")
        structure = RandomFixedSizeColumnArrayDouble()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowArrayDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowArrayDouble()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size array list")
        structure = RandomDynamicSizeArrayDouble(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size column array list")
        structure = RandomDynamicSizeColumnArrayDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowArrayDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

## Of type complex float32
class ArrayConversionCheckCFloat(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size array")
        structure = RandomDynamicSizeArrayCFloat(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size array")
        structure = RandomFixedSizeArrayCFloat()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size array")
        structure = RandomHalfDynamicSizeArrayCFloat(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size column array")
        structure = RandomDynamicSizeColumnArrayCFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size column array")
        structure = RandomFixedSizeColumnArrayCFloat()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowArrayCFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowArrayCFloat()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size array list")
        structure = RandomDynamicSizeArrayCFloat(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size column array list")
        structure = RandomDynamicSizeColumnArrayCFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowArrayCFloat(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

## Of type complex float
class ArrayConversionCheckCDouble(unittest.TestCase):
    def test_Matrices(self):
        print("Launch Dynamic size array")
        structure = RandomDynamicSizeArrayCDouble(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Fixed size array")
        structure = RandomFixedSizeArrayCDouble()
        mat = structure.get()
        self.assertTrue(structure.check(mat))

        print("Launch Half-dynamic size array")
        structure = RandomHalfDynamicSizeArrayCDouble(8)
        mat = structure.get()
        self.assertTrue(structure.check(mat))

    def test_vectors(self):
        print("Launch Dynamic size column array")
        structure = RandomDynamicSizeColumnArrayCDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size column array")
        structure = RandomFixedSizeColumnArrayCDouble()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_row_vectors(self):
        print("Launch Dynamic size row array")
        structure = RandomDynamicSizeRowArrayCDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec))

        print("Launch Fixed size row array")
        structure = RandomFixedSizeRowArrayCDouble()
        vec = structure.get()
        self.assertTrue(structure.check(vec))

    def test_list_Matrices(self):
        print("Launch Dynamic size array list")
        structure = RandomDynamicSizeArrayCDouble(5, 8)
        mat = structure.get()
        self.assertTrue(structure.check(mat.tolist()))

    def test_list_vectors(self):
        print("Launch Dynamic size column array list")
        structure = RandomDynamicSizeColumnArrayCDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

    def test_list_row_vectors(self):
        print("Launch Dynamic size row array list")
        structure = RandomDynamicSizeRowArrayCDouble(8)
        vec = structure.get()
        self.assertTrue(structure.check(vec.tolist()))

if __name__ == '__main__':
    unittest.main()
