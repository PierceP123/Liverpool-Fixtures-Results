# ⚽ Liverpool Fixtures-Results Script

This Python script pulls **Liverpool FC's** fixtures-results for the 24/25 season using the free [Football-Data.org](https://www.football-data.org/) API. It can be easily changed to display the fixtures and results of any team by changing the team ID.

## ✨ Features

- 🏆 **Pull Fixtures and Results**: Displays Liverpool's fixtures and results, with details about the competition, teams, scores, and the date/time in Sydney (Australia) timezone (can be changed based on location).
- 🔄 **Team Customization**: You can change the team by modifying the `LIVERPOOL_ID` variable in the script to the desired team's ID.
- 🆓 **Free API Access**: The Football-Data.org API provides free access to football data. Simply sign up for an API key and use it in the script.

## 🛠️ Requirements

- 🐍 **Python 3.x**
- 📦 **requests** library
- 🌍 **pytz** library
- 🔑 **python-dotenv** for loading environment variables

### 🧰 Install the required libraries:

- pip install requests python-dotenv pytz

### 🚀 Usage

- **API key access:** Go to Football-Data.org and sign up for a free API key.
- **Set up your environment:**

- Create a .env file in the root of the project.
- Add your API key to the .env file:
- bash
- Copy code
- API_KEY=your_api_key_here
- **Run the script:**
- bash
- Copy code
- python liverpool_fixtures.py
- Change the team (Optional):
- Replace LIVERPOOL_ID with the ID of the team you want to get fixtures-results for. You can find the team IDs in the API documentation.

### 🔮 Future Updates
- **📅 Google Calendar Integration:** Future updates will include integration with the Google Calendar API. This will allow fixtures and results to be added directly to your phone's calendar.
- **⚙️ Automation on a Server:** Plans to run this script as an automated service on a server, ensuring that fixtures and results are updated regularly without manually running script.