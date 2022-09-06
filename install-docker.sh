echo 'Uninstall any older versions of Docker'
echo 'It is okay if this command fails and reports that none of these packages are installed'
echo ''
sleep 2
sudo apt-get remove docker docker-engine docker.io containerd runc
echo ''

echo 'Begin install docker'
echo ''
sudo apt-get update -y
echo ''

echo 'Installing necessary prerequisite packages'
echo ''
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
echo ''

echo "Adding Docker's official GPG key"
echo ''
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo ''

echo 'Setting up the stable repository'
echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
echo ''

echo 'Installing docker engine'
echo ''
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
echo ''

if [ ! -f /usr/bin/docker ]; then
    echo 'Docker installation failed'
    exit 1
fi

echo 'Installing docker-compose'
echo ''
sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo 'Docker-compose installation succeeded'
echo ''
echo 'Docker installation complete'
echo ''
echo 'Managing to run Docker as a non-root user'
echo ''
sudo groupadd docker
sudo usermod -aG docker $USER
echo ''

sleep 1
echo ''
echo 'Restart your VM/system to enable Docker being run as non-root user'
echo 'Do you want to restart now? [y/n]'
read answer
if [ "$answer" = "y" ]; then
    echo 'Restarting VM'
    sudo reboot
else 
    echo 'OK, do not forget to restart later'
    exit 1
fi