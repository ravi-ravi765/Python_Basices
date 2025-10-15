import os

# how do you check in which directory you are working
print(os.getcwd())

# how do i list all the files in a directory
list_dir = os.listdir("/home/ravi/Downloads/Data_eng_workspace/Python_Basices")
print(list_dir)

# creating and removing folder in using os module

# os.mkdir('my_new')
# os.makedirs('old/new',exist_ok=True)

# removing directory 
# os.rmdir("my_new")
# os.removedirs("old/new")


# check if file or folder path exists 
print(os.path.exists("/home/ravi/Downloads/Data_eng_workspace/Python_Basices/Python_modules_for_data_eng/os_module/old/new"))
# how do you check if this folder 
print(os.path.isdir("/home/ravi/Downloads/Data_eng_workspace/Python_Basices/Python_modules_for_data_eng"))

# Path Operations
# splict file_name from the path
basename = os.path.basename("/home/ravi/Downloads/Data_eng_workspace/Python_Basices/Python_modules_for_data_eng/os_module/orders.csv")
# how do you seperate folder name
dirname = os.path.dirname("/home/ravi/Downloads/Data_eng_workspace/Python_Basices/Python_modules_for_data_eng/os_module/orders.csv")
# how you combine both basename and dirname
print(os.path.join(dirname,basename))


home_dir = os.environ.get("HOME")
print(home_dir)

for root,dir,files in os.walk("/home/ravi/Downloads/Data_eng_workspace/Python_Basices/Python_modules_for_data_eng/os_module"):
    print('root :',root)
    print('dir : ',dir)
    print('files :',files)

# os.mkdir('archive')
Path = "/home/ravi/Downloads/Data_eng_workspace/Python_Basices/Python_modules_for_data_eng/os_module"
Path1 = "/home/ravi/Downloads/Data_eng_workspace/Python_Basices/Python_modules_for_data_eng/os_module/archive"
# csv_files = [f for f in os.listdir(Path) if f.endswith('.csv')]
# print(csv_files)

# for file in csv_files:
#     os.rename(f'{Path1}/{file}',f'{Path}/{file}')

# print(os.listdir(Path1))

# try:
#     if not os.path.exists(Path1):
#         os.mkdir('archive')

#     list_of_csv_files = [f for f in os.listdir(Path) if f.endswith(".csv")]

#     for file in list_of_csv_files:
#         os.rename(f'{Path}/{file}',f'{Path1}/{file}')

# except FileNotFoundError as e:
#     print(f'Error check file or folder : {e}')

# except FileExistsError as e:
#     print(f'file already present.. : {e}')

#creating destination folder if not exists
os.makedirs(Path1,exist_ok=True)

# list of all csv files only
csv_files = [f for f in os.listdir(Path) if f.endswith('.csv')]

# loop throup files and make source path and destination path
for file in csv_files:
    src = os.path.join(Path,file)
    dest = os.path.join(Path1,file)

    try:
        if os.path.exists(dest):
            print("file present in destination")
            continue

        os.rename(src,dest)
        print(f'moved file {os.path.basename(src)} to {os.path.dirname(dest)} folder')

    except FileExistsError :
        print('file already present...')

    except FileNotFoundError :
        print('file not found invalid path')


    