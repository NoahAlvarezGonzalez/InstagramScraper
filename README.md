# InstagramScraper
https://instagram-scraper-noah.herokuapp.com

# Goal

Scrap any instagram account infos and return it into a CSV to the user

# Requirements

* Streamlit : to showcase the app
* Pandas : to create the CSV for the user
* Instaloader : to scrape Instagral

# How it works

* The user is asked to enter one or multiple Instagram account
* When he presses enter, the entered accounts are turned into a list
* Each account is passed to Instaloader wich scrape it's data, and appened into a new list
* This list is converted into a CSV file
* The CSV is displayed on screen and the user can choose to download it by pressing the Download button
* If he does, an hyperlink appears and by clicking on it, he can download the CSV file

# Result
