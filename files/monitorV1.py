# CPU + MEMORY MONITOR (BASIC)

# read CPU info
with open("/proc/stat", "r") as f:
    cpu_line = f.readline()

# read memory info
with open("/proc/meminfo", "r") as f:
    mem_lines = f.readlines()

print("===== SYSTEM MONITOR =====\n")

print("CPU RAW DATA:")
print(cpu_line)

print("\nMEMORY RAW DATA:")
print(mem_lines[:5])
