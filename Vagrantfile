Vagrant.configure("2") do |config|
  config.vm.box = "debian/contrib-jessie64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end

  config.vm.define "manager" do |manager|
    manager.vm.synced_folder ".", "/home/vagrant/ansible"
    manager.vm.host_name = "manager.local"
    manager.vm.network "private_network", ip: "192.168.11.101"
  end

  config.vm.define "db0" do |db0|
    db0.vm.host_name = "db0.local"
    db0.vm.network "private_network", ip: "192.168.11.110"
  end

  config.vm.define "app0" do |app0|
    app0.vm.host_name = "app0.local"
    app0.vm.network "private_network", ip: "192.168.11.120"
  end

  config.vm.define "app1" do |app1|
    app1.vm.host_name = "app1.local"
    app1.vm.network "private_network", ip: "192.168.11.121"
  end

  config.vm.define "memcache0" do |memcache0|
    memcache0.vm.host_name = "memcache0.local"
    memcache0.vm.network "private_network", ip: "192.168.11.130"
  end
end
