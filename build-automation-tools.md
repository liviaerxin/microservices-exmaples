# Build Automation Tools

[Gradle vs. Maven](https://dzone.com/articles/gradle-vs-maven)  
[Java Build Tools: Ant vs Maven vs Gradle
](https://technologyconversations.com/2014/06/18/build-tools/)   
[Gradle vs Maven Comparison
](https://gradle.org/maven-vs-gradle/)  


#### Build Phases

- Initialization

    Gradle supports single and multi-project builds. During the initialization phase, Gradle determines which projects are going to take part in the build, and creates a Project instance for each of these projects.

  For instance, Gradle will look on the `settings.gradle` file during this phase.

- Configuration

    During this phase the project objects are configured. The build scripts of all projects which are part of the build are executed.

    For instance, Gradle will search the `build.gradle` file and understand such block,

    ```
    dependencies {

      implementation "ch.qos.logback:logback-classic:1.1.3"  
      testImplementation group: "org.springframework.boot", name: "spring-boot-starter-test", version:springBootVersion

    }
    ```

    It will use the built-in support for `dependency management` to configurate the dependencies which should be used for compiling source code whereas others only need to be available at runtime.

- Execution

    Gradle determines the subset of the tasks, created and configured during the configuration phase, to be executed. The subset is determined by the task name arguments passed to the gradle command and the current directory. Gradle then executes each of the selected tasks.

    For instance, when run the command to see what tasks are executed, 

    ```sh

      gradle generateProto
      
      Path  Started after Duration  Class
      :extractIncludeProto
      0.824s  0.335s  com.google.protobuf.gradle.ProtobufExtract  
      :extractProto
      1.159s  0.005s  com.google.protobuf.gradle.ProtobufExtract  
      :generateProto
      1.165s  0.050s  com.google.protobuf.gradle.GenerateProtoTask

    ```


    ```sh

    gradle bootJar

    Path  Started after Duration  Class
    :extractIncludeProto
      0.867s  0.309s  com.google.protobuf.gradle.ProtobufExtract  
      :extractProto
      1.177s  0.001s  com.google.protobuf.gradle.ProtobufExtract  
      :generateProto
      1.178s  0.050s  com.google.protobuf.gradle.GenerateProtoTask  
      :compileJava
      1.229s  0.511s  org.gradle.api.tasks.compile.JavaCompile  
      :processResources
      1.740s  0.004s  org.gradle.language.jvm.tasks.ProcessResources  
      :classes
      1.744s  0.001s  org.gradle.api.DefaultTask  
      :bootJar
      1.745s  0.348s  org.springframework.boot.gradle.tasks.bundling.BootJar

    ```


#### Tasks in build   
To get the list of all tasks that Gradle can run with the current configuration, please execute the following. 

```sh
gradle tasks --all
```
For instance,
```sh
[build.gradle]
apply plugin: 'java'
```
This simple line of code adds 20+ tasks waiting for us to use.



### Use **DSL(domain-specific language)** based on the programming language **Groovy** to write configuration scripts.

## Maven

[Apache Maven Tutorial](https://www.baeldung.com/maven)

- Build Lifecycles  
  comprise defined and sequence `phases`, which has `goals` in equalibrium of `tasks` in `gradle`. Considering customization, user can inject the other plugins which contain the specified `goals`.

- Use **XML** to write configuration scripts.

## How to Choose  
- Customized builds.  
  With Maven, you can easily define your project’s metadata and dependencies, but creating a highly customized build might be a nightmare for Maven users. The POM file can easily get bloated as your project grows and might as well be an unreadable XML file later on. The DSL based on Groovy led to **smaller** configuration files with less clutter.

- Dependency management and directory structure.  
  Both build systems provide built-in capability to resolve dependencies from configurable repositories. Both are able to cache dependencies locally and download them in parallel. 

  Maven allows one to override a dependency, but only by version. Gradle provides customizable dependency selection and substitution rules that can be declared once and handle unwanted dependencies project-wide. This substitution mechanism enables Gradle to build multiple source projects together to create composite builds.

- Plugins and integrations.  
  Maven also supports a wide variety of build life-cycle steps and integrates seamlessly with third-party tools such as CI servers, code coverage plugins, and artifact repository systems, among others. As far as plugins go, there is a growing number of available plugins now, and there are large vendors that have Gradle-compatible plugins. However, there are still more available plugins for Maven compared to the number available for Gradle.

- Flexibility.  
  Gradle's model also allows it to be used for native development with C/C++ and can be expanded to cover any ecosystem.

  Both Gradle and Maven provide convention over configuration. However, Maven provides a very rigid model that makes customization tedious and sometimes impossible. While this can make it easier to understand any given Maven build, as long as you don’t have any special requirements, it also makes it unsuitable for many automation problems. Gradle, on the other hand, is built with an empowered and responsible user in mind.

- Performance  
  These and more performance features make Gradle at least twice as fast for nearly every scenario (100x faster for large builds using the build cache) in this Gradle vs Maven performance comparison.




# Migrate Project to Gradle