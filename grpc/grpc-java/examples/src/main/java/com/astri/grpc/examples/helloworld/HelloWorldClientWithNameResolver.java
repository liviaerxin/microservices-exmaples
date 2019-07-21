package com.astri.grpc.examples.helloworld;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import io.grpc.util.RoundRobinLoadBalancerFactory;


import java.util.logging.Level;
import java.util.logging.Logger;

import java.util.List;
import java.util.concurrent.TimeUnit;

public class HelloWorldClientWithNameResolver {
    private static Logger logger = Logger.getLogger(HelloWorldClientWithNameResolver.class.getName());
    private final ManagedChannel channel;
    private final GreeterGrpc.GreeterBlockingStub blockingStub;

    /**
     * Consul NameResolver Usage.
     *
     * @param serviceName  consul service name.
     * @param consulHost   consul agent host.
     * @param consulPort   consul agent port.
     * @param ignoreConsul if true, consul is not used. instead, the static node list will be used.
     * @param hostPorts    the static node list, for instance, Arrays.asList("host1:port1", "host2:port2")
     */
    public HelloWorldClientWithNameResolver(String serviceName, String consulHost, int consulPort, boolean ignoreConsul,
                                            List<String> hostPorts) {

        String consulAddr = "consul://" + consulHost + ":" + consulPort;
        logger.info("consulAddr: " + consulAddr);
        int pauseInSeconds = 5;
        channel = ManagedChannelBuilder
                .forTarget(consulAddr)
                .nameResolverFactory(new ConsulNameResolver.ConsulNameResolverProvider(serviceName, pauseInSeconds, ignoreConsul, hostPorts))
                .defaultLoadBalancingPolicy("round_robin")
                //.loadBalancerFactory(RoundRobinLoadBalancerFactory.getInstance())
                .usePlaintext()
                .build();
        blockingStub = GreeterGrpc.newBlockingStub(channel);
    }

    public void shutdown() throws InterruptedException {
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }

    /**
     * Say hello to server.
     */
    public void greet(String name) {
        logger.info("Will try to greet " + name + " ...");
        HelloRequest request = HelloRequest.newBuilder().setName(name).build();
        HelloReply response;
        try {
            response = blockingStub.sayHello(request);
        } catch (StatusRuntimeException e) {
            logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
            return;
        }
        logger.info("Greeting: " + response.getMessage());
    }

    /**
     * Greet server. If provided, the first element of {@code args} is the name to use in the
     * greeting.
     */
    public static void main(String[] args) throws Exception {
        // service name which is registered in consul service discovery.
        String serviceName = "helloworld.Greeter";
        String consulHost = "localhost";
        int consulPort = 8500;
        boolean ignoreConsul = false;
        // init. client which do load balancing using consul.
        HelloWorldClientWithNameResolver client = new HelloWorldClientWithNameResolver(serviceName, consulHost, consulPort, ignoreConsul, null);

        try {
            /* Access a service running on the local machine on port 50051 */
            String user = "world";
            if (args.length > 0) {
                user = args[0]; /* Use the arg as the name to greet if provided */
            }
            client.greet(user);
            logger.info("over");
        } finally {
            client.shutdown();
        }
        //System.exit(1);
    }
}