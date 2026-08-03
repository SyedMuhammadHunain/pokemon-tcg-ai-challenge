import json
from kaggle_environments import make
from src.agent import agent

def main():
    print("Initializing cabt environment...")
    env = make("cabt")
    
    print("Running match: Heuristic Agent vs Random Agent")
    try:
        steps = env.run([agent, "random"])
        print(f"Match completed successfully in {len(steps)} steps!")
        
        # Determine winner
        last_step = steps[-1]
        p1_status = last_step[0]["status"]
        p2_status = last_step[1]["status"]
        p1_reward = last_step[0]["reward"]
        p2_reward = last_step[1]["reward"]
        
        print("\n--- Match Results ---")
        print(f"Player 1 (Heuristic) Status: {p1_status}, Reward: {p1_reward}")
        print(f"Player 2 (Random)    Status: {p2_status}, Reward: {p2_reward}")
        
        if p1_reward is not None and p2_reward is not None:
            if p1_reward > p2_reward:
                print("🏆 Player 1 (Heuristic Agent) Wins!")
            elif p2_reward > p1_reward:
                print("🏆 Player 2 (Random Agent) Wins!")
            else:
                print("🤝 It's a Tie!")
                
    except Exception as e:
        print("Match crashed due to an error:")
        print(e)

if __name__ == "__main__":
    main()
