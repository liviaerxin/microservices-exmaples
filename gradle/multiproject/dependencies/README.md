# Dependencies

[sample sources codes](https://github.com/gradle/gradle/tree/master/subprojects/docs/src/samples/userguide/multiproject/dependencies)


## Dependencies and Execution Order

The code for this example can be found at `./messages`.

```sh
$ gradle -q action
Consuming message: null
Producing message:
```

If nothing else is defined, Gradle will execute the tasks in alphanumeric order. Therefore, Gradle will execute `:consumer:action` before `:producer:action`. That's not what we want. To resovle this problem, let's use a hack by renaming the `producer` project to `aProducer`.

## Real Life Examples

1. One good example consists of two web application projects and a parent project that creates a distribution including the two web applications. For the example we use only one build script and do `cross project configuration`.

## Project Lib Dependencies

What if one project needs a jar produced by another project in its compile path, and not just a jar but also the transitive dependencies of this jar? Obviously, this is a very common use case for Java multi-project builds.

