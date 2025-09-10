import streamlit as st
import pandas as pd
import datetime
import math
import json
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Islamic Companion App",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    .prayer-time {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .dhikr-counter {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #667eea;
    }
    .quranic-verse {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 10px;
        font-style: italic;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'dhikr_count' not in st.session_state:
    st.session_state.dhikr_count = 0
if 'prayer_tracker' not in st.session_state:
    st.session_state.prayer_tracker = {}
if 'daily_adhkar_completed' not in st.session_state:
    st.session_state.daily_adhkar_completed = []

# Sample data
PRAYER_TIMES = {
    "Fajr": "05:30",
    "Dhuhr": "12:45",
    "Asr": "16:15",
    "Maghrib": "18:30",
    "Isha": "20:00"
}

QURANIC_VERSES = [
    {
        "arabic": "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا",
        "translation": "And whoever fears Allah - He will make for him a way out",
        "reference": "Quran 65:2"
    },
    {
        "arabic": "وَمَا تَوْفِيقِي إِلَّا بِاللَّهِ",
        "translation": "And my success is not but through Allah",
        "reference": "Quran 11:88"
    },
    {
        "arabic": "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا",
        "translation": "For indeed, with hardship [will be] ease",
        "reference": "Quran 94:5"
    }
]

DAILY_ADHKAR = [
    {"dhikr": "سُبْحَانَ اللهِ", "translation": "Glory be to Allah", "count": 33},
    {"dhikr": "الْحَمْدُ للهِ", "translation": "Praise be to Allah", "count": 33},
    {"dhikr": "اللهُ أَكْبَرُ", "translation": "Allah is Greatest", "count": 34},
    {"dhikr": "لَا إِلَٰهَ إِلَّا اللهُ", "translation": "There is no god but Allah", "count": 100},
    {"dhikr": "أَسْتَغْفِرُ اللهَ", "translation": "I seek forgiveness from Allah", "count": 100}
]

ISLAMIC_CALENDAR_MONTHS = [
    "Muharram", "Safar", "Rabi' al-Awwal", "Rabi' al-Thani", 
    "Jumada al-Awwal", "Jumada al-Thani", "Rajab", "Sha'ban", 
    "Ramadan", "Shawwal", "Dhu al-Qi'da", "Dhu al-Hijja"
]

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🕌 Islamic Companion App</h1>
        <p>Your Digital Islamic Guide and Companion</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a feature:", [
        "🏠 Dashboard",
        "🕐 Prayer Times",
        "📖 Daily Quran",
        "📿 Dhikr Counter",
        "🌙 Islamic Calendar",
        "🧭 Qibla Direction",
        "🎯 Daily Goals",
        "📚 Islamic Knowledge",
        "🤲 Du'a Collection",
        "📊 Prayer Tracker"
    ])
    
    if page == "🏠 Dashboard":
        dashboard()
    elif page == "🕐 Prayer Times":
        prayer_times()
    elif page == "📖 Daily Quran":
        daily_quran()
    elif page == "📿 Dhikr Counter":
        dhikr_counter()
    elif page == "🌙 Islamic Calendar":
        islamic_calendar()
    elif page == "🧭 Qibla Direction":
        qibla_direction()
    elif page == "🎯 Daily Goals":
        daily_goals()
    elif page == "📚 Islamic Knowledge":
        islamic_knowledge()
    elif page == "🤲 Du'a Collection":
        dua_collection()
    elif page == "📊 Prayer Tracker":
        prayer_tracker()

def dashboard():
    st.header("📊 Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Today's Dhikr Count", st.session_state.dhikr_count, "Keep going!")
    
    with col2:
        completed_prayers = len([p for p in st.session_state.prayer_tracker.get(str(datetime.now().date()), {}).values() if p])
        st.metric("Prayers Completed Today", f"{completed_prayers}/5", "May Allah accept")
    
    with col3:
        current_time = datetime.now().strftime("%H:%M")
        st.metric("Current Time", current_time, "")
    
    # Next prayer time
    st.subheader("⏰ Next Prayer")
    next_prayer_info = get_next_prayer()
    if next_prayer_info:
        st.info(f"**{next_prayer_info['name']}** at {next_prayer_info['time']} ({next_prayer_info['remaining']})")
    
    # Daily verse
    st.subheader("📖 Daily Verse")
    import random
    daily_verse = random.choice(QURANIC_VERSES)
    st.markdown(f"""
    <div class="quranic-verse">
        <h3 style="text-align: center;">{daily_verse['arabic']}</h3>
        <p style="text-align: center;"><strong>{daily_verse['translation']}</strong></p>
        <p style="text-align: center; font-size: 0.9em;">{daily_verse['reference']}</p>
    </div>
    """, unsafe_allow_html=True)

