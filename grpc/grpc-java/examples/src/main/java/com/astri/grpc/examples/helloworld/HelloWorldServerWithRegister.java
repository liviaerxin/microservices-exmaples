package com.astri.grpc.examples.helloworld;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.services.HealthStatusManager;
import io.grpc.stub.StreamObserver;
import io.grpc.health.v1.HealthCheckResponse.ServingStatus;

import java.io.IOException;
import java.util.logging.Logger;

public class HelloWorldServerWithRegister {

    private static final Logger logger = Logger.getLogger(HelloWorldServer.class.getName());

    private Server server;

    private int port = 50051;

    // Health Service
    private final HealthStatusManager manager = new HealthStatusManager();

    private void start() throws IOException {
        /* Prepare services */

        manager.setStatus(GreeterGrpc.SERVICE_NAME, ServingStatus.SERVING);

        /* The port on which the server should run */
        server = ServerBuilder
                .forPort(port)
                .addService(new HelloWorldServerWithRegister.GreeterImpl())
                .addService(manager.getHealthService()) //health service
                .build()
                .start();
        logger.info("Server started, listening on " + port);
        Runtime.getRuntime().addShutdownHook(new Thread() {
            @Override
            public void run() {
                // Use stderr here since the logger may have been reset by its JVM shutdown hook.
                System.err.println("*** shutting down gRPC server since JVM is shutting down");
                HelloWorldServerWithRegister.this.stop();
                System.err.println("*** server shut down");
            }
        });
    }

    private void stop() {
        if (server != null) {
            server.shutdown();
        }
    }

    static class GreeterImpl extends GreeterGrpc.GreeterImplBase {

        @Override
        public void sayHello(HelloRequest req, StreamObserver<HelloReply> responseObserver) {
            HelloReply reply = HelloReply.newBuilder().setMessage("Hello " + req.getName()).build();
            responseObserver.onNext(reply);
            responseObserver.onCompleted();
        }
    }
    /**
     * Await termination on the main thread since the grpc library uses daemon threads.
     */
    private void blockUntilShutdown() throws InterruptedException {
        if (server != null) {
            server.awaitTermination();
        }
    }

    /**
     * Register service into consul
     * @param serviceName
     */
    private void registerToConsul(String serviceName){

        String consulHost = "127.0.0.1";
        int consulPort = 8500;
        ServiceDiscovery serviceDiscovery = ConsulServiceDiscovery.singleton(consulHost, consulPort);
        serviceDiscovery.createService(serviceName, serviceName+"_1", null, "192.168.1.100",
                50051, null,
                "192.168.1.100:50051", "10s", "1s");

    }


    /**
     * Main launches the server from the command line.
     */
    public static void main(String[] args) throws IOException, InterruptedException {
        final HelloWorldServerWithRegister server = new HelloWorldServerWithRegister();
        // register to consul
        String serviceName = GreeterGrpc.SERVICE_NAME;
        server.registerToConsul(serviceName);

        // start server
        server.start();
        server.blockUntilShutdown();
    }

}
