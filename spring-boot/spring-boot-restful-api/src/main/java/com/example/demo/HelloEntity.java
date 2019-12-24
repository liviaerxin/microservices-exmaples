package com.example.demo;

public class HelloEntity {
    private final long id;
    private final String content;

    public HelloEntity(long id, String content) {
        this.id = id;
        this.content = content;
    }

    public long getId() {
        return id;
    }

    public String getContent() {
        return content;
    }
}
