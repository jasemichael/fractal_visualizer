# CS 1440 Assignment 4.1 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 20 pts | Concrete fractal classes inherit from the abstract `Fractal` class<br/>The `Fractal` class cannot be instantiated. `Julia` and `Mandelbrot` fractals inherit from `Fractal`.
| 10 pts | Add a third concrete fractal class embodying an algorithm of your choice.<br/>The `Config` module/class handles any custom parameters needed by this fractal.
| 10 pts | `FractalFactory` returns a concrete fractal object when given a configuration object or raises `NotImplementedError`
| 10 pts | Concrete gradient classes which inherit from abstract class `Gradient`<br/>The `Gradient` class cannot be instantiated, but defines methods which may be overridden by subclasses. Two or more concrete polymorphic gradient classes are provided which inherit from `Gradient`
| 10 pts | Two or more concrete polymorphic gradient classes<br/>At least two new gradient classes which inherit from Gradient are written. These classes are polymorphic in that they each provide the same methods and may be used interchangeably
| 10 pts | `GradientFactory` creates concrete gradient objects.<br/>When no command-line argument is supplied, create a default gradient object.<br/>Otherwise, produce the gradient object requested on the command line or raise `NotImplementedError`.
| 10 pts | UML Class diagram describes involved classes' relationships, data members and methods accurately
| 5 pts  | Class diagram adheres to UML standards as far as these were explained in class<br/>Abstract classes in UML write the class name in *italics*
| 5 pts  | Users' Manual accurately describes the program's user interface

**Total points: 90**


## Penalties

Review the [Course Rules](https://gitlab.cs.usu.edu/erik.falor/sp20-cs1440-lecturenotes/blob/master/Course_Rules.md)
document to avoid general penalties which apply to all assignments.

In particular, don't forget to include your *Software Development Plan* and
*Sprint Signature* documents in the `doc/` directory.

Pay attention to the name you give your repository on GitLab.
