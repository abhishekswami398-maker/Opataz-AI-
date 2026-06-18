[app]

title = Opataz AI
package.name = opatazai
package.domain = org.opataz

source.dir = .
source.include_exts = py,png,jpg,kv,ttf,csv

version = 1.0

requirements = python3,kivy==2.3.0,kivymd,numpy,pandas

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

[buildozer]

log_level = 2
warn_on_root = 1
