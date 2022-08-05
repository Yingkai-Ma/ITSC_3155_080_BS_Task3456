#import beautifulsoup and request here
import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup as BS


def displayJobDetails(jobDetails):
    print("Display Job Details:")
    for job in jobDetails:
        print ()
        pprint(list(job), indent=4)

#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'

def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
   
    # request from the talent url
    response = requests.get(url)
    # print the status code here if passed
    # Check for exceptions, 200 passes
    if (response.status_code != 200):
        raise Exception(response.status_code + " Error")
    
    soup = BS(response.text,'html.parser')
    JobDetails = soup.find_all('div', class_='card card__job')
    # Create an array Here
    for job in JobDetails:
       jobTitle = job.find('h2', class_='card__job-title').text.strip()
       company = job.find('div', class_='card__job-empname-label').text.strip()
       description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
       jobDetailsjson = {
           "Title": jobTitle,
           "Company": company,
           "Description": description
       }

    return jobDetailsjson # defined array


#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")
    with open('jobDetails.json', 'w') as file:
        file.write(json.dumps(jobDetails))
    return


#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    
    # Complete the missing part of this function here
    print("\nEnter the location you want to search")
    location = input()
    
    print("Searching....")
    print("Results:\n")
    # get request and pull the data from the url
    jobDetails = getJobList(role, location)
    displayJobDetails(jobDetails)
    saveDataInJSON(jobDetails)

    
if __name__ == '__main__':
    main()


