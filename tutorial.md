mkdir -p 
# microservices Communication
In a monolithic application, components invoke one another via language-level method or function calls. In contrast, a microservices-based application is a distributed system running on multiple machines. Each service instance is typically a process. Consequently, services must interact using an inter-process communication(IPC) mechanism.
If your service needs to trigger some action in another service, do that outside of the request/reponse cycle.

## services communicate
- `sychronous` protocols such as `HTTP/REST`
- `asychronous` protocols such as `AMQP`

## database
each service has it own database, decoupled from other serices.

### Saga Pattern
[saga](http://microservices.io/patterns/data/saga.html)
maintain data consistency between services.
Implement each business transaction that spans multiple services as a `saga`. Each `saga` is a sequence of local transactions. Each local transaction will updates the database and publishes the message or event to trigger next local transaction in `saga`. If the local transaction fails because it violates business rules, it will ack the some compensating transactions to undo the changes. This is also completed through publishing the message to its preceding service to execute transactions to undo the changes.


### API Composition
`query join` is performed in higher application level rather than in database. For example, an aggregated service(or the API gateway) could retrieve the customer and his shopping orders by first retrieving the customer data from customer service and then querying the order service to acquire the customer's most recent orders.
### Command Query Responsibility Segregation (CQRS)

# REST API
## Spring
[](https://blog.tratif.com/2017/11/23/effective-restful-search-api-in-spring)  [](http://www.baeldung.com/queries-in-spring-data-mongodb)  
[](http://www.baeldung.com/queries-in-spring-data-mongodb)  
[](https://docs.spring.io/spring/docs/current/spring-framework-reference/index.html)  
## REST API Design Best Practices
[](https://blog.philipphauer.de/restful-api-design-best-practices/)   
[](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/)  



# references
[spring boot code structure](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-structuring-your-code.html)  
[microservices](http://microservices.io/)  
[microservices examples](https://github.com/cer/microservices-examples)  
[](http://callistaenterprise.se/blogg/teknik/2015/05/20/blog-series-building-microservices/)  
