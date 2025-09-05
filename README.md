# ⚽ Liverpool Fixtures-Results Script

This Python script pulls **Liverpool FC's** fixtures-results for the 24/25 season using the free [Football-Data.org](https://www.football-data.org/) API. It can be easily changed to display the fixtures and results of any team by changing the team ID. Added Google Calendar API to automatically add fixtures to your phones calendar.

![Screenshot 2024-10-15 120849](https://github.com/user-attachments/assets/e8ff6838-88c9-4d4c-a60a-a33c6750ad61)

## ✨ Features

- 🏆 **Pull Fixtures and Results**: Displays Liverpool's fixtures and results, with details about the competition, teams, scores, and the date/time in Sydney (Australia) timezone (can be changed based on location).
- 🔄 **Team Customization**: You can change the team by modifying the `LIVERPOOL_ID` variable in the script to the desired team's ID.
- 🆓 **Free API Access**: The Football-Data.org API provides free access to football data. Simply sign up for an API key and use it in the script.
- 📅 **Google Calendar**: Adds all Liverpool fixtures for the season 24/25 to mobiles calendar using Google Calendar API. Giving updates of fixtures and times.

## 🛠️ Requirements

- 🐍 **Python 3.x**
- 📦 **requests** library
- 🌍 **pytz** library
- 🔑 **python-dotenv** for loading environment variables

### 🧰 Install the required libraries:

- pip install requests python-dotenv pytz
- pip install requests python-dotenv pytz google-api-python-client google-auth-httplib2 google-auth-oauthlib

### 🚀 Usage

- **API key access:** Go to Football-Data.org and sign up for a free API key. Go to Google Cloud Console for OAuth 2.0 json file.
- **Set up your environment:**

- Create a .env file in the root of the project.
- Add your API key to the .env file:
- bash
- Copy code
- API_KEY=api_key
- **Run the script:**
- bash
- Copy code
- python fixtures-results.py
- Change the team (Optional):
- Replace LIVERPOOL_ID with the ID of the team you want to get fixtures-results for. You can find the team IDs in the API documentation.

### 🔮 Future Updates
- **⚙️ Automation on a Server:** Plans to run this script as an automated service on a server, ensuring that fixtures and results are updated regularly without manually running script.
-  **🔁 Automation Run Time:** In future will add syncing so calendar will stau up to date on results/changed fixtures or any chances.
