sleep 1
echo 'Trusting the Draios GPG key, configuring the apt repository, and updating the package list'
echo ''
sleep 1
curl -s https://s3.amazonaws.com/download.draios.com/DRAIOS-GPG-KEY.public | gpg --dearmor | sudo tee /usr/share/keyrings/sysdig.gpg
sudo curl -s -o /etc/apt/sources.list.d/draios.list https://s3.amazonaws.com/download.draios.com/stable/deb/draios.list  
sudo apt-get update -y
echo ''

echo 'Installing the kernel headers'
echo ''
sleep 1
sudo apt-get -y install linux-headers-$(uname -r)
echo ''

echo 'Installing sysdig'
echo ''
sleep 1
sudo apt-get -y install sysdig
echo ''

echo 'Installing libssl1.0.0'
echo ''
sleep 1
sudo sh -c 'cat xenial-source.txt >> /etc/apt/sources.list'
sudo apt-get update -y
sudo apt install libssl1.0.0 -y
echo ''

echo 'Installing lua socket module'
echo ''
sleep 1
sudo apt install luarocks -y
sudo luarocks install luasocket
echo ''

echo 'fin.'
echo ''
sleep 3