# 🚀 System Resource Monitor (Project 2)

![System Monitor](assets/project2.png)

> 🧠 Observe • Analyze • Monitor  
> A Python-based system that reads **live Linux kernel data** from `/proc` and converts it into real-time CPU and Memory insights.

---

## 📌 Project Overview

Modern Linux systems expose internal system data through the `/proc` filesystem. Engineers use this data to:

- ⚙️ Monitor CPU performance  
- 📊 Analyze memory usage  
- 🧠 Understand system behavior  

This project simulates a **real-world system monitoring pipeline**, evolving across multiple versions.

---

## 🗂️ Project Structure

![Project Files](assets/files.png)

---

## 🔄 System Workflow

```
Linux Kernel (/proc)
        ↓
📥 Data Reading (file handling)
        ↓
🔍 Processing (CPU & Memory calculation)
        ↓
📊 Interpretation (usage %)
        ↓
🖥️ Output (terminal / live dashboard)
```

---

# 🧪 Version 1 — Raw System Data Access

![V1 Output](assets/v1.png)

### ⚙️ Features

- Reads CPU data from:
  ```bash
  /proc/stat
  ```
- Reads memory data from:
  ```bash
  /proc/meminfo
  ```
- Displays raw system values  

---

### 🧠 CPU Data Explanation

```
cpu 232363 505 39573 6541623 5753 0 723 0 0 0
```

- 👤 user → user processes  
- 🐢 nice → low priority processes  
- 🧩 system → kernel processes  
- 💤 idle → idle CPU time  
- 💽 iowait → waiting for I/O  
- ⚡ irq → hardware interrupts  
- 🔁 softirq → software interrupts  

👉 Values are **cumulative since boot**

---

### 🧠 Memory Data Explanation

```
MemTotal: 7753576 kB
MemFree: 2558164 kB
MemAvailable: 4495260 kB
Buffers: 123536 kB
Cached: 2488812 kB
```

- 📦 MemTotal → total RAM  
- 🆓 MemFree → unused RAM  
- 📊 MemAvailable → actual usable RAM  
- 💾 Buffers → disk buffer  
- ⚡ Cached → reusable memory  

---

### ❌ Limitations

- No calculations  
- No percentages  
- Raw output only  

---

# ⚙️ Version 2 — System Usage Calculation

![V2 Output](assets/v2.png)

### ⚙️ Features

- Calculates:
  - ⚡ CPU Usage (%)  
  - 📊 Memory Usage (%)  
- Uses time-based measurement  
- Displays structured output  

---

### 🧠 CPU Calculation Logic

```python
CPU % = 100 × (1 - idle_delta / total_delta)
```

- ⏱️ idle_delta → change in idle time  
- 🔢 total_delta → change in total CPU time  

---

### 🧠 Memory Calculation

```python
Used = MemTotal - MemAvailable
Usage % = (Used / MemTotal) × 100
```

---

### 📊 Example Output

```
CPU: 14.32%
Memory: 41.78%
```

---

### 🚀 Improvements

- 📊 Real system interpretation  
- ⚙️ Percentage-based output  

---

### ❌ Limitations

- Output stacking  
- No screen refresh  

---

# 🧠 Version 3 — Real-Time System Monitor

![V3 Output](assets/v3.png)

### ⚙️ Features

- 🔄 Continuous monitoring  
- 🧹 Clears terminal dynamically  
- 📊 Live CPU & Memory tracking  
- ⏱️ Real-time updates  

---

### 🖥️ Example Output

```
===== SYSTEM MONITOR =====

CPU Usage     : 18.45%
Memory Usage  : 42.10%

Press Ctrl + C to stop...
```

---

### 🧠 Internal Logic

```python
while True:
    read_cpu()
    read_memory()
    calculate_usage()
    clear_screen()
    print_output()
```

---

### 🚀 Improvements

- 🔄 Real-time behavior  
- 🧼 Clean UI  
- 📈 Continuous updates  

---

# 🎯 Key Learning Outcomes

- 🐧 Linux `/proc` filesystem  
- 🧠 Kernel-level data understanding  
- 🐍 Python system programming  
- 📊 CPU & memory computation  
- ⏱️ Time-based monitoring  

---

## ▶️ How to Run

```
python3 monitorV1.py
👉 [View Code](Files/monitorV1.py)

python3 monitorV2.py
👉 [View Code](Files/monitorV2.py)

python3 monitorV3.py
👉 [View Code](Files/monitorV3.py)
```

---

# 🔮 Future Improvements

- 📈 Process monitoring  
- 💾 Disk & network stats  
- 🎨 Colored UI (htop style)  
- 🖥️ GUI dashboard  

---

# 📌 Final Note

This project demonstrates a **progressive evolution from raw kernel data to a real-time monitoring system**, similar to real-world system tools.

---

## 👨‍💻 Author

**Lokesh Jaya Rao**
