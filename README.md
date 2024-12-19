# SSH-Brute-Forcer
A simple python script that can run a wordlist attack against an ssh server using the Paramiko module.


# How it works
1) The user input the wordlist the want to use , the hostname/IP address of server that the target user is on , and the username of the target user ( as well as the number of threads the user would like to spawn
2) The program goes through the inputted wordlist, and appends the word on each line to a queue
3) The program will then spawn the dersired number of threads to carry out the brute force attack - each thread will take a potential password from the queue, and try to connect to the target ssh server on port 22 using the inputted username and the password
4) If the thread is able to connect to the server using that combination of username and password , then we know that that is the password of the user
5) If the thread receives an "Authentication Exception" then we can determine that the password the thread is trying to use to connect to the server is incorrect , and no the target users password
6) If the thread cannot connect otherwise , then it will sleep for a minute before restarting the attack. This may be due to the server blocking the rapid number of attempt connections coming from the thread / threads

# Troubleshooting
