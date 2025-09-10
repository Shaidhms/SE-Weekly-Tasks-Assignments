# 🕌 Islamic Companion App

[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A comprehensive Islamic companion application built with Streamlit, designed to help Muslims in their daily religious practices and learning.

## 📱 Features

### 🏠 Dashboard
- Real-time overview of daily Islamic activities
- Next prayer time countdown
- Daily Quranic verse display
- Progress metrics for prayers, dhikr, and goals

### 🕐 Prayer Times
- Display of all 5 daily prayers (Fajr, Dhuhr, Asr, Maghrib, Isha)
- Current prayer time highlighting
- Interactive prayer schedule visualization
- Location-based prayer times (ready for API integration)

### 📖 Daily Quran Reading
- Surah and Ayah selection interface
- Beautiful Arabic text display with translations
- Reading progress tracking
- Audio recitation support (ready for API integration)

### 📿 Digital Dhikr Counter
- Interactive counter with add/reset functionality
- Daily Adhkar checklist with completion tracking
- Target setting and progress monitoring
- Traditional dhikr phrases in Arabic with translations

### 🌙 Islamic Calendar
- Hijri to Gregorian date conversion
- Islamic months visualization
- Important Islamic dates and events
- Calendar comparison display

### 🧭 Qibla Direction
- Accurate Qibla direction calculation
- Interactive compass visualization
- GPS coordinate input
- Direction bearing display in degrees

### 🎯 Daily Islamic Goals
- Track 5 categories: Prayers, Quran Reading, Dhikr, Du'a, Learning
- Progress bars and completion percentages
- Weekly progress charts and analytics
- Customizable targets

### 📚 Islamic Knowledge Center
- **Pillars of Islam**: Detailed explanations of the five pillars
- **Islamic History**: Timeline of important historical events
- **Daily Hadith**: Authentic sayings of Prophet Muhammad (PBUH)
- **Interactive Quiz**: Test your Islamic knowledge

### 🤲 Du'a Collection
- Categorized authentic supplications
- Arabic text with translations and transliterations
- Categories: Daily, Travel, Food, Morning/Evening, Special Occasions
- Easy-to-read formatting

### 📊 Prayer Tracker
- Daily prayer completion checkboxes
- Weekly and monthly prayer statistics
- Visual analytics and completion rates
- Historical prayer data tracking

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Shaidhms/islam-campion-using-streamlit.git

```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
Navigate to `http://localhost:5000`

## 📦 Dependencies

```python
streamlit>=1.28.0
pandas>=1.5.0
plotly>=5.0.0
datetime
math
```

Create a `requirements.txt` file:
```txt
streamlit>=1.28.0
pandas>=1.5.0
plotly>=5.0.0
```

## 🔧 Configuration

### Sample Data
The app currently uses sample data for demonstration purposes. All features are functional with mock data.

### API Integration Ready
The application is structured for easy integration with real APIs:

- **Prayer Times**: [Aladhan API](http://api.aladhan.com/)
- **Quran Text & Audio**: [Quran API](https://quran.api-docs.io/)
- **Islamic Calendar**: [IslamicFinder API](https://www.islamicfinder.org/)
- **Geolocation**: Browser Geolocation API



## 🎨 Design Features

- **Modern UI**: Clean, Islamic-themed interface
- **Responsive Design**: Works on desktop and mobile
- **Arabic Support**: Proper RTL text rendering
- **Interactive Elements**: Dynamic counters, progress bars, charts
- **Color Scheme**: Islamic green and blue gradients
- **Typography**: Clear, readable fonts for Arabic and English

## 🛠️ Technical Architecture

```
islamic-companion-app/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── screenshots/          # App screenshots  - in progress 
├── assets/               # Static assets (future use)
└── data/                 # Sample data files - in progress 
```

### Key Technical Features

- **Session State Management**: Persistent data across pages
- **Modular Design**: Each feature as separate function
- **Custom CSS**: Enhanced styling with Islamic themes
- **Data Visualization**: Plotly charts for analytics
- **Mathematical Calculations**: Qibla direction, prayer times
- **Responsive Layout**: Multi-column layouts for different screen sizes

## 🔮 Future Enhancements

### Phase 1: API Integration
- [ ] Real prayer times API integration
- [ ] Authentic Quran text and audio
- [ ] GPS-based location detection
- [ ] Islamic calendar conversion API

### Phase 2: Community Features
- [ ] Local mosque finder
- [ ] Community prayer groups
- [ ] Islamic event calendar
- [ ] Study groups and discussions

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and test thoroughly
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex functions
- Test your changes before submitting
- Update documentation if needed
- Respect Islamic values in all contributions

## 📄 License

This project is licensed under the MIT License

## 🙏 Acknowledgments

- **Islamic Resources**: All Islamic content is based on authentic sources
- **Streamlit Community**: For the amazing framework
- **Contributors**: Thanks to all who contribute to this project
- **Islamic Organizations**: For providing authentic Islamic content APIs


## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=https://github.com/Shaidhms/islam-campion-using-streamlit&type=Date)](https://star-history.com/#yourusername/islamic-companion-app&Date)

## 📊 Project Status

![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/islamic-companion-app)
![GitHub issues](https://img.shields.io/github/issues/yourusername/islamic-companion-app)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/islamic-companion-app)
![GitHub stars](https://img.shields.io/github/stars/yourusername/islamic-companion-app)

---

**Made with ❤️ by Shaid - for the Muslim Community**

*"And whoever relies upon Allah - then He is sufficient for him. Indeed, Allah will accomplish His purpose."* - Quran 65:3
