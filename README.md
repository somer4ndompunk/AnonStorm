AnonStorm v2.0

*********
*Credits*
*********
Jedipi especially, thank you so much for the awesome additions and core of this project <3
Prophet and kyzersane for the input and initial guidance in the project

**********************
*Requirements & Setup*
**********************
     Python, Python-Twitter, Python-pip, OAuth2, simplejson, httplib2

********
*Debian*
********
   sudo apt-get install python
   sudo apt-get install python-pip
   sudo pip install python-twitter

*********
*Windows*
*********
Replace XX with your python version number. Example: Python10, Python27, Python31, etc

   reference: https://python-guide.readthedocs.org/en/latest/starting/install/win.html
   Install Python
   Create scripts folder in C:\PythonXX -> "C:\PythonXX\Scripts"
   distribute and pip

Pip & Distribute setup

   Save http://python-distribute.org/distribute_setup.py to scripts folder (You do not need virtualenv)
   Set environment variables. Change the system variable "path" and add ";C:\Python27\;C:\Python27\Scripts\"
   Open CMD
   cd C:\PythonXX
   execute easy_install pip
   Let it run the setup and wait for it to finish

Install dependencies

   execute pip install python-twitter
   End result -> "Successfully installed python-twitter simplejson oauth2 httplib2"
                                *****
                                *Mac*
                                *****
   sudo easy_install pip
   sudo pip install python-twitter

*******
*Usage*
*******
You MUST run auth.py prior to running the storm.py script.
Simply run "python auth.py" and follow the onscreen instructions.
The end result is you will now have an Access Token Key and an Access Token Secret, be sure to save these somewhere safe for future use.
If you save the Key and Secret, there is no need to run this script again, unless you intend to use more than 1 account with the script.

To run the storm script:

   python storm.py --access_token_key <twitter access_token_key> --access_token_secret <twitter access_token_secret> --tweet_file_url <tweet_file_url>  (optional; if not used, will default to AnonStorm/TweetLog.txt)

This script can run with more than one instance. You will need to enter your Key and Secret each time you run the script. This means if you open 5 command windows, each can utilize it's own Key and Secret.

*********************************
*Setting a Static Key and Secret*
*********************************
If you so wish, you can save your Key and Secret within the script and not have to use the --access_token_secret and --access_token_key with each run.
To do this, edit the storm.py file and locate lines 62 and 63, they look like:

    arg_parser.add_argument("--access_token_key",required=True,type=str,help="Twitter access token key (see file for instructions)")
    arg_parser.add_argument("--access_token_secret",required=True,type=str,help="Twitter access token secret (see file for instructions)")

Simply add default="YOUR_KEY_HERE" on line 62 and
default="YOUR_SECRET_HERE" on line 63, like so:

    arg_parser.add_argument("--access_token_key",default="ggadhfj543ddbvbt543",required=True,type=str,help="Twitter access token key (see file for instructions)")
    arg_parser.add_argument("--access_token_secret",default="gghcnryhghbvvc854336vjnhy6",required=True,type=str,help="Twitter access token secret (see file for instructions)")

Then save the file.
YOU WILL STILL RETAIN ABILITY TO OVERRIDE BY USING THE --access_token_key and --access_token_secret ARGUMENTS
