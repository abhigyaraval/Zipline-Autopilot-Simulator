import subprocess

p1 = subprocess.run('ls -la', shell=True, capture_output=True, text=True)

#p1 = p1.stdout.decode()
print(p1)
