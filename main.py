import streamlit as st

# Custom CSS styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Set colors for both light and dark modes
primary_color = "#6C63FF"  # Purple
secondary_color = "#FF6B6B"  # Coral
background_color = "#FFFFFF"  # White
text_color = "#000000"  # Black
card_color = "#F5F5F5"  # Light Gray

# Custom CSS
custom_css = f"""
    <style>
        :root {{
            --primary-color: {primary_color};
            --secondary-color: {secondary_color};
            --background-color: {background_color};
            --text-color: {text_color};
            --card-color: {card_color};
        }}
        @media (prefers-color-scheme: dark) {{
            :root {{
                --background-color: #1A1A1A;
                --text-color: #FFFFFF;
                --card-color: #2D2D2D;
            }}
        }}
        .css-1aumxhk {{
            background-color: var(--background-color);
            color: var(--text-color);
        }}
        .st-bb {{ background-color: var(--background-color); }}
        .st-at {{ background-color: var(--primary-color); }}
        .footer {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: teal;
            color: white;
            text-align: center;
            padding: 1rem;
            border-radius: 15px 15px 0 0;
        }}
        .navbar {{
            padding: 2rem;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            animation: fadeIn 1s ease-in-out;
            text-align: center;
        }}
        .conversion-box {{
            background-color: var(--card-color);
            padding: 2rem;
            border-radius: 15px;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .conversion-box:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.2);
        }}
        .info-box {{
            background-color: var(--card-color);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .info-box:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.2);
        }}
        .stButton>button {{
            background-color: var(--primary-color);
            color: white;
            border-radius: 8px;
            padding: 0.5rem 2rem;
            font-size: 1rem;
            transition: all 0.3s ease;
        }}
        .stButton>button:hover {{
            transform: scale(1.05);
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }}
        @keyframes fadeIn {{
            0% {{ opacity: 0; transform: translateY(-20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
    """

# Unit conversion functions
def convert_units(value, from_unit, to_unit, conversion_type):
    conversions = {
        'length': {
            'meter': 1,
            'kilometer': 1000,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'mile': 1609.34,
            'yard': 0.9144,
            'foot': 0.3048,
            'inch': 0.0254
        },
        'mass': {
            'kilogram': 1,
            'gram': 0.001,
            'milligram': 1e-6,
            'pound': 0.453592,
            'ounce': 0.0283495,
            'tonne': 1000
        },
        'force': {
            'newton': 1,
            'kilonewton': 1000,
            'pound-force': 4.44822,
            'kilogram-force': 9.80665
        },
        'temperature': {
            'celsius': ('fahrenheit', lambda x: (x * 9/5) + 32),
            'fahrenheit': ('celsius', lambda x: (x - 32) * 5/9),
            'kelvin': ('celsius', lambda x: x - 273.15)
        },
        'volume': {
            'liter': 1,
            'milliliter': 0.001,
            'gallon': 3.78541,
            'quart': 0.946353,
            'pint': 0.473176,
            'cup': 0.24
        },
        'time': {
            'second': 1,
            'minute': 60,
            'hour': 3600,
            'day': 86400,
            'week': 604800,
            'year': 31536000
        },
        'area': {
            'square meter': 1,
            'square kilometer': 1e6,
            'square mile': 2.58999e6,
            'acre': 4046.86,
            'hectare': 10000,
            'square foot': 0.092903,
            'square inch': 0.00064516
        },
        'speed': {
            'meters per second': 1,
            'kilometers per hour': 0.277778,
            'miles per hour': 0.44704,
            'knots': 0.514444,
            'feet per second': 0.3048
        },
        'pressure': {
            'pascal': 1,
            'bar': 1e5,
            'atmosphere': 101325,
            'psi': 6894.76,
            'torr': 133.322
        },
        'energy': {
            'joule': 1,
            'kilojoule': 1e3,
            'calorie': 4.184,
            'kilocalorie': 4184,
            'BTU': 1055.06,
            'kilowatt-hour': 3.6e6,
            'electronvolt': 1.60218e-19
        },
        'power': {
            'watt': 1,
            'kilowatt': 1e3,
            'megawatt': 1e6,
            'horsepower (metric)': 735.499,
            'horsepower (imperial)': 745.7
        },
        'electricity': {
            'coulomb': 1,
            'ampere-hour': 3600,
            'milliampere-hour': 3.6
        }
    }
    
      if conversion_type == 'temperature':
        if from_unit == to_unit:
            return value
        # Convert to Celsius first if needed
        if from_unit == 'fahrenheit':
            value = (value - 32) * 5/9  # Convert Fahrenheit to Celsius
        elif from_unit == 'kelvin':
            value = value - 273.15  # Convert Kelvin to Celsius
        # Now convert from Celsius to the target unit
        if to_unit == 'celsius':
            return value
        elif to_unit == 'fahrenheit':
            return (value * 9/5) + 32  # Convert Celsius to Fahrenheit
        elif to_unit == 'kelvin':
            return value + 273.15  # Convert Celsius to Kelvin
    else:
        return value * conversions[conversion_type][from_unit] / conversions[conversion_type][to_unit]

