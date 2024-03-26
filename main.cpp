#include <stdlib.h>
#include <stdio.h>
#include <iostream>

int main () {

	std::cout<<"Downloading Python3..." << std::endl;
	system("curl -O https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe");

	std::cout <<"Starting Python3 installation..."<<std::endl;
	system("python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1");
	std::cout <<"Python3 installation complete"<<std::endl;

	system("python3 opn_install.py");

	return 0;
}
