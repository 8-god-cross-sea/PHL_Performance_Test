from locust import HttpLocust, TaskSet, task
import json
import random
import resource
import httplib
import uuid

class Spike_Test(TaskSet):
    def login(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/user/login", data=json.dumps({"username": "user", "password": "user"}),
                         headers=headers)

    def on_start(self):
        self.login()

    @task(1)
    def get_test(self):
        self.client.get("api/exam")



class WebSiteUser(HttpLocust):
    httplib._MAXHEADERS = 5000
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))
    task_set = Spike_Test
    min_wait=5000
    max_wait=10000
