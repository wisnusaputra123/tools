import os, time

os.system("clear")

logo = """\x1b[1;38m
 ____                           _ 
|  _ \ ___ _ __ _   _ ___  __ _| | __ 
| |_) / _ \ '__| | | / __|/ _` | |/ / 
|  __/  __/ |  | |_| \__ \ (_| |   < 
|_|   \___|_|   \__,_|___/\__,_|_|\_\ Wisnusaputra123 
"""

print logo
print "\x1b[1;33m\ntools ini digunakan untuk merusak hp korban"
time.sleep(2)
print "\x1b[1;31mSubscribe Channel Pembuat Script ini \n \x1b[1;36mBlum buat asw"
print "github = https://github.com/MrTaufik909/perusakhp"
print "youtube =Blom Buat asw"
time.sleep(5)
print "Whatsapp = 082215060250"
time.sleep(1)
nohp = raw_input("\x1b[1;33mNomor Hp Korban : ")
time.sleep(3)
os.system("clear")
if  nohp.isalpha():

   print "tolong masukkan nomor telepon"
   os.sys.exit()
   os.system("python2 perusak.py")
a = 1
def loop(a):
    for i in range(1000000):
       	   print "\x1b[1;32m" + (str(a)) + " \x1b[1;33mVirus Berbahaya Telah Dikirim ke " + "\x1b[1;34m" + nohp
    	   time.sleep(0.2)
    	   print "\x1b[1;31mMerusak hp korban...."
    	   time.sleep(0.1)
    	   print "\x1b[1;34mSubscribe Blom Buat asw"
    	   time.sleep(0.2)
	   a += 1

if __name__ == '__main__':
    loop(a)

