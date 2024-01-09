import random

import pomdp_py

from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState, AjanOOState, AjanAgentState


class TransitionModel(pomdp_py.TransitionModel):
    def __init__(self, name, model_id, epsilon=1e-9):
        self._epsilon = epsilon
        self.name = name
        self.model_id = model_id

    def probability(self, next_state, state, action):
        if isinstance(state, AjanOOState):
            state = state.object_states[next_state['id']]
        if next_state != state:
            return self._epsilon
        else:
            return 1.0 - self._epsilon

    def sample(self, state, action):
        return self.argmax(state, action)

    def argmax(self, state: AjanOOState, action):
        if isinstance(state, AjanOOState):
            state = state.object_states[self.model_id]
        if self.name == "person":
            if action.name == "perceive":
                return AjanEnvObjectState("Person", self.model_id,
                                          {"pose": None, "gesture": random.choices(['left', 'right', None])[0]})
            else:
                return state
        elif self.name == "drone":
            if action.name == "perceive":
                return AjanAgentState("Drone", self.model_id, {"pose": state.attributes["pose"],
                                                               "gesture_found": random.choices([True, False])[0]})
            if action.name == "move":
                x, y = state.attributes["pose"]
                if action.attributes["motion"] == "left":
                    x -= 1
                elif action.attributes["motion"] == "right":
                    x += 1
                y += 1
                return AjanAgentState("Drone", self.model_id, {"pose": (x, y),
                                                               "gesture_found": False})
