Vagrant.configure("2") do |config|
  config.vm.box = "debian/contrib-jessie64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end

  config.vm.define "manager" do |manager|
    manager.vm.synced_folder ".", "/home/vagrant/ansible"
    manager.vm.host_name = "manager.local"
    manager.vm.network "private_network", ip: "192.168.1.101"
  end

  config.vm.define "db0" do |app0|
    test0.vm.host_name = "db0.local"
    test0.vm.network "private_network", ip: "192.168.1.110"
  end

  config.vm.define "app0" do |app0|
    test0.vm.host_name = "app0.local"
    test0.vm.network "private_network", ip: "192.168.1.120"
  end

  config.vm.define "app1" do |app1|
    test0.vm.host_name = "app1.local"
    test0.vm.network "private_network", ip: "192.168.1.121"
  end
end
