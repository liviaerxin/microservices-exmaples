package com.example.microservices.restfulapi.person;

/*
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class PersonRepository {

    @Autowired
    MongoTemplate mongoTemplate;

    public long countAllPersons() {
        return mongoTemplate.count(null, Person.class);
    }
}*/

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

public interface PersonRepository extends MongoRepository<Person, String> {

	public Person findByFirstName(String firstName);
    public List<Person> findByLastName(String lastName);

}