## Connectivator

Simple wrapper functions for connecting to and loading data.

### Current State

* Connect to Postgres / Redshift

### Environment Variables

* Add a `.env` file to the project root directory.
* Add the following environment variables, replacing with values relevant for your connections. Format:

**Postgres/Redshift Connection**

```
export PGHOST = instance-name.abc123.us-east-1.redshift.amazonaws.com
export PGPORT = 5439
export PGUSER = your_user_name
export PGPASSWORD = your_password
```

* Load the environment variables before running the script. For example, by running `source .env` in the terminal you are using to run Python scripts.
