from threading import Timer
import logging


class TrafficObject(object):

    def set_car_state(self, car_state):
        pass

    @staticmethod
    def is_close_by(obj, frame_height, min_height_pct=0.05):
        # default: if a sign is 10% of the height of frame
        obj_height = obj.bounding_box[1][1]-obj.bounding_box[0][1]
        return obj_height / frame_height > min_height_pct


class RedTrafficLight(TrafficObject):

    def set_car_state(self, car_state):
        logging.debug('red light: stopping car')
        car_state['speed'] = 0


class GreenTrafficLight(TrafficObject):

    def set_car_state(self, car_state):
        logging.debug('green light detected')


class Person(TrafficObject):

    def set_car_state(self, car_state):
        logging.debug('pedestrian: stopping car')

        car_state['speed'] = 0
        
class Cyclist(TrafficObject):

    def set_car_state(self, car_state):
        logging.debug('cyclist: stopping car')

        car_state['speed'] = 0


class SpeedLimit(TrafficObject):

    def __init__(self, speed_limit):
        self.speed_limit = speed_limit

    def set_car_state(self, car_state):
        logging.debug('speed limit: set limit to %d' % self.speed_limit)
        car_state['speed_limit'] = self.speed_limit


class StopSign(TrafficObject):

     def set_car_state(self, car_state):
        logging.debug('stop sign: stopping car')

        car_state['speed'] = 0
