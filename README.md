# firstattempt

Firstattempt is a menu driven internet radio station player.  The Wrapper, or interface, consists of a menu of 7 music genres presented as listening choices, with the eighth choice being one to exit the program (0).
__
As a user selects a genre choice(inputs an integer), another python program is run using the subprocess.call function.  The integer  denotes which subprocess to run, and the subprocess simply and randomly chooses an internet radio station url from a pre-populated list.  Not coincidently, the list of radio stations are all stations of the chosen genre.  Mpg123 is used to play the chosen station, and in most cases, the station choice is displayed on the simple user interface.
__
The simplistic design should allow easy edits to the menu by swapping out Genres as needed. Also included in the repository are the sub-scripts that are called based on the menu choice. Their function is to house a list of pre defined internet stations of a particular genre.  A random selection is made by the subscript and passed back to the wrapper by the subprocess.call function. All lists deployed by the wrapper are noted by "test", followed by their menu reference as an integer, followed by "a.py".  Any list currently not deployed contains a description of the music for future reference.  There is also a template for additional or future use. 
__
For now, firstattempt is designed to be a sandbox for testing.  A subsequent attempt will be derived to have buttons replace the menu, with a color code on the button representing a genre instead of an integer menu choice.
