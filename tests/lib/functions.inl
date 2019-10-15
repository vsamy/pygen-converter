// MIT License

// Copyright (c) 2019 Vincent SAMY

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

/***********************************************************************
 *                               Matrix                                *
 ***********************************************************************/
template <typename T>
RandomDynamicSizeMatrix<T>::RandomDynamicSizeMatrix(Eigen::Index row, Eigen::Index col)
    : mat_(EigenType::Random(row, col))
{
}

template <typename T>
typename RandomDynamicSizeMatrix<T>::EigenType RandomDynamicSizeMatrix<T>::get()
{
    return mat_;
}

template <typename T>
bool RandomDynamicSizeMatrix<T>::check(const EigenType& mat)
{
    return mat_.isApprox(mat);
}

template <typename T>
RandomFixedSizeMatrix<T>::RandomFixedSizeMatrix()
    : mat_(EigenType::Random())
{
}

template <typename T>
typename RandomFixedSizeMatrix<T>::EigenType RandomFixedSizeMatrix<T>::get()
{
    return mat_;
}

template <typename T>
bool RandomFixedSizeMatrix<T>::check(const EigenType& mat)
{
    return mat_.isApprox(mat);
}

template <typename T>
RandomHalfDynamicSizeMatrix<T>::RandomHalfDynamicSizeMatrix(Eigen::Index col)
    : mat_(EigenType::Random(4, col))
{
}

template <typename T>
typename RandomHalfDynamicSizeMatrix<T>::EigenType RandomHalfDynamicSizeMatrix<T>::get()
{
    return mat_;
}

template <typename T>
bool RandomHalfDynamicSizeMatrix<T>::check(const EigenType& mat)
{
    return mat_.isApprox(mat);
}

/***********************************************************************
 *                               Vector                                *
 ***********************************************************************/
template <typename T>
RandomDynamicSizeVector<T>::RandomDynamicSizeVector(Eigen::Index row)
    : vec_(EigenType::Random(row))
{
}

template <typename T>
typename RandomDynamicSizeVector<T>::EigenType RandomDynamicSizeVector<T>::get()
{
    return vec_;
}

template <typename T>
bool RandomDynamicSizeVector<T>::check(const EigenType& vec)
{
    return vec_.isApprox(vec);
}

template <typename T>
RandomDynamicSizeRowVector<T>::RandomDynamicSizeRowVector(Eigen::Index col)
    : vec_(EigenType::Random(col))
{
}

template <typename T>
typename RandomDynamicSizeRowVector<T>::EigenType RandomDynamicSizeRowVector<T>::get()
{
    return vec_;
}

template <typename T>
bool RandomDynamicSizeRowVector<T>::check(const EigenType& vec)
{
    return vec_.isApprox(vec);
}

template <typename T>
RandomFixedSizeVector<T>::RandomFixedSizeVector()
    : vec_(EigenType::Random())
{
}

template <typename T>
typename RandomFixedSizeVector<T>::EigenType RandomFixedSizeVector<T>::get()
{
    return vec_;
}

template <typename T>
bool RandomFixedSizeVector<T>::check(const EigenType& vec)
{
    return vec_.isApprox(vec);
}

template <typename T>
RandomFixedSizeRowVector<T>::RandomFixedSizeRowVector()
    : vec_(EigenType::Random())
{
}

template <typename T>
typename RandomFixedSizeRowVector<T>::EigenType RandomFixedSizeRowVector<T>::get()
{
    return vec_;
}

template <typename T>
bool RandomFixedSizeRowVector<T>::check(const EigenType& vec)
{
    return vec_.isApprox(vec);
}

/***********************************************************************
 *                               Array                                 *
 ***********************************************************************/
template <typename T>
RandomDynamicSizeArray<T>::RandomDynamicSizeArray(Eigen::Index row, Eigen::Index col)
    : mat_(EigenType::Random(row, col))
{
}

template <typename T>
typename RandomDynamicSizeArray<T>::EigenType RandomDynamicSizeArray<T>::get()
{
    return mat_;
}

template <typename T>
bool RandomDynamicSizeArray<T>::check(const EigenType& mat)
{
    return mat_.isApprox(mat);
}

template <typename T>
RandomFixedSizeArray<T>::RandomFixedSizeArray()
    : mat_(EigenType::Random())
{
}

template <typename T>
typename RandomFixedSizeArray<T>::EigenType RandomFixedSizeArray<T>::get()
{
    return mat_;
}

template <typename T>
bool RandomFixedSizeArray<T>::check(const EigenType& mat)
{
    return mat_.isApprox(mat);
}

template <typename T>
RandomHalfDynamicSizeArray<T>::RandomHalfDynamicSizeArray(Eigen::Index col)
    : mat_(EigenType::Random(4, col))
{
}

template <typename T>
typename RandomHalfDynamicSizeArray<T>::EigenType RandomHalfDynamicSizeArray<T>::get()
{
    return mat_;
}

template <typename T>
bool RandomHalfDynamicSizeArray<T>::check(const EigenType& mat)
{
    return mat_.isApprox(mat);
}

/***********************************************************************
 *                           Vector Array                              *
 ***********************************************************************/
template <typename T>
RandomDynamicSizeColumnArray<T>::RandomDynamicSizeColumnArray(Eigen::Index row)
    : vec_(EigenType::Random(row))
{
}

template <typename T>
typename RandomDynamicSizeColumnArray<T>::EigenType RandomDynamicSizeColumnArray<T>::get()
{
    return vec_;
}

template <typename T>
bool RandomDynamicSizeColumnArray<T>::check(const EigenType& vec)
{
    return vec_.isApprox(vec);
}

template <typename T>
RandomDynamicSizeRowArray<T>::RandomDynamicSizeRowArray(Eigen::Index col)
    : vec_(EigenType::Random(col))
{
}

template <typename T>
typename RandomDynamicSizeRowArray<T>::EigenType RandomDynamicSizeRowArray<T>::get()
{
    return vec_;
}

template <typename T>
bool RandomDynamicSizeRowArray<T>::check(const EigenType& vec)
{
    return vec_.isApprox(vec);
}

template <typename T>
RandomFixedSizeColumnArray<T>::RandomFixedSizeColumnArray()
    : vec_(EigenType::Random())
{
}

template <typename T>
typename RandomFixedSizeColumnArray<T>::EigenType RandomFixedSizeColumnArray<T>::get()
{
    return vec_;
}

template <typename T>
bool RandomFixedSizeColumnArray<T>::check(const EigenType& vec)
{
    return vec_.isApprox(vec);
}

template <typename T>
RandomFixedSizeRowArray<T>::RandomFixedSizeRowArray()
    : vec_(EigenType::Random())
{
}

template <typename T>
typename RandomFixedSizeRowArray<T>::EigenType RandomFixedSizeRowArray<T>::get()
{
    return vec_;
}

template <typename T>
bool RandomFixedSizeRowArray<T>::check(EigenType vec)
{
    return vec_.isApprox(vec);
}
