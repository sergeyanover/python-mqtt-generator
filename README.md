# MQTT generator on Python in Docker for RabbitMQ.

The python script generates and publishes messages periodically instead of using some IoT hardware. 
The messages are increasing integer numbers with the some period.
You should create docker image and run it with your settings in pythonmqtt.ini :

    git clone https://github.com/sergeyanover/python-mqtt-generator
    cd python-mqtt-generator
    docker build -t pythonmqtt .
    docker run -d -rm --name=pythonmqtt pythonmqtt

## You can start your own RabbitMQ server in Docker for testing:

    docker run --rm -it --hostname rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management

http://<your IP address>:15672
login: guest
password: guest
