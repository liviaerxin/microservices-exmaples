# Ingress
An API object that manages external access to the services in a cluster, typically HTTP.

Ingress can provide load balancing, SSL termination and name-based virtual hosting.

```
    internet
        |
   [ Ingress ]
   --|-----|--
   [ Services ]
```

For example, you might want to send requests to `example.com/api/v1/` to an `api-v1` service, and requests to `example.com/api/v2/` to the `api-v2` service. 

# Ingress Controller
In order for ingress resource to work, the k8s cluster must have a ingress 
controller running.

- Kubernetes default [nginx ingress controller](https://kubernetes.github.io/ingress-nginx/).
- NGINX, Inc. offers support and maintenance for the [NGINX Ingress Controller for Kubernetes](https://www.nginx.com/products/nginx/kubernetes-ingress-controller).
- [Traefik](https://github.com/containous/traefik) is a fully featured ingress controller (Let’s Encrypt, secrets, http2, websocket).

# Bare-metal Considerations

[Ingress Controller On Bare-metal Cluster](https://kubernetes.github.io/ingress-nginx/deploy/baremetal/)

- Host Network  
[Kubernetes Ingress On Premise](https://medium.com/@maniankara/kubernetes-tcp-load-balancer-service-on-premise-non-cloud-f85c9fd8f43c)

- [MetalLB](https://metallb.universe.tf/)



# TLS Certificates
[cert-manager](https://github.com/jetstack/cert-manager)

[Quick-Start using Cert-Manager with NGINX Ingress](https://docs.cert-manager.io/en/latest/tutorials/acme/quick-start/index.html)

[How to Set Up an Nginx Ingress with Cert-Manager on DigitalOcean Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nginx-ingress-with-cert-manager-on-digitalocean-kubernetes)

[How to launch nginx-ingress and cert-manager in Kubernetes](https://medium.com/containerum/how-to-launch-nginx-ingress-and-cert-manager-in-kubernetes-55b182a80c8f)

[The Kubernetes Package Manager Helm](https://github.com/helm/helm)


# Reference
[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

[Understanding ConfigMaps and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#understanding-configmaps-and-pods)



