from os import system
names = ["tayyab","arshad","shoaib","khan","jarvis"]
for i in names:
    system(f"say {i}")#f is used for formatted string literals ,system is used to run system commands,name variable is passed to say command of mac os

#or
system("say john")
system("say smith")
system("say steve")
system("say kane")
system("say thor")