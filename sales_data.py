
#Import Modules
import time;

#Global variables
filelua = open("D:/Programming/ESOP/ArkadiusTradeToolsSalesData01.txt")
f = open("D:/Programming/ESOP/exported_sales.txt","w")

#Create a list of lines from the source file
def write_sales():
    lines = filelua.readlines() #Creates a list which contains the lines of the source file
    number_of_commas = 0 

    for i in range(8,len(lines)):

        if (
            ("buyerName" in lines[i]) or ("guildName" in lines[i]) or 
            ("taxes" in lines[i])     or ("itemLink" in lines[i]) or 
            ("timeStamp" in lines[i]) or ("sellerName" in lines[i]) or 
            ("quantity" in lines[i])  or ("price" in lines[i]) or ("internal" in lines[i])
           ): 
            string = lines[i]
            len_of_line = len(string)
            x_starter = string.find('= ') + 2

            for x in range(x_starter,len_of_line-1):
                f.write(string[x])
                if string[x] == ",":
                    number_of_commas += 1

            if number_of_commas%9 == 0:
                f.write("\n")

#Close the opened files
def close_files():
    f.close()
    filelua.close()

#Convert epoch time to human readable
def convert_epoch_to_human():
    epoch = 1592395250
    print(time.strftime("%a, %Y.%m.%d, %H:%M:%S", time.localtime(epoch)))

#Main program
def main():
    write_sales()
    close_files()

#main()
convert_epoch_to_human()