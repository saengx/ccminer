
# CCMINER IN TERMUX

* แตะจอค้าง เลือก more
* เลือก Keep screen on

```
termux-setup-storage
```
* กดยอมรับ

```
pkg up -y && pkg upg -y
```
พิมพ์ N ในทุกการเรียกถาม
```
pkg install git -y
```

## การติดตั้งตามขั้นตอน
```
git clone https://github.com/saengx/ccminer && cd ccminer && chmod +x setup.sh setupdate.sh && ./setup.sh
```

# เพิ่มเติมการใช้โปรแกรม

## กรณีหากเป็น zergpool การใส่password ไม่ต้องใส่ ID=ชื่อ ระบบจะทำการaddใส่ให้อัตโนมัติ
* หากต้องการหยุดขุดให้ใช้กด ```CTRL + C```
* หากต้องการเปลี่ยน ชื่อเครื่องและจำนวนเทรด ใช้คำสั่ง ```edit-miner```
* หากต้องการเปิดขุด ใช้คำสั่ง ```run-miner```

* หากต้องการเปลี่ยนไฟล์ สำหรับเชื่อมต่อ ใช้คำสั่ง ```add-file```
# CCMINER-GITHUB
