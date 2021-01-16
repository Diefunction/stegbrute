from os import system

# installing requirements
requirements = input('Do you want to install the requirements? (y/n) ')
if requirements == 'y':
        system('sudo apt install steghide')
        system('sudo apt install figlet')
        system('sudo apt install ruby')
        system('git clone https://github.com/busyloop/lolcat')
        system('cd lolcat/bin && gem install lolcat')
        system('wget https://raw.githubusercontent.com/jopraveen/HTB-INVITE/main/Bloody.flf')
        system('sudo chmod +x Bloody.flf')
        system('echo "REQUIREMENTS SATISFIED !" | lolcat -a -d 5')

#banner
system('clear')
system('figlet -f ./Bloody "S B R U T E" | lolcat -a -d 3')
system('echo "CREDITS: Diefunction" | lolcat -a -d 2')
print()

# Actual code
def parseArgs():
    import argparse
    from sys import argv

    parser = argparse.ArgumentParser(epilog='Example: {} -i steg.jpg -o output.txt -w wordlist.txt'.format(argv[0]))
    parser._optionals.title = 'OPTIONS'
    parser.add_argument('-i', '--image', help='select stego image', required=True)
    parser.add_argument('-o', '--output', help='select file name for extracted data', required=True)
    parser.add_argument('-w', '--wordlist', help='select a wordlist', required=True)
    return parser.parse_args().image, parser.parse_args().output, parser.parse_args().wordlist 

print()
system('echo "Please wait your file is cracking..." | lolcat -a -d 2')
print()
def steghide(password):
    from subprocess import call, DEVNULL
    cmd = 'steghide extract -sf {0} -xf {1} -p {2}'.format(image, output, password)
    if call(cmd.split(), stdout = DEVNULL, stderr = DEVNULL) == 0:
        print('[#] password: {}\n[ctrl + c] to stop'.format(password))

if __name__ == '__main__':
    from multiprocessing import Pool
    from time import time

    image, output, wordlist = parseArgs()
    pool = Pool()
    start = time()
    pool.map(steghide, [password.rstrip() for password in open(wordlist, errors = 'ignore')])
    totalTime = time() - start
    timeFormat = 'seconds'
    if(totalTime >= 60):
        totalTime = totalTime/60
        timeFormat = 'minutes'
        if(totalTime >= 3600):
            totalTime = totalTime/60
            timeFormat = 'hours'
    print('[#] Finished : {0:.2f} {1}'.format(totalTime, timeFormat))
