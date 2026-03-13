def totalseconds=42*60+42
print (totalseconds)
miles=10/1.61
totalmiles=round(miles,2)
print (totalmiles)
pace_second=round(totalseconds/totalmiles,2)
pace_min=pace_second/60
pace_sec=pace_second%60
print(pace_min, pace_sec)
hour=totalseconds/3600
avg_mph=round(miles/hour,2)
print(avg_mph)