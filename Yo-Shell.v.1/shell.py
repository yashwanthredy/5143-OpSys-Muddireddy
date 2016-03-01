"""
Version : 2.7.1
@Authors: 
1.Yashwanth Reddy  Muddireddy
2.kiran Reddy Kancharla
"This code is to interpret shell through python"
it takes the shell commands like copy,move,chmod,ls -l ,ls -a and more and implements as like of shell
@Program Name: shell.py
@Description:
          historyManager - manages a history of commands
          parserManager - handles parsing of commands into command , arguments, flags
          commandManager - gets commands parsed and then runs appropriate functions for command
          driver - drives the entire shell
"""

import os
import sys
import stat
import time
import shutil
"""
@Name: historyManager
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@Methods:
    push_command - add command to history
    get_commands - get all commands from history
    number_commands - get number of commands in history
"""
class historyManager(object):
    def __init__(self):
        self.command_history = []

    """
    @Name: push_command
    @Description:
        Add command to history
    @Params:
        cmd (string) - Command added to history
    @Returns: None
    """
    def push_command(self,cmd):
        self.command_history.append(cmd)
        
    """
    @Name: get_commands
    @Description:
        get all commands from history
    @Params: None
    @Returns: None
    """
    def get_commands(self):
        return self.command_history
        
    """
    @Name: number_commands
    @Description:
        get number of commands in history
    @Params: None
    @Returns: 
        (int) - number of commands
    """
    def number_commands(self):
        return len(self.command_history)

"""
@Name: parserManager
@Description:
    Handles parsing of commands into command , arguments, flags.
@Methods:
    parse - does actual parsing of command
"""
class parserManager(object):
    def __init__(self):
        self.parts = []
    """
    @Name: parse
    @Description:
        Parses command into a list (right now). 
    @Params: 
        cmd (string) - The command to be parsed
    @Returns: 
        (int) - number of commands
    """
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
        
"""
@Name: commandManager
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@Methods:
    run_command - Runs a parsed command
    ls - Directory_listing
    cat - File dump
"""
class commandManager(parserManager):
    def __init__(self):
        self.command = None
    """
    @Name: run_command
    @Description:
        Runs a parsed command
    @Params: 
        cmd (string) - The command
    @Returns: 
        (list) - With the command parts (It shouldn't return the list, it should RUN the appropriate command from this method.
    """
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command

    """
    @Name: ls
    @Description:
        Does a directory listing
    @Params: 
        dir (string) - The directory to be listed
    @Returns: None
    
    """
    def ls(self):
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))
    
    def printl(self):
        a=['File Name','Size','Permissions','Accessed','Modified','Changed']
        print('  {0:48s}      {1:8s}  {2:10s}           {3:20s}          {4:10s}                {5:10s} '.format(a[0],a[1],a[2],a[3],a[4],a[5]))
        print(' {0:48s}      {1:8s}  {2:10s}       {3:24s}   {4:24s}    {5:24s}'.format("-------------------------","---------","-------------","----------------","-------------------","-------------------","-------------------"))

    """
    @Name: ls all 
    @Description: directory listing associated with flags
    @params:flag(-l,-a,-m,-s) and dir(string) the directory to be listed
    @returns: none
    
    """
    #lsall is a method for ls with different flags
    def lsall(self,dir,flag):
        str1 = []
        str2 = []
        str3 = []
        str4 = []
        str5 =[]
        str6 = []
      	str7=[]
        files_list = []
        str8=[]
        str9=[]
        str10=[]
        str11=[]
        str12=[]
        str13=[]
	for dirname, dirnames, filenames in os.walk(dir):
	    for filename in filenames:
            
		str1.append(os.path.join(dirname, filename))
                str2.append(os.path.getsize(filename))
                str3.append(oct(stat.S_IMODE(os.lstat(filename).st_mode)))
                str4.append(time.ctime(os.path.getmtime(filename)))
                str5.append(time.ctime(os.path.getatime(filename)))
		str6.append(time.ctime(os.path.getctime(filename)))

	if ((flag =='-a') | (flag == '-la')):
           for i in range(len(str5)):
               str8.append(str5[i].split())
               str7.append(str8[i])
           str7.sort(key = lambda row: (row[0],row[1],row[2],row[3],row[4]))
           str7.reverse()
           self.printl()
           for i in range(len(str5)):
               for j in range(len(str5)):
                   if str(str7[i])==str(str8[j]):
                      print('{0:48s}    {1:8d}        {2:10s}    {3:20s}    {4:10s}    {5:10s}'.format(str1[j],str2[j],str3[j],str4[j],str5[j],str6[j]))
    	elif ((flag=='-c') | (flag =='-lc')):
             for i in range(len(str6)):
                 str10.append(str6[i].split())
                 str9.append(str10[i])
             str9.sort(key = lambda row: (row[0],row[1],row[2],row[3],row[4]))
             self.printl()
             str9.reverse()
             for i in range(len(str6)):
                 for j in range(len(str6)):
                     if str(str9[i])==str(str10[j]):
                        print('{0:48s}    {1:8d}        {2:10s}    {3:20s}    {4:10s}    {5:10s}'.format(str1[j],str2[j],str3[j],str4[j],str5[j],str6[j]))
        elif flag=='-l':
             self.printl()
             for j in range(len(str1)):
                 print('{0:48s}    {1:8d}        {2:10s}    {3:20s}    {4:10s}    {5:10s}'.format(str1[j],str2[j],str3[j],str4[j],str5[j],str6[j]))
        elif ((flag=='-s') | (flag=='-ls')):
             for i in range(len(str2)):
                 str13.append(str2[i])
             str13.sort()
             self.printl()
             for i in range(len(str2)):
                 for j in range(len(str2)):
                     if str(str13[i])==str(str2[j]):
                        print('{0:48s}    {1:8d}        {2:10s}    {3:20s}    {4:10s}    {5:10s}'.format(str1[j],str2[j],str3[j],str4[j],str5[j],str6[j]))
        elif ((flag=='-m') | (flag == '-lm')):
             for i in range(len(str4)):
                 str12.append(str4[i].split())
                 str11.append(str12[i])
             str11.sort(key = lambda row: (row[0],row[1],row[2],row[3],row[4]))
             str11.reverse()
             self.printl()
             for i in range(len(str4)):
                 for j in range(len(str4)):
                     if str(str11[i])==str(str12[j]):
                        print('{0:48s}    {1:8d}        {2:10s}    {3:20s}    {4:10s}    {5:10s}'.format(str1[j],str2[j],str3[j],str4[j],str5[j],str6[j]))
   	else:
	    print("invaild flag (ls command)")
    """
    @Name: cat
    @Description:
        Dumps a file
    @Params: 
        file (string) - The file to be dumped
    @Returns: None
    """    
    def cat(self,file):
        f = open(file,'r')
        print(f.read())
    """
    @Name: chmod
    @Description:
       change mode file
    @Params:
       
    @Returns: None
    """
    def chmodo(self,filename,mode):
        os.chmod(filename,mode);
        print("mode changed successfully")
       

    """
    @Name: wc
    @Description:
       word count of a file
    @Params:
       
    @Return : none
    """

    def wc(self,flag,file):
        if(os.path.isfile(file)):
          print(int(check_output(["wc","-l",file]).split()[0]))
        else:
            print("file does not exist")

    """
    @Name: rm
    @Description:
       removes a file
    @Params:file name
       
    @Return : none
    """
    def rm(self,file):
        os.remove(file)
        print("removed successfully")
    
    """
    @Name: copy
    @Description:
       copy a file
    @Params:
       
    @Return :none
    """
    def cop(self,file1,file2):
        shutil.copy(file1,file2)
        print("copied successfully")
    
    """
    @Name: cd
    @Description:
       change directory
    @Params:
       
    @Return : none
    """
    def cd(self,directory):
        if(directory == '..'):
          os.chdir('..')
          new=os.getcwd()
          print(new)
        elif(directory=='~'):
            home=os.path.expanduser('~')
            os.chdir(home)
            new=os.getcwd()
            print(new)
        else:
            if(os.path.isdir(directory)):
              os.chdir(directory)
              new=os.getcwd()
              print(new)
            else:
                print("directory does not exist")
    
    """
    @Name: mv
    @Description:
       rename a file
    @Params:oldfile, new file
       
    @Return : none
    """
    def mv(self,file1,file2):
        shutil.move(file1,file2)
        print("file renamed successfully")
    
    """
    @Name: history
    @Description:
       displays the history of commands
    @Params: none
       
    @Return : none
    """
    def history(self):
        his=historyManager.get_commands(self)
        return his

