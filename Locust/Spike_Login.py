from locust import HttpLocust, TaskSet, task
import json
import random
import resource
import httplib
import uuid

class Spike_Login(TaskSet):

    @task(1)
    def login_as_admin(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/user/login", data=json.dumps({"username": "admin", "password": "admin"}), headers=headers)

    @task(10)
    def login_as_user(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/user/login", data=json.dumps({"username": "user", "password": "user"}), headers=headers)


class WebSiteUser(HttpLocust):
    httplib._MAXHEADERS = 5000
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))
    task_set = Spike_Login
    min_wait=5000
    max_wait=10000
