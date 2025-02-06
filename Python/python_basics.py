price_list = [100,90,70,110,120,60,200,95,135]
gst = 0.17
new_price_list = []
for i in price_list:
    if(i>100):
        new_price_list.append(i+(gst*i))
    else:
        new_price_list.append(i)
print(new_price_list)            