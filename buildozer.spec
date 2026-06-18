[app]

title = Opataz AI
package.name = opatazai
package.domain = org.opataz

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,csv

version = 1.0

requirements = python3,kivy==2.3.0,kivymd,numpy,pandas

orientation = portrait

fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21

android.sdk = 33
android.ndk = 25b

android.build_tools = 33.0.2

presplash.filename = logo.png
icon.filename = logo.png

log_level = 2

[buildozer]

warn_on_root = 1
