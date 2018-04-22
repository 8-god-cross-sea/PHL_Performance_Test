from locust import HttpLocust, TaskSet, task
import json
import random
import resource
import httplib
import uuid

class Department1(TaskSet):

    @task(1)
    def login(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/user/login", data=json.dumps({"username": "user", "password": "user"}), headers=headers)


class WebSiteUser(HttpLocust):
    httplib._MAXHEADERS = 5000
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))
    task_set = Department1
    min_wait=2000
    max_wait=2000
