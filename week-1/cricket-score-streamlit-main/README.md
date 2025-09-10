# 🏏 Live Cricket Score Tracker

A real-time cricket score tracking application built with Streamlit that displays live match data, score progressions, commentary, and statistics.

![Cricket Tracker Demo](https://img.shields.io/badge/demo-streamlit-red) ![Python](https://img.shields.io/badge/python-3.8+-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Features

- **📱 Live Score Updates** - Real-time cricket match scores with auto-refresh ( currently static live after api integration) 
- **📈 Score Progression Charts** - Visual representation of score trends over time  
- **📰 Live Commentary** - Ball-by-ball updates and match events
- **📊 Match Statistics** - Live run rates, required rates, and key metrics
- **🔄 Auto-Refresh** - Configurable refresh intervals (5-60 seconds)
- **🎯 Multiple Matches** - Track multiple ongoing matches simultaneously
- **📱 Responsive Design** - Works on desktop and mobile devices



## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shaidhms/cricket-score-streamlit.git
   cd live-cricket-tracker
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv cricket-env
   source cricket-env/bin/activate  # On Windows: cricket-env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   ```
   http://localhost:8501
   ```

## 📦 Dependencies

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
requests>=2.31.0
plotly>=5.15.0
```

## ⚙️ Configuration

### API Setup (for real data)

1. **Get API Key**
   - Sign up at [CricAPI](https://www.cricapi.com/)
   - Or use [ESPN Cricket API](https://www.espncricinfo.com/ci/content/site/developer/)

2. **Environment Variables**
   ```bash
   # Create .env file
   CRICKET_API_KEY=your_api_key_here
   REFRESH_INTERVAL=10
   ```

3. **Update API Configuration**
   ```python
   # In app.py, replace simulated data function
   def get_live_cricket_data():
       api_key = os.getenv('CRICKET_API_KEY')
       url = f"https://api.cricapi.com/v1/currentMatches?apikey={api_key}"
       # ... rest of API logic
   ```

## 🎯 Usage

### Basic Usage
```python
# Run the app
streamlit run app.py

# Access features:
# - Toggle auto-refresh in sidebar
# - Adjust refresh intervals
# - View multiple match cards
# - Monitor live charts
```

### Advanced Features

**Custom Refresh Intervals:**
```python
# Modify refresh settings
refresh_interval = st.sidebar.slider("Refresh Interval (seconds)", 5, 60, 10)
```

**API Integration:**
```python
# Replace with your preferred cricket API
def get_real_cricket_data():
    # Your API implementation
    pass
```

## 📁 Project Structure

```
live-cricket-tracker/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation

```

## 🔧 Customization

### Adding New Data Sources

1. **Create API Client**
   ```python
   # utils/api_client.py
   class CricketAPIClient:
       def __init__(self, api_key):
           self.api_key = api_key
       
       def get_live_matches(self):
           # Your API logic here
           pass
   ```

2. **Update Main App**
   ```python
   # Import your client
   from utils.api_client import CricketAPIClient
   
   # Use in main app
   client = CricketAPIClient(api_key)
   matches = client.get_live_matches()
   ```

### Styling Customization

```python
# Custom CSS
st.markdown("""
<style>
.match-card {
    border: 2px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)
```


## 📊 Available APIs

| API Service | Free Tier | Features | Rate Limit |
|-------------|-----------|----------|------------|
| CricAPI | ✅ | Live scores, commentary | 100 req/day |
| ESPN Cricket | ✅ | Comprehensive data | Varies |
| RapidAPI Cricket | 💰 | Multiple providers | Plan-based |
| CricketData.org | ✅ | Open source | Unlimited |



## 📝 License

This project is licensed under the MIT License 

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - Amazing framework for data apps
- [CricAPI](https://www.cricapi.com/) - Cricket data API
- [Plotly](https://plotly.com/) - Interactive visualizations
- Cricket community for inspiration

## 🔮 Roadmap

- [ ] **v2.0** - WebSocket real-time updates
- [ ] **v2.1** - Player statistics integration
- [ ] **v2.2** - Historical match data
- [ ] **v2.3** - Mobile app version
- [ ] **v2.4** - Machine learning predictions
- [ ] **v2.5** - Multi-language support

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Built with ❤️ by Shaid using Streamlit** | **Happy Coding!** 🏏
