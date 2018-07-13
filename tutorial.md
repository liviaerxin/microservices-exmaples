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
