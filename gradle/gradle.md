# Gradle

## Multi-Project Builds

[Executing Multi-Project Builds](https://docs.gradle.org/current/userguide/intro_multi_project_builds.html)

**tips**:

1. Seem as a single `projects`

2. project structure

    .
    ├── app
    │   └── build.gradle
    │   └── settings.gradle
    ├── nginx
    │   └── build.gradle
    │   └── settings.gradle
    ├── build.gradle
    └── settings.gradle

    The `build.gradle` in the root project is dedicated to building docker image.

    The `build.gradle` in the sub projects are supposed to be used for their own build logics.

    The task to `build image` in root `build.gradle` always goes after the `default` task of each sub-project.

3. only the `setting.gradle` takes effect when doing mulit-project builds from root project, because we violate the principle in gradle and specify the `setting.gradle` files for each sub-project.

**problems**:

1. for multi-project build in Gradle, it's a best practice to define one `settings.gradle` file in the root project. However, here we want make the `:app` project independently run in its scope, so a `settings.gradle` file is specified in the sub-project. There is no clean way to deal with this if you want to use multi-project build. Alternatively, `composite-build` maybe will conform to the requirement and completely isolate the sub-projects.

## Composite Build

1. the included project will be imported by other projects as `module` dependency type, whereas in multi-project the project is regarded as `project` dependency type.

**extracts**:

1. every project included in the composite build project by `settings.gradle` is independently developed and more isolated in comparison with `Multiple-Project Build`.
2. Included builds interact with each other builds via [dependency substitution](https://docs.gradle.org/current/userguide/composite_builds.html#included_build_declaring_substitutions).



So there are some **limitations**:

1. Configuration can not be shared between the composite build. It can not do some operations such as `cross configuration`, `configuration injecttion` which are avaible in `multi-project` build. So in basic, project properties
can not be shared by B project from A project.

## Gradle Docker Plugin

[Use CLI docker](https://github.com/palantir/gradle-docker)

[Docker Remote API by Docker Java Library](https://bmuschko.github.io/gradle-docker-plugin/#getting_started)
