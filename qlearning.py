import numpy as np
import matplotlib.pyplot as plt

# Define the Q-learning function
def q_learning(num_states, num_actions, alpha, gamma, num_episodes, max_steps):
    Q = np.zeros((num_states, num_actions))
    episode_rewards = []
    for i in range(num_episodes):
        state = np.random.randint(num_states)
        episode_reward = 0
        for j in range(max_steps):
            action = np.argmax(Q[state, :] + np.random.randn(1, num_actions) / (i + 1))
            next_state = np.random.randint(num_states)
            reward = -1 if next_state != num_states - 1 else 0
            Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])
            episode_reward += reward
            state = next_state
            if state == num_states - 1:
                break
        episode_rewards.append(episode_reward)
    return Q, episode_rewards

# Get user-defined input
num_states = int(input("Enter the number of states: "))
num_actions = int(input("Enter the number of actions: "))
alpha = float(input("Enter the learning rate (alpha): "))
gamma = float(input("Enter the discount factor (gamma): "))
num_episodes = int(input("Enter the number of episodes: "))
max_steps = int(input("Enter the maximum number of steps per episode: "))

# Run the Q-learning algorithm
Q, episode_rewards = q_learning(num_states, num_actions, alpha, gamma, num_episodes, max_steps)

# Plot the episode rewards
plt.plot(range(num_episodes), episode_rewards)
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Q-learning Rewards")
plt.show()



OUTPUT:
    Enter the number of states: 3
Enter the number of actions: 4
Enter the learning rate (alpha): 0.1
Enter the discount factor (gamma): 0.2
Enter the number of episodes: 1000
Enter the maximum number of steps per episode: 100
