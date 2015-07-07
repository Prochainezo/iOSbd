# iOSbd
iOSbd is a simple yet practical tool that will allow you to place a persistent backdoor inside of any cydia package desired. iOSbd relies on metasploit for it's payload, and LaunchDaemons for it's persistence. `ios_dump.rb` is a metasploit post module compatible with iOSbd, and can be installed by simply moving it to the `post/osx/gather/` directory. Youtube explaination and demo: https://www.youtube.com/watch?v=34VYX57vJm0

Dependencies
--------------
The following dependencies are needed before using iOSbd
- Metasploit: https://github.com/rapid7/metasploit-framework
- Dpkg: sudo apt-get install dpkg

Usage
-------------
```
usage: iosbd.py [-h] [-p package] [-lh LHOST] [-lp LPORT] [-o output]

optional arguments:
  -h, --help            show this help message and exit
  -p package, --package package
                        Package to backdoor
  -lh LHOST, --lhost LHOST
                        Host for reverse shell
  -lp LPORT, --lport LPORT
                        Port for reverse shell
  -o output, --output output
                        Path to save backdoored package
                        
```
