import redis
from typing import Dict


class RedisWorker:
    def __init__(self):
        self.redis_client = redis.Redis()

    def update_dictionary(self, input_dictionary: Dict):
        self.redis_client.mset(input_dictionary)

    def query_dictionary(self, input_key: str):
        return self.redis_client.get(input_key)


if __name__ == '__main__':
    redis_worker = RedisWorker()

    # Input dictionary
    input_dict = {"Croatia": "Zagreb", "Bahamas": "Nassau"}
    redis_worker.update_dictionary(input_dict)

    # Query the Dictionary
    key = "Bahamas"
    output_value = redis_worker.query_dictionary(key)
    print(f"Output value fetched for {key} is {str(output_value)}")