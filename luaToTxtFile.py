import shutil

original_data = r'C:\Users\Imi-PC\Documents\Elder Scrolls Online\live\SavedVariables\ArkadiusTradeToolsSalesData01.lua'
target_data = r'D:\Programming\ESOP\ArkadiusTradeToolsSalesData01.lua'
#call shutil module's copyfile function, to copy the original_data to target_data
shutil.copyfile(original_data, target_data)

import os
#file's type from lua to txt
os.rename(r'D:\Programming\ESOP\ArkadiusTradeToolsSalesData01.lua',r'D:\Programming\ESOP\ArkadiusTradeToolsSalesData01'+'.txt')