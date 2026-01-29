class Environment:
    def __init__(self):
        # Three rooms (A, B, C) all start Dirty
        self.rooms = {'A': 'Dirty', 'B': 'Dirty', 'C': 'Dirty'}
        self.agent_location = 'A'
        self.cleaned_rooms = 0

    def get_percept(self):
        return self.agent_location, self.rooms[self.agent_location]

    def execute_action(self, action):
        if action == 'Vacuum':
            if self.rooms[self.agent_location] == 'Dirty':
                self.rooms[self.agent_location] = 'Clean'
                self.cleaned_rooms += 1
        elif action == 'Right':
            if self.agent_location == 'A':
                self.agent_location = 'B'
            elif self.agent_location == 'B':
                self.agent_location = 'C'
        elif action == 'Left':
            if self.agent_location == 'C':
                self.agent_location = 'B'
            elif self.agent_location == 'B':
                self.agent_location = 'A'

    def all_clean(self):
        return all(state == 'Clean' for state in self.rooms.values())


class SimpleReflexAgent:
    def __init__(self):
        self.rules = {
            ('A', 'Dirty'): 'Vacuum',
            ('B', 'Dirty'): 'Vacuum',
            ('C', 'Dirty'): 'Vacuum',
            ('A', 'Clean'): 'Right',
            ('B', 'Clean'): 'Left',
            ('C', 'Clean'): 'Left'
        }

    def select_action(self, percept):
        return self.rules.get(percept, 'NoOp')


# === Simulation ===
env = Environment()
agent = SimpleReflexAgent()
steps_log = []

print("=== Vacuum Cleaner Simulation ===\n")
print(f"Initial rooms: {env.rooms}")
print(f"Agent starting location: {env.agent_location}\n")

for step in range(1, 6):
    location, status = env.get_percept()
    action = agent.select_action((location, status))
    env.execute_action(action)
    result = ""

    # Describe what happened
    if action == 'Vacuum':
        result = f"Room {location} becomes Clean"
    elif action == 'Right':
        result = f"Agent moves to the next room on the right ({env.agent_location})"
    elif action == 'Left':
        result = f"Agent moves to the next room on the left ({env.agent_location})"
    else:
        result = "No operation performed"

    steps_log.append((step, location, status, action, result))

    # Print step summary
    print(f"Step {step}:")
    print(f"• Percept = ({location!r}, {status!r}) → Action = {action!r}")
    print(f"• Result: {result}\n")

print("=== Final Room States ===")
print(env.rooms)
print("\n=== Simulation Summary ===")
print("Code Walkthrough:")
print("• Environment represents the rooms and dirt status.")
print("• SimpleReflexAgent uses condition-action rules.")
print("• The simulation runs for 5 steps.\n")
print("Let’s say this is the situation at the start:")
print("• Room A: Dirty\n• Room B: Dirty\n• Agent is in Room A\n")

for step, loc, stat, act, result in steps_log:
    print(f"Step {step}:")
    print(f"• Percept = ('{loc}', '{stat}') → Action = '{act}'")
    print(f"• Result: {result}\n")
