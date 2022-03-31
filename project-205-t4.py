import glob
import os
import sys
import argparse
import random
import time


try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actors = []

"""Main function of the script"""
try:
    client = carla.Client('127.0.0.1', 2000)
    client.set_timeout(2.0)
    world = client.get_world()

    blueprint = world.get_blueprint_library()
    vehicle_bp = blueprint.filter('ninja')[0]
    vehicle_transform = random.choice(world.get_map().get_spawn_points())

    dropped_vehicle = world.spawn_actor(vehicle_bp, vehicle_transform) #call vehicle with variable name dropped_vehicle
    dropped_vehicle.set_autopilot(True) #set vehicle as autopilot

    spectator_transform = carla.Transform(vehicle_transform.location, vehicle_transform.rotation)
    spectator_transform.location += vehicle_transform.get_forward_vector() * 20
    spectator_transform.rotation.yaw += 180
    spectator = world.get_spectator()
    spectator.set_transform(spectator_transform)
    dropped_vehicle.set_transform(vehicle_transform)
    actors.append(dropped_vehicle)

    time.sleep(1000)


finally:
    print('destroying actors')
    for x in actors:
        x.destroy()
    print('done.')


