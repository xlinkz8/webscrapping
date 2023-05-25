
# Conversation opened. 1 read message.

# Skip to content
# Using Gmail with screen readers
# 7 of 7,830
# try & excerpt condition
# Inbox

# Lawrence Akpan <ten12visuals@gmail.com>
# Attachments
# May 24, 2023, 9:58 PM (14 hours ago)
# to me, issabolanle44@gmail.com, chinelomojekwu@gmail.com, ten12visuals@gmail.com

#  If there are network issues or the server is not reachable this will improve the functionality and error handling of your code.
 

#  One attachment
#   •  Scanned by Gmail
# import necessary modules (re, requests, os, sys) 
import os
import sys
import re
import requests

#function takes a text input and uses regular expressions (re.findall) to extract phone numbers

def extract_phone_numbers(text):
    pattern = r"234[789][01]\d{8}\b" 
    # pattern = r"^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

# function takes a text input and uses regular expressions to extract email addresses. The regular expression pattern

def extract_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = re.findall(pattern, text)
    return emails

#function takes a text input and uses regular expressions to extract HTML links. The regular expression pattern
def extract_links(text):
    pattern = r'<a\s+(?:[^>]*)?href="([^"]*)"'
    links = re.findall(pattern, text)
    return links

def save_to_file(data, filename):
    with open(os.path.join(sys.path[0], filename), 'w') as file:
        for item in data:
            file.write(item + '\n')
#function takes data and a url as input. 
def main():
    url = input("Enter the website URL: ")
    
#this improve functionality and error handling of the code.
    try:
#It opens the file with the specified filename and writes each item in the data list to the file, separated by a newline.
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        html_content = response.text

        phone_numbers = extract_phone_numbers(html_content)
        emails = extract_emails(html_content)
        links = extract_links(html_content)

        save_to_file(phone_numbers, 'phone_numbers.txt')
        save_to_file(emails, 'emails.txt')
        save_to_file(links, 'links.txt')

        print("Extraction complete. Phone numbers, emails, and links saved to separate files.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while retrieving the webpage: {e}")
        
# The if _name_ == '_main_': condition ensures that the main() function is only executed if the script is run directly and not imported as a module.

if __name__ == '__main__':
    main()
# try&exerpt.txt
# Displaying try&exerpt.txt.