from machine import Pin, Timer
from time import sleep_ms
import ubluetooth

message = ""


class ESP32_BLE():
    def __init__(self, name):
        self.led = Pin(2, Pin.OUT)
        self.timer = Timer(0)
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()

    def connected(self):
        self.led.value(1)
        self.timer.deinit()

    def disconnected(self):
        self.timer.init(
            period=100,
            mode=Timer.PERIODIC,
            callback=lambda t: self.led.value(not self.led.value()),
        )

    def ble_irq(self, event, data):
        global message
        if event == 1:
            self.connected()
        elif event == 2:
            self.advertiser()
            self.disconnected()
        elif event == 3:
            buffer = self.ble.gatts_read(self.rx)
            message = buffer.decode("UTF-8").strip()
            print(message)

    def register(self):
        NUS_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
        RX_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
        TX_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
        BLE_NUS = ubluetooth.UUID(NUS_UUID)
        BLE_RX = (ubluetooth.UUID(RX_UUID), ubluetooth.FLAG_WRITE)
        BLE_TX = (ubluetooth.UUID(TX_UUID), ubluetooth.FLAG_NOTIFY)
        BLE_UART = (
            BLE_NUS,
            (
                BLE_TX,
                BLE_RX,
            ),
        )
        SERVICES = (BLE_UART,)
        (
            (
                self.tx,
                self.rx,
            ),
        ) = self.ble.gatts_register_services(SERVICES)

    def send(self, data):
        self.ble.gatts_notify(0, self.tx, data, "\n")

    def advertiser(self):
        name = bytes(self.name, "UTF-8")
        adv_data = bytearray("\x02\x01\x02") + bytearray((len(name) + 1, 0x09)) + name
        self.ble.gap_advertise(100, adv_data)
        print(adv_data)
        print("\r\n")


led = Pin(2, Pin.OUT)
but = Pin(0, Pin.IN)
ble = ESP32_BLE("ESP32BLE")


def buttons_irq(pin):
    led.value(not led.value())
    ble.send("LED state will be toggled")
    print("LED State will be toggled")


but.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)
while True:
    if message == "STATUS":
        message = ""
        print("LED is ON" if led.value() else "LED is OFF")
        ble.send("LED is ON" if led.value() else "LED is OFF")
    sleep_ms(100)
