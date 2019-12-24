### Step1: Build Image
FROM maven:3.6-jdk-8 as builder

RUN mkdir -p /build
WORKDIR /build

COPY pom.xml /build/
# a trick to use the docker layer cache, another choose is volume cache. But it only can be
# used during `docker run` not `docker build` phase.
RUN mvn dependency:go-offline
# Build application
COPY src/ /build/src/
RUN mvn clean package


### Step2: Runtime Image
FROM openjdk:8-slim

WORKDIR /app

#Copy executable jar file from the builder image
COPY --from=builder /build/target/*.jar /app/app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]