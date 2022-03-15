#!/bin/bash
cd /
var=$(fdisk -l | grep /dev/sda | grep Linux | cut -d ' ' -f1)
mount $var mnt/
cd mnt/
chroot . /usr/bin/sh << "EOT"
pwd
grep docker /proc/1/cgroup | wc -l
ps
EOT
cd ..