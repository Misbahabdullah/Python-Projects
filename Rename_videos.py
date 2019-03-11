### Someone presented me a renaming challenge. Which I gladly undertook. 
### The challenge was to rename mp4 files. Each mp4 file had a number at its end. 
### I was supposed to put that number at the beginning of the file name, and remove the number from the end
### However, the actual challenge was that: the videos were in different folders. And each folder had a random number
### of videos. Some of the folders had subfolders, and subfolders had further subfolders
### It was required to iterate through the subfolders till I reached a folder which had no subfolders
### The below code worked perfectly fine.

import os

f=open("foldername.txt","w+")
f5=open("filename.txt","w+")
f2=open("new_filename.txt","w+")

b=".mp4"
c="-"

def folder_rename(start_path):

    file_list=os.listdir(start_path)
    new_path=start_path

    for a in file_list:
        if not "." in a: #If its a folder
            f.write(start_path+"/"+a+"/"+"\n")
            new_path=start_path+"/"+a+"/"
            folder_rename(new_path) #Recursive call
        else: #if its a file
            try: #This try is needed because some file names are giving error
                f5.write(a+"\n") #This writes all the files that it found

                if a.endswith(b): # If mp4 found, search for number before .mp4
                    os.chdir(new_path)
                    file_rename(a)

            except:
                pass

def file_rename(a):

    if  (b in a) and (c in a):
        remainder=None

        length=len(a)
        position=a.find("-")
        #print(a, position)
        if position>-1:
            remainder=a[position+1:length-4]

        try:
            if remainder:
                tail= int(remainder)

                new_name="_"+ remainder +" "+(a[:position])+".mp4"
                f2.write("old name : " + a + "\n")
                f2.write("New Name : " + new_name + "\n")
                os.rename(a, new_name)
        except:
            pass
#f.close()
#f2.close()
    return()

folder_rename("e:/lynda")
