import time
import os

def get_cpu_usage():
    with open("/proc/stat", "r") as f:
        line1 = f.readline()

    values1 = list(map(int, line1.split()[1:]))
    idle1 = values1[3]
    total1 = sum(values1)

    time.sleep(0.5)

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
interval = int(input("Enter refresh interval (seconds): "))

while True:
    cpu = get_cpu_usage()
    mem = get_memory_usage()

    # CLEAR SCREEN
    os.system("clear")

    print("===== LIVE SYSTEM MONITOR =====\n")

    print(f"CPU Usage     : {cpu:.2f}%")
    print(f"Memory Usage  : {mem:.2f}%")

    print("\nPress Ctrl + C to stop...")

    time.sleep(interval)
