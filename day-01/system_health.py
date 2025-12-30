import psutil

# define a function
def check_cpu_threshold():
    
    # Take threshold values form user input
    cpu_threshold = float(input("Enter the value of CPU threshold : "))
    disk_threshold = float(input("Enter the value of Disk threshold : "))
    memory_threshold = float(input("Enter the value of Memory threshold : "))
    print("\n")

    # fetches system metrics using a Python library (psutil)
    current_cpu_threshold = psutil.cpu_percent(interval=1)
    current_disk_threshold = psutil.disk_usage('/').percent
    current_memory_threshold = psutil.virtual_memory().percent
    
    # Compares metrics against thresholds
        # Compare CPU metrics
    if current_cpu_threshold > cpu_threshold:
        print(f"CPU usage is High {current_cpu_threshold} %")
    else:
        print(f"CPU usage is Noramal {current_cpu_threshold} %")
    
        # Compare Disk metrics
    if current_disk_threshold > disk_threshold:
        print(f"Disk usage is High {current_disk_threshold} %")
    else:
        print(f"Disk usage is Noramal {current_disk_threshold} %")
        
        # Compare Memory metrics
    if current_memory_threshold > memory_threshold:
        print(f"Memory usage is High {current_memory_threshold} %")
    else:
        print(f"Memory usage is Normal {current_memory_threshold} %")

check_cpu_threshold() # call a function 