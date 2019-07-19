# gRPC

## Basic Knowledge


## Protocol-Buffer

[Language Guide (proto3)](https://developers.google.com/protocol-buffers/docs/proto3)

- **extracts**

1. option fields definition, like `java_outer_classname`.



## Work with gRPC


1. **Defining the service**


2. **Generating client and server code**

We need to generate the gRPC client and server interfaces from our `.proto` service definition file. To integrate these interfaces with our client or server implementation class, we can do this using following 2 steps,

- using protocol buffer [proto3](https://github.com/protocolbuffers/protobuf/releases) compiler. Then import these java files into projects.  

- using Gradle or Maven(ignore step 1 as gradle/maven plugins automatically incorporate the complier). The protoc build plugin can generate the necessary code as part of the build. You can refer the [README](https://github.com/grpc/grpc-java/blob/master/README.md) for how to generate code from your own `.proto` files. 


3. **Creating the pseudo-server**




2. **Creating the client**



## Load Balancing and Service Discovery

When gPRC servers are deployed in cluster such as microservices, `service discovery` and `load balancing` are entailed when client call server.

[TCP vs HTTP(S) Load Balancing](https://medium.com/martinomburajr/distributed-computing-tcp-vs-http-s-load-balancing-7b3e9efc6167)

[gRPC in Microservices](https://levelup.gitconnected.com/grpc-in-microservices-5887caef195)

[gRPC Load Balancing](https://grpc.io/blog/loadbalancing/)

[gRPC service discovery with Consul](https://developpaper.com/grpc-service-discovery-with-consul/)








**Question**:

1. Does one client/stub send multiple requests simultaneously on opening multiple connections?

Right also wrong, one stub can send multiple requests but one stub only bind to one channel/connection. gRPC's underlying transport protocol is `HTTP/2` which support [multiplexing](https://developers.google.com/web/fundamentals/performance/http2/#request_and_response_multiplexing) and is in way to be very important to reduce the network latency and improve the performance in comparison with `HTTP/1.1`.

[](https://github.com/grpc/grpc-go/issues/85)

[Client](https://grpclib.readthedocs.io/en/latest/client.html)


1. What I have known so far is that the sevice has full service name of `{package}/{service}` and the method also has full method name of `{package}/{service}/{method}`, which are unique to exist in a gRPC server. And the `*.proto` file does not tell the `server` host address or domain name but contains `{package}`, `{service}` and `{method}`. Therefore, how the gRPC client could discover which host is running the `service` it wishes to call? By now, the host domain name is hard-coded into the client.


load-balanced in the transport layer (L3/L4) or application layer (L7)?


## HTTP/2

[What does multiplexing mean in HTTP/2](https://stackoverflow.com/questions/36517829/what-does-multiplexing-mean-in-http-2)

[Introduction to HTTP/2](https://developers.google.com/web/fundamentals/performance/http2/) (*read it later today)

[Use HTTP/2.0 between nginx reverse-proxy and backend webserver](https://serverfault.com/questions/765258/use-http-2-0-between-nginx-reverse-proxy-and-backend-webserver)

[7 Tips for Faster HTTP/2 Performance](https://www.nginx.com/blog/7-tips-for-faster-http2-performance/)
