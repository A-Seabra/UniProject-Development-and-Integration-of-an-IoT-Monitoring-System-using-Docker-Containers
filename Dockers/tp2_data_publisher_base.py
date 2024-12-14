import paho.mqtt.publish as pub
import numpy as np
import os
import time

# para rodar
# docker-compose down     
# docker-compose up -d --build 


def generate(median=90, err=10, outlier_err=30, size=1000, outlier_size=10):
    errs = err * np.random.rand(size) * np.random.choice((-1, 1), size)
    data = median + errs

    lower_errs = outlier_err * np.random.rand(outlier_size)
    lower_outliers = median - err - lower_errs

    upper_errs = outlier_err * np.random.rand(outlier_size)
    upper_outliers = median + err + upper_errs

    data = np.concatenate((data, lower_outliers, upper_outliers))
    np.random.shuffle(data)

    return data

if __name__ == '__main__':
    print('Start program')
    # TODO: retrieve the environment variable values for the mqtt broker and the desired rate for the publishe
    broker = os.getenv('Broker')
    print(broker)

    rate = float(os.getenv('Rate'))  # Default publish rate is 1 message per second
    print(rate)

    topic = os.getenv('Topic')
    print(topic)

    Sensor = os.getenv('Sensor')

    # TODO: use the generate function to create a pool of values for the publisher
    data = generate()
    print(data)

    # TODO: publish a msg with a value randomly sampled from the data array. 
    # make it so that there's a 10% chance the value sent is null to emulate a sensor failure
    # you should filter these null values in Node Red 

     
    while True:
        value = np.random.choice(data)
        # Emulate a 10% chance that the value sent is null to emulate a sensor failure
        if np.random.random() < 0.1:
            value = None
        
        # Construct message including sensor information
        if value is not None:
            message = f"{Sensor}: {value}"
        else:
            message = f"{Sensor}: null"
        
        pub.single(topic, message, hostname=broker)
        print(f"Published: {message}")

        time.sleep(rate)

        
