import time
from locust import HttpUser, between, task
import random
import io

class WebsiteUser(HttpUser):
    wait_time = between(1,5)
    test_samples = (1, 5, 23, 158, 4, 14581, 102789173, 47438, 4398)

    # @task
    # def prime_page(self):
    #     self.client.get(f"prime/{random.choice(self.test_samples)}")
    #
    @task
    def prime(self):
        self.client.get(url=f'prime/5')

    @task
    def invert(self):
        in_file = open("test.jpg", "rb")
        data = in_file.read()
        self.client.post(url='picture/invert', files={'file': data})

    @task
    def time_page(self):
        self.client.get("show-time")