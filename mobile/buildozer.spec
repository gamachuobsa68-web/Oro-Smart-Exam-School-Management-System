[app]

title = Go-Exam

package.name = goexam

package.domain = org.goexam

source.dir = .

source.include_exts = py,kv,png,jpg,json

version = 1.0.0


requirements = python3,kivy,requests


orientation = portrait

fullscreen = 0


android.permissions = INTERNET


android.api = 35

android.minapi = 23


# APK maqaa
android.entrypoint = org.kivy.android.PythonActivity
