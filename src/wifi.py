import machine
import network

def connect_wifi(ssid: str, password: str) -> None:
    print(f"Connecting to {ssid}...")
    wlan = network.WLAN()
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            machine.idle()
    print('Network config: ', wlan.ifconfig())
