import time
import unittest

import numpy
import pomdp_py
import rdflib
from rdflib.plugins.sparql import CUSTOM_EVALS

import CustomSPARQLFunctions.math as custom_functions
import CustomSPARQLFunctions.semantic_fields as semantic_fields
from POMDPService.ajan_pomdp_planning.oopomdp.agent.agent import AjanAgent
from POMDPService.ajan_pomdp_planning.oopomdp.agent.belief import initialize_belief, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState, AjanAgentState
from POMDPService.ajan_pomdp_planning.oopomdp.env.env import AjanEnvironment

from POMDPService.ajan_pomdp_planning.oopomdp.models.observation_model import AjanObservationModel, \
    AjanOOObservationModel
from POMDPService.ajan_pomdp_planning.oopomdp.models.policy_model import AjanPolicyModel
from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel, AjanOOTransitionModel
from POMDPService.ajan_pomdp_planning.oopomdp.problem import AjanOOPOMDP, update_belief
from tests.test_models.alternate_models.python_observation_model import ObservationModel
from tests.test_models.alternate_models.python_policy_model import PolicyModel
from tests.test_models.alternate_models.python_reward_model import RewardModel
from tests.test_models.alternate_models.python_transition_model import TransitionModel
from tests.test_models.helpers.drone_agent_data import AGENT_DATA, ENV_DATA, RIGHT_KEYPOINT
from tests.test_models.helpers.drone_reward_model_queries import PROBABILITY_QUERY_D_R, ARGMAX_QUERY_D_R, \
    SAMPLE_QUERY_D_R, DATA_D_R
from tests.test_models.helpers.drone_transition_model_queries import DATA_D_T, SAMPLE_QUERY_D_T, ARGMAX_QUERY_D_T, \
    PROBABILITY_QUERY_D_T
from tests.test_models.helpers.observation_model_queries import (PROBABILITY_QUERY_OBS, DATA_OBS, SAMPLE_QUERY_OBS,
                                                                 ARGMAX_QUERY_OBS)
from tests.test_models.helpers.person_reward_model_queries import DATA_P_R, PROBABILITY_QUERY_P_R, SAMPLE_QUERY_P_R, \
    ARGMAX_QUERY_P_R
from tests.test_models.helpers.person_transition_model_queries import DATA_P_T, PROBABILITY_QUERY_P_T, SAMPLE_QUERY_P_T, \
    ARGMAX_QUERY_P_T
from tests.test_models.helpers.policy_model_queries import ROLLOUT_QUERY_POLICY, SAMPLE_QUERY_POLICY, \
    GET_ALL_ACTIONS_QUERY, DATA_POLICY, GET_ALL_ACTIONS_QUERY1, ROLLOUT_QUERY_POLICY1, SAMPLE_QUERY_POLICY1


def get_default_belief():
    left_person_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
    right_person_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
    none_person_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
    drone_state = AjanAgentState("Drone", 100, {"pose": (0, 0), "gesture_found": False})
    person = {left_person_state: 0.10, right_person_state: 0.85, none_person_state: 0.05}
    drone = {drone_state: 1.0}
    belief_states = {"Person": person, "Drone": drone}
    return initialize_belief(0, 100, {0: belief_states}, "histogram")


def get_observation(action):
    action: AjanAction = action
    if action.name == "perceive":
        return AjanObservation({"pose": RIGHT_KEYPOINT}, ["pose"])
    else:
        return AjanObservation({"pose": None}, ["pose"])


def print_config(problem):
    config_string = "Running with the following configuration:\n"
    config_string += "Agent: "
    config_string += "AjanRewardModel, " if isinstance(problem.agent.reward_model, AjanRewardModel) else "RewardModel, "
    config_string += "AjanPolicyModel, " if isinstance(problem.agent.policy_model, AjanPolicyModel) else "PolicyModel, "
    for model_id, model in problem.agent.observation_model.observation_models.items():
        config_string += "Drone: " if model_id == 100 else "Person: "
        config_string += "AjanObservationModel, " if isinstance(model, AjanObservationModel) else "ObservationModel, "
    for model_id, model in problem.agent.transition_model.transition_models.items():
        config_string += "Drone: " if model_id == 100 else "Person: "
        config_string += "AjanTransitionModel, " if isinstance(model, AjanTransitionModel) else "TransitionModel, "
    config_string += "\b\b\n"
    config_string += "Environment: "
    config_string += "AjanRewardModel, " if isinstance(problem.env.reward_model, AjanRewardModel) else "RewardModel, "
    config_string += "Transition Model: "
    for model_id, model in problem.env.transition_model.transition_models.items():
        config_string += "Drone: " if model_id == 100 else "Person: "
        config_string += "AjanTransitionModel, " if isinstance(model, AjanTransitionModel) else "TransitionModel, "
    config_string += "\b\b\n"
    print(config_string)


