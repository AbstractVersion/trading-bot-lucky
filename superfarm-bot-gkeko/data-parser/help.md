# Connect to influx from cli
gain a shell on the container and execute :
```sell
    influx -host localhost -port 8086 -database pv_adapt -username admin -password admin
```

deploy on infer :

docker-compose -f docker-compose.infer.yml --env-file .infer.env up