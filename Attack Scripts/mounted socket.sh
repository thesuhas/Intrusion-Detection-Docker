#!/bin/bash
cd /
cd host/
chroot . /usr/bin/sh << "EOT"
pwd
grep docker /proc/1/cgroup | wc -l
ps
EOT
cd ..