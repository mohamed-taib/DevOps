Vagrant.configure("2") do |config|
  config.vm.define"MicroService1" do |microservice|
    microservice.vm.box = "ubuntu/focal64"
    microservice.vm.box_check_update = false
    microservice.vm.network "private_network", ip: "192.168.33.10"
    microservice.vm.network "forwarded_port",guest:5000,host:5000
    microservice.vm.synced_folder "./post_service", "/home/vagrant/microservice1"
    microservice.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y python3 python3-pip
      pip install flask flask-sqlalchemy
    SHELL
    microservice.vm.hostname="microservice1"
  end
  config.vm.define"MicroService2" do |microservice|
    microservice.vm.box = "ubuntu/focal64"
    microservice.vm.box_check_update = false
    microservice.vm.network "private_network", ip: "192.168.33.11"
    microservice.vm.network "forwarded_port",guest:5001,host:5001
    microservice.vm.synced_folder "./user_service", "/home/vagrant/microservice2"
    microservice.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y python3 python3-pip
      pip install flask flask-sqlalchemy
    SHELL
    microservice.vm.hostname="microservice2"
  end
  
end