class TestSystemWorkflow(unittest.TestCase):
    rdflib.plugins.sparql.CUSTOM_EVALS["sample_values"] = custom_functions.sample_values
    rdflib.plugins.sparql.CUSTOM_EVALS["math_dist"] = custom_functions.distance
    rdflib.plugins.sparql.CUSTOM_EVALS["semantic_field_near"] = semantic_fields.near

    # region Agent models
    policy_model = AjanPolicyModel(DATA_POLICY, None, SAMPLE_QUERY_POLICY1, ROLLOUT_QUERY_POLICY1, GET_ALL_ACTIONS_QUERY1)
    # policy_model = PolicyModel()
    observation_model = AjanObservationModel(DATA_OBS, None, PROBABILITY_QUERY_OBS, SAMPLE_QUERY_OBS, ARGMAX_QUERY_OBS)
    # observation_model = ObservationModel(112)
    agent_drone_transition_model = AjanTransitionModel(100, DATA_D_T, None, PROBABILITY_QUERY_D_T, SAMPLE_QUERY_D_T,
                                                       ARGMAX_QUERY_D_T)
    agent_person_transition_model = AjanTransitionModel(112, DATA_P_T, None, PROBABILITY_QUERY_P_T, SAMPLE_QUERY_P_T,
                                                        ARGMAX_QUERY_P_T)
    # agent_drone_transition_model = TransitionModel("drone", 100)
    # agent_person_transition_model = TransitionModel("person", 112)

    drone_reward_model = AjanRewardModel(DATA_D_R, None, PROBABILITY_QUERY_D_R,
                                         SAMPLE_QUERY_D_R, ARGMAX_QUERY_D_R)
    # drone_reward_model = RewardModel(drone_id=100)

    agent_oo_transition_model = AjanOOTransitionModel({100: agent_drone_transition_model,
                                                       112: agent_person_transition_model})

    agent_oo_observation_model = AjanOOObservationModel({112: observation_model})
    init_belief = get_default_belief()
    # endregion

    agent = AjanAgent(100, AGENT_DATA, init_belief, policy_model, agent_oo_transition_model,
                      agent_oo_observation_model, drone_reward_model)

    # region Environment models
    person_reward_model = AjanRewardModel(DATA_P_R, None, PROBABILITY_QUERY_P_R, SAMPLE_QUERY_P_R, ARGMAX_QUERY_P_R)
    # person_reward_model = RewardModel(drone_id=100, person_id=112)
    env_drone_transition_model = AjanTransitionModel(100, DATA_D_T, None, PROBABILITY_QUERY_D_T, SAMPLE_QUERY_D_T,
                                                     ARGMAX_QUERY_D_T)
    env_person_transition_model = AjanTransitionModel(112, DATA_P_T, None, PROBABILITY_QUERY_P_T, SAMPLE_QUERY_P_T,
                                                      ARGMAX_QUERY_P_T)
    # env_drone_transition_model = TransitionModel("drone", 100)
    # env_person_transition_model = TransitionModel("person", 112)
    env_oo_transition_model = AjanOOTransitionModel({100: env_drone_transition_model,
                                                     112: env_person_transition_model})
    init_state = AjanOOState({100: AjanAgentState("Drone", 100, {"pose": (0, 0), "gesture_found": False}),
                              112: AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})})
    # endregion

    env = AjanEnvironment(ENV_DATA, init_state, env_oo_transition_model, person_reward_model)

    problem = AjanOOPOMDP("", "AjanPOMDPProblem", agent, env)

    planner = pomdp_py.POUCT(max_depth=10,
                             discount_factor=0.95,
                             planning_time=-1,
                             num_sims=-1,
                             exploration_const=1000,
                             rollout_policy=policy_model)
    _total_reward = 0

    def test_planner_run(self):
        print_config(self.problem)

        for i in range(10):
            _start = time.time()
            action = AjanAction("perceive")
            action = self.planner.plan(self.problem.agent)
            _time_used = time.time() - _start
            if action.attributes is not None:
                print("move " + str(action.attributes["motion"]) + " in " + str(_time_used) + " seconds")
            else:
                print(str(action) + " in " + str(_time_used) + " seconds")
            observation = get_observation(action)

            next_state = self.problem.env.get_next_state(action)
            # get updated position and then update the state
            pose_data = observation.attributes["pose"]
            if pose_data is not None:
                next_state.object_states[100].attributes["gesture_found"] = True
            reward = self.problem.env.reward_model.sample(self.problem.env.state, action, next_state)
            self.problem.env.apply_transition(next_state)

            self.problem.agent.clear_history()
            self.problem.agent.update_history(action, observation)
            update_belief(self.problem.agent, action, observation,
                          self.planner,
                          state_id=100,
                          next_agent_state=self.problem.env.state.object_states[100])
            self._total_reward += reward
            _time_used += time.time() - _start
            if self.problem.env.state.object_states[100].attributes["gesture_found"]:
                print("Gesture Found!!")


if __name__ == '__main__':
    unittest.main()
