from locust import HttpLocust, TaskSet, task
import json
import random
import resource
import httplib
import uuid

class Department1(TaskSet):

    @task(1)
    def department_get_1(self):
        self.client.get("/api/department/1")


class WebSiteUser(HttpLocust):
    httplib._MAXHEADERS = 5000
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))
    task_set = Department1
    min_wait=0
    max_wait=0
