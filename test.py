from GPS import locatie

i=0

#while i < 10:
#    print(locatie())
#    i+=1
#    continue

parsedlat = 52.089816
parsedlon = 5.227723

coor = string2latlon(parsedlat/100,parsedlon, 'd% %m% %S%')
Data = [ coor.to_string('D%')]

print(Data)