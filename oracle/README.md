1. Run the Oracle Database Container with Mount

```bash
docker run -d --name oracle-db \
  -p 1521:1521 -p 5500:5500 \
  -e ORACLE_PWD=<your_password> \
  -v /path/to/oracle_data:/ORCL \
  container-registry.oracle.com/database/free:latest
```

`-p 1521:1521`: Maps port 1521 of the container (default Oracle Database port).
`-p 5500:5500`: Maps port 5500 for Oracle Enterprise Manager.

stop container: `docker stop oracle-db`

start container: `docker start oracle-db`

2. Execute a Shell in the Oracle Container:

`docker exec -it oracle-db /bin/bash`

Once inside the container, you can use SQL*Plus:

`sqlplus sys as sysdba`

`as sysdba` clause qualifies the type of access level, SYSDBA stands for "System Database Administrator."  

`SYS` user is a special administrative account in Oracle Database that has the highest level of privileges. 

3. get SID

`SELECT instance_name, instance_number FROM v$instance;`: This will return the instance name, which corresponds to your SID.

4. create SID




