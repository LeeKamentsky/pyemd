#include "numpy/arrayobject.h"
#include <algorithm>
#include <vector>

template<typename T> T *npy_getptr1(PyArrayObject *obj, npy_intp i) {
    return (T *)PyArray_GETPTR1(obj, i);
}

template<typename T> T *npy_getptr2(PyArrayObject *obj, npy_intp i, npy_intp j) {
    return (T *)PyArray_GETPTR2(obj, i, j);
}

template<typename T> void np1D_to_vector(PyArrayObject *obj, std::vector<T> &v) {
    v.assign(npy_getptr1<T>(obj, 0),
             npy_getptr1<T>(obj, PyArray_DIM(obj, 0)));
}

template<typename T> void np2D_to_vector(
    PyArrayObject *obj, std::vector<std::vector<T>> &v) 
{
    const npy_intp n_i = PyArray_DIM(obj, 0);
    const npy_intp n_j = PyArray_DIM(obj, 1);
    v.resize(n_i);
    for (int i=0; i<n_i; i++) {
        const T *ptr = npy_getptr2<T>(obj, i, 0);
        v[i].assign(ptr, ptr+n_j);
    }
}

template<typename T> void vector_to_np2D(
    PyArrayObject *obj, std::vector<std::vector<T>> &v) 
{
    for (std::vector<std::vector<T>>::iterator i=v.begin(); i<v.end(); i++) {
        T *ptr = npy_getptr2<T>(obj, i-v.begin(), 0);
        copy(i->begin(), i->end(), ptr);
    }
}    