def prayer_times():
    st.header("🕐 Prayer Times")
    
    # Location input
    col1, col2 = st.columns(2)
    with col1:
        city = st.text_input("City", "Mecca")
    with col2:
        country = st.text_input("Country", "Saudi Arabia")
    
    st.info("📍 Prayer times shown for sample location. In a deployed version, this would integrate with a real prayer times API.")
    
    # Display prayer times
    st.subheader(f"Prayer Times for {city}, {country}")
    
    for prayer, time in PRAYER_TIMES.items():
        is_current = is_current_prayer_time(prayer, time)
        status = "🟢 Current" if is_current else "⏰"
        
        st.markdown(f"""
        <div class="prayer-time">
            <h4>{status} {prayer}: {time}</h4>
        </div>
        """, unsafe_allow_html=True)
    
    # Prayer time chart
    st.subheader("📊 Prayer Times Visualization")
    prayer_df = pd.DataFrame(list(PRAYER_TIMES.items()), columns=['Prayer', 'Time'])
    fig = px.bar(prayer_df, x='Prayer', y='Time', title="Daily Prayer Schedule")
    st.plotly_chart(fig, use_container_width=True)

def daily_quran():
    st.header("📖 Daily Quran Reading")
    
    # Surah selection
    col1, col2 = st.columns(2)
    with col1:
        surah_number = st.number_input("Surah Number", min_value=1, max_value=114, value=1)
    with col2:
        ayah_number = st.number_input("Ayah Number", min_value=1, value=1)
    
    st.info("📚 In a deployed version, this would connect to a Quran API for real verses and audio recitation.")
    
    # Sample verse display
    sample_verse = QURANIC_VERSES[0]  # Using sample data
    st.markdown(f"""
    <div class="quranic-verse">
        <h2 style="text-align: center; direction: rtl;">{sample_verse['arabic']}</h2>
        <p style="text-align: center; font-size: 1.2em;"><strong>{sample_verse['translation']}</strong></p>
        <p style="text-align: center; color: #666;">{sample_verse['reference']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Reading progress
    st.subheader("📈 Reading Progress")
    progress = st.slider("Mark your daily reading progress", 0, 100, 0)
    st.progress(progress / 100)
    
    if st.button("🎧 Play Audio (Sample)"):
        st.success("🎵 Audio would play here with real Quran recitation API integration")

def dhikr_counter():
    st.header("📿 Digital Dhikr Counter")
    
    # Counter display
    st.markdown(f"""
    <div class="dhikr-counter">
        <h1>Current Count: {st.session_state.dhikr_count}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("➕ Add Count", type="primary"):
            st.session_state.dhikr_count += 1
            st.rerun()
    
    with col2:
        if st.button("🔄 Reset"):
            st.session_state.dhikr_count = 0
            st.rerun()
    
    with col3:
        target = st.number_input("Set Target", min_value=1, value=100)
    
    # Progress bar
    progress = min(st.session_state.dhikr_count / target, 1.0)
    st.progress(progress)
    st.write(f"Progress: {st.session_state.dhikr_count}/{target}")
    
    # Daily Adhkar checklist
    st.subheader("📋 Daily Adhkar Checklist")
    
    for i, adhkar in enumerate(DAILY_ADHKAR):
        completed = f"adhkar_{i}" in st.session_state.daily_adhkar_completed
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            **{adhkar['dhikr']}** - {adhkar['translation']} 
            
            *Target: {adhkar['count']} times*
            """)
        
        with col2:
            if st.checkbox("✅", key=f"check_{i}", value=completed):
                if f"adhkar_{i}" not in st.session_state.daily_adhkar_completed:
                    st.session_state.daily_adhkar_completed.append(f"adhkar_{i}")
            else:
                if f"adhkar_{i}" in st.session_state.daily_adhkar_completed:
                    st.session_state.daily_adhkar_completed.remove(f"adhkar_{i}")

def islamic_calendar():
    st.header("🌙 Islamic Calendar")
    
    # Current Islamic date (approximate - in real app would use proper calculation)
    gregorian_date = datetime.now()
    islamic_year = 1445  # Sample year
    islamic_month = "Rabi' al-Awwal"
    islamic_day = 15
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**Gregorian Date:** {gregorian_date.strftime('%B %d, %Y')}")
    
    with col2:
        st.info(f"**Islamic Date:** {islamic_day} {islamic_month}, {islamic_year}")
    
    # Islamic months
    st.subheader("📅 Islamic Months")
    months_df = pd.DataFrame({
        'Month': ISLAMIC_CALENDAR_MONTHS,
        'Order': range(1, 13)
    })
    
    fig = px.bar(months_df, x='Order', y='Month', orientation='h', 
                 title="Islamic Calendar Months")
    st.plotly_chart(fig, use_container_width=True)
    
    # Important Islamic dates
    st.subheader("⭐ Important Islamic Dates")
    important_dates = [
        {"Event": "Ramadan Begins", "Approximate Date": "March 10, 2024"},
        {"Event": "Laylat al-Qadr", "Approximate Date": "April 5, 2024"},
        {"Event": "Eid al-Fitr", "Approximate Date": "April 10, 2024"},
        {"Event": "Hajj Period", "Approximate Date": "June 15-20, 2024"},
        {"Event": "Eid al-Adha", "Approximate Date": "June 17, 2024"}
    ]
    
    for date_info in important_dates:
        st.markdown(f"• **{date_info['Event']}**: {date_info['Approximate Date']}")

def qibla_direction():
    st.header("🧭 Qibla Direction")
    
    # Location input
    col1, col2 = st.columns(2)
    with col1:
        lat = st.number_input("Your Latitude", value=25.2048, format="%.4f")
    with col2:
        lon = st.number_input("Your Longitude", value=55.2708, format="%.4f")
    
    # Calculate Qibla direction (simplified calculation)
    kaaba_lat = 21.4225
    kaaba_lon = 39.8262
    
    qibla_bearing = calculate_qibla_direction(lat, lon, kaaba_lat, kaaba_lon)
    
    st.success(f"🧭 Qibla Direction: {qibla_bearing:.1f}° from North")
    
    # Compass visualization
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[1, 1],
        theta=[0, qibla_bearing],
        mode='lines+markers',
        name='Qibla Direction',
        line=dict(color='green', width=5),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=False),
            angularaxis=dict(direction='clockwise', theta0=90)
        ),
        title="Qibla Compass",
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("📱 In a deployed version, this would use your device's GPS for automatic location detection.")

def daily_goals():
    st.header("🎯 Daily Islamic Goals")
    
    # Goal categories
    goals = {
        "Prayer": {"target": 5, "completed": 0},
        "Quran Reading (pages)": {"target": 2, "completed": 0},
        "Dhikr (count)": {"target": 100, "completed": st.session_state.dhikr_count},
        "Du'a": {"target": 3, "completed": 0},
        "Islamic Learning (minutes)": {"target": 30, "completed": 0}
    }
    
    st.subheader("📊 Today's Progress")
    
    for goal, data in goals.items():
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.write(f"**{goal}**")
        
        with col2:
            new_completed = st.number_input(
                "Completed", 
                min_value=0, 
                value=data["completed"], 
                key=f"goal_{goal}"
            )
        
        with col3:
            st.write(f"Target: {data['target']}")
        
        # Progress bar
        progress = min(new_completed / data["target"], 1.0)
        st.progress(progress)
        st.write(f"{new_completed}/{data['target']} ({progress*100:.0f}%)")
        st.markdown("---")
    
    # Weekly goals chart
    st.subheader("📈 Weekly Progress")
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sample_data = {
        'Day': days,
        'Prayer': [5, 4, 5, 3, 5, 5, 4],
        'Quran': [2, 1, 2, 1, 3, 2, 2],
        'Dhikr': [100, 80, 120, 60, 150, 100, 90]
    }
    
    df = pd.DataFrame(sample_data)
    fig = px.line(df, x='Day', y=['Prayer', 'Quran', 'Dhikr'], 
                  title="Weekly Islamic Activities Progress")
    st.plotly_chart(fig, use_container_width=True)

def islamic_knowledge():
    st.header("📚 Islamic Knowledge Center")
    
    tabs = st.tabs(["📖 Pillars of Islam", "🕌 Islamic History", "📚 Hadith", "🎓 Quiz"])
    
    with tabs[0]:
        st.subheader("The Five Pillars of Islam")
        pillars = [
            ("Shahada", "Declaration of Faith", "لا إله إلا الله محمد رسول الله"),
            ("Salah", "Prayer", "Five daily prayers facing Mecca"),
            ("Zakat", "Charity", "Obligatory giving to those in need"),
            ("Sawm", "Fasting", "Fasting during the month of Ramadan"),
            ("Hajj", "Pilgrimage", "Pilgrimage to Mecca at least once in lifetime")
        ]
        
        for i, (name, desc, detail) in enumerate(pillars, 1):
            with st.expander(f"{i}. {name} - {desc}"):
                st.write(f"**Details:** {detail}")
                st.write("This is a fundamental pillar that every Muslim should understand and practice.")
    
    with tabs[1]:
        st.subheader("📜 Islamic History Timeline")
        historical_events = [
            {"Year": "570 CE", "Event": "Birth of Prophet Muhammad (PBUH)"},
            {"Year": "610 CE", "Event": "First Revelation in Cave Hira"},
            {"Year": "622 CE", "Event": "Hijra - Migration to Medina"},
            {"Year": "632 CE", "Event": "Death of Prophet Muhammad (PBUH)"},
            {"Year": "661-750 CE", "Event": "Umayyad Caliphate"},
            {"Year": "750-1258 CE", "Event": "Abbasid Caliphate"}
        ]
        
        for event in historical_events:
            st.markdown(f"**{event['Year']}**: {event['Event']}")
    
    with tabs[2]:
        st.subheader("📖 Daily Hadith")
        sample_hadith = {
            "Arabic": "إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ",
            "Translation": "Actions are but by intention",
            "Source": "Sahih al-Bukhari"
        }
        
        st.markdown(f"""
        <div class="quranic-verse">
            <h3 style="text-align: center;">{sample_hadith['Arabic']}</h3>
            <p style="text-align: center;"><strong>{sample_hadith['Translation']}</strong></p>
            <p style="text-align: center; font-size: 0.9em;">Source: {sample_hadith['Source']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[3]:
        st.subheader("🎓 Islamic Knowledge Quiz")
        
        questions = [
            {
                "question": "How many chapters (Surahs) are in the Quran?",
                "options": ["110", "114", "116", "120"],
                "correct": 1
            },
            {
                "question": "What is the first pillar of Islam?",
                "options": ["Salah", "Zakat", "Shahada", "Hajj"],
                "correct": 2
            }
        ]
        
        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = []
        
        for i, q in enumerate(questions):
            st.write(f"**Question {i+1}:** {q['question']}")
            answer = st.radio("Choose your answer:", q['options'], key=f"q_{i}")
            
            if st.button(f"Submit Answer {i+1}", key=f"submit_{i}"):
                if q['options'].index(answer) == q['correct']:
                    st.success("✅ Correct!")
                    if i not in st.session_state.quiz_answered:
                        st.session_state.quiz_score += 1
                        st.session_state.quiz_answered.append(i)
                else:
                    st.error(f"❌ Incorrect. The correct answer is: {q['options'][q['correct']]}")
        
        st.write(f"Current Score: {st.session_state.quiz_score}/{len(questions)}")

def dua_collection():
    st.header("🤲 Du'a Collection")
    
    categories = st.selectbox("Choose Category:", [
        "Daily Du'as", "Travel Du'as", "Food Du'as", "Morning/Evening", "Special Occasions"
    ])
    
    duas = {
        "Daily Du'as": [
            {
                "name": "Before Sleep",
                "arabic": "اللَّهُمَّ بِاسْمِكَ أَمُوتُ وَأَحْيَا",
                "translation": "O Allah, in Your name I die and I live",
                "transliteration": "Allahumma bismika amutu wa ahya"
            }
        ],
        "Travel Du'as": [
            {
                "name": "Starting Journey",
                "arabic": "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَٰذَا",
                "translation": "Glory to Him who subjected this to us",
                "transliteration": "Subhan alladhi sakhkhara lana hadha"
            }
        ]
    }
    
    if categories in duas:
        for dua in duas[categories]:
            st.markdown(f"""
            <div class="quranic-verse">
                <h4>{dua['name']}</h4>
                <h3 style="text-align: center; direction: rtl;">{dua['arabic']}</h3>
                <p style="text-align: center;"><strong>{dua['translation']}</strong></p>
                <p style="text-align: center; font-style: italic;">{dua['transliteration']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.info("📚 In the full version, this would contain hundreds of authentic du'as from Quran and Sunnah.")

def prayer_tracker():
    st.header("📊 Prayer Tracking")
    
    today = str(datetime.now().date())
    
    if today not in st.session_state.prayer_tracker:
        st.session_state.prayer_tracker[today] = {
            "Fajr": False, "Dhuhr": False, "Asr": False, 
            "Maghrib": False, "Isha": False
        }
    
    st.subheader("Today's Prayers")
    
    col1, col2 = st.columns(2)
    
    for i, (prayer, time) in enumerate(PRAYER_TIMES.items()):
        column = col1 if i % 2 == 0 else col2
        
        with column:
            current_status = st.session_state.prayer_tracker[today].get(prayer, False)
            new_status = st.checkbox(
                f"{prayer} ({time})", 
                value=current_status,
                key=f"prayer_{prayer}"
            )
            st.session_state.prayer_tracker[today][prayer] = new_status
    
    # Prayer statistics
    st.subheader("📈 Prayer Statistics")
    
    # Create sample data for the last 7 days
    dates = [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6, -1, -1)]
    prayer_data = []
    
    for date in dates:
        if date in st.session_state.prayer_tracker:
            completed = sum(st.session_state.prayer_tracker[date].values())
        else:
            completed = 3 + (hash(date) % 3)  # Sample data
        prayer_data.append({"Date": date, "Prayers Completed": completed})
    
    df = pd.DataFrame(prayer_data)
    fig = px.bar(df, x="Date", y="Prayers Completed", 
                 title="Daily Prayer Completion (Last 7 Days)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Monthly view
    st.subheader("📅 Monthly Overview")
    monthly_completion = (sum(st.session_state.prayer_tracker[today].values()) / 5) * 100
    st.metric("Today's Completion Rate", f"{monthly_completion:.0f}%")

# Helper functions
def get_next_prayer():
    current_time = datetime.now().time()
    current_minutes = current_time.hour * 60 + current_time.minute
    
    for prayer, time_str in PRAYER_TIMES.items():
        prayer_time = datetime.strptime(time_str, "%H:%M").time()
        prayer_minutes = prayer_time.hour * 60 + prayer_time.minute
        
        if prayer_minutes > current_minutes:
            remaining_minutes = prayer_minutes - current_minutes
            hours = remaining_minutes // 60
            minutes = remaining_minutes % 60
            return {
                "name": prayer,
                "time": time_str,
                "remaining": f"{hours}h {minutes}m remaining"
            }
    
    # If no prayer found for today, return Fajr of next day
    return {
        "name": "Fajr (Tomorrow)",
        "time": PRAYER_TIMES["Fajr"],
        "remaining": "Next day"
    }

def is_current_prayer_time(prayer, time_str):
    current_time = datetime.now().time()
    prayer_time = datetime.strptime(time_str, "%H:%M").time()
    
    # Simple check if within 30 minutes of prayer time
    current_minutes = current_time.hour * 60 + current_time.minute
    prayer_minutes = prayer_time.hour * 60 + prayer_time.minute
    
    return abs(current_minutes - prayer_minutes) <= 30

def calculate_qibla_direction(lat, lon, kaaba_lat, kaaba_lon):
    """Calculate Qibla direction using simplified formula"""
    lat1 = math.radians(lat)
    lon1 = math.radians(lon)
    lat2 = math.radians(kaaba_lat)
    lon2 = math.radians(kaaba_lon)
    
    dlon = lon2 - lon1
    
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    
    bearing = math.atan2(y, x)
    bearing = math.degrees(bearing)
    bearing = (bearing + 360) % 360
    
    return bearing

if __name__ == "__main__":
    main()