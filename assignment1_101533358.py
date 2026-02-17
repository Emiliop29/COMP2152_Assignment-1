"""
Author: Barron Carlos
Assignment: #1
"""

# Step b: Create 4 variables (with type comments to the right)
gym_member = "Alex Alliton"          # str
preferred_weight_kg = 20.5           # float
highest_reps = 25                    # int
membership_active = True             # bool

# Step c: Create a dictionary named workout_stats
# keys: friend names (str)
# values: tuple of 3 ints (yoga, running, weightlifting minutes)
workout_stats = {
    "Alex": (30, 45, 40),
    "Jamie": (25, 35, 50),
    "Taylor": (40, 30, 20),
    "Morgan": (20, 55, 35)
}

# Step d: Add total workout minutes for each friend into the same dictionary
friends = list(workout_stats.keys())

for name in friends:
    yoga, running, weightlifting = workout_stats[name]
    total_minutes = yoga + running + weightlifting
    workout_stats[f"{name}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list (rows=friends, cols=activities)
workout_list = [list(workout_stats[name]) for name in friends]  # list[list[int]]

print("Workout data (workout_list):")
for i, name in enumerate(friends):
    print(f"  {name}: {workout_list[i]}  (yoga, running, weightlifting)")

# Step f: Use slicing to extract
# f(i) Yoga and running for all friends
yoga_running_all = [row[:2] for row in workout_list]
print("\nYoga and Running minutes for all friends:")
for i, name in enumerate(friends):
    print(f"  {name}: yoga={yoga_running_all[i][0]}, running={yoga_running_all[i][1]}")

# f(ii) Weightlifting for last two friends
last_two_names = friends[-2:]
last_two_weightlifting = [row[2] for row in workout_list[-2:]]
print("\nWeightlifting minutes for the last two friends:")
for i, name in enumerate(last_two_names):
    print(f"  {name}: weightlifting={last_two_weightlifting[i]}")

# Step g: If-statement in a loop for friends whose totals meet/exceed 120 minutes
print("\nFriends with total workout minutes >= 120:")
for name in friends:
    total = workout_stats[f"{name}_Total"]
    if total >= 120:
        print(f"Great job staying active, {name}!")

# Step h: Input prompt to look up a friend's workout stats
user_friend = input("\nEnter a friend's name to look up: ").strip()
user_key = user_friend.title()

if user_key in friends:
    yoga, running, weightlifting = workout_stats[user_key]
    total = workout_stats[f"{user_key}_Total"]

    print(f"\n{user_key}'s workout minutes:")
    print(f"  Yoga: {yoga}")
    print(f"  Running: {running}")
    print(f"  Weightlifting: {weightlifting}")
    print(f"  Total: {total}")
else:
    print(f"Friend {user_friend} not found in the records.")

# Step i: Highest and lowest total workout minutes
totals = {name: workout_stats[f"{name}_Total"] for name in friends}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("\nSummary:")
print(f"Highest total workout minutes: {highest_friend} with {totals[highest_friend]}")
print(f"Lowest total workout minutes: {lowest_friend} with {totals[lowest_friend]}")
