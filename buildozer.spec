[app]

title = Opataz AI
package.name = opatazai
package.domain = org.opataz

source.dir = .
source.include_exts = py,png,jpg,kv,ttf,csv

version = 1.0

requirements = python3,kivy,kivymd,numpy,pandas

orientation = portrait

fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21

[buildozer]

log_level = 2
warn_on_root = 1
