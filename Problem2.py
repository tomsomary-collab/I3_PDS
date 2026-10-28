
total_second = 9875
hour = total_second // 3600 
minute = (total_second % 3600) // 60
seconds = (total_second % 3600) % 60 
print(hour ,"h", minute,"mn",seconds,"s")
print("Checkkkk:",(hour * 3600) + (minute * 60) +  seconds == total_second )