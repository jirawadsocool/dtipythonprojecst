#แสดงข้อมูลหลายๆ ประเภทใน pritn เดียว

#1. ใฃ้ , โดยที่จะมี space ในแต้ละ ,
print("SAU",5555,123,456,True,10+50)

#2. ใช้ + มีข้อแม้ ข้อมูลที่ไม่ใฃ้ String ต้องแปลงเป็น sting และไม่มี space ให้เหมือนกับ 
print("SAU"+str(555)+' '+str(123.456)+' '+str(True)+ ' '+str(10+50))

#3. ใช้เมธอดชื่อ format
print("SAU {} {} {} {}".format(555,123.465, True, 10+50))
print("SAU {} {} {} {}".format(555,123.465, True, 10+50))

#4. ใฃ้ f-string ****
print(f'SAU {5555} {123.456} {True} {10+50}')

#--------------
#กรณี 1 บรรทัดมีหลาย Statment ให้คั่นด้วย ;
print('aaa'); print(111); print(False)