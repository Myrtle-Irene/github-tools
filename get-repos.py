#writes a .txt file with links to all user's repositories

import sys
import requests
from bs4 import BeautifulSoup

def getRepos(userName):
    try :
        request=requests.get("https://github.com/"+userName+"?tab=repositories")
        soup=BeautifulSoup(request.text,"html.parser")
        count=0
        links = []
        for i in soup.find_all("a",{"itemprop": "name codeRepository"}):
            count+=1
            links.append(repo_link)
        print('Total Repositories :'+str(count))
    except Exception as exception:
        print(type(exception).__name__)
    return links

def write_file(link_list):
    filename = str('Myrtle-Irene') + '.txt'
    with open(filename, 'w') as fd:
        for x in link_list:
            fd.write(x + '\n')
            

if not(len(sys.argv)==2):
    print("\nusage : python get-repos.py 'username'\n")
else:
    if(sys.argv[1]=='-h' or sys.argv[1]=='--help'):
        print("\nusage : python get-repos.py 'username'")
        print("Options and arguments (and corresponding environment variables):")
        print("-h     : print this help message and exit (also --help)\n")
    else:
       write_file(write_file(getRepos(sys.argv[1])))
 
