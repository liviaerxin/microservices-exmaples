```sh
awk '{sub("\r", "", $1); printf("DELETE FROM Analytics WHERE id=\"%s\";\n", $1)}' rm_analytics_id.txt > delete.sql 
```
