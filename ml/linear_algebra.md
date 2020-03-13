## Linear Algebra
* [Python notebook](https://github.com/ageron/handson-ml2/blob/master/math_linear_algebra.ipynb)
* Studies vector spaces and linear transformations between vector spaces.

### Vectors
* A *vector* is a quantity defined by a magnitude and a direction.
* Purpose in ML: represent observations and predictions.

* **Norm**: The *norm* of a vector u, noted ||u||, is a measure of the length (a.k.a. the magnitude) of u.
* `import numpy.linalg as LA; LA.norm(u)`

* Victor **addition** is *commutative*, also *associative*
* **Scalar multiplication** results in changing the scale of a figure. Commutative, associative, distributive.
* A **zero-vector** is a vector full of 0s.
* A **unit vector** is a vector with a norm equal to 1.
* A **normalized vector** of a non-null vactor u, is the unit vector that points in the same detection as u.

* **Dot product**: u.v. np.dot(). The * will perform an elementwise multiplication, not a dot product.
* Calculating the angle between vectors.
* Projecting a point onto an axis.
* 1D to 2D, u.T, u[:,np.newaxis]

### Matrices
* np.array(), A[1,:], A[:2], A[1:2,:] excluded
* square, triangular, diagonal and identity matrices. np.diag(), np.eye().
* multiplication, `A@D; np.matmul()
* transpose, A.T. Symmetric matrix: M.T=M. M.dot(M.T) is symmetric.
