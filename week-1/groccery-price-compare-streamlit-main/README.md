# 🛒 Grocery Price Comparison App

A comprehensive Streamlit web application that compares grocery prices across three major Indian online grocery platforms: **Zepto**, **Blinkit**, and **BigBasket**.


## 🚀 Features

- **Multi-Platform Comparison**: Compare prices across Zepto, Blinkit, and BigBasket
- **Smart Product Selection**: Choose from predefined common groceries or add custom items
- **Real-time Price Analysis**: Get instant best deal recommendations
- **Interactive Dashboard**: Clean, modern UI with responsive design
- **Data Export**: Download comparison results as CSV
- **Performance Metrics**: Platform-wise statistics and insights
- **Progress Tracking**: Real-time search progress indicators

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Web Scraping**: Requests, BeautifulSoup4
- **Data Processing**: Pandas
- **Styling**: Custom CSS
- **Python**: 3.8+

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shaidhms/groccery-price-compare-streamlit.git
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
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
   - Navigate to `http://localhost:5000`
   - The app will automatically open in your default browser

## 📋 Requirements

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
requests>=2.31.0
beautifulsoup4>=4.12.0
pandas>=2.0.0
lxml>=4.9.0
```

## 🎯 Usage

### Quick Start

1. **Select Products**: Choose from predefined items or add custom products
2. **Search Prices**: Click "Search Prices" to fetch current prices
3. **View Results**: Analyze prices in the comparison table
4. **Best Deals**: Check the best deal recommendations
5. **Export Data**: Download results as CSV for future reference

### Predefined Products

The app comes with these common grocery items:
- Milk (1L)
- Bread
- Eggs (12 pieces)
- Rice (1kg)
- Cooking Oil (1L)
- Sugar (1kg)

### Custom Products

Add up to 6 custom grocery items using the sidebar input fields.

## 🏗️ Project Structure

```
grocery-price-comparison/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation

```

## 🔧 Configuration

### Customizing Mock Data

Currently, the app uses mock data for demonstration. To modify prices, edit the mock_prices dictionaries in the scraper methods:

```python
mock_prices = {
    "milk": 65.0,
    "bread": 25.0,
    "eggs": 85.0,
    # Add more products
}
```

### Adding Real Web Scraping

To implement real web scraping:

1. Study each platform's HTML structure
2. Handle dynamic content loading
3. Implement proper error handling
4. Add rate limiting and respect robots.txt

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly
- Ensure compatibility with Python 3.8+

## 🐛 Known Issues

- **Mock Data**: Currently using simulated data instead of real web scraping
- **Rate Limiting**: No rate limiting implemented for actual scraping
- **Location-based Pricing**: Doesn't account for location-specific prices
- **Product Matching**: Simple keyword matching may not be accurate

## 🔮 Roadmap

### Version 2.0
- [ ] Real web scraping implementation
- [ ] User location-based pricing
- [ ] Price history tracking
- [ ] Email notifications for price drops
- [ ] Mobile-responsive design improvements

### Version 2.1
- [ ] Additional platforms (Amazon Fresh, Dunzo)
- [ ] Product categorization
- [ ] Advanced filtering options
- [ ] API integration for real-time data

## 📈 Performance

- **Load Time**: ~2-3 seconds for mock data
- **Memory Usage**: ~50MB typical
- **Concurrent Users**: Suitable for personal use
- **Data Processing**: Handles 6+ products simultaneously

## 🔒 Privacy & Legal

- **No Personal Data**: App doesn't collect user information
- **Respect robots.txt**: Implement proper scraping etiquette
- **Terms of Service**: Ensure compliance with platform ToS
- **Rate Limiting**: Implement respectful scraping practices


## 📄 License

This project is licensed under the MIT License 

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 🙏 Acknowledgments

- **Streamlit Team**: For the amazing framework
- **BeautifulSoup**: For web scraping capabilities
- **Pandas**: For data manipulation


## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/grocery-price-comparison)
![GitHub forks](https://img.shields.io/github/forks/yourusername/grocery-price-comparison)
![GitHub issues](https://img.shields.io/github/issues/yourusername/grocery-price-comparison)

---

**Made with ❤️ by Shaid using Streamlit**

*If this project helped you, please consider giving it a ⭐!*
