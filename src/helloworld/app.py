"""
An app with a button, where if you click it, Python code runs.

Based on:

https://github.com/paulproteus/Python-Android-sample-apps/blob/master/PythonStubsApp
"""
import datetime
import json
import random
import urllib.request
import sys

from rubicon.java import JavaClass, JavaInterface


def print_int_list():
    numbers = [random.randint(0, 99) for i in range(5)]
    print("random integers from 0 to 99 (inclusive)")
    print(">>> [random.randint(0, 99) for i in range(5)]")
    print(numbers)


def print_beeware_members():
    response = urllib.request.urlopen(
        "https://api.github.com/orgs/beeware/members"
    )
    body = response.read()
    parsed = json.loads(body)
    print(">>> parsed = json.loads(urllib.request.urlopen(...).read())")
    print(">>> [item['login'] for item in parsed]")
    print([item["login"] for item in parsed])


def print_now():
    now = datetime.datetime.now()
    print("Current time in current time zone")
    print(">>> datetime.datetime.now().isoformat()")
    print(now.isoformat())
    utcnow = datetime.datetime.utcnow()
    print("Current time in UTC")
    print(">>> datetime.datetime.utcnow().isoformat()")
    print(utcnow.isoformat())


def run_demo_code():
    print_now()
    print_int_list()
    print_beeware_members()


OnClickListener = JavaInterface("android/view/View$OnClickListener")
IPythonApp = JavaInterface("org/beeware/android/IPythonApp")

Button = JavaClass("android/widget/Button")
LinearLayout = JavaClass("android/widget/LinearLayout")


class OnClickRunDemoCode(OnClickListener):
    def onClick(self, _view):
        run_demo_code()


class Application(IPythonApp):
    def onCreate(self):
        print("called Python onCreate method")

    def onStart(self):
        print("called Python onStart method")
        self.make_button()

    def onResume(self):
        print("called Python onResume method")

    def make_button(self):
        activity_class = JavaClass("org/beeware/android/MainActivity")
        java_activity_instance = activity_class.singletonThis

        linear_layout = LinearLayout(java_activity_instance)
        java_activity_instance.setContentView(linear_layout)
        button = Button(java_activity_instance)
        button.setText("Python made this button! Click Me")
        button.setOnClickListener(OnClickRunDemoCode())
        linear_layout.addView(button)


app = Application()
print("app launched", app, file=sys.stderr)

activity_class = JavaClass("org/beeware/android/MainActivity")
activity_class.setPythonApp(app)
print("Successfully stored reference to Python app in Java field")
