
def fcfs(processes):
    result = []
    time = 0

    for p in sorted(processes, key=lambda x: x["arrival"]):
        if time < p["arrival"]:
            time = p["arrival"]

        start = time
        time += p["burst"]

        result.append({
            "id": p["id"],
            "waiting": start - p["arrival"],
            "turnaround": time - p["arrival"],
            "response": start - p["arrival"]
        })

    return result


def sjf(processes):
    result = []
    remaining = processes[:]
    time = 0

    while remaining:
        available = [p for p in remaining if p["arrival"] <= time]

        if not available:
            time = min(p["arrival"] for p in remaining)
            continue

        p = min(available, key=lambda x: x["burst"])
        start = time
        time += p["burst"]

        result.append({
            "id": p["id"],
            "waiting": start - p["arrival"],
            "turnaround": time - p["arrival"],
            "response": start - p["arrival"]
        })

        remaining.remove(p)

    return result


def priority_scheduling(processes):
    result = []
    remaining = processes[:]
    time = 0

    while remaining:
        available = [p for p in remaining if p["arrival"] <= time]

        if not available:
            time = min(p["arrival"] for p in remaining)
            continue

        # Smaller priority number means higher priority
        p = min(available, key=lambda x: x["priority"])
        start = time
        time += p["burst"]

        result.append({
            "id": p["id"],
            "waiting": start - p["arrival"],
            "turnaround": time - p["arrival"],
            "response": start - p["arrival"]
        })

        remaining.remove(p)

    return result


def round_robin(processes, quantum):
    result = []
    remaining = {p["id"]: p["burst"] for p in processes}
    first_start = {}
    finish = {}
    time = 0
    queue = []
    arrived = sorted(processes, key=lambda x: x["arrival"])
    i = 0

    while i < len(arrived) or queue:
        if not queue and i < len(arrived):
            time = max(time, arrived[i]["arrival"])

        while i < len(arrived) and arrived[i]["arrival"] <= time:
            queue.append(arrived[i])
            i += 1

        if not queue:
            continue

        p = queue.pop(0)
        pid = p["id"]

        if pid not in first_start:
            first_start[pid] = time

        run_time = min(quantum, remaining[pid])
        time += run_time
        remaining[pid] -= run_time

        while i < len(arrived) and arrived[i]["arrival"] <= time:
            queue.append(arrived[i])
            i += 1

        if remaining[pid] > 0:
            queue.append(p)
        else:
            finish[pid] = time

    for p in processes:
        pid = p["id"]

        result.append({
            "id": pid,
            "waiting": finish[pid] - p["arrival"] - p["burst"],
            "turnaround": finish[pid] - p["arrival"],
            "response": first_start[pid] - p["arrival"]
        })

    return result
