# flexray
A Whitted-style ray tracer implementation in python named after my dad, Felix. The code is based on Jami's Buck's excellent book [The Ray Tracer Challenge](https://pragprog.com/titles/jbtracer/the-ray-tracer-challenge/).

### Behavior Driven Development

Run `behave` feature scenarios that are tagged with `@dev`.

```
$ cd code
$ export PYTHONPATH=${PYTHONPATH}:`pwd`
$ behave --tags=@dev --no-skipped
$ behave --tags=@dev --no-skipped features/matrices.feature
```

#### Notes

Checking the python search path.

```
$ python
>>> import sys
>>> print(sys.path)
```
