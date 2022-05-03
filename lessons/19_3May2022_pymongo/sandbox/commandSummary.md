#### CS312S2022

#### Introduction

MongoDB commands to get into a Docker container and run the noSQL MongoDB system.

Note: The below are linux and MacOS commands but the Windows commands will be similar. Please copy and paste these below commands going line by line to determine any errors.

#### create container for Mongodb

```
sudo docker pull mongo
```

#### create directory to contain data

```
mkdir -p ~/mongodata
```

#### start Mongo server

```
sudo docker run -it -v ~/mongodata:/data/db --name mongodb -d mongo
```

#### check server

```
sudo docker logs mongodb
```

#### check server logs

```
sudo docker ps
```

#### start the bash

```
sudo docker exec -it mongodb bash
```

#### start client inside container

```
mongo
```

#### Trouble?

Remove Docker image and container and restart the above code

##### remove image

```
sudo docker image rm mongo -f
```

##### remove container

```
sudo docker container rm mongodb -f
```
