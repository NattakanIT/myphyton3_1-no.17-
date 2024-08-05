def circle(radius):
    area = 22/7*(radius*radius)
    #print("พื้นที่วงกลม %.3f" % area)
    return area
R = int(input("รัศมี:"))
print("พื้นที่วงกลม %.3f" % circle(R))

    