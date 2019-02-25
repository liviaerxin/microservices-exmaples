# Microservices
## Communication
In a monolithic application, components invoke one another via language-level method or function calls. In contrast, a microservices-based application is a distributed system running on multiple machines. Each service instance is typically a process. Consequently, services must interact using an inter-process communication(IPC) mechanism.
If your service needs to trigger some action in another service, do that outside of the request/reponse cycle.

- `sychronous` protocols such as `HTTP/REST`
- `asychronous` protocols such as `AMQP`

## Database
each service has it own database, decoupled from other serices.

### Saga Pattern
[saga](http://microservices.io/patterns/data/saga.html)
maintain data consistency between services.
Implement each business transaction that spans multiple services as a `saga`. Each `saga` is a sequence of local transactions. Each local transaction will updates the database and publishes the message or event to trigger next local transaction in `saga`. If the local transaction fails because it violates business rules, it will ack the some compensating transactions to undo the changes. This is also completed through publishing the message to its preceding service to execute transactions to undo the changes.


### API Composition
`query join` is performed in higher application level rather than in database. For example, an aggregated service(or the API gateway) could retrieve the customer and his shopping orders by first retrieving the customer data from customer service and then querying the order service to acquire the customer's most recent orders.
### Command Query Responsibility Segregation (CQRS)

## Authentication and Authorization
[Microservices Authentication and Authorization Solutions](https://medium.com/tech-tajawal/microservice-authentication-and-authorization-solutions-e0e5e74b248a)  

# references
[microservices](http://microservices.io/)  
[microservices examples](https://github.com/cer/microservices-examples)  
[](http://callistaenterprise.se/blogg/teknik/2015/05/20/blog-series-building-microservices/)  


# Web Server
[Web Server IO Performance Among NODE PHP JAVA GO](https://www.toptal.com/back-end/server-side-io-performance-node-php-java-go)  
[Java Application Servers](https://stackify.com/tomcat-vs-jetty-vs-glassfish-vs-wildfly/)  

# Authentication and Authorization
1. Authentication and Authorization should be externalized from the business logic.
2. Authentication and Authorization should be centrally managed.

[Authentication and Authorization for RESTful APIs](https://dzone.com/articles/steps-to-building-authentication-and-authorization)  
[API Security: Ways to Authenticate and Authorize](https://dzone.com/articles/api-security-ways-to-authenticate-and-authorize)  

# LDAP
[How To Install and Configure OpenLDAP and phpLDAPadmin on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-openldap-and-phpldapadmin-on-ubuntu-16-04)  

# Store Files Such As Images In Web Application.
- database
- ile-system
- third-party cloud service.

[](https://stackoverflow.com/questions/348363/what-is-the-best-place-for-storing-uploaded-images-sql-database-or-disk-file-sy)  

# Long-running Task/Process/Thread In Java
## Thread Pool:  
Use a thread pool, create a task and submit it to the thread pool.
pros:
- control how many concurrent threads run, and how many tasks can wait in the thread pool's queue of waiting tasks.
cons:

## Publish/Subscribe Message Queue: 

[](https://news.ycombinator.com/item?id=17064730)  



# Docker Insight
In docker swarm networks, 
- `ingress` overlay
  `docker network inspect ingress`
  In general the default address configuration is, 
  ```
        "IPAM": {
          "Driver": "default",
          "Options": null,
          "Config": [
              {
                  "Subnet": "10.255.0.0/16",
                  "Gateway": "10.255.0.1"
              }
          ]
        },  
  ```



- `{DPMS_STACK_NAME}_default` overlay
  The address configuration might be, 
  ```
        "IPAM": {
          "Driver": "default",
          "Options": null,
          "Config": [
              {
                  "Subnet": "10.0.0.0/24",
                  "Gateway": "10.0.0.1"
              }
          ]
        },
  ```

When access from outside networks, the traffic will go through `ingress` network to reach the docker internal nginx service. Because of it, the real remote address recoginzed by nginx would be `10.255.X.X`.
When access from docker swarm internal networks, the traffic will go through `{DPMS_STACK_NAME}_default` network to reach the docker internal nginx service. Because of it, the real remote address recoginzed by nginx would be `10.0.0.X`.

