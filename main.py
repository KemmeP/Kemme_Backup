import shutil
import os
import datetime

userinput = int(input(f'Welcome to Kimmys Backup! \nPlease choose: \n[1]Full \n[2]Differential \n'))

x = datetime.datetime.now()
x2 = x.strftime("%d-%m-%Y - %H.%M.%S")

bck_dir = 'C:/Users/kpo/OneDrive - RTX/Documents/TechCollege H4/Serverautomatisering/bck_logs/'
src_dir = 'C:/Users/kpo/OneDrive - RTX/Documents/TechCollege H4/Serverautomatisering/bck_src/'
path = 'C:/Users/kpo/OneDrive - RTX/Documents/TechCollege H4/Serverautomatisering/bck_dst/Full '+ x2
dpath = 'C:/Users/kpo/OneDrive - RTX/Documents/TechCollege H4/Serverautomatisering/bck_dst/Diff '+ x2

files = os.listdir(src_dir)


def full_backup():
    os.mkdir(path)
    shutil.copytree(src_dir, path, dirs_exist_ok=True)
    log()


def diff_backup():
    os.mkdir(dpath)
    mtime = os.path.getmtime(src_dir+'Testfil1.txt')
    mtime1 = os.path.getmtime(bck_dir+'log.txt')

    if mtime == mtime1:
        pass
    elif mtime != mtime1:
        #shutil.copy(src_dir+files, dpath)
        with open(bck_dir+"full-log.txt", 'r') as diffread:
            Lastfull = diffread.read()
            print(Lastfull)
            full_backup_dirlists = os.listdir(Lastfull)
            print(os.listdir(src_dir))
            for files in full_backup_dirlists:
                path_to_file = os.path.join(Lastfull, "", files)
                os.path.getmtime(path_to_file)
                path_to_srcfile = os.path.join(src_dir, "", files)
                os.path.getmtime(path_to_srcfile)
                print(os.path.getmtime(path_to_srcfile))
                if os.path.getmtime(path_to_file) == os.path.getmtime(path_to_srcfile):
                    pass
                elif os.path.getmtime(path_to_file) != os.path.getmtime(path_to_srcfile):
                    shutil.copy(src_dir + files, dpath)



def log():
        with open(bck_dir+"full-log.txt", 'w') as file:
            file.write(path)
        with open(bck_dir+"log.txt", 'a') as file:
            file.write("-"*50+"\n""full backup"+x2+"\n")
            for dirs in files:
                file.write(dirs+"\n")


if userinput == 1:
    full_backup()
    print('Full')

elif userinput == 2:
    diff_backup()
    print('Differential')

else:
    print('Wrong input, try again!')
