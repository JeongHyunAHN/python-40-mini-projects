import psutil as ps
import time

currSent = 0
currRecv = 0

prevSent = 0
prevRecv = 0

while True:
    # cpu_p = ps.cpu_percent(interval=1)
    # print(f"CPU Usage : {cpu_p}%")
    
    # mem = ps.virtual_memory()
    # mem_avail = round(mem.available/1024**3,1)
    # print(f"Available Memory : {mem_avail}GB")

    t = time.localtime()
    currTime = time.strftime("%M:%S",t)
    
    net = ps.net_io_counters()
    currRecv = net.bytes_recv/1024**2
    currSent = net.bytes_sent/1024**2
    
    sent = round(currRecv-prevRecv,1)
    recv = round(currSent-prevSent,1)
    
    print(f"{currTime} - Sent : {sent}MB, Received : {recv}MB")
    
    prevSent = currSent
    prevRecv = currRecv
    
    time.sleep(1)