package com.example.microservices.restfulapi.person;

import java.net.URI;
import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;


@RestController
public class PersonController {

	@Autowired
	private PersonRepository personRepository;
	
	//curl http://localhost:8080/person
	@RequestMapping(method=RequestMethod.GET, path = "/person")
    public Collection<Person> getAll() {
        return personRepository.findAll();
    }
	
	//curl -i -X POST -H "Content-Type:application/json" -d "{  \"firstName\" : \"Frodo\",  \"lastName\" : \"Baggins\" }" http://localhost:8080/person
	@RequestMapping(method=RequestMethod.POST, path = "/person")
	ResponseEntity<?> add(@RequestBody Person input) {
		Person result = personRepository.save(new Person(input.getFirstName(), input.getLastName()));
		URI location = ServletUriComponentsBuilder.
				fromCurrentRequest().path("/{id}").buildAndExpand(result.getId()).toUri();
		
		return ResponseEntity.created(location).build();
    }
	
}
