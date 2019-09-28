<?php ?><?php
if (strtolower(substr(PHP_OS, 0, 3)) == "win") {
    $bersih = "cls";
} else {
    $bersih = "clear";
}
date_default_timezone_set('Asia/Jakarta');
$date = date('d-M-Y H:i:s');
$green = "\e[92m";
$red = "\e[91m";
$yellow = "\e[93m";
$blue = "\e[36m";
$cyan = "\e[0;36m";
$purple = "\e[0;35m";
$brown = "\e[0;33m";
$lightgray = "\e[0;37m";
$darkgray = "\e[1;30m";
$lightblue = "\e[1;34m";
$lightgreen = "\e[1;32m";
$lightcyan = "\e[1;36m";
$lightred = "\e[1;31m";
$lightpurple = "\e[1;35m";
pilih:
    system($bersih);
    echo "
$lightgreen __      _(_)___ _ __  _   _
$lightgreen \ \ /\ / / / __| '_ \| | | | $lightred Hacker
$lightgreen  \ V  V /| \__ \ | | | |_| |
$lightgreen   \_/\_/ |_|___/_| |_|\__,_|";
    echo "

$purple Author  : wisnu saputra
$yellow Type    : quotes
$brown Github  : http://github.com/wisnusaputra123
$blue Fanspage : https://facebook.com/wisnu.saputra
$red Instagram : https://instagram.com/wisnu_as123
$purple Version : 1.0
$lightgray Date    : $date
";
    echo " 
";
    @header('Content-Type: text/html; charset=UTF-8');
    function input($echo) {
        echo "$echo : ";
    }
    echo " $red sedang masuk ke server";
    echo "$green _";
    sleep(1.5);
    echo "__";
    sleep(1.5);
    echo "___";
    sleep(1.5);
    echo "____";
    sleep(1.5);
    echo "_____";
    sleep(1.5);
    echo "______";
    sleep(1.5);
    echo "______";
    sleep(1.5);
    echo "________";
    sleep(1.5);
    echo "_________";
    sleep(1.5);
    echo "__________
";
    sleep(2);
    echo " 
";
    input("$yellow Yakin Ingin Pakai Script Ini ? $green [y/n]");
    $pilih = trim(fgets(STDIN));
    echo "
";
    if ($pilih == "n") {
        die("$red (!) See You $red (!)
");
    } elseif ($pilih == "y") {
        echo "$red PERINGATAN :$green ini hanya hiburan semata
";
        echo "$brown gak suka tinggal ketik exit
";
echo "$darkgray Sumber Script https://github.com/wisnusaputra123
";

   echo " $red Kumpulan Kata Kata Bijak Jaman Now";
   sleep(5.1);
  echo " ___________________________________________


";

  echo " $yellow 1.Mohon Maaf Script Belum Selesai


";

        sleep(1);
        echo "$red terima kasih";
        sleep(1.5);
        echo "
";
    }
?>
