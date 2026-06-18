[app]

title = Opataz AI
package.name = opatazai
package.domain = org.opataz

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,csv

version = 1.0

requirements = python3,kivy,kivymd,numpy,pandas

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

log_level = 2

[buildozer]

warn_on_root = 1
