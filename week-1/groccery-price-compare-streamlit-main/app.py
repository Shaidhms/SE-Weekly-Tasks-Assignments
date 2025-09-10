import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from urllib.parse import quote

# Set page config
st.set_page_config(
    page_title="Grocery Price Comparison",
    page_icon="🛒",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 2rem;
    }
    .price-table {
        margin: 2rem 0;
    }
    .error-msg {
        background-color: #ffebee;
        color: #c62828;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success-msg {
        background-color: #e8f5e8;
        color: #2e7d32;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

class GroceryPriceScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def clean_price(self, price_text):
        """Extract numeric price from text"""
        if not price_text:
            return None
        # Remove currency symbols and extract numbers
        price_match = re.search(r'[\d,]+\.?\d*', price_text.replace(',', ''))
        if price_match:
            return float(price_match.group())
        return None

    def search_zepto(self, product_name):
        """Scrape price from Zepto (mock implementation)"""
        try:
            # Note: This is a simplified mock implementation
            # In real scenario, you'd need to handle Zepto's specific API/structure
            search_url = f"https://www.zeptonow.com/search?query={quote(product_name)}"
            
            # Simulate API call delay
            time.sleep(1)
            
            # Mock response - replace with actual scraping logic
            mock_prices = {
                "milk": 65.0,
                "bread": 25.0,
                "eggs": 85.0,
                "rice": 45.0,
                "oil": 180.0,
                "sugar": 55.0
            }
            
            for key in mock_prices:
                if key.lower() in product_name.lower():
                    return mock_prices[key]
            
            return None
            
        except Exception as e:
            st.warning(f"Zepto scraping failed for {product_name}: {str(e)}")
            return None

    def search_blinkit(self, product_name):
        """Scrape price from Blinkit (mock implementation)"""
        try:
            # Note: This is a simplified mock implementation
            search_url = f"https://blinkit.com/search?q={quote(product_name)}"
            
            time.sleep(1)
            
            # Mock response - replace with actual scraping logic
            mock_prices = {
                "milk": 68.0,
                "bread": 28.0,
                "eggs": 90.0,
                "rice": 48.0,
                "oil": 175.0,
                "sugar": 58.0
            }
            
            for key in mock_prices:
                if key.lower() in product_name.lower():
                    return mock_prices[key]
            
            return None
            
        except Exception as e:
            st.warning(f"Blinkit scraping failed for {product_name}: {str(e)}")
            return None

    def search_bigbasket(self, product_name):
        """Scrape price from BigBasket (mock implementation)"""
        try:
            # Note: This is a simplified mock implementation
            search_url = f"https://www.bigbasket.com/search/?q={quote(product_name)}"
            
            time.sleep(1)
            
            # Mock response - replace with actual scraping logic
            mock_prices = {
                "milk": 62.0,
                "bread": 30.0,
                "eggs": 88.0,
                "rice": 50.0,
                "oil": 185.0,
                "sugar": 52.0
            }
            
            for key in mock_prices:
                if key.lower() in product_name.lower():
                    return mock_prices[key]
            
            return None
            
        except Exception as e:
            st.warning(f"BigBasket scraping failed for {product_name}: {str(e)}")
            return None

    def get_all_prices(self, products):
        """Get prices from all platforms for given products"""
        results = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        total_products = len(products)
        
        for i, product in enumerate(products):
            if product.strip():  # Only process non-empty products
                status_text.text(f"Searching prices for: {product}")
                
                zepto_price = self.search_zepto(product)
                blinkit_price = self.search_blinkit(product)
                bigbasket_price = self.search_bigbasket(product)
                
                results.append({
                    'Product': product,
                    'Zepto (₹)': zepto_price if zepto_price else "N/A",
                    'Blinkit (₹)': blinkit_price if blinkit_price else "N/A",
                    'BigBasket (₹)': bigbasket_price if bigbasket_price else "N/A",
                })
                
                # Update progress
                progress_bar.progress((i + 1) / total_products)
        
        status_text.text("Search completed!")
        time.sleep(1)
        status_text.empty()
        progress_bar.empty()
        
        return results

def main():
    st.markdown('<h1 class="main-header">🛒 Grocery Price Comparison</h1>', unsafe_allow_html=True)
    st.markdown("Compare prices of grocery items across Zepto, Blinkit, and BigBasket")
    
    # Initialize scraper
    if 'scraper' not in st.session_state:
        st.session_state.scraper = GroceryPriceScraper()
    
    # Sidebar for input
    st.sidebar.header("🔍 Search Products")
    
    # Predefined products
    st.sidebar.subheader("Quick Select:")
    predefined_products = ["Milk (1L)", "Bread", "Eggs (12 pieces)", "Rice (1kg)", "Cooking Oil (1L)", "Sugar (1kg)"]
    
    selected_predefined = st.sidebar.multiselect(
        "Choose from common items:",
        predefined_products,
        default=predefined_products[:3]
    )
    
    # Custom products
    st.sidebar.subheader("Custom Products:")
    custom_products = []
    for i in range(6):
        product = st.sidebar.text_input(f"Product {i+1}:", key=f"custom_{i}")
        if product:
            custom_products.append(product)
    
    # Combine all products
    all_products = list(selected_predefined) + custom_products
    
    # Remove duplicates while preserving order
    unique_products = []
    for product in all_products:
        if product not in unique_products:
            unique_products.append(product)
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if unique_products:
            st.subheader("Selected Products:")
            for i, product in enumerate(unique_products, 1):
                st.write(f"{i}. {product}")
    
    with col2:
        st.subheader("Actions:")
        search_button = st.button("🔍 Search Prices", type="primary")
        clear_button = st.button("🗑️ Clear All")
    
    if clear_button:
        st.experimental_rerun()
    
    # Search and display results
    if search_button and unique_products:
        st.markdown("---")
        st.subheader("🏪 Price Comparison Results")
        
        with st.spinner("Searching prices across platforms..."):
            results = st.session_state.scraper.get_all_prices(unique_products)
        
        if results:
            # Create DataFrame
            df = pd.DataFrame(results)
            
            # Display table
            st.markdown('<div class="price-table">', unsafe_allow_html=True)
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Analysis
            st.subheader("📊 Price Analysis")
            
            # Calculate best prices for each product
            analysis_data = []
            for result in results:
                prices = {}
                if isinstance(result['Zepto (₹)'], (int, float)):
                    prices['Zepto'] = result['Zepto (₹)']
                if isinstance(result['Blinkit (₹)'], (int, float)):
                    prices['Blinkit'] = result['Blinkit (₹)']
                if isinstance(result['BigBasket (₹)'], (int, float)):
                    prices['BigBasket'] = result['BigBasket (₹)']
                
                if prices:
                    best_platform = min(prices, key=prices.get)
                    best_price = prices[best_platform]
                    analysis_data.append({
                        'Product': result['Product'],
                        'Best Price': f"₹{best_price}",
                        'Best Platform': best_platform
                    })
            
            if analysis_data:
                st.subheader("🎯 Best Deals")
                analysis_df = pd.DataFrame(analysis_data)
                st.dataframe(
                    analysis_df,
                    use_container_width=True,
                    hide_index=True
                )
                
                # Platform statistics
                platform_counts = {}
                for item in analysis_data:
                    platform = item['Best Platform']
                    platform_counts[platform] = platform_counts.get(platform, 0) + 1
                
                st.subheader("🏆 Platform Performance")
                for platform, count in platform_counts.items():
                    percentage = (count / len(analysis_data)) * 100
                    st.write(f"**{platform}**: {count} best deals ({percentage:.1f}%)")
            
            # Download option
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="grocery_price_comparison.csv",
                mime="text/csv"
            )
        
        else:
            st.markdown('<div class="error-msg">No results found. Please try different products.</div>', unsafe_allow_html=True)
    
    elif search_button and not unique_products:
        st.markdown('<div class="error-msg">Please select or enter at least one product to search.</div>', unsafe_allow_html=True)
    
    # Instructions
    with st.expander("📋 How to use this app"):
        st.markdown("""
        1. **Quick Select**: Choose from predefined common grocery items
        2. **Custom Products**: Enter your own product names (up to 6 custom items)
        3. **Search**: Click 'Search Prices' to compare prices across platforms
        4. **Results**: View prices in a table format with analysis
        5. **Download**: Export results as CSV for future reference
        
        **Note**: This app uses web scraping which may take a few seconds per product.
        Results depend on product availability and current prices on the platforms.
        """)
    
    # Disclaimer
    st.markdown("---")
    st.markdown("""
    <small>
    **Disclaimer**: Prices are fetched in real-time and may vary. This tool is for comparison purposes only.
    Actual prices may differ due to location, offers, or stock availability.
    </small>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()