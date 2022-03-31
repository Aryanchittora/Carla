import glob
import os
import sys
import time

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actor_list = []


def generate_radar_blueprint(blueprint):
    radar = blueprint.filter('sensor.other.radar')[0]
    radar.set_attribute('horizontal_fov', str(35))
    radar.set_attribute('vertical_fov', str(20))
    radar.set_attribute('points_per_second', str(1500))
    radar.set_attribute('range', str(20))
    return radar

def carControl():
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.5))
    time.sleep(5.5)
    
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.4, steer=-0.4))
    time.sleep(2)

    dropped_vehicle.apply_control(carla.VehicleControl(throttle=9))
    time.sleep(5)

    dropped_vehicle.apply_control(carla.VehicleControl(hand_brake=True))
    time.sleep(2)

try:
    client = carla.Client('127.0.0.1', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

    get_blueprint_of_world = world.get_blueprint_library()
    car_model = get_blueprint_of_world.filter('model3')[0]
    spawn_point = (world.get_map().get_spawn_points()[1])
    dropped_vehicle = world.spawn_actor(car_model, spawn_point)


    simulator_camera_location_rotation = carla.Transform(spawn_point.location, spawn_point.rotation)
    simulator_camera_location_rotation.location += spawn_point.get_forward_vector() * 30
    simulator_camera_location_rotation.rotation.yaw += 180
    simulator_camera_view = world.get_spectator()
    simulator_camera_view.set_transform(simulator_camera_location_rotation)
    actor_list.append(dropped_vehicle)
    radar_sensor = generate_radar_blueprint(get_blueprint_of_world)
    sensor_radar_spawn_point = carla.Transform(carla.Location(x=-0.5, z=1.8))
    sensor = world.spawn_actor(radar_sensor, sensor_radar_spawn_point, attach_to=dropped_vehicle)
    


    sensor.listen(lambda data : _radar_data(data))

    def _radar_data(data):
        for x in data:
            print('Depth -', str(x.depth))
            print('Azimuth -', str(x.azimuth))
            print('Altitude', str(x.altitude))
            print('Velocity -', str(x.velocity))
     
    #carControl()    
    dropped_vehicle.set_autopilot()

    actor_list.append(sensor)

    time.sleep(1000)
finally:
    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')
