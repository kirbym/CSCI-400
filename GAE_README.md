Michael Kirby - wrote sections of python and html files
Andrew Kittridge - wrote sections of python and html files
Tyler Scott - wrote sections of python and html files

Application link:
https://crypto-truck-162319.appspot.com/

Google App Engine Services: Memcache, Users, Mail

Description:
We decided to create a simple survey application. This survey asks for the user's name; whether they are male or female;
if they prefer memes, cats, or dogs; and finally what their favorite programming language is from a choice of PHP, Java, Python,
C#, and C++. Upon submitting the selections, the results of the survey are tabulated on the side of the page and are updated
whenever another survey is successfully completed. The user also has the option of sending the results of the survey to the
email they are currently signed in with.

We used Google's Users service in order to get the current user. If the user is already signed in with an account under the Google
umbrella, then the user is automatically directed to the Survey page. If the user is not signed in, the application invokes 
Google's sign-on protocol, and after logging in, the user is taken to the survey page. The Users module is also used to get the
current user's email address so as to be able to send an email message with survey results.

Google's Memcache service was used to help keep track of the survey results as well as what users signed on. After a survey is
completed, memcache is checked to see if that value has been chosen before. If it has, then the number of times that the value has
been chosen increases by one. If not, the value is added to memcache for quick retrieval the next time it is chosen.

The Mail service from Google was used to simply send an email message through Gmail on behalf of the application. This makes it
incredibly easy to send emails from an App Engine application as Google is able to handle all the necessary steps to physically
send the email while the programmer only has to call a function.
