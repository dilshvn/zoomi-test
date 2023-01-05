fps = 60 #example fps
sys_time = system_time()
nano_seconds_interval = 3 #exampls ns_interval
prev_ftime = 
new_ftime = 

delay_ns(nano_seconds_interval)

while True:
    img = generate_image() #assumed this function is given
    send_image(img)

