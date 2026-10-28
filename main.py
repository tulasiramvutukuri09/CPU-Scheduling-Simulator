
import scheduler

processes = []

n = int(input("Enter number of processes: "))

for i in range(n):
    print("\nProcess", i + 1)

    arrival = int(input("Arrival time: "))
    burst = int(input("Burst time: "))
    priority = int(input("Priority (smaller number = higher priority): "))

    processes.append({
        "id": "P" + str(i + 1),
        "arrival": arrival,
        "burst": burst,
        "priority": priority
    })

while True:
    print("\n--- CPU Scheduling Simulator ---")
    print("1. FCFS")
    print("2. SJF")
    print("3. Priority Scheduling")
    print("4. Round Robin")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        results = scheduler.fcfs(processes)
        name = "FCFS"

    elif choice == "2":
        results = scheduler.sjf(processes)
        name = "SJF"

    elif choice == "3":
        results = scheduler.priority_scheduling(processes)
        name = "Priority Scheduling"

    elif choice == "4":
        quantum = int(input("Enter time quantum: "))

        if quantum <= 0:
            print("Time quantum must be positive.")
            continue

        results = scheduler.round_robin(processes, quantum)
        name = "Round Robin"

    elif choice == "5":
        print("Exiting simulator.")
        break

    else:
        print("Invalid choice. Try again.")
        continue

    print("\nAlgorithm:", name)
    print("\nProcess | Waiting | Turnaround | Response")
    print("-----------------------------------------")

    total_waiting = 0
    total_turnaround = 0
    total_response = 0

    for r in results:
        print(
            r["id"], "|",
            r["waiting"], "|",
            r["turnaround"], "|",
            r["response"]
        )

        total_waiting += r["waiting"]
        total_turnaround += r["turnaround"]
        total_response += r["response"]

    print("\nAverage Waiting Time:", round(total_waiting / n, 2))
    print("Average Turnaround Time:", round(total_turnaround / n, 2))
    print("Average Response Time:", round(total_response / n, 2))
