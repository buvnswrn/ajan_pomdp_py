import pomdp_py


class RewardModel(pomdp_py.RewardModel):
    def __init__(self, big=1000, small=1, drone_id=None, person_id=None):
        self._drone_id = drone_id
        self.big = big
        self.small = small
        self.person_id = person_id

    def probability(self, reward, state, action, next_state):
        if reward == self.__reward_func(state, action, next_state):
            return 1.0
        else:
            return 0.0

    def sample(self, state, action, next_state):
        return self.__reward_func(state, action, next_state)

    def argmax(self, state, action, next_state):
        return self.__reward_func(state, action, next_state)

    def __reward_func(self, state, action, next_state):
        reward = 0
        drone_state = state.object_states[self._drone_id]
        drone_next_state = next_state.object_states[self._drone_id]
        if action.name == "perceive":
            if drone_state.attributes["gesture_found"] and drone_next_state.attributes["gesture_found"]:
                return 0
            if (not drone_state.attributes["gesture_found"]) and drone_next_state.attributes["gesture_found"]:
                reward += self.big
        if self.person_id is not None:
            person_state = state.object_states[self.person_id]
            person_next_state = next_state.object_states[self.person_id]
            if person_state.attributes["gesture"] == person_next_state.attributes["gesture"]:
                if action.name == "move":
                    if person_state.attributes["gesture"] is not None:
                        if person_state.attributes["gesture"] == 'left' and action.attributes["motion"] == "left":
                            reward += self.big
                        elif person_state.attributes["gesture"] == 'right' and action.attributes["motion"] == "right":
                            reward += self.big
                    else:
                        reward -= self.big
        return reward
