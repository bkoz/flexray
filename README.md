# flexray
A Whitted-style ray tracer implementation in python named after my dad, Felix. The code is based on Jami Buck's book [The Ray Tracer Challenge](https://pragprog.com/titles/jbtracer/the-ray-tracer-challenge/).

### Behavior Driven Development

Run `behave` feature scenarios that are tagged with `@dev`.

```
$ cd code
$ export PYTHONPATH=${PYTHONPATH}:`pwd`
$ behave --tags=@dev --no-skipped
$ behave --tags=@dev --no-skipped features/matrices.feature
```

#### Notes

Finished up to chapter 6. I'll probably stop here and take a look at Pete Shirley's [ray tracing books](https://raytracing.github.io/). 
