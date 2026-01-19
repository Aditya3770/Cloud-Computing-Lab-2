from locust import HttpUser, task, constant

class EventsUser(HttpUser):
    wait_time = constant(1)

    @task
    def view_events(self):
        self.client.get("/events?user=locust_user", name="/events")
