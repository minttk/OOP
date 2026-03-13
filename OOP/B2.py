import math
def volume_of_a_sphere(r):
    return round((4/3)*math.pi*r**3,2)
print(volume_of_a_sphere(5))
def total_cost(price,discount,copies):
    book_price=price*(1-discount)
    ship_price=3+(copies-1)*(0.75)
    return book_price*copies + ship_price
print(total_cost(24.95,0.4,60))
def time_to_get_home(start_hour,start_minute):
    start_second=start_hour*3600+start_minute*60
    run_time=2*(8*60+15)+3*(7*60+12)
    total=start_second+run_time
    hour=total//3600
    minute=(total%3600)//60
    return hour,minute
a,b=time_to_get_home(6,52)
print(a,":",b)
    
