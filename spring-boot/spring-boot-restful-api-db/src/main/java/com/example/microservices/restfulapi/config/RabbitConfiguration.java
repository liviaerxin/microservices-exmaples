package com.example.microservices.restfulapi.config;

import org.springframework.amqp.core.Queue;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitAdmin;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitConfiguration {

	@Bean
	public Queue queue1() {
	    return new Queue("AAA", false);
	}

	@Bean
	public Queue queue2() {
	    return new Queue("BBB", false); 
	}
    @Bean
    public ConnectionFactory connectionFactory() {
    	CachingConnectionFactory cf = new CachingConnectionFactory();
    	cf.setAddresses("sidewinder.rmq.cloudamqp.com");
    	cf.setUsername("vovucotc");
    	cf.setPassword("CeTejZDlNKK9VPOWGNLzRTCnyFCmYnbH");
    	cf.setVirtualHost("vovucotc");
        return cf;
    }

    @Bean
    public RabbitAdmin admin() {
    	return new RabbitAdmin(connectionFactory());
    }
    
    @Bean
    public RabbitTemplate rabbitTemplate() {
        return new RabbitTemplate(connectionFactory());
    }
    
}

