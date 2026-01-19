from locust import HttpUser, task, constant

class MyEventsUser(HttpUser):
    wait_time = constant(1)

    @task
    def view_my_events(self):
        self.client.get("/my-events", name="/my-events")
