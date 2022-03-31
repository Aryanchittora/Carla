import glob
import os
import sys
import time
import math
from turtle import distance

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actor_list = []

object_id = {"None": 0,
             "Buildings": 1,
             "Fences": 2,
             "Other": 3,
             "Pedestrians": 4,
             "Poles": 5,
             "RoadLines": 6,
             "Roads": 7,
             "Sidewalks": 8,
             "Vegetation": 9,
             "Vehicles": 10,
             "Wall": 11,
             "TrafficsSigns": 12,
             "Sky": 13,
             "Ground": 14,
             "Bridge": 15,
             "RailTrack": 16,
             "GuardRail": 17,
             "TrafficLight": 18,
             "Static": 19,
             "Dynamic": 20,
             "Water": 21,
             "Terrain": 22
             }
key_list = list(object_id.keys())
val_list = list(object_id.values())


def generate_lidar_blueprint(blueprint_library):
    lidar_blueprint = blueprint_library.find('sensor.lidar.ray_cast_semantic')
    lidar_blueprint.set_attribute('channels', str(64))
    lidar_blueprint.set_attribute('points_per_second', str(56000))
    lidar_blueprint.set_attribute('rotation_frequency', str(40))
    lidar_blueprint.set_attribute('range', str(100))
    return lidar_blueprint


def check_traffic_lights():
    if dropped_vehicle.is_at_traffic_light():
        trafficLight = dropped_vehicle.get_traffic_light()
        if trafficLight.get_state() == carla.TrafficLightState.Red:
            print(trafficLight.get_state())
            dropped_vehicle.apply_control(carla.VehicleControl(hand_brake=True))
    else:
        dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.51))

def semantic_lidar_data(point_cloud):
    distanceName = {}
    for x in point_cloud:
        pos = val_list.index(x.object_tag)
        distance = math.sqrt((x.point.x ** 2) + (x.point.y ** 2) + (x.point.z ** 2))
        distanceName['distance'] = distance
        print("Distance", distanceName['distance'])
        distanceName['name'] = key_list[pos]

        for y in object_id:
            if distanceName['name'] == y and distanceName['distance'] > 5 and distanceName['distance'] < 7:
                dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.31))

                if distanceName['name'] == y and distanceName['distance'] > 3 and distanceName['distance'] < 6:
                    dropped_vehicle.apply_control(carla.VehicleControl(hand_brake=True))
                    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.31))
                    dropped_vehicle.set_light_state(carla.VehicleLightState(carla.VehicleLightState.Brake | carla.VehicleLightState.LowBeam))
                    print(f"Object near our car : {y} and distance : {distanceName['distance']}")
                    break
            else :
                print(f"Object near our car : {y} and distance : {distanceName['distance']}")
                
try:
    client = carla.Client('127.0.0.1', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

    get_blueprint_of_world = world.get_blueprint_library()
    car_model = get_blueprint_of_world.filter('model3')[0]
    spawn_point = (world.get_map().get_spawn_points()[47])
    dropped_vehicle = world.spawn_actor(car_model, spawn_point)

    simulator_camera_location_rotation = carla.Transform(spawn_point.location, spawn_point.rotation)
    simulator_camera_location_rotation.location += spawn_point.get_forward_vector() * 30
    simulator_camera_location_rotation.rotation.yaw += 180
    simulator_camera_view = world.get_spectator()
    simulator_camera_view.set_transform(simulator_camera_location_rotation)
    actor_list.append(dropped_vehicle)

    lidar_sensor = generate_lidar_blueprint(get_blueprint_of_world)
    sensor_lidar_spawn_point = carla.Transform(carla.Location(x=0, y=0, z=2.0),
                                               carla.Rotation(pitch=0.000000, yaw=90.0, roll=0.000000))
    lidar_sensor_data = world.spawn_actor(lidar_sensor, sensor_lidar_spawn_point, attach_to=dropped_vehicle)

    lidar_sensor_data.listen(lambda data: semantic_lidar_data(data))

    check_traffic_lights()
    actor_list.append(lidar_sensor_data)
    check_traffic_lights()
    time.sleep(1000)
finally:
    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')
