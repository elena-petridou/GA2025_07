from datetime import datetime
import click
import glob
import os
from home_messages_db import HomeMessagesDB
import helperFile as hf

@click.command() #function below should be treated as cli command
@click.option('-d','--dburl', help='DBURL into which to insert the database (must be a SQLAlchemy database URL)', required = True) # option -d for user
@click.option('-q','--query', default=None, is_flag=True, help='Run a query instead of inserting files')
@click.option('-e','--erasetable', default=None, is_flag=True, help='Removes all data from table')
@click.option('-s', '--size', default = None, is_flag = True, help = 'Output the current size (number of entries) of smartthings table in the database')
@click.argument('filename',nargs=-1)

def smartthings(dburl,query,size,erasetable,filename):
    """
    Very clear explanation of the function which will be written in the future

    """

    # initialize db
    mydb = HomeMessagesDB(dburl)
    mydb.create_db()
        
    # File gathering and insertion 
    if erasetable:
        hf.erase(mydb, "smartthings")
    
    elif query:
        click.echo('Would you like output specified on date or locationname')
        userinp= input()
        
        if userinp.lower() =='date':
            hf.return_entries_between_dates(mydb, 'smartthings')
        elif userinp =="name":
            hf.query_name(mydb,'smartthings')    
    
    elif size:
        hf.query_size(mydb, "smartthings")
    
    elif filename:
        files = hf.check_filepaths(filename, "smartthings")
        hf.file_insertion(files, mydb, "smartthings")
        click.echo("Files inserted")
    
if __name__ == '__main__':
    smartthings()
    
    # # file insertion
    # ## gathering files
    # all_files=[] # ini empty list to gather files from users input
    # # gather user specified files
    # for pattern in files:
    #     #check if a pattern in user input
    #     if '*' in pattern or '?' in pattern:
    #         #if so use it to find all files
    #         matched_files=glob.glob(pattern)
    #         #and add them to all_files list 
    #         all_files.extend(matched_files)
            
    #         # if glob does not find anything it gives back an empty list
    #         # therefore check if list matched files is empty and if so echo a warning 
    #         ## could be made better with Try and raiseError maybe
    #         ##although its cli so ???
    #         if len(matched_files)==0:
    #             click.echo('No files found using pattern!')
    #             return None
        
    #     # if user wrote down a filepath        
    #     else:    
    #         #check if path exists
    #         if os.path.exists(pattern):
    #             #add path to all_files
    #             all_files.append(pattern)
    #         else:
    #             click.echo(f'No file "{pattern}" found!')
    #             return None
    
    # ## insert files into the database 
    # with click.progressbar(all_files, label='inserting files') as bar:
    #     for files in bar:
    #         db.insert_table_smartthings(files)

    # Options 
    ## remove content
    # if rm:
    #     click.echo('Are you sure you want to remove all data from the table? Yes/No')
    #     userinp= input()
    #     if userinp.lower() == 'yes':    
    #         db.erase_table_content('smartthings')
    #         click.echo('table content removed')
    #         return
    #     elif userinp.lower() =='no':
    #         return
    #     return  
    
    # ## query cluster
    # if query:
    #     click.echo('Would you like output specified on date, name or size of the database?')
    #     userinp= input()
    #     # check if user input is date 
        
        
    #     if userinp.lower() =='date':
    #         click.echo('from when until when? YYYY-mm-dd:YYYY-mm-dd')
    #         timeinp=input()
            
    #         #check if user put in two dates
    #         if ':' in timeinp:  
    #             dates=timeinp.split(':') # split dates based on :
    #             datepars1=list(map(int, dates[0].split('-'))) # convert string input into numeric list
    #             date1= int(datetime(*datepars1).timestamp()) # convert numeric list into date
                
    #             datepars2=list(map(int, dates[1].split('-')))
    #             date2=int(datetime(*datepars2).timestamp())
    #         else: #if user only put in 1 date
    #             datepars1=list(map(int, timeinp.split('-')))
    #             date1= int(datetime(*datepars1).timestamp())
    #             date2=date1
    #         output=db.query_db(f'SELECT * FROM smartthings WHERE epoch >= {date1} AND epoch <= {date2}')
            
    #     elif userinp =="name":
    #         name_inp = input("Which name do you want to filter the dataset for?")
    #         query = f"SELECT * FROM smartthings WHERE name = '{name_inp}'"
    #         output = db.query_db(query)
            
    #     elif userinp =='size':
    #         output = db.query_db(f'SELECT COUNT(*) as number_of_rows FROM smartthings')
    #     click.echo(output)
    #     return    



