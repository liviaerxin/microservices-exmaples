# gRPC



## Basic Knowledge


## Protocol Buffer

[Language Guide (proto3)](https://developers.google.com/protocol-buffers/docs/proto3)

- **extracts**

1. option fields definition, like `java_outer_classname`.

### Manage Protocol Buffer Files

[How We Build gRPC Services At Namely](https://medium.com/namely-labs/how-we-build-grpc-services-at-namely-52a3ae9e7c35)



## Work with gRPC


1. **Defining the service**


2. **Generating client and server code**

We need to generate the gRPC client and server interfaces from our `.proto` service definition file. To integrate these interfaces with our client or server implementation class, we can do this using following 2 steps,

- using protocol buffer [proto3](https://github.com/protocolbuffers/protobuf/releases) compiler. Then import these java files into projects.  

- using Gradle or Maven(ignore step 1 as gradle/maven plugins automatically incorporate the complier). The protoc build plugin can generate the necessary code as part of the build. You can refer the [README](https://github.com/grpc/grpc-java/blob/master/README.md) for how to generate code from your own `.proto` files. 


3. **Creating the pseudo-server**




4. **Creating the client**





## Load Balancing

When gPRC servers are deployed in cluster such as microservices, `service discovery` and `load balancing` are entailed when client call server.

[gRPC Load Balancing](https://grpc.io/blog/loadbalancing/)*

[TCP vs HTTP(S) Load Balancing](https://medium.com/martinomburajr/distributed-computing-tcp-vs-http-s-load-balancing-7b3e9efc6167)

[gRPC in Microservices](https://levelup.gitconnected.com/grpc-in-microservices-5887caef195)

[Building scalable microservices with gRPC](https://www.bugsnag.com/blog/grpc-and-microservices-architecture)

[Pattern: Server-side service discovery](https://microservices.io/patterns/server-side-discovery.html)

[Service Discovery in a Microservices Architecture](https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/)

### Load Balancing Model

1. Proxy Load Balancer options
   - L3/L4 (Transport)
   - L7 (Application)
     - NGINX gRPC
      [Introducing gRPC Support with NGINX 1.13.10](https://www.nginx.com/blog/nginx-1-13-10-grpc/)
     - Traefic gRPC
      [gRPC examples¶](https://docs.traefik.io/user-guide/grpc/)
     - HAProxy gPRC
      [HAProxy 1.9.2 Adds gRPC Support](https://www.haproxy.com/blog/haproxy-1-9-2-adds-grpc-support/)
     - Envoy gRPC
      [Envoy proxy](https://www.envoyproxy.io/)

2. Client side LB options
   - Thick client
    the data center middleware (service discovery service) can be selected as follows:
     - Consul
        [Consul by HashiCorp](https://learn.hashicorp.com/consul/)

        [gRPC service discovery with Consul](https://developpaper.com/grpc-service-discovery-with-consul/)

        [HowTo: Container Orchestration with Nomad and Consul](https://medium.com/@mykidong/howto-container-orchestration-with-nomad-and-consul-f99430abcc85)

     - etcd

     - Zookeeper
   - Lookaside Load Balancing


### Question

1. Does one client/stub send multiple requests simultaneously on opening multiple connections?

   Right also wrong, one stub can send multiple requests but one stub only bind to one channel/connection. gRPC's underlying transport protocol is `HTTP/2` which support [multiplexing](https://developers.google.com/web/fundamentals/performance/http2/#request_and_response_multiplexing) and is in way to be very important to reduce the network latency and improve the performance in comparison with `HTTP/1.1`.

   [](https://github.com/grpc/grpc-go/issues/85)

   [Client](https://grpclib.readthedocs.io/en/latest/client.html)

2. How the gRPC client could discover which host is running the `service` it wishes to call?

   What I have known so far is that the service has full service name of `{package}.{service}` and the method also has full method name of `{package}.{service}/{method}`, which are unique to exist in a gRPC server. And the `*.proto` file does not tell the `server` host address or domain name but contains `{package}`, `{service}` and `{method}`. By now, the domain name of host which provides services is hard-coded into the client.

   ```java
   public final class GreeterGrpc {

   private GreeterGrpc() {}

   public static final String SERVICE_NAME = "helloworld.Greeter";
   ....
   ```

3. load-balanced in the transport layer (L3/L4) or application layer (L7)?




## Health Check

[GRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)

[Health checking gRPC servers on Kubernetes](https://kubernetes.io/blog/2018/10/01/health-checking-grpc-servers-on-kubernetes/)

## Reflection


[GRPC Server Reflection Protocol](https://github.com/grpc/grpc/blob/master/doc/server-reflection.md)

## HTTP/2

[What does multiplexing mean in HTTP/2](https://stackoverflow.com/questions/36517829/what-does-multiplexing-mean-in-http-2)

[Introduction to HTTP/2](https://developers.google.com/web/fundamentals/performance/http2/) (*read it later today)

[Use HTTP/2.0 between nginx reverse-proxy and backend webserver](https://serverfault.com/questions/765258/use-http-2-0-between-nginx-reverse-proxy-and-backend-webserver)

[7 Tips for Faster HTTP/2 Performance](https://www.nginx.com/blog/7-tips-for-faster-http2-performance/)
