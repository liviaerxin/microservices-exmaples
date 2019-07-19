# Docker


## Docker-compose

rebuild images from any changed and restart containers:
docker-compose up -d --build

rebuild and restart a single service that changed:
docker-compose up -d --build worker

## Docker for Multi-platform

**What's it?**
When you build a docker container image, it's typically only built for on operating system(`linux`) and one architecture(`arm64`). As the growing demand for application running on `arm` device, it's much significant to build docker container images for different architectures such as X86, arm, arm64 by using [Docker Desktop](https://www.docker.com/products/docker-desktop) or [docker buildx](https://github.com/docker/buildx).

**Useful Links**
[Docker Official Images are now Multi-platform](https://blog.docker.com/2017/09/docker-official-images-now-multi-platform/)

[Docker Desktop](https://www.docker.com/products/docker-desktop)

[Cross building ARM images on Docker Desktop](https://medium.com/@carlosedp/cross-building-arm64-images-on-docker-desktop-254d1e0bc1f9)

[How I built ARM based Docker Images for Raspberry Pi using buildx CLI Plugin on Docker Desktop?](http://collabnix.com/building-arm-based-docker-images-on-docker-desktop-made-possible-using-buildx/)

[Building Multi-Arch Images for Arm and x86 with Docker Desktop](https://engineering.docker.com/2019/04/multi-arch-images/)

[Using docker-buildx for Multi-architecture Containers](https://www.mjpitz.com/blog/2019/05/07/docker-buildx/)

[Getting started with Docker for Arm using buildx on Linux](https://community.arm.com/developer/tools-software/tools/b/tools-software-ides-blog/posts/getting-started-with-docker-for-arm-on-linux)


**Examples**

```sh
# 1. Install buildx
# platform information
frankchen@:~$ docker system info
Operating System: Ubuntu 18.04.2 LTS
OSType: linux
Architecture: x86_64
...

# current docker builder
frankchen@:1$ docker buildx ls
NAME/NODE DRIVER/ENDPOINT STATUS  PLATFORMS
default * docker                  
  default default         running linux/amd64

# register Arm executables on linux x64
frankchen@:1$ docker run --rm --privileged docker/binfmt:820fdd95a9972a5308930a2bdfb8573dd4447ad3


# 2. Creating the new builder
frankchen@:1$ docker buildx create --name mybuilder
# switch to the new builder 
frankchen@:1$ docker buildx use mybuilder
# newbuilder information
frankchen@:1$ docker buildx inspect --bootstrap
[+] Building 9.0s (1/1) FINISHED                                                                                                       
 => [internal] booting buildkit                                                                                                   9.0s
 => => pulling image moby/buildkit:master                                                                                         7.8s
 => => creating container buildx_buildkit_mybuilder0                                                                              1.2s
Name:   mybuilder
Driver: docker-container

Nodes:
Name:      mybuilder0
Endpoint:  unix:///var/run/docker.sock
Status:    running
Platforms: linux/amd64, linux/arm64, linux/arm/v7, linux/arm/v6

# 3. Building
frankchen@:1$ docker buildx build --platform linux/arm64,linux/amd64 --push -t 1yue8haogaoqi/hello_go:v1 .

# 4. Running
docker run --rm -p 8080:8080 1yue8haogaoqi/hello_go:v1

```

