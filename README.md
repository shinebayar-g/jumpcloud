# Jumpcloud assignment

## Start server

### Prerequisites

1. Make sure you've fairly recent version of `docker` and `docker-compose` installed.
1. Run `docker-compose up -d`

## API Usage:

*get useful information about your organization*
```shell script
curl -X GET http://localhost:5000/api/v1.0/info \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}'
```

*get all system user*

```shell script
curl -X GET http://localhost:5000/api/v1.0/systemusers \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}'
```

*create new system user*

```shell script
curl -X POST http://localhost:5000/api/v1.0/systemusers \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}' \
  -d '{
	"username":"{username}",
	"email":"{email_address}",
	"firstname":"{Name}",
	"lastname":"{Name}"
}'
```

*get system user*

```shell script
curl -X PUT http://localhost:5000/api/v1.0/systemusers/{UserID} \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}' \
  -d '{
	"email":"{email_address}",
	"firstname":"{Name}",
	"lastname":"{Name}"
}'
```

*update system user*
```shell script
curl -X PUT http://localhost:5000/api/v1.0/systemusers/{UserID} \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}' \
  -d '{
	"email":"{email_address}",
	"firstname":"{Name}",
	"lastname":"{Name}"
}'
```

*delete system user*

```shell script
curl -X DELETE http://localhost:5000/api/v1.0/systemusers/{UserID} \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}' 
```