# Static currency conversion rates (as of a specific date)
CURRENCY_RATES = {
    'USD': 1.0,       # US Dollar (Base)
    'EUR': 0.92,      # Euro
    'GBP': 0.79,      # British Pound
    'JPY': 144.50,    # Japanese Yen
    'INR': 82.90,     # Indian Rupee
    'PKR': 277.50,    # Pakistani Rupee
    'AUD': 1.54,      # Australian Dollar
    'CAD': 1.35,      # Canadian Dollar
    'CNY': 7.25,      # Chinese Yuan
    'AED': 3.67       # UAE Dirham
}

# Currency conversion function
def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    # Convert to USD first, then to target currency
    amount_in_usd = amount / CURRENCY_RATES[from_currency]
    return amount_in_usd * CURRENCY_RATES[to_currency]

# Main app
def main():
    st.set_page_config(page_title="Ultimate Converter Pro", page_icon="🌐", layout="wide")
    
    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    
    # Sidebar for navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center;">
            <h1 style='color:orange;'>🌐 Ultimate Converter Pro</h1>
            <p style="color:teal;">Your All-in-One Conversion Solution 🔄</p>
        </div>
        """, unsafe_allow_html=True)
        
        # User name input
        user_name = st.text_input("Enter your name to personalize your experience:", placeholder="John Doe")
        if user_name:
            st.markdown(f"""
            <div style="text-align:center; margin:1rem 0;">
                <h2 style="color:green;">Welcome, {user_name}! 👋</h2>
            </div>
            """, unsafe_allow_html=True)
        
        # Conversion type selection
        conversion_type = st.radio("Choose Conversion Type", ["📏 Unit Converter", "💱 Currency Converter"])
    
    # Main content
    if conversion_type == "📏 Unit Converter":
        st.markdown("""
        ## 📐 Unit Conversion
        Convert between various units with ease and precision! Here's why you'll love it:
        - 🎯 **Accurate Results**: Reliable and precise conversions.
        - 🚀 **Fast & Easy**: Instant results at your fingertips.
        - 🌍 **Wide Range**: From length to electricity, we've got it all!
        """)
        
        conversion_types = {
            '📏 Length': 'length',
            '⚖️ Mass': 'mass',
            '🏋️ Force': 'force',
            '🌡️ Temperature': 'temperature',
            '🧪 Volume': 'volume',
            '⏳ Time': 'time',
            '📐 Area': 'area',
            '🚀 Speed': 'speed',
            '💨 Pressure': 'pressure',
            '⚡ Energy': 'energy',
            '🔌 Power': 'power',
            '🔋 Electricity': 'electricity'
        }
        
        selected = st.selectbox("Choose Conversion Type", list(conversion_types.keys()))
        conversion_type = conversion_types[selected]
        
        units = {
            'length': ['meter', 'kilometer', 'centimeter', 'millimeter', 'mile', 'yard', 'foot', 'inch'],
            'mass': ['kilogram', 'gram', 'milligram', 'pound', 'ounce', 'tonne'],
            'force': ['newton', 'kilonewton', 'pound-force', 'kilogram-force'],
            'temperature': ['celsius', 'fahrenheit', 'kelvin'],
            'volume': ['liter', 'milliliter', 'gallon', 'quart', 'pint', 'cup'],
            'time': ['second', 'minute', 'hour', 'day', 'week', 'year'],
            'area': ['square meter', 'square kilometer', 'square mile', 'acre', 'hectare', 'square foot', 'square inch'],
            'speed': ['meters per second', 'kilometers per hour', 'miles per hour', 'knots', 'feet per second'],
            'pressure': ['pascal', 'bar', 'atmosphere', 'psi', 'torr'],
            'energy': ['joule', 'kilojoule', 'calorie', 'kilocalorie', 'BTU', 'kilowatt-hour', 'electronvolt'],
            'power': ['watt', 'kilowatt', 'megawatt', 'horsepower (metric)', 'horsepower (imperial)'],
            'electricity': ['coulomb', 'ampere-hour', 'milliampere-hour']
        }
        
           
        with st.container():
            st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            
            with col1:
                value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1)
            
            with col2:
                from_unit = st.selectbox("From", units[conversion_type])
            
            with col3:
                to_unit = st.selectbox("To", units[conversion_type])
            
            if st.button("Convert", key="unit_convert"):
                result = convert_units(value, from_unit, to_unit, conversion_type)
                st.markdown(f"""
                <div style="text-align:center; margin:2rem 0;">
                    <h3>{value} {from_unit} =</h3>
                    <h2 style="color: var(--primary-color);">{round(result, 6)} {to_unit}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Conversion Tips in beautiful boxes
        st.markdown("## 📚 Conversion Tips & Facts")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-box">
                <h4>Temperature Tips 🌡️</h4>
                <ul>
                    <li>Water freezes at 0°C (32°F)</li>
                    <li>Human body temperature: 37°C (98.6°F)</li>
                    <li>Absolute zero: -273.15°C</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-box">
                <h4>Energy Facts ⚡</h4>
                <ul>
                    <li>1 calorie = energy to raise 1g water by 1°C</li>
                    <li>1 BTU = energy to raise 1lb water by 1°F</li>
                    <li>1 kWh = 3.6 million joules</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-box">
                <h4>Metric System 📏</h4>
                <ul>
                    <li>Used worldwide except 3 countries</li>
                    <li>Based on powers of 10</li>
                    <li>Official name: SI (Système International)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-box">
                <h4>Electricity Basics 🔋</h4>
                <ul>
                    <li>1 ampere-hour = 3600 coulombs</li>
                    <li>1 volt = 1 joule per coulomb</li>
                    <li>1 ohm = 1 volt per ampere</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    elif conversion_type == "💱 Currency Converter":
        st.markdown("""
        ## 💱 Currency Conversion
        Convert between world currencies using fixed exchange rates.
        <small style="opacity:0.7;">(Rates are for demonstration purposes only)</small>
        """, unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            
            with col1:
                amount = st.number_input("Enter Amount", min_value=0.0, value=1.0, step=0.1, key="currency_amount")
            
            with col2:
                from_currency = st.selectbox("From Currency", list(CURRENCY_RATES.keys()), key="from_currency")
            
            with col3:
                to_currency = st.selectbox("To Currency", list(CURRENCY_RATES.keys()), key="to_currency")
            
            if st.button("Convert", key="currency_convert"):
                result = convert_currency(amount, from_currency, to_currency)
                st.markdown(f"""
                <div style="text-align:center; margin:2rem 0;">
                    <h3>{amount} {from_currency} =</h3>
                    <h2 style="color: var(--primary-color);">{round(result, 4)} {to_currency}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Currency Tips
        st.markdown("## 💹 Currency Facts")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-box">
                <h4>World Currencies 🌍</h4>
                <ul>
                    <li>USD: United States Dollar</li>
                    <li>EUR: Euro (European Union)</li>
                    <li>JPY: Japanese Yen</li>
                    <li>GBP: British Pound</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-box">
                <h4>Exchange Rates 💱</h4>
                <ul>
                    <li>Rates are fixed for demonstration</li>
                    <li>Real rates fluctuate daily</li>
                    <li>Central banks influence rates</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        Made with ❤️ by Conversion Master Pro |
        ℹ️ Certified Accurate Conversions 
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
