# cfg-python-project
## Project Brief: __Search__<br>
- In this project you'll create a program to search for recipes based on an ingredient. <br>
- The standard project uses the Edamam Recipe API, but can be changed to use a different API after completing the required tasks.

## Setup
- To use the Edamam API you will need to register for an account. In your Edamam account
dashboard you can find an Application ID and Application Key, which you will need to make
requests to the API.
- To make a request to the Edamam API use the following URL:
https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}

    - For example, if the App ID and App Key for me account were “ch37j44” and “a58hia” I wanted to
search for “cheese”, the url would look like this:
https://api.edamam.com/search?q=cheese&app_id=ch37j44&app_key=a58hia