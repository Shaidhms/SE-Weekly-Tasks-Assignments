import streamlit as st
import requests
import time
import pandas as pd
import numpy as np
from datetime import datetime
import json

# Configure page
st.set_page_config(
    page_title="Live Cricket Tracker",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 Live Cricket Score Tracker")

# Method 1: Auto-refresh with rerun
st.sidebar.header("Settings")
auto_refresh = st.sidebar.checkbox("Auto Refresh", value=True)
refresh_interval = st.sidebar.slider("Refresh Interval (seconds)", 5, 60, 10)

# Method 2: Manual refresh button
if st.sidebar.button("🔄 Refresh Now"):
    st.rerun()

# Placeholder for live scores (simulated data since we can't use real API without keys)
def get_live_cricket_data():
    """
    Simulate live cricket data - replace with real API call
    Real APIs: cricapi.com, cricketdata.org, or ESPN Cricket API
    """
    teams = ["India", "Australia", "England", "Pakistan", "South Africa", "New Zealand"]
    
    # Simulate multiple matches
    matches = []
    for i in range(3):
        team1, team2 = np.random.choice(teams, 2, replace=False)
        
        match_data = {
            "match_id": f"M{i+1}",
            "team1": team1,
            "team2": team2,
            "team1_score": f"{np.random.randint(150, 350)}/{np.random.randint(3, 10)}",
            "team2_score": f"{np.random.randint(150, 350)}/{np.random.randint(3, 10)}",
            "overs": f"{np.random.randint(15, 50)}.{np.random.randint(0, 6)}",
            "status": np.random.choice(["Live", "Completed", "Upcoming"]),
            "last_update": datetime.now().strftime("%H:%M:%S"),
            "current_rr": round(np.random.uniform(4.5, 8.5), 2),
            "required_rr": round(np.random.uniform(6.0, 12.0), 2)
        }
        matches.append(match_data)
    
    return matches

# Method 3: Using session state to store data
if 'match_data' not in st.session_state:
    st.session_state.match_data = []
    st.session_state.last_update = datetime.now()

# Get live data
live_matches = get_live_cricket_data()

# Display live matches
col1, col2, col3 = st.columns(3)

for i, match in enumerate(live_matches):
    with [col1, col2, col3][i]:
        # Status indicator
        status_color = "🔴" if match["status"] == "Live" else "🟢" if match["status"] == "Completed" else "🟡"
        
        st.markdown(f"""
        <div style="border: 2px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px 0;">
            <h4>{status_color} {match['team1']} vs {match['team2']}</h4>
            <p><strong>{match['team1']}:</strong> {match['team1_score']}</p>
            <p><strong>{match['team2']}:</strong> {match['team2_score']}</p>
            <p><strong>Overs:</strong> {match['overs']}</p>
            <p><strong>Status:</strong> {match['status']}</p>
            <p><strong>Current RR:</strong> {match['current_rr']}</p>
            <p><strong>Required RR:</strong> {match['required_rr']}</p>
            <p><small>Last updated: {match['last_update']}</small></p>
        </div>
        """, unsafe_allow_html=True)

# Method 4: Real-time chart updates
st.header("📈 Live Score Progression")

# Simulate score progression data
if 'score_history' not in st.session_state:
    st.session_state.score_history = pd.DataFrame(columns=['Over', 'Team1_Score', 'Team2_Score'])

# Add new data point (simulated)
current_over = len(st.session_state.score_history) + 1
if current_over <= 50:  # Max 50 overs
    new_row = pd.DataFrame({
        'Over': [current_over],
        'Team1_Score': [current_over * np.random.randint(4, 8) + np.random.randint(0, 10)],
        'Team2_Score': [current_over * np.random.randint(4, 8) + np.random.randint(0, 10)]
    })
    st.session_state.score_history = pd.concat([st.session_state.score_history, new_row], ignore_index=True)

# Display live chart
if not st.session_state.score_history.empty:
    st.line_chart(st.session_state.score_history.set_index('Over')[['Team1_Score', 'Team2_Score']])

# Method 5: Live commentary/updates
st.header("📰 Live Commentary")

commentary_placeholder = st.empty()

sample_commentary = [
    "🏏 FOUR! Beautiful cover drive by the batsman!",
    "⚡ Quick single taken, good running between the wickets",
    "🎯 SIX! That's gone way over the boundary!",
    "😮 Close call! Appeal for LBW turned down",
    "🔥 Wicket! Caught behind, what a delivery!",
    "🏃 Two runs completed, excellent placement",
]

# Display random commentary
current_comment = np.random.choice(sample_commentary)
commentary_placeholder.write(f"**Latest:** {current_comment}")

# Method 6: Live statistics
st.header("📊 Live Match Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Runs", "287", "12")
with col2:
    st.metric("Wickets", "4", "-1")
with col3:
    st.metric("Run Rate", "7.2", "0.3")
with col4:
    st.metric("Required Rate", "8.5", "1.2")

# Auto-refresh mechanism
if auto_refresh:
    time.sleep(refresh_interval)
    st.rerun()

# Real API Integration Example (commented out)
"""
# Example with real cricket API (requires API key)
def get_real_cricket_data():
    api_key = "YOUR_API_KEY"
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={api_key}&offset=0"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['data']
        else:
            st.error("Failed to fetch data")
            return []
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return []
"""

# Instructions for real implementation
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔧 For Real Implementation:")
st.sidebar.markdown("""
**APIs to use:**
- CricAPI (cricapi.com)
- ESPN Cricket API
- CricketData.org
- RapidAPI Cricket APIs

**Required:**
- API Key registration
- Replace simulated data with real API calls
- Handle API rate limits
- Error handling for network issues
""")

st.sidebar.markdown("### ⚡ Auto-refresh Options:")
st.sidebar.markdown("""
1. **st.rerun()** - Full page refresh
2. **Placeholder updates** - Update specific sections
3. **WebSocket connections** - Real-time streaming
4. **Streamlit-autorefresh** - Third-party component
""")

# Footer
st.markdown("---")
st.markdown("🏏 **Note:** This demo uses simulated data. For real cricket scores, integrate with cricket APIs like CricAPI or ESPN.")