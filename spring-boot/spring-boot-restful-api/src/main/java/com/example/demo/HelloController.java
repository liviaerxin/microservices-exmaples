package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.concurrent.atomic.AtomicLong;

@Controller
public class HelloController {

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @RequestMapping("/hello")
    @ResponseBody
    public HelloEntity hello(@RequestParam(value="name", defaultValue="World") String name) {
        return new HelloEntity(counter.incrementAndGet(),
                String.format(template, name));
    }

}
