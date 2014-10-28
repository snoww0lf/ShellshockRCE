Shellshock ( Bash CVE-2014-6271 ) Remote Command Execution Injector
=============

Usage : ./shellsh0ck.py -c "command" -u "vulnsite" -m 1/2 <br>
Ex : ./shellsh0ck.py -c "whoami" -u "http://127.0.0.1/snoww0lf.cgi" -m 1 <br>
More info : ./shellsh0ck.py -h 

Make sure you have installed "curl" in your system before you'll using this file.

<h1>Overview</h1>
A critical vulnerability has been reported in the GNU Bourne-Again Shell (Bash), the common command-line shell used in many Linux/UNIX operating systems and Apple’s Mac OS X. The flaw could allow an attacker to remotely execute shell commands by attaching malicious code in environment variables used by the operating system [1] (link is external). The United States Department of Homeland Security (DHS) is releasing this Technical Alert to provide further information about the GNU Bash vulnerability.
