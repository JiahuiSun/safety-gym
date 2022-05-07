#!/usr/bin/env python

import argparse
import gym
import safety_gym  # noqa
import numpy as np  # noqa
import sys

def run_random(env_name):
    env = gym.make(env_name)

    weight = {}
    weight['buttons_cost'] = 0.6
    weight['gremlins_contact_cost'] = 1.2
    weight['hazards_cost'] = 1.2
    weight['reward_distance'] = 0.6
    weight['reward_goal'] = 1.4

    obs = env.reset()
    done = False
    ep_ret = 0
    ep_cost = 0
    while True:
        if done:
            print('Episode Return: %.3f \t Episode Cost: %.3f'%(ep_ret, ep_cost))
            ep_ret, ep_cost = 0, 0
            obs = env.reset()
        assert env.observation_space.contains(obs)
        act = env.action_space.sample()
        assert env.action_space.contains(act)
        obs, reward, done, info = env.step(act)
        
        print('reward', reward)
        print('cost', info.get('cost', 0))
        sys.exit(0)
        ep_ret += reward
        ep_cost += info.get('cost', 0)
        #env.render()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--env', default='Safexp-PointButton1-v0')
    args = parser.parse_args()
    run_random(args.env)
