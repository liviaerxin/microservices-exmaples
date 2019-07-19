# REST API

## REST API Design Best Practices  
[Understanding REST HTTP Methods](https://spring.io/understanding/REST)  
[](https://blog.philipphauer.de/restful-api-design-best-practices/)   
[](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/)  


## Resource Naming
[REST Resource Naming Guide](https://restfulapi.net/resource-naming/)  


## HTTP Method  
[Put vs Post? Which is used when CreateOrUpdate, Create and Update ](https://stackoverflow.com/questions/630453/put-vs-post-in-rest)  




## Security  
Mainstream ORM packages use parameterized SQL, which will protect you from a direct SQL injection attack.





# Spring
[](https://blog.tratif.com/2017/11/23/effective-restful-search-api-in-spring) 



## Spring Boot
[Java Configure Tomcat Connector Properties In Spring Boot 2.0](https://stackoverflow.com/questions/47700115/tomcatembeddedservletcontainerfactory-is-missing-in-spring-boot-2)  
[Enable Mulitple Connectors In Tomcat](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#howto-enable-multiple-connectors-in-tomcat)  
[Custom Arguments Parser In Controllers](https://sdqali.in/blog/2016/01/29/using-custom-arguments-in-spring-mvc-controllers/)  
[spring boot code structure](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-structuring-your-code.html)  
[Spring Nonwebapplication]()  



## Spring Data MongoDB  

[Spring Data MongoDB : Update document](https://www.mkyong.com/mongodb/spring-data-mongodb-update-document/)  
In Spring data – MongoDB, you can use following methods to update documents.

1. save – Update the whole object, if “_id” is present, perform an update, else insert it.
2. updateFirst – Updates the first document that matches the query.
3. updateMulti – Updates all documents that match the query.
4. Upserting – If no document that matches the query, a new document is created by combining the query and update object.
5. findAndModify – Same with updateMulti, but it has an extra option to return either the old or newly updated document.

[Spring Data MongoDB – Indexes, Annotations and Converters](https://www.baeldung.com/spring-data-mongodb-index-annotations-converter)  



[](http://www.baeldung.com/queries-in-spring-data-mongodb)  
[](http://www.baeldung.com/queries-in-spring-data-mongodb)  
[](https://docs.spring.io/spring/docs/current/spring-framework-reference/index.html)  


## Spring Data JPA

`Spring Data JPA` -> `Hibernate` vs `JDBC template` -> `MySQL driver`
[What Is the Difference Between Hibernate and Spring Data JPA?](https://dzone.com/articles/what-is-the-difference-between-hibernate-and-sprin-1)

[Differences between spring jdbctemplate and Hibernate](https://stackoverflow.com/questions/17301122/differences-between-spring-jdbctemplate-and-hibernate/17301317)  

[Introduction to Spring Data JPA](https://www.baeldung.com/the-persistence-layer-with-spring-data-jpa)  

**Database Initialization**

[how the initialization machenism in Spring Data JPA](https://docs.spring.io/spring-boot/docs/current/reference/html/howto-database-initialization.html#howto-database-initialization)  




### JPA(Java Persist API)
- CRUD Operations
  - Deleting
  1. Cascade Remove is independent in JPA and database, JPA will remove all the associated entities before delete the aimed entity.

  [Deleting JPA Entity Objects](https://www.objectdb.com/java/jpa/persistence/delete)  
  [JPA Cascade Types](https://howtodoinjava.com/hibernate/hibernate-jpa-cascade-types/)  
  [Hibernate CascadeType.REMOVE Example](https://examples.javacodegeeks.com/enterprise-java/hibernate/hibernate-cascadetype-remove-example/)  

### Examples

[Spring Boot + Spring data JPA](https://www.mkyong.com/spring-boot/spring-boot-spring-data-jpa/)  
[Spring Boot + Spring data JPA + MySQL](https://www.mkyong.com/spring-boot/spring-boot-spring-data-jpa-mysql-example/)  


## Spring RestTemplate
[Rest Client Response Exception](https://stackoverflow.com/questions/15404605/spring-resttemplate-invoking-webservice-with-errors-and-analyze-status-code)  

## Spring Event
[Spring Event Listener](https://mydevgeek.com/spring-4-3-event-listener/)  