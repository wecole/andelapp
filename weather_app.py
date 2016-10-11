"""Weather app

--help
If you get an error , re-check the spelling of the city/town.
Though some places are not incorporated into the api, for example Turkana
All major towns in Kenya have their info in the api


"""
from docopt import docopt #import docopt lib
city = str(raw_input('Enter City/Town Name(e.g Nairobi) :  ')) #gets raw data from user
#city='nairobi'
import urllib2 #imports urllib2 library (am using python 2 thats why)
response = urllib2.urlopen('http://api.wunderground.com/api/edac91112bb37041/conditions/q/CA/'+city+'.json') #equivalent to the HTTP verb of GET
feedback = response.read() #info is read and stored in variable called feedback
print feedback #info is printed for the user




if __name__ == '__main__': #initialises the docopt lib
    arguments = docopt(__doc__, version='andela_1.0.0')
    print(arguments)
