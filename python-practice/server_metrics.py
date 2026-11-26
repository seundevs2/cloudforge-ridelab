total_disk = 100
used_disk = 65

available_disk = total_disk - used_disk
usage_percentage = (used_disk / total_disk) * 100

print("Total Disk:", total_disk, "GB")
print("Used Disk:", used_disk, "GB")
print("Available Disk:", available_disk, "GB")
print("Disk Usage:", usage_percentage, "%")