"""
@Name: driver
@Description:
    Drives the entire shell environment
@Methods:
    run_shell - Loop that drives the shel environment
"""
class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
        
    """
    @Name: runShell
    @Description:
        Loop that drives the shel environment
    @Params: None
    @Returns: None
    """ 
    def runShell(self):
        number_commands = 0
        while True:
            self.input = raw_input("parser-$ ")         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            print(parts)
	    
 	    if parts[0]=='cat':
               if len(parts)==2:
                  self.commands.cat(parts[1])
               else:
                   print("file arguments  missing for cat command")
            elif parts[0]=='ls':
                 if(len(parts)==1):
                    self.commands.ls()
                 elif (len(parts)==2):
		       dir=os.getcwd()
		       self.commands.lsall(dir,parts[1])
            elif parts[0]=='cp':
                if(len(parts)==3):
                  self.commands.cop(parts[1],parts[2])
                elif (len(parts)==2):
                     print("source or destination file operand is missing")
                else:
                    print("excedded arguments for cp command")
            elif parts[0]=='chmod':
                if(len(parts)==3):
                    self.commands.chmodo(parts[2],int(parts[1]))
                else:
                    print("excedded arguments for chmod command")
            elif parts[0]=='cd':
                if(len(parts)==2):
                    self.commands.cd(parts[1])
                elif(len(parts)>2):
                    print("excedded arguments for cd command")
            elif parts[0]=='wc':
                if(len(parts)==2):
                    self.commands.wc(parts[1])
                elif(len(parts)==3):
                    self.commands.wc(parts[2],parts[1])
                elif(len(parts)>3):
                    print("excedded arguments for wc command")
                else:
                    print("operands missing  in wc")
            elif parts[0]=='rm':
                if(len(parts)==2):
                    self.commands.rm(parts[1])
                elif(len(parts)>2):
                    print("excedded arguments for wc command")
                else:
                    print("filename missing in rm command")
            elif parts[0]=='mv':
                if(len(parts)==3):
                    self.commands.mv(parts[1],parts[2])
                elif (len(parts)==2):
                    print("source or destination file missing operand")
                elif(len(parts)>3):
                    print("excedded arguments for mv command")
                else:
                    print("source and destination file name missing operand")
            elif parts[0]=='history':
                his=self.history.get_commands()
                if(len(parts)==1):
                    for item in his:
                        print(item)
                else:
                    print("excedded arguments in history command")
            elif parts[0]=='exit()':
                 print("****exit****")
                 raise SystemExit
            else:
                print("command not found") 
if __name__=="__main__":
    d = driver()    
    d.runShell()
Status API Training Shop Blog About Pricing

