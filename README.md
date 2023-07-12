**API KEYS NEEDED**

1.YouTube Data API v3 key:

Navigate to the Google Cloud Console at https://console.cloud.google.com/.
Sign in with your Google account or create a new one.
Create a new project by clicking on the project drop-down and selecting NEW PROJECT in the top-right corner of the header.
Give your project a name, then click CREATE.
After the project is created, navigate to the project dashboard. Click on Navigation Menu > APIs & Services > Library.
Search for YouTube Data API v3 and select it.
Click ENABLE.
After the API is enabled, click on CREATE CREDENTIALS on the right side of the screen.
Select YouTube Data API v3 for the API, Other non-UI for the application type, and Public data for the data type. Click What credentials do I need?.
Copy the API key that is displayed.


2. OAuth 2.0 Client ID and Client Secret:

Navigate back to your project dashboard.
Click on Navigation Menu > APIs & Services > Credentials.
Click CREATE CREDENTIALS and select OAuth client ID.
Configure the OAuth consent screen as needed. For the application type, select Desktop app.
Click CREATE.
Copy the Client ID and Client Secret that are displayed.
On the right side of the created credential, click Download JSON. This file (client_secret.json) will be used in the Python script to authorize the application to access YouTube on your behalf.


**HOW TO USE:**
1. get your API keys from the instructions above.
2. Put them in the config.py file.
3. Run the main.py file, youtube video URLs should look like this -> https://www.youtube.com/watch?v=2XbpmBy73j0
