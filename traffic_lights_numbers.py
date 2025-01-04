# Traffic Lights Simulation: Skip divisible by 3, stop after 25
print("🚦 Traffic Lights Simulation: Processing numbers from 1 to 30")

# Iterate through the range of numbers from 1 to 30
for number in range(1, 31):
    # Yellow light: Skip numbers divisible by 3
    if number % 3 == 0:
        print(f"Yellow light for {number}: Skipping this number 🚧")
        continue
    
    # Red light: Stop the loop if the number is greater than 25
    if number > 25:
        print(f"Red light for {number}: Stopping the loop 🚨")
        break

    # Green light: Print the current number
    print(f"Green light for {number}: Proceed 🚗")
