from locust import HttpLocust, TaskSet, task
import json
import random
import resource

class UserBehavior(TaskSet):
    def on_start(self):
        #self.login()
        pass

    def login(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/user/login", data=json.dumps({"username": "admin", "password": "admin"}), headers=headers)

    @task(1)
    def user_get(self):
        self.client.get("/api/user/")

    @task(1)
    def department_get(self):
        self.client.get("/api/department/")

    @task(1)
    def department_getid(self):
        #id = random.randint(1, 100)
        self.client.get("/api/department/1")

    @task(0)
    def department_put(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/api/department/", data=json.dumps({"name": "LoadTest", "description": "LoadTest"}),
                     headers=headers)

    @task(1)
    def medicine_get(self):
        self.client.get("/api/medicine/")

    @task(0)
    def medicine_getid(self):
        id=random.randint(1,100)
        self.client.get("/api/medicine/"+str(id))

    @task(0)
    def medicine_put(self):
        headers = {'content-type': 'application/json'}
        self.client.put("/api/department/", data=json.dumps({"name": "LoadTest", "price": "233", "count":"233"}),
                        headers=headers)


class WebSiteUser(HttpLocust):
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))
    task_set = UserBehavior
    min_wait=500
    max_wait=5000
