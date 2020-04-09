# @author: Gopal Oswal
# @date: 8 April 2020
# @description: basic hello world

from flask import Flask #importing Flask from flask

app = Flask('__main__') # creating an app with the help of the class named as Flask

# from the app we are defining the routes by default we are having '/' route
@app.route('/')
def hello_world(): # defining a function to be called when that route url is requested
    return 'Hello, World' # returning a hello world.

# handling the error for the routes
@app.errorhandler(404)
def page_not_found(error): # defining a function to be called when that route url is requested
    return 'Page not found' # returning a page not found.