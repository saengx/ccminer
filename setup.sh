#!/bin/sh

pkg update -y
pkg install libjansson build-essential clang binutils python3 nano wget -y
pip3 install progress

chmod +x auto
chmod +x edit-miner
chmod +x run-miner
chmod +x add-file
chmod +x update
chmod +x down-grade
chmod +x ANSI_Shadow.flf
chmod +x backup
chmod +x restore
chmod +x install.txt
chmod +x bash.bashrc
pkg install figlet -y

mv auto /data/data/com.termux/files/usr/bin
mv miner /data/data/com.termux/files/usr/etc
mv edit-miner /data/data/com.termux/files/usr/bin
mv run-miner /data/data/com.termux/files/usr/bin
mv add-file /data/data/com.termux/files/usr/bin
mv update /data/data/com.termux/files/usr/bin
mv down-grade /data/data/com.termux/files/usr/bin
mv ANSI_Shadow.flf /data/data/com.termux/files/usr/share/figlet
mv backup /data/data/com.termux/files/usr/bin
mv restore /data/data/com.termux/files/usr/bin
mv install.txt /storage/emulated/0/download
mv cpuminer /data/data/com.termux/files/usr/bin
mv bash.bashrc /data/data/com.termux/files/usr/etc
run-miner


cd && cd /data/data/com.termux/files/usr/etc/miner/ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
CXX=clang++ CC=clang ./build.sh

chmod +x ccminer

#cd && cd /data/data/com.termux/files/usr/etc/miner/ccminer
#mv ccminer /data/data/com.termux/files/home/ccminer

run-miner
