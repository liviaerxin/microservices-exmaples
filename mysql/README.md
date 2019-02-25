# remove records by `id` file
```sh
awk '{sub("\r", "", $1); printf("DELETE FROM Analytics WHERE id=\"%s\";\n", $1)}' rm_analytics_id.txt > delete.sql 
```

# Locking Mechanism
The neccessity of locking: `handle concurrency conflicts`
Let's take a case: `N numberof client` are accessing the same data at the same time, and they want to do some changes and these changes will cause `discrepancy` or `inconsistency` in that data, so to avoid overwriting each others work, we have to restrict access to one of them at a time for specific table or row or column.


[Locking Rows In MYSQL](https://medium.com/@ibraheemabukaff/locking-rows-in-mysql-e84fd3bbb8cd)  
[Database Locking: What it is, Why it Matters and What to do About it](http://www.methodsandtools.com/archive/archive.php?id=83)  
[Concurrency control in web development](https://www.spectory.com/blog/Concurrency%20control%20in%20web%20development)  
[Concurrent Editing Without Locking](http://jim-mcbeath.blogspot.com/2009/02/concurrent-editing-without-locking.html)  


## Locking in JPA/Hibernate
[Optimistic locking in JPA/Hibernate](https://blog.arnoldgalovics.com/optimistic-locking-in-jpa-hibernate/)  
[Pessimistic Locking in JPA](https://www.baeldung.com/jpa-pessimistic-locking)   