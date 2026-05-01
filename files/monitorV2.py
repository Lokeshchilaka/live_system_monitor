import time

def get_cpu_usage():
    with open("/proc/stat", "r") as f:
        line1 = f.readline()

    values1 = list(map(int, line1.split()[1:]))
    idle1 = values1[3]
    total1 = sum(values1)

    time.sleep(1)

    with open("/proc/stat", "r") as f:
        line2 = f.readline()

    values2 = list(map(int, line2.split()[1:]))
    idle2 = values2[3]
    total2 = sum(values2)

    idle_delta = idle2 - idle1
    total_delta = total2 - total1

    cpu_usage = 100 * (1 - (idle_delta / total_delta))
    return cpu_usage


def get_memory_usage():
    mem_total = 0
    mem_available = 0

    with open("/proc/meminfo", "r") as f:
        for line in f:
            if "MemTotal" in line:
                mem_total = int(line.split()[1])
            elif "MemAvailable" in line:
                mem_available = int(line.split()[1])

    used = mem_total - mem_available
    usage_percent = (used / mem_total) * 100

    return usage_percent


# USER INPUT
runs = int(input("How many times do you want to monitor? "))
interval = int(input("Enter refresh interval (seconds): "))

print("\n===== SYSTEM MONITOR =====\n")

for i in range(runs):
    cpu = get_cpu_usage()
    mem = get_memory_usage()

    print(f"[{i+1}] CPU: {cpu:.2f}% | Memory: {mem:.2f}%")
