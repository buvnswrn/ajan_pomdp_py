import math
import random

import numpy as np
import pomdp_py

from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation


class ObservationModel(pomdp_py.ObservationModel):

    def __init__(self, person_id):
        self.epsilon = 1
        self.person_id = person_id

    def probability(self, observation, state, action):
        if action.name != "perceive":
            if observation.attributes["pose"] is None:
                return 1.0
            else:
                return 0.0
        if state.objclass.lower().__contains__("person"):
            sigma = 5
            dist = 0
            pose = observation.attributes["pose"]
            gesture = state.attributes["gesture"]
            if pose is not None and len(pose) > 0:
                if gesture == 'left':
                    dist = math.dist(pose[11], pose[9])
                elif gesture == 'right':
                    dist = math.dist(pose[12], pose[10])
                return 1 - math.exp(-((dist / 10) ** 2) / (2 * sigma ** 2))
            return 1.0

    def sample(self, state, action):
        obs = self.argmax(state, action)
        return obs

    def argmax(self, state, action):
        if action.name != "perceive":
            return AjanObservation({"pose": None}, ["pose"])
        num_points = 17
        x_values = np.random.uniform(0, 640, num_points)
        y_values = np.random.uniform(0, 480, num_points)
        keypoints = np.column_stack((x_values, y_values))
        choice = random.choices([None, keypoints])[0]
        return AjanObservation({"pose": choice}, ["pose"])
