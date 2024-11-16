from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import os
import subprocess
import webview
from kivy import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Disable OpenGL multisampling and set resizable window to 0 for better compatibility with WebView
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'resizable', '0')

class MyDjangoApp(App):
    def build(self):
        # Start Django server in the background
        self.start_django_server()

        # Start WebView to show the Django app
        self.open_webview()

        layout = BoxLayout(orientation='vertical')
        button = Button(text="Open WebView", size_hint=(1, 0.2))
        layout.add_widget(button)

        return layout

    def start_django_server(self):
        """Start Django server as a subprocess"""
        django_path = os.path.join(os.path.dirname(__file__), "project")  # Adjust your Django project path here
        manage_py = os.path.join(django_path, "manage.py")

        # Start Django server in a new subprocess
        print("Starting Django server...")
        subprocess.Popen(
            ["python", manage_py, "runserver", "127.0.0.1:8000"],
            cwd=django_path,
        )

    def open_webview(self):
        """Open the WebView to show the Django app"""
        print("Opening WebView...")  # Debugging message

        # Start WebView with Django running on localhost (127.0.0.1:8000)
        webview.create_window("Django App", "http://127.0.0.1:8000")
        webview.start()

    def on_stop(self):
        """Called when the app is stopped (closed)"""
        print("Stopping the app...")

        # Kill the Django server process
        if self.django_process:
            self.django_process.terminate()

        # Optionally: Wait for the webview to close or clean up
        if hasattr(self, 'webview_thread'):
            self.webview_thread.join()

        super().on_stop()

if __name__ == "__main__":
    MyDjangoApp().run()

