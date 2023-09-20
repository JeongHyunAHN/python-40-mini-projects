import psutil as ps

cpuCore = ps.cpu_count(logical=False)
print(cpuCore)

memory = ps.virtual_memory()
print("메모리 정보 : \n")
print(memory)
memoryTotal = round(memory.total / 1024**3) # 세제곱
print(f'메모리 : {memoryTotal}GB')

disk = ps.disk_partitions()
print("디스크 정보 : \n")
print(disk)
for p in disk:
    print(p.mountpoint, p.fstype, end = " ")
    du = ps.disk_usage(p.mountpoint)
    diskTotal = round(du.total / 1024**3)
    print(f"디스크 크기 : {diskTotal}GB")

net = ps.net_io_counters()
print("네트워크를 통해 보내고 받은 데이터량 : \n")
print(net)
sent = round(net.bytes_sent / 1024**2, 1)
recv = round(net.bytes_recv / 1024**2, 1)
print(f"보내기 : {sent}MB, 받기 : {recv}MB")