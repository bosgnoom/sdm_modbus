#!/usr/bin/env python3

import argparse
import sdm_modbus


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--device", type=str, default='/dev/ttyUSB0', help="Modbus device")
    argparser.add_argument("--stopbits", type=int, default=1, help="Stop bits")
    argparser.add_argument("--parity", type=str, default="N", choices=["N", "E", "O"], help="Parity")
    argparser.add_argument("--baud", type=int, default=9600, help="Baud rate")
    argparser.add_argument("--timeout", type=int, default=1, help="Connection timeout")
    argparser.add_argument("--unit", type=int, default=1, help="Modbus unit")

    args = argparser.parse_args()

    meter = sdm_modbus.SDM120(
        device=args.device,
        stopbits=args.stopbits,
        parity=args.parity,
        baud=args.baud,
        timeout=args.timeout,
        unit=args.unit
    )

    # Read all INPUT registers, because example-rtu gives me only the first batch
    for (k, v) in meter.registers.items():
        address, length, rtype, dtype, vtype, label, fmt, batch, sf = v

        if rtype == sdm_modbus.meter.registerType.INPUT:
            value = meter.read(k, scaling=True)
            if type(fmt) is list:
                print(f"{k} {label}: {fmt[value]}")
            elif type(fmt) is dict:
                print(f"{k} {label}: {fmt[str(value)]}")
            elif vtype is float:
                print(f"{k} {label}: {value:.2f}{fmt}")
            else:
                print(f"{k} {label}: {value}{fmt}")
