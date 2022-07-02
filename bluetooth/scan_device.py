import asyncio
from bleak import BleakScanner


async def main():
    async with BleakScanner() as scanner:
        await asyncio.sleep(5.0)
    for d in scanner.discovered_devices:
        print(d.name, d.address, d.rssi, d.details, d.metadata)


asyncio.run(main())
