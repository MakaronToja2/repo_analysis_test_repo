import os

# BAD: using system() directly (OS command injection risk)
os.system("ls -l")

# BAD: use of eval (arbitrary code execution risk)
user_input = "1 + 1"
result = eval(user_input)

# BAD: hardcoded password
password = "SuperSecret123"
