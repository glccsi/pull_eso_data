
#Import Modules
import time
import shutil
import os

#Create a list of lines from the source file
def write_sales():
    filelua = open("D:/Programming/pull_eso_data/ArkadiusTradeToolsSalesData01.txt")
    f_sales = open("D:/Programming/pull_eso_data/exported_sales.csv","w")
    lines = filelua.readlines() #Creates a list which contains the lines of the source file
    number_of_commas = 0 #Number of commas in a line

    for i in range(8,len(lines)):

        if (
            ("buyerName" in lines[i]) or ("guildName" in lines[i]) or 
            ("taxes" in lines[i])     or ("itemLink" in lines[i]) or 
            ("timeStamp" in lines[i]) or ("sellerName" in lines[i]) or 
            ("quantity" in lines[i])  or ("price" in lines[i]) or
            ("internal" in lines[i])
           ): 
            string = lines[i]
            len_of_line = len(string)
            x_starter = string.find('= ') + 2

            for x in range(x_starter,len_of_line-1):
                f_sales.write(string[x])
                if string[x] == ",":
                    number_of_commas += 1

            if number_of_commas%9 == 0:
                f_sales.write("\n")

    f_sales.close()
    filelua.close()



#Open the original file, copy and paste it into program's directory
def import_sales():
    
    original_data = r'C:\Users\Imi-PC\Documents\Elder Scrolls Online\live\SavedVariables\ArkadiusTradeToolsSalesData01.lua'
    target_data = r'D:\Programming\pull_eso_data\ArkadiusTradeToolsSalesData01.lua'
    #call shutil module's copyfile function, to copy the original_data to target_data
    shutil.copyfile(original_data, target_data)

    #file's type from lua to txt
    os.rename(r'D:\Programming\pull_eso_data\ArkadiusTradeToolsSalesData01.lua',r'D:\Programming\pull_eso_data\ArkadiusTradeToolsSalesData01'+'.txt')

#Convert epoch time to human readable
def convert_epoch_to_human():
    epoch = 1592395250
    print(time.strftime("%a, %Y.%m.%d, %H:%M:%S", time.localtime(epoch)))

#Main program
def main():
    write_sales()

main()
convert_epoch_to_human()