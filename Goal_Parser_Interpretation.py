class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        for i in range(len(command)):
            if command[i]!="(" and command[i]!=")":
                s+=command[i]
            if command[i]=="(" and command[i+1]==")" and i+1<len(command):
                s+='o'
            if command[i]=="(":
                continue
            if command[i]==")":
                continue
        return s