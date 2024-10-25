import psutil
import time
import matplotlib.pyplot as plt

# Data lists for plotting
cpu_data = []
memory_data = []
disk_data = []
time_data = []

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return disk_info.percent

def plot_data():
    plt.figure(figsize=(10, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(time_data, cpu_data, label="CPU Usage (%)", color='r')
    plt.ylabel('CPU (%)')
    
    plt.subplot(3, 1, 2)
    plt.plot(time_data, memory_data, label="Memory Usage (%)", color='b')
    plt.ylabel('Memory (%)')

    plt.subplot(3, 1, 3)
    plt.plot(time_data, disk_data, label="Disk Usage (%)", color='g')
    plt.ylabel('Disk (%)')
    plt.xlabel('Time (s)')

    plt.tight_layout()
    plt.show()

def collect_performance_data():
    start_time = time.time()
    
    while True:
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        disk = get_disk_usage()

        # Append data for plotting
        current_time = time.time() - start_time
        time_data.append(current_time)
        cpu_data.append(cpu)
        memory_data.append(memory)
        disk_data.append(disk)

        # Print data to console
        print(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

        # Plot after collecting 10 data points
        if len(cpu_data) >= 10:
            plot_data()
            break

        time.sleep(5)

if __name__ == "__main__":
    collect_performance_data()
