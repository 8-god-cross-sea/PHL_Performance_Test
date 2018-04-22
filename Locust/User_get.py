from locust import HttpLocust, TaskSet, task
import json
import random
import resource
import httplib
import uuid

class PromiscuousScene(TaskSet):
    def on_start(self):
        self.login()


    def login(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/user/login", data=json.dumps({"username": "admin", "password": "admin"}), headers=headers)


    @task(1)
    def user_get(self):
        self.client.get("/api/user/")


class WebSiteUser(HttpLocust):
    httplib._MAXHEADERS = 5000
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))
    task_set = PromiscuousScene
    min_wait=0
    max_wait=0
