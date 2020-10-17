#!/usr/bin/env python3

import os
import asyncio
from mavsdk import System, telemetry


async def run():
    # Init the drone
    drone = System(mavsdk_server_address='127.0.0.1', port=50051)
    await drone.connect(system_address="udp://127.0.0.1:14550")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    # If ping ground station fail, return to launch
    async for flight_mode in drone.telemetry.flight_mode():
        print(flight_mode)
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
