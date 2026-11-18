[app]
title = KING REIGNS CYBERY WORD BUILDER
package.name = kingwordbuilder
package.domain = org.kingreigns.cybery
source.dir = app
source.include_exts = py,json,txt,kv,ttf
source.include_patterns = data/dictionary_final.json,data/english_frequency_50k.txt
source.exclude_dirs = __pycache__
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.api = 35
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
