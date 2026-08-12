[app]
title = ReminGame
package.name = remingame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,mp3
version = 0.1
requirements = python3,kivy,pygame
orientation = landscape
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
archs = armeabi-v7a
api = 31
minapi = 21
ndk = 25b
accept_sdk_license = True
