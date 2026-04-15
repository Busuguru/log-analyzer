# log-analyzer
Python tool to analyze logs and detect suspicious activity

#  Log Analyzer

##  Description

A Python-based tool that analyzes log files and detects suspicious login activity such as repeated failed login attempts.

##  Features

* Detects failed login attempts
* Identifies suspicious IP addresses
* Counts repeated login failures
* Simple and efficient log parsing

## Technologies Used

* Python
* File Handling

##  Usage

```bash
python main.py
```

##  Sample Log File

```text
Failed login from 192.168.1.10
Successful login from 192.168.1.5
Failed login from 192.168.1.10
Failed login from 10.0.0.2
Successful login from 192.168.1.5
Failed login from 10.0.0.2
Failed login from 10.0.0.2
```

##  Example Output

```text
 Suspicious Activity Report:

IP 192.168.1.10 has 2 failed login attempts!
IP 10.0.0.2 has 3 failed login attempts!
```

##  What I Learned

* Log analysis fundamentals
* Detecting suspicious behavior from logs
* Parsing and processing text files in Python

