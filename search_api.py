'''
TODO: 
1.Read the Edamam API documentation ★ 
https://developer.edamam.com/edamam-docs-recipe-api 
2.Ask the user to enter an ingredient that they want to search for 
3.Create a function that makes a request to the Edamam API with the required ingredient  as 
part of the search query (also included your Application ID and Application Key 
4.Get the returned recipes from the API response 
5.Display the recipes for each search result 
'''
import requests
'''
2.Ask the user to enter an ingredient that they want to search for 
'''
def ingredient_input():
    ingred_input = input("What is the name of the ingredient you want to look for? ")
    return ingred_input.lower()

'''
3.Create a function that makes a request to the Edamam API with the required ingredient as 
part of the search query (also included your Application ID and Application Key 
'''
def api_request(ingredient):
    app_id = "9b99a79e"
    app_key = "685b85e54d9239c5ef342f4f65e84ae3"
    request_result = requests.get("https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient, app_id, app_key))
    
    '''4.Get the returned recipes from the API response 
    '''
    data = request_result.json()
    return data['hits']

def api_result():
    ingred = ingredient_input()
    results = api_request(ingred)
    
    '''5.Display the recipes for each search result 
    '''
    for result in results:
        spec_names = result["recipe"] # list of more specific categories of the input ingredient
        print(f"Name: {spec_names['label']}")
        print(f"Link: {spec_names['url']}")
        print()
        
def main():
    start_search = input("Do you want to start searching for ingredients? (Y/N) ")
    if (start_search.lower() == 'y'):
        print("Awesome, let's get started!")
        api_result()
    elif (start_search.lower() == 'n'):
        print("Oh right, see you next time.")
    else:
        print("Invalid response, please try again")
        main()
        
    is_continue = True
    while (is_continue == True):
        continue_request = input("Do you want to search for some other ingredient? (Y/N) ")
        if (continue_request.lower() == 'y'):
            is_continue = True
            api_result()
        elif (continue_request.lower() == 'n'):
            print("Hope you have found what you need. See you next time!")
            is_continue = False
        else:
            is_continue = True
            print("Invalid response, please try again")
        
if __name__ == '__main__':
    main()