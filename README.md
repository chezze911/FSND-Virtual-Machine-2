udacity-fullstack
=============

Item Catalog Project


VirtualBox

VirtualBox is the software that actually runs the VM. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

Ubuntu 14.04 Note: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from vagrantup.com. Install the version for your operating system.

Windows Note: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

Fetch the Source Code and VM Configuration

Windows: Use the Git Bash program (installed with Git) to get a Unix-style terminal.
Other systems: Use your favorite terminal program.

From the terminal, run:

git clone https://github.com/chezze911/FSND-Virtual-Machine-2
This will give you a directory named catalog complete with the source code for the flask application, a vagrantfile, and a bootstrap.sh file for installing all of the necessary tools.

Run the virtual machine!

Using the terminal, change directory to vagrant (cd vagrant) from within the FSND-Virtual-Machine-2 directory, then type vagrant up to launch your virtual machine.

Running the Item Catalog App

Once it is up and running, type vagrant ssh. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt. To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.

Now that you have Vagrant up and running type vagrant ssh to log into your VM. change to the /vagrant directory by typing cd /vagrant/catalog. This will take you to the shared folder between your virtual machine and host machine.

Type ls to ensure that you are inside the directory that contains catalog_project.py, catalog_database_setup.py, and two directories named 'templates' and 'static'

Now type python catalog_database_setup.py to initialize the database.

Type python catalog_lotsofmenus.py to populate the database with catalogs and items. (Optional)

Type python catalog_project.py to run the Flask web server. In your browser visit http://localhost:5000 to view the catalog items app. You should be able to view, add, edit, and delete items and catalogs.
