# UniProject-Development-and-Integration-of-an-IoT-Monitoring-System-using-Docker-Containers

University project about developing a container-based solution capable of integrating data from various sources, using Node-Red, Python and Docker, and integrating tools like MongoDB, InfluxDB and Grafana.

The goal was to develop a container-based solution capable of integrating data from various sources (data generator 1, 2, ..., N), performing pre-processing, and subsequently storing the data in two NoSQL databases, one for historical records and the other for real-time values of the last hour. 
This data also served as the foundation for developing a monitoring dashboard capable of alerting the user to potential anomalies.
The communication was leveraged through a Publish/Subscribe mechanism. In this case, the data extracted by the Python sources was sent to topics created in the Mosquitto MQTT broker, and later consumed by the Node-Red integration platform. 
This platform plays a facilitating role in both system integration and dashboard development.

