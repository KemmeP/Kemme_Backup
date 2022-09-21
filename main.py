# Moduler som bruges til funktioner
import shutil
import os
import datetime

# Tekst til input interfacet, tvinges til at kun modtage integer (hele tal)
userinput = int(input(f'Welcome to Kimmys Backup! \nPlease choose: \n[1]Full \n[2]Differential \n'))

# Tidsstyring til timestamps
x = datetime.datetime.now()
x2 = x.strftime("%d-%m-%Y - %H.%M.%S")

# Variabler med info om hvor filer skal hentes/gemmes/læses

# Log filer
bck_dir = 'C:/Users/kpo/OneDrive - RTX/Documents/TechCollege H4/Serverautomatisering/bck_logs/'
# Source filer
src_dir = 'C:/Users/kpo/OneDrive - RTX/Documents/TechCollege H4/Serverautomatisering/bck_src/'
# Full Backup filer
path = 'C:/Users/kpo/OneDrive - RTX/Documents/TechCollege H4/Serverautomatisering/bck_dst/Full ' + x2
# Differential backup filer
dpath = 'C:/Users/kpo/OneDrive - RTX/Documents/TechCollege H4/Serverautomatisering/bck_dst/Diff ' + x2

# Liste af alle filer fra Source filer
files = os.listdir(src_dir)


# Full Backup funktion
def full_backup():
    # Oprettelse af mappe til filer
    os.mkdir(path)
    # Kopiering af alle filer source directory, til path, check om mappen eksisterer.
    shutil.copytree(src_dir, path, dirs_exist_ok=True)
    # Kalder log funktionen
    log()


# Differential Backup funktion
def diff_backup():
    # Oprettelse af mappe til filer
    os.mkdir(dpath)
    # Checker Modified time for Source filer
    mtime = os.path.getmtime(src_dir + 'Testfil1.txt')
    # Trækker timestamp for sidst udførte full backup, som skal bruges til sammenligning af med ovenstående
    mtime1 = os.path.getmtime(bck_dir + 'log.txt')

    # Hvis timestamps er ens gør ingenting
    if mtime == mtime1:
        pass
    # Hvis timestamps er forskellige fortsæt med næste
    elif mtime != mtime1:
        # Åben log fil og læs dato for sidste Full backup
        with open(bck_dir + "full-log.txt", 'r') as diffread:
            # Gem ovenstående dato i en variabel
            Lastfull = diffread.read()
            ###print(Lastfull)
            # Laver liste over de filer som er blevet backed up ved sidste backup
            full_backup_dirlists = os.listdir(Lastfull)
            ###print(os.listdir(src_dir))
            # For hver fil i listen tjekkes hvornår de sidst er modificeret (getmtime)
            for files in full_backup_dirlists:
                path_to_file = os.path.join(Lastfull, "", files)
                os.path.getmtime(path_to_file)
                path_to_srcfile = os.path.join(src_dir, "", files)
                os.path.getmtime(path_to_srcfile)
                ###print(os.path.getmtime(path_to_srcfile))
                # Hvis timestamps er ens, så pass
                if os.path.getmtime(path_to_file) == os.path.getmtime(path_to_srcfile):
                    pass
                # Hvis timestamps er forskellige, kopier filer til stien med diff. filer (dpath)
                elif os.path.getmtime(path_to_file) != os.path.getmtime(path_to_srcfile):
                    shutil.copy(src_dir + files, dpath)

# Log funktion
def log():
    # Åbner filen i bck_dir med navnet full-log.txt og skriver (w) til "file"
    with open(bck_dir + "full-log.txt", 'w') as file:
        file.write(path)
    # Åbner filen i bck_dir med navnet full-log.txt og tilføjer (a=append) til filen
    with open(bck_dir + "log.txt", 'a') as file:
        file.write("-" * 50 + "\n""full backup " + x2 + "\n")
        # Skriver en linje for hvert entry i files
        for dirs in files:
            file.write(dirs + "\n")


# User input 1 starter full backup
if userinput == 1:
    full_backup()
    print('Full')

# User input 2 starter incremential backup
elif userinput == 2:
    diff_backup()
    print('Differential')

# Alle andre inputs printer "fejl"
else:
    print('Wrong input, try again!')
