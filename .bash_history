rpmdev-setuptree
ls
ls -la
cd rpmbuild/
ls
pwd
cd /home/
ls
cd vlad/
ls
cd ~
ls
cd /
ls
cd /home/rpmbuild/
ls
cd rpmbuild/
ls
cp /etc/squid_redirector/squid_redirector.py SOURCES/
cp /etc/squid_redirector/squid_redirector.json SOURCES/
ls So
ls SOURCES/
ls /etc/squid_redirector/
cp /etc/rsyslog.d/squid-redirector.conf SOURCES/
cp /etc/logrotate.d/squid-redirector SOURCES/
vim SPECS/squid-redirector.spec
rpmbuild -bb SPECS/squid-redirector.spec 
ls /var/tmp/rpm-tmp.S0pL0Z 
ls -la /var/tmp/rpm-tmp.S0pL0Z 
ls
tar -cvf SPECS/ squid-redirector.tar.bz2
mkdir -p SOURCES
ls
cp /etc/squid_redirector/squid_redirector.py SOURCES/
cp /etc/squid_redirector/squid_redirector.json SOURCES/
cp /etc/rsyslog.d/squid-redirector.conf SOURCES/
cp /etc/logrotate.d/squid-redirector SOURCES/
tar -czf squid-redirector.tar.bz2 SOURCES/*
ls
rm SOURCES/*
ls SOURCES/
mv squid-redirector.tar.bz2 SOURCES/
ls
ls SOURCES/
tar -xvf SOURCES/squid-redirector.tar.bz2 -c temp
mkdir temp
tar -xvf SOURCES/squid-redirector.tar.bz2 -c temp
tar -xvf SOURCES/squid-redirector.tar.bz2 -C temp
ls temp/
rm -rf temp/
ls SOURCES/
vim SPECS/squid-redirector.spec 
mkdir temp
cd temp/
ls
cd ..
cp /etc/squid_redirector/squid_redirector.py temp/
cp /etc/squid_redirector/squid_redirector.json temp/
cp /etc/rsyslog.d/squid-redirector.conf temp
cp /etc/logrotate.d/squid-redirector temp
cd temp/
ls
tar cvf * squid-redirector.tar.bz2
ls
ls -la
cat squid_redirector.py 
ls
tar -cvzf squid-redirector.tar.bz2 ./
ls
tar -xvf squid-redirector.tar.bz2 -C temp
mkdir temp
tar -xvf squid-redirector.tar.bz2 -C temp
ls temp/
cd ..
ls
ls SOURCES/
rm SOURCES/squid-redirector.tar.bz2 
mv temp/squid-redirector.tar.bz2 SOURCES/
ls SOURCES/
rm -rf temp/
rpmbuild -bb SPECS/squid-redirector.spec 
ls
ls BUILD
ls RPMS/
ls SRPMS/
ls
ls SOURCES/
vim SPECS/squid-redirector.spec 
ls
cd ..
ls
cd ..
ls
cd rpmbuild/
ls
cp rpmbuild/BUILD/* squid-redirector
mkdir squid-redirector
cp rpmbuild/BUILD/* squid-redirector
cd squid-redirector/
ls
vim setup.py
python3 setup.py bdist_rpm
python
yum install python3
su -
