from locust import HttpLocust, TaskSet, task
import json
import random
import resource
import httplib
import uuid

class PromiscuousScene(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/user/login", data=json.dumps({"username": "admin", "password": "admin"}), headers=headers)

    def logout(self):
        self.client.get("/api/user/logout")
        pass

    @task(10)
    def user_get(self):
        self.client.get("/api/user/")

    @task(10)
    def department_get(self):
        self.client.get("/api/department/")

    @task(10)
    def department_getid(self):
        #id = random.randint(1, 100)
        id=1
        self.client.get("/api/department/"+str(id))

    @task(1)
    def department_post(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/department/", data=json.dumps({"name": "LoadTest", "description": "LoadTest"}),headers=headers)

    @task(10)
    def medicine_get(self):
        self.client.get("/api/medicine/")

    @task(10)
    def medicine_getid(self):
        #id=random.randint(1,100)
        id=1
        self.client.get("/api/medicine/"+str(id))

    @task(1)
    def medicine_post(self):
        name=str(uuid.uuid4())
        headers = {'content-type': 'application/json'}
        self.client.post("/api/medicine/", data=json.dumps({"name": name, "price": "233", "count":"233"}),
                        headers=headers)


class WebSiteUser(HttpLocust):
    httplib._MAXHEADERS = 5000
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))
    task_set = PromiscuousScene
    min_wait=1000
    max_wait=3000
