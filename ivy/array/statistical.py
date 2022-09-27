# global
from typing import Optional, Union, Sequence
import abc

# local
import ivy

# ToDo: implement all methods here as public instance methods


class ArrayWithStatistical(abc.ABC):
    def min(
        self: ivy.Array,
        /,
        *,
        axis: Union[int, Sequence[int]] = None,
        keepdims: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.min(self._data, axis=axis, keepdims=keepdims, out=out)

    def max(
        self: ivy.Array,
        /,
        *,
        axis: Union[int, Sequence[int]] = None,
        keepdims: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.max(self._data, axis=axis, keepdims=keepdims, out=out)

    def mean(
        self: ivy.Array,
        /,
        *,
        axis: Union[int, Sequence[int]] = None,
        keepdims: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """ivy.Array instance method variant of ivy.mean. This method simply
        wraps the function, and so the docstring for ivy.mean also applies
        to this method with minimal changes.

        **Special Cases**

        Let ``N`` equal the number of elements over which to compute the
        arithmetic mean.
        -   If ``N`` is ``0``, the arithmetic mean is ``NaN``.
        -   If ``x_i`` is ``NaN``, the arithmetic mean is ``NaN`` (i.e., ``NaN``
            values propagate).

        Parameters
        ----------
        self
            input array. Should have a floating-point data type.
        axis
            axis or axes along which arithmetic means must be computed. By default,
            the mean must be computed over the entire array. If a Sequence of
            integers, arithmetic means must be computed over multiple axes.
            Default: ``None``.
        keepdims
            bool, if ``True``, the reduced axes (dimensions) must be included in the
            result as singleton dimensions, and, accordingly, the result must be
            compatible with the input array (see :ref:`broadcasting`). Otherwise,
            if ``False``, the reduced axes (dimensions) must not be included in
            the result. Default: ``False``.
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            array, if the arithmetic mean was computed over the entire array, a
            zero-dimensional array containing the arithmetic mean; otherwise, a
            non-zero-dimensional array containing the arithmetic means.
            The returned array must have the same data type as ``x``.

        Examples
        --------
        With :class:`ivy.Array` input:

        >>> x = ivy.array([3., 4., 5.])
        >>> y = x.mean()
        >>> print(y)
        ivy.array(4.)

        >>> x = ivy.array([-1, 0, 1])
        >>> y = ivy.mean(x)
        >>> print(y)
        ivy.array(0.)

        >>> x = ivy.array([0.1, 1.1, 2.1])
        >>> y = ivy.array(0.)
        >>> x.mean(out=y)
        >>> print(y)
        ivy.array(1.1)

        >>> x = ivy.array([1., 2., 3., 0., -1.])
        >>> y = ivy.array(0.)
        >>> ivy.mean(x, out=y)
        >>> print(y)
        ivy.array(1.)

        >>> x = ivy.array([[-0.5, 1., 2.], [0.0, 1.1, 2.2]])
        >>> y = ivy.array([0., 0., 0.])
        >>> x.mean(axis=0, out=y)
        >>> print(y)
        ivy.array([-0.25,  1.05,  2.1])

        >>> x = ivy.array([[0., 1., 2.], [3., 4., 5.]])
        >>> y = ivy.array([0., 0.])
        >>> ivy.mean(x, axis=1, out=y)
        >>> print(y)
        ivy.array([1., 4.])

        """
        return ivy.mean(self._data, axis=axis, keepdims=keepdims, out=out)

    def var(
        self: ivy.Array,
        /,
        *,
        axis: Union[int, Sequence[int]] = None,
        correction: Union[int, float] = 0.0,
        keepdims: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.var. This method simply 
        wraps the function, and so the docstring for ivy.var also applies 
        to this method with minimal changes.

        **Special Cases**

        Let N equal the number of elements over which to compute the variance.

        If N - correction is less than or equal to 0, the variance is NaN.

        If x_i is NaN, the variance is NaN (i.e., NaN values propagate).

        Parameters
        ----------
        self
            input array. Should have a floating-point data type.
        axis
            axis or axes along which variances must be computed. By default, the
            variance must be computed over the entire array. If a tuple of integers,
            variances must be computed over multiple axes. Default: None.
        correction
            degrees of freedom adjustment. Setting this parameter to a value other 
            than 0 has the effect of adjusting the divisor during the calculation
            of the variance according to N-c where N corresponds to the total 
            number of elements over which the variance is computed and c corresponds
            to the provided degrees of freedom adjustment. When computing the variance
            of a population, setting this parameter to 0 is the standard choice
            (i.e., the provided array contains data constituting an entire population).
            When computing the unbiased sample variance, setting this parameter to 1 
            is the standard choice (i.e., the provided array contains data sampled
            from a larger population; this is commonly referred to as Bessel's
            correction). Default: 0.
        keepdims
            if True, the reduced axes (dimensions) must be included in the result as
            singleton dimensions, and, accordingly, the result must be compatible
            with the input array (see Broadcasting). Otherwise, if False, the
            reduced axes (dimensions) must not be included in the result.
            Default: False.
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            if the variance was computed over the entire array, a zero-dimensional array
            containing the variance; otherwise, a non-zero-dimensional array containing
            the variances. The returned array must have the same data type as x.

        Examples
        --------
        >>> x = ivy.array([[0.0, 1.0, 2.0], \
                           [3.0, 4.0, 5.0], \
                           [6.0, 7.0, 8.0]])
        >>> y = x.var()
        >>> print(y)
        ivy.array(6.6666665)

        >>> x = ivy.array([[0.0, 1.0, 2.0], \
                           [3.0, 4.0, 5.0], \
                           [6.0, 7.0, .08]])
        >>> y = x.var(axis=0)
        >>> print(y)
        ivy.array([6., 6., 4.1])

        >>> x = ivy.array([[0.0, 1.0, 2.0], \
                           [3.0, 4.0, 5.0], \
                           [6.0, 7.0, .08]])
        >>> y = ivy.array([0., 0., 0.])
        >>> x.var(axis=1, out=y)
        >>> print(y)
        ivy.array([0.667, 0.667, 9.33 ])

        """
        return ivy.var(
            self._data, axis=axis, correction=correction, keepdims=keepdims, out=out
        )

    def prod(
        self: ivy.Array,
        /,
        *,
        axis: Union[int, Sequence[int]] = None,
        keepdims: bool = False,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.prod(self._data, axis=axis, keepdims=keepdims, dtype=dtype, out=out)

    def sum(
        self: ivy.Array,
        /,
        *,
        axis: Union[int, Sequence[int]] = None,
        keepdims: bool = False,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.sum(self, axis=axis, dtype=dtype, keepdims=keepdims, out=out)

    def std(
        self: ivy.Array,
        /,
        *,
        axis: Union[int, Sequence[int]] = None,
        correction: Union[int, float] = 0.0,
        keepdims: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.std(self._data, axis=axis, keepdims=keepdims, out=out)

    # Extra #
    # ----- #

    def cumsum(
        self: ivy.Array,
        /,
        *,
        axis: int = 0,
        exclusive: bool = False,
        reverse: bool = False,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.cumsum. This method simply wraps the
        function, and so the docstring for ivy.cumsum also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            Input array to apply cumsum.
        axis
            Axis along which the cumulative sum is computed. Default is 0.
        exclusive
            Whether to perform cumsum exclusively. Default is ``False``.
        reverse
            Whether to perform the cumsum from last to first element in the selected
            axis. Default is False (from first to last element)
        dtype
            Data type of the returned array. Default is ``None``.
        out
            Optional array container. Default is None.

        Returns
        -------
        ret
            Array which holds the result of applying cumsum at each
            original array elements along the specified axis.

        Examples
        --------
        >>> x = ivy.array([1, 2, 3, 4, 5])
        >>> y = x.cumsum()
        >>> print(y)
        ivy.array([ 1,  3,  6, 10, 15])

        >>> x = ivy.array([2, 6, 4, 10])
        >>> y = x.cumsum(axis=0, exclusive=False, reverse=True, dtype='float64')
        >>> print(y)
        ivy.array([22., 20., 14., 10.])

        >>> x = ivy.array([[2, 3], [4, 6], [8, 12]])
        >>> y = ivy.zeros((3, 2))
        >>> x.cumsum(axis=1, exclusive=True, reverse=False, out=y)
        >>> print(y)
        ivy.array([[0, 2],
                   [0, 4],
                   [0, 8]])

        >>> x = ivy.array([[1, 5, 2], \
                           [4, 3, 0], \
                           [4, 8, 2]])
        >>> y = x.cumsum(axis=1, exclusive=True, reverse=True)
        >>> print(y)
        ivy.array([[ 7,  2,  0],
                   [ 3,  0,  0],
                   [10,  2,  0]])

        >>> x = ivy.array([[1, 5, 10], [4, 8, 10], [2, 3, 5]])
        >>> x.cumsum(axis=0, out=x)
        >>> print(x)
        ivy.array([[ 1,  5, 10],
                   [ 5, 13, 20],
                   [ 7, 16, 25]])
        """
        return ivy.cumsum(self._data, axis, exclusive, reverse, dtype=dtype, out=out)

    def cumprod(
        self: ivy.Array,
        /,
        *,
        axis: int = 0,
        exclusive: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.cumprod. This method simply wraps the
        function, and so the docstring for ivy.cumprod also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            input array
        axis
            int, axis along which to take the cumulative product. Default is 0.
        exclusive
            optional bool, whether to exclude the first value of the input array.
            Default is False.
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            Input array with cumulatively multiplied elements along the specified axis.

        Examples
        --------
        >>> x = ivy.array([1, 2, 3, 4, 5])
        >>> y = x.cumprod()
        >>> print(y)
        ivy.array([1, 2, 6, 24, 120])

        >>> x = ivy.array([[2, 3], [5, 7], [11, 13]])
        >>> y = ivy.zeros((3, 2), dtype="int32")
        >>> x.cumprod(axis=1, exclusive=True, out=y)
        >>> print(y)
        ivy.array([[1, 2],
                   [1, 5],
                   [1, 11]])
        """
        return ivy.cumprod(self._data, axis, exclusive, out=out)

    def einsum(
        self: ivy.Array,
        equation: str,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.einsum(equation, self._data, out=out)
