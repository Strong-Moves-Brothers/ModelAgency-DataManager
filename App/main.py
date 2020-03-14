from App.app import ModelAgencyDataManagerApp

"""
WARNING1: The termination Team and Course can be confusing, but the choice of this name is because, class would be 
really more confusing.
WARNING2: Remember to change the inputs in the Initializer __init__ to your own MySQL user, password and database.
"""


if __name__ == '__main__':
    ModelAgencyDataManagerApp().run()