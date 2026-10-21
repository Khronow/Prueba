
[app]

title = Volante Bluetooth
package.name = volantebluetooth
package.domain = org.volante

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,plyer,pyjnius

orientation = landscape
fullscreen = 0

android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_CONNECT, BLUETOOTH_SCAN
android.api = 35
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

p4a.branch = v2024.01.21

[buildozer]

log_level = 2
warn_on_root = 1
