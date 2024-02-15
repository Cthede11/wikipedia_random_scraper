- This project is a web scraper that is design specifically for use with wikipedia

SETUP
- download the code from github
- go into the "Scraper.py" file and run it
- after you hit run, it should start a local server that you can access from the terminal
- It should say something like: Running on http://111.1.1.1:5000 (with different numbers)
- click on that and it should open the scraper UI in your browser
- from there, setup is complete, you may now use the scaper, hit CTRL + C in your terminal to terminate the program

PAST PAGES
- there is a "Past Pages" section that displays the last 5 displayed pages.
- the links are able to be clicked to return to a previous page
- (issue) currently you must enter a starting page each time you start the program before you utilize the past pages
- (issue) currently when a link from past pages is clicked it shows the page but does not navigate to the URL
this means that when you hit "randomize" it will randomize based on the last page randomized and not the link clicked

USING THE SCRAPER
- As a user you will need to have the url of a wikipedia page to start from
- Enter that url into the text box and hit the "scrape" button
- From there the iframe below should navigate to the page you entered
- After the iframe navigates to your page, you may hit the "randomize" button 
    to follow a random link found in that article. This is repeatable
    (You may also click a link in the iframe to follow a specific link)
