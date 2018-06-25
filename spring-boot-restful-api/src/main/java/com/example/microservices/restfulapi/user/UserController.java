package com.example.microservices.restfulapi.user;

import java.net.URI;
import java.util.Collection;

import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;


@RestController
public class UserController {
	
	@Autowired
	private UserRepository userRepository;
	
	@Autowired
	private RabbitTemplate rabbitTemplate;
	
	//curl http://localhost:8080/user
	@RequestMapping(method=RequestMethod.GET, path = "/user")
    public Collection<User> getAll() {
        return userRepository.findAll();
    }
	
	//curl -i -X POST -H "Content-Type:application/json" -d "{  \"emailAddress\" : \"123@gmail.com\",  \"password\" : \"123\" }" http://localhost:8080/user
	@RequestMapping(method=RequestMethod.POST, path = "/user")
	ResponseEntity<?> add(@RequestBody User input) {
		User result = userRepository.save(new User(input.getEmailAddress(), input.getPassword()));
		URI location = ServletUriComponentsBuilder.
				fromCurrentRequest().path("/{id}").buildAndExpand(result.getId()).toUri();
		
		rabbitTemplate.convertAndSend("test", "Hello New User!");
		return ResponseEntity.created(location).build();
    }
}
