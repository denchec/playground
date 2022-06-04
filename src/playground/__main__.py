from json import dumps
import time
from datetime import datetime
from kafka import KafkaProducer

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def main():
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

    for i in range(10):
        data = {
            'num': i,
            'ts': datetime.now().strftime(TIME_FORMAT)
        }
        producer.send(topic="test_message", value=data)
        time.sleep(1)


if __name__ == "__main__":
    main()
