# GoFundMe
sign up* = make new line in Auth.csv

log in* = loop on Auth.csv to verify E-mail&Password are in column1&2 of the same row

new case* = make a text file saved in dir "Cases" 
new case/file contents = file contain [ title, details, money needed(target), start date, end date, creator password] seprated by "\n"
new case/ID = Urgency level(input) - title - random number from 1:9999  E.g.: 3GoFundMe0822

Donate = the donated money subtracted by target and overwritten as the target

list cases* = list files in Cases directory

Search by date* = loop on files in cases and get files IDs that contain the searched date

Edit* = overwrite the old LINE with the new one \\ work with (details, target, end date)
Edit/verify = verify the User by the checking password in the file

delete* = remove file from dir
delete/verify = verify the User by the checking password in the file

listMyCases = loop on files and get files contain user's password




* = things asked by the lab
