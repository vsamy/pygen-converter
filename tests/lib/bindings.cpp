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

#include "functions.h"
#include "converters.h"
#include <boost/python.hpp>
#include <boost/python/numpy.hpp>
#include <complex>
#include <string>

namespace py = boost::python;
namespace np = boost::python::numpy;
using namespace pygen;

template <typename T>
struct TypeName {
    static constexpr const char* name = typeid(T).name();
};

template <>
struct TypeName<int> {
    static constexpr const char* name = "Int";
};

template <>
struct TypeName<float> {
    static constexpr const char* name = "Float";
};

template <>
struct TypeName<double> {
    static constexpr const char* name = "Double";
};

template <>
struct TypeName<std::complex<float> > {
    static constexpr const char* name = "CFloat";
};

template <>
struct TypeName<std::complex<double> > {
    static constexpr const char* name = "CDouble";
};

template <typename T>
void bindEigen()
{
    // Create convertors for type T
    convert<T>(Converters::All, true);

    // Matrix
    auto name = std::string("RandomDynamicSizeMatrix") + TypeName<T>::name;
    py::class_<RandomDynamicSizeMatrix<T> >(name.c_str(), py::init<Eigen::Index, Eigen::Index>())
        .def("get", &RandomDynamicSizeMatrix<T>::get)
        .def("check", &RandomDynamicSizeMatrix<T>::check);
    name = std::string("RandomFixedSizeMatrix") + TypeName<T>::name;
    py::class_<RandomFixedSizeMatrix<T> >(name.c_str(), py::init<>())
        .def("get", &RandomFixedSizeMatrix<T>::get)
        .def("check", &RandomFixedSizeMatrix<T>::check);
    name = std::string("RandomHalfDynamicSizeMatrix") + TypeName<T>::name;
    py::class_<RandomHalfDynamicSizeMatrix<T> >(name.c_str(), py::init<Eigen::Index>())
        .def("get", &RandomHalfDynamicSizeMatrix<T>::get)
        .def("check", &RandomHalfDynamicSizeMatrix<T>::check);

    // Vector
    name = std::string("RandomDynamicSizeVector") + TypeName<T>::name;
    py::class_<RandomDynamicSizeVector<T> >(name.c_str(), py::init<Eigen::Index>())
        .def("get", &RandomDynamicSizeVector<T>::get)
        .def("check", &RandomDynamicSizeVector<T>::check);
    name = std::string("RandomDynamicSizeRowVector") + TypeName<T>::name;
    py::class_<RandomDynamicSizeRowVector<T> >(name.c_str(), py::init<Eigen::Index>())
        .def("get", &RandomDynamicSizeRowVector<T>::get)
        .def("check", &RandomDynamicSizeRowVector<T>::check);
    name = std::string("RandomFixedSizeVector") + TypeName<T>::name;
    py::class_<RandomFixedSizeVector<T> >(name.c_str(), py::init<>())
        .def("get", &RandomFixedSizeVector<T>::get)
        .def("check", &RandomFixedSizeVector<T>::check);
    name = std::string("RandomFixedSizeRowVector") + TypeName<T>::name;
    py::class_<RandomFixedSizeRowVector<T> >(name.c_str(), py::init<>())
        .def("get", &RandomFixedSizeRowVector<T>::get)
        .def("check", &RandomFixedSizeRowVector<T>::check);

    // Array
    name = std::string("RandomDynamicSizeArray") + TypeName<T>::name;
    py::class_<RandomDynamicSizeArray<T> >(name.c_str(), py::init<Eigen::Index, Eigen::Index>())
        .def("get", &RandomDynamicSizeArray<T>::get)
        .def("check", &RandomDynamicSizeArray<T>::check);
    name = std::string("RandomFixedSizeArray") + TypeName<T>::name;
    py::class_<RandomFixedSizeArray<T> >(name.c_str(), py::init<>())
        .def("get", &RandomFixedSizeArray<T>::get)
        .def("check", &RandomFixedSizeArray<T>::check);
    name = std::string("RandomHalfDynamicSizeArray") + TypeName<T>::name;
    py::class_<RandomHalfDynamicSizeArray<T> >(name.c_str(), py::init<Eigen::Index>())
        .def("get", &RandomHalfDynamicSizeArray<T>::get)
        .def("check", &RandomHalfDynamicSizeArray<T>::check);

    // Array Vector
    name = std::string("RandomDynamicSizeColumnArray") + TypeName<T>::name;
    py::class_<RandomDynamicSizeColumnArray<T> >(name.c_str(), py::init<Eigen::Index>())
        .def("get", &RandomDynamicSizeColumnArray<T>::get)
        .def("check", &RandomDynamicSizeColumnArray<T>::check);
    name = std::string("RandomDynamicSizeRowArray") + TypeName<T>::name;
    py::class_<RandomDynamicSizeRowArray<T> >(name.c_str(), py::init<Eigen::Index>())
        .def("get", &RandomDynamicSizeRowArray<T>::get)
        .def("check", &RandomDynamicSizeRowArray<T>::check);
    name = std::string("RandomFixedSizeColumnArray") + TypeName<T>::name;
    py::class_<RandomFixedSizeColumnArray<T> >(name.c_str(), py::init<>())
        .def("get", &RandomFixedSizeColumnArray<T>::get)
        .def("check", &RandomFixedSizeColumnArray<T>::check);
    name = std::string("RandomFixedSizeRowArray") + TypeName<T>::name;
    py::class_<RandomFixedSizeRowArray<T> >(name.c_str(), py::init<>())
        .def("get", &RandomFixedSizeRowArray<T>::get)
        .def("check", &RandomFixedSizeRowArray<T>::check);
}

BOOST_PYTHON_MODULE(pygenTestLib)
{
    Py_Initialize();
    np::initialize();

    // Eigen default global matrix types are: int, float, double, std::complex<float> and std::complex<double>
    bindEigen<int>();
    bindEigen<float>();
    bindEigen<double>();
    bindEigen<std::complex<float> >();
    bindEigen<std::complex<double> >();
}