# webapp-template-python
Webapp template using docker-compose with python flask, nginx and mongoDB.

## Use case

This docker-compose project can be used as a template for different web applications. The services included are an [nginx][1] webserver, a [mongo][2] database and an [python][3]/[Flask][4] template app, which can be built upon.


## Prerequisites

### Simple exemplary flask webapp is included

Main webapp is located at `app/app.py` with html files located at `app/templates` and resources located in `app/static`. The app shows a simple page that adds a tile with access information on every refresh. This information is saved in and queried from the included mongoDB.

### Preparing app for containerization

The `app/requirements.txt` file containing all necessary python packages is mounted by volume and run on entry.

## Creating an app based on this template

An app can be built by using the generated python/Flask foundation. By using docker-compose with mongoDB and nginx, the app will have an integrated database it can call upon as well as a complete webserver proxy to host the app.

The template is fairly flexible and may be adjusted to the needs required by the app.

### App debugging

Keep the mongoDB data within the container by commenting out a line within the `docker-compose.yml` that mounts a volume containing the data:

```yml
volumes:
  - ./mongodb/database/data:/data/db
```

This prevents testing data from being written to disk, including configurations such as user permissions that may change and lead to unexpected behaviour while developing.

The app is run in debug mode, which means that any change is instantly integrated without needing to reboot the app. The debug handle and other app related variables are set within `app/.env`.

When run locally the mongoDB can be accessed by using [compass][5] and the user information provided within `mongodb/.env` or `mongodb/.init.js`.

Omit `--detach` option when building the containers.

The template is set up as to reach the app at `localhost`.

## nginx configuration

nginx configurations can be done using the `nginx/nginx.conf`-file. SSL certificates are expected per default and can be added into `nginx/ssl`.
Generate self signed RSA certificates for testing purposes using [openSSL][6]:

```bash
sudo mkdir nginx/ssl
cd nginx/ssl

# Generate key pair
sudo openssl req -new -x509 -nodes -newkey rsa:4096 -keyout server.key -out server.crt

# Set correct key permissions
sudo chmod 400 server.key
sudo chmod 444 server.crt
```

## Building the docker container

`docker-compose up --build --detach`

## Stop and remove docker-compose containers

```bash
sudo docker-compose stop app nginx mongodb
sudo docker-compose rm app nginx mongodb
```


[1]: https://nginx.org/en/docs/
[2]: https://docs.mongodb.com/
[3]: https://www.python.org/doc/versions/
[4]: http://flask.pocoo.org/docs
[5]: https://www.mongodb.com/products/compass
[6]: https://www.openssl.org/docs/manmaster/man1/openssl-req.html