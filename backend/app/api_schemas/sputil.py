import psutil

# Découvrons la structure exacte
memory = psutil.virtual_memory()
print("Type memory:", type(memory))
print("Attributs memory:", dir(memory))
print("memory.percent:", memory.percent, type(memory.percent))

disk = psutil.disk_usage('.')
print("Type disk:", type(disk))
print("disk.percent:", disk.percent, type(disk.percent))

cpu = psutil.cpu_percent(interval=1)
print("Type CPU:", type(cpu))
print("CPU value:", cpu)