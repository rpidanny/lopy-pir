# LoPy PIR

Logs PIR data to [Adafruit.io](https://io.adafruit.com/).

## Usage

- Make a copy of `scripts/config_example.py` and rename it to `scripts/config.py`
- Fill in your `WiFi credentials`, `Adafruit Configs` and `PIR Configs`.
- Upload the code to LoPy.

## Wiring

| LoPy                                      | Transmitter   |
| :---------------------------------------- | :------------ |
| `G10` (or any pin specified in config.py)  | `Data`        |
| `3.3V`                                    | `VCC`         |
| `GND`                                     | `GND`         |
