import os, time

os.system("clear")

logo = """\x1b[1;38m                       
 Wisnusaputra 
"""

print logo
print "\x1b[1;33m\ntools ini digunakan untuk Transfer File Ke Hp"
time.sleep(2)
print "\x1b[1;31mSubscribe Channel Pembuat Script ini \n \x1b[1;36mDSV plankton"
print "github = https://github.com/wisnusaputra123/tools"
print "instagram =wisnu_as123"
time.sleep(5)
print "Whatsapp = 085718945758"
time.sleep(1)
nohp = raw_input("\x1b[1;33mJenis Hp Target : ")
time.sleep(3)
os.system("clear")
if  nohp.isalpha():

   print "tolong Masukkan Nama Hp Target"
   os.sys.exit()
   os.system("python2 perusak.py")
a = 1
def loop(a):
    for i in range(1000):
       	   print "\x1b[1;32m" + (str(a)) + " \x1b[1;33mFile Telah Dikirim ke " + "\x1b[1;34m" + nohp
    	   time.sleep(0.2)
    	   print "\x1b[1;31mMengirim File ke Target...."
    	   time.sleep(0.1)
    	   print "\x1b[1;34mFile Sedang Dikirim"
    	   time.sleep(0.2)
	   a += 1

if __name__ == '__main__':
    loop(a)

