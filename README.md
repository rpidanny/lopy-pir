# LoPy PIR

Logging PIR data to Adafruit.io

## Usage

- Make a copy of `scripts/config_example.py` and rename it to `scripts/config.py`
- Fill in your `WiFi credentials`, `MQTT Configs` and `GPIO Configs`.
- Upload the code to LoPy.

The device subscribes to a MQTT topic specified in `scripts/config.py`.


## Wiring

| LoPy                                      | Transmitter   |
| :---------------------------------------- | :------------ |
| `P9` (or any pin specified in config.py)  | `Data`        |
| `3.3V`                                    | `VCC`         |
| `GND`                                     | `GND`         |
