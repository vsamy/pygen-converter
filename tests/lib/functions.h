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

#pragma once

#include <Eigen/Core>

/***********************************************************************
 *                               Matrix                                *
 ***********************************************************************/
template <typename T>
class RandomDynamicSizeMatrix {
public:
    using EigenType = Eigen::Matrix<T, Eigen::Dynamic, Eigen::Dynamic>;

public:
    RandomDynamicSizeMatrix(Eigen::Index row, Eigen::Index col);

    EigenType get();
    bool check(const EigenType& mat);

private:
    EigenType mat_;
};

template <typename T>
class RandomFixedSizeMatrix {
public:
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
public:
    using EigenType = Eigen::Matrix<T, 4, 4>;

public:
    RandomFixedSizeMatrix();

    EigenType get();
    bool check(const EigenType& mat);

private:
    EigenType mat_;
};

template <typename T>
class RandomHalfDynamicSizeMatrix {
public:
    using EigenType = Eigen::Matrix<T, 4, Eigen::Dynamic>;

public:
    RandomHalfDynamicSizeMatrix(Eigen::Index col);

    EigenType get();
    bool check(const EigenType& mat);

private:
    EigenType mat_;
};

/***********************************************************************
 *                               Vector                                *
 ***********************************************************************/
template <typename T>
class RandomDynamicSizeVector {
public:
    using EigenType = Eigen::Matrix<T, Eigen::Dynamic, 1>;

public:
    RandomDynamicSizeVector(Eigen::Index row);

    EigenType get();
    bool check(const EigenType& vec);

private:
    EigenType vec_;
};

template <typename T>
class RandomDynamicSizeRowVector {
public:
    using EigenType = Eigen::Matrix<T, 1, Eigen::Dynamic>;

public:
    RandomDynamicSizeRowVector(Eigen::Index col);

    EigenType get();
    bool check(const EigenType& vec);

private:
    EigenType vec_;
};

template <typename T>
class RandomFixedSizeVector {
public:
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
public:
    using EigenType = Eigen::Matrix<T, 4, 1>;

public:
    RandomFixedSizeVector();

    EigenType get();
    bool check(const EigenType& vec);

private:
    EigenType vec_;
};

template <typename T>
class RandomFixedSizeRowVector {
public:
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
public:
    using EigenType = Eigen::Matrix<T, 1, 4>;

public:
    RandomFixedSizeRowVector();

    EigenType get();
    bool check(const EigenType& vec);

private:
    EigenType vec_;
};


/***********************************************************************
 *                               Array                                 *
 ***********************************************************************/
template <typename T>
class RandomDynamicSizeArray {
public:
    using EigenType = Eigen::Array<T, Eigen::Dynamic, Eigen::Dynamic>;

public:
    RandomDynamicSizeArray(Eigen::Index row, Eigen::Index col);

    EigenType get();
    bool check(const EigenType& mat);

private:
    EigenType mat_;
};

template <typename T>
class RandomFixedSizeArray {
public:
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
public:
    using EigenType = Eigen::Array<T, 4, 4>;

public:
    RandomFixedSizeArray();

    EigenType get();
    bool check(const EigenType& mat);

private:
    EigenType mat_;
};

template <typename T>
class RandomHalfDynamicSizeArray {
public:
    using EigenType = Eigen::Array<T, 4, Eigen::Dynamic>;

public:
    RandomHalfDynamicSizeArray(Eigen::Index col);

    EigenType get();
    bool check(const EigenType& mat);

private:
    EigenType mat_;
};

/***********************************************************************
 *                           Vector Array                              *
 ***********************************************************************/
template <typename T>
class RandomDynamicSizeColumnArray {
public:
    using EigenType = Eigen::Array<T, Eigen::Dynamic, 1>;

public:
    RandomDynamicSizeColumnArray(Eigen::Index row);

    EigenType get();
    bool check(const EigenType& vec);

private:
    EigenType vec_;
};

template <typename T>
class RandomDynamicSizeRowArray {
public:
    using EigenType = Eigen::Array<T, 1, Eigen::Dynamic>;

public:
    RandomDynamicSizeRowArray(Eigen::Index col);

    EigenType get();
    bool check(const EigenType& vec);

private:
    EigenType vec_;
};

template <typename T>
class RandomFixedSizeColumnArray {
public:
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
public:
    using EigenType = Eigen::Array<T, 4, 1>;

public:
    RandomFixedSizeColumnArray();

    EigenType get();
    bool check(const EigenType& vec);

private:
    EigenType vec_;
};

template <typename T>
class RandomFixedSizeRowArray {
public:
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
public:
    using EigenType = Eigen::Array<T, 1, 4>;

public:
    RandomFixedSizeRowArray();

    EigenType get();
    bool check(EigenType vec);

private:
    EigenType vec_;
};

#include "functions.inl"