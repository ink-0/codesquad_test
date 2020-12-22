cmd = list(input('cube> '))
while "'" in cmd:
    if "'" in cmd:
        cmd[cmd.index("'") - 1] += "'"
        cmd.pop(cmd.index("'"))
print(cmd)