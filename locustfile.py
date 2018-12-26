from locust import HttpLocust, TaskSet, task
import json

JSESSION = 'session id here!'


class SimpleTaskSet(TaskSet):

    def on_start(self):
        pass

    @task
    def post(self):
        payload = {
            'aaa': 'bbb',
        }
        headers = {
            'Cookie': 'JSESSION=' + JSESSION + ';'
        }
        self.client.post('/search', data=json.dumps(payload), headers=headers)


class SimpleLocust(HttpLocust):
    task_set = SimpleTaskSet  # 各ユーザーが前回のrequestを送信した後、何秒を待つかという設定
    min_wait = 0
    max_wait = 10
    host = 'https://somethinghost.com'
