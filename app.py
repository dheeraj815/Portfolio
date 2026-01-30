import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Dheeraj Muley - AI Engineer & Full Stack Developer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Clean Professional Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main background */
    .main {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1d3a 25%, #2d1b4e 50%, #1a1d3a 75%, #0a0e27 100%);
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .block-container {
        padding: 2rem 1.5rem;
        max-width: 1400px;
    }
    
    /* Hero Section */
    .hero-wrapper {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.95) 0%, rgba(31, 41, 55, 0.9) 100%);
        backdrop-filter: blur(20px);
        padding: 50px 40px;
        border-radius: 24px;
        margin: 20px 0 50px 0;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 
                    0 0 0 1px rgba(99, 102, 241, 0.2);
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    
    .hero-name {
        font-size: 3.5rem;
        font-weight: 900;
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #818cf8 0%, #6366f1 30%, #a855f7 70%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        line-height: 1.1;
        letter-spacing: -2px;
        text-align: center;
    }
    
    .hero-role {
        font-size: 1.5rem;
        color: #818cf8;
        margin: 15px 0;
        font-weight: 700;
        text-align: center;
    }
    
    .hero-tagline {
        font-size: 1.1rem;
        color: #cbd5e1;
        max-width: 750px;
        margin: 15px auto;
        line-height: 1.7;
        text-align: center;
    }
    
    .hero-highlight {
        display: inline-flex;
        align-items: center;
        gap: 12px;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        padding: 12px 28px;
        border-radius: 50px;
        font-size: 1rem;
        color: #e0e7ff;
        font-weight: 600;
        margin: 15px 0;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
    }
    
    .availability-badge {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.15) 0%, rgba(59, 130, 246, 0.15) 100%);
        padding: 10px 24px;
        border-radius: 50px;
        font-size: 0.95rem;
        color: #86efac;
        font-weight: 600;
        border: 1.5px solid rgba(34, 197, 94, 0.3);
    }
    
    .pulse-dot {
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
        box-shadow: 0 0 10px rgba(34, 197, 94, 0.8);
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.4; }
        50% { transform: scale(1.15); opacity: 0.7; }
    }
    
    .social-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 25px;
        flex-wrap: wrap;
    }
    
    .social-link {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white !important;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.3);
        display: inline-block;
    }
    
    .social-link:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0 16px 40px rgba(99, 102, 241, 0.5);
        color: white !important;
    }
    
    /* Stats Grid */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 25px;
        margin: 40px 0;
    }
    
    .stat-box {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 40px 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.2);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .stat-box:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3);
        border-color: #6366f1;
    }
    
    .stat-num {
        font-size: 3rem;
        font-weight: 900;
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #818cf8 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
    }
    
    .stat-text {
        font-size: 1rem;
        color: #cbd5e1;
        margin-top: 12px;
        font-weight: 600;
    }
    
    /* Section Title */
    .section-title {
        font-size: 2.8rem;
        font-weight: 900;
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #818cf8 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin: 60px 0 40px 0;
        letter-spacing: -1.5px;
    }
    
    .section-title::after {
        content: '';
        display: block;
        width: 120px;
        height: 5px;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        margin: 20px auto 0;
        border-radius: 3px;
        box-shadow: 0 4px 16px rgba(99, 102, 241, 0.4);
    }
    
    /* Streamlit Native Elements Styling */
    .main h1 {
        color: #e0e7ff !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin: 30px 0 20px 0 !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    .main h2 {
        color: #e0e7ff !important;
        font-size: 1.9rem !important;
        font-weight: 800 !important;
        margin: 25px 0 15px 0 !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    .main h3 {
        color: #818cf8 !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        margin: 25px 0 15px 0 !important;
        padding-left: 15px !important;
        border-left: 4px solid #6366f1 !important;
    }
    
    .main h4 {
        color: #a855f7 !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        margin: 20px 0 12px 0 !important;
    }
    
    .main p {
        color: #cbd5e1 !important;
        font-size: 1.05rem !important;
        line-height: 1.8 !important;
        margin-bottom: 15px !important;
    }
    
    .main strong {
        color: #e0e7ff !important;
        font-weight: 700 !important;
    }
    
    .main ul {
        margin: 15px 0 20px 25px !important;
    }
    
    .main ul li {
        color: #cbd5e1 !important;
        font-size: 1.05rem !important;
        line-height: 1.8 !important;
        margin-bottom: 8px !important;
    }
    
    .main ul li::marker {
        color: #6366f1 !important;
    }
    
    .main code {
        background: rgba(99, 102, 241, 0.1) !important;
        color: #c4b5fd !important;
        padding: 2px 6px !important;
        border-radius: 4px !important;
        font-size: 0.95rem !important;
    }
    
    /* Project Card */
    .project-card {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.9) 0%, rgba(31, 41, 55, 0.85) 100%);
        backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 40px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(129, 140, 248, 0.25);
        border-top: 4px solid #6366f1;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3);
        border-color: #6366f1;
    }
    
    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        gap: 20px;
        flex-wrap: wrap;
    }
    
    .project-title {
        font-size: 2rem;
        font-weight: 800;
        color: #e0e7ff;
        font-family: 'Space Grotesk', sans-serif;
        margin: 0;
    }
    
    .project-badges {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }
    
    .category-badge {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(168, 85, 247, 0.2) 100%);
        color: #c4b5fd;
        padding: 8px 18px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        border: 1.5px solid rgba(129, 140, 248, 0.4);
    }
    
    .status-badge {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.2) 0%, rgba(16, 185, 129, 0.2) 100%);
        color: #86efac;
        padding: 8px 18px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        border: 1.5px solid rgba(34, 197, 94, 0.4);
    }
    
    /* Tech Badge */
    .tech-badge {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        color: #e0e7ff;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        display: inline-block;
        margin: 4px;
        transition: all 0.3s;
    }
    
    .tech-badge:hover {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        transform: translateY(-2px);
    }
    
    /* Divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, rgba(129, 140, 248, 0.3) 50%, transparent 100%);
        margin: 40px 0;
    }
    
    /* Skills */
    .skill-container {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.2);
        margin-bottom: 25px;
    }
    
    .skill-header {
        font-size: 1.8rem;
        font-weight: 800;
        color: #e0e7ff;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .skill-list {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
    }
    
    .skill-chip {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        color: #e0e7ff;
        padding: 10px 22px;
        border-radius: 25px;
        font-size: 0.95rem;
        font-weight: 600;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        transition: all 0.3s;
    }
    
    .skill-chip:hover {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
    }
    
    /* Contact Cards */
    .contact-card {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 40px 30px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.2);
        text-align: center;
        transition: all 0.4s;
    }
    
    .contact-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3);
        border-color: #6366f1;
    }
    
    .contact-emoji {
        font-size: 3rem;
        margin-bottom: 18px;
    }
    
    .contact-label {
        font-size: 0.95rem;
        color: #94a3b8;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    .contact-info {
        font-size: 1.15rem;
        color: #e0e7ff;
        font-weight: 700;
        margin-bottom: 20px;
        word-break: break-word;
    }
    
    /* About Content */
    .about-content {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.2);
        margin-bottom: 25px;
    }
    
    .about-para {
        font-size: 1.15rem;
        color: #cbd5e1;
        line-height: 1.8;
        margin-bottom: 20px;
        text-align: justify;
    }
    
    /* Timeline */
    .timeline-item {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.7) 0%, rgba(31, 41, 55, 0.6) 100%);
        backdrop-filter: blur(12px);
        padding: 30px;
        border-radius: 18px;
        margin-bottom: 20px;
        border-left: 4px solid #6366f1;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s;
    }
    
    .timeline-item:hover {
        transform: translateX(8px);
        border-left-color: #a855f7;
        box-shadow: 0 12px 40px rgba(99, 102, 241, 0.25);
    }
    
    .timeline-year {
        font-size: 1.05rem;
        font-weight: 700;
        color: #818cf8;
        margin-bottom: 8px;
    }
    
    .timeline-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #e0e7ff;
        margin-bottom: 10px;
    }
    
    .timeline-desc {
        font-size: 1rem;
        color: #cbd5e1;
        line-height: 1.6;
    }
    
    .achievement-box {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.08) 0%, rgba(59, 130, 246, 0.08) 100%);
        border: 1.5px solid rgba(34, 197, 94, 0.25);
        padding: 18px;
        border-radius: 14px;
        margin-top: 12px;
    }
    
    .achievement-text {
        color: #86efac;
        font-size: 0.95rem;
        font-weight: 600;
        line-height: 1.6;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 14, 39, 0.95) 0%, rgba(26, 29, 58, 0.95) 100%) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(129, 140, 248, 0.2);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #e0e7ff !important;
    }
    
    /* Radio Button Styling */
    .stRadio > label {
        color: #e0e7ff !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        margin-bottom: 15px !important;
    }
    
    .stRadio > div {
        gap: 10px !important;
    }
    
    .stRadio > div > label {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%) !important;
        padding: 12px 24px !important;
        border-radius: 14px !important;
        color: #e0e7ff !important;
        border: 1.5px solid rgba(129, 140, 248, 0.3) !important;
        cursor: pointer !important;
        transition: all 0.3s !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    .stRadio > div > label:hover {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        transform: translateX(8px);
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.4);
    }
    
    .stRadio > div > label[data-baseweb="radio"] > div:first-child {
        background-color: transparent !important;
        border-color: #818cf8 !important;
    }
    
    .stRadio > div > label[data-baseweb="radio"][aria-checked="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
    }
    
    .stRadio > div > label[data-baseweb="radio"][aria-checked="true"] > div:first-child {
        background-color: white !important;
        border-color: white !important;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(10, 14, 39, 0.6);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #6366f1 0%, #a855f7 100%);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #818cf8 0%, #c084fc 100%);
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        color: #e0e7ff;
        border-radius: 12px;
    }
    
    .stSelectbox label {
        color: #e0e7ff !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        margin-bottom: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected' not in st.session_state:
    st.session_state.selected = "🏠 HOME"

# Sidebar Navigation
with st.sidebar:
    st.markdown("## 🎯 NAVIGATION")

    nav_options = [
        "🏠 HOME",
        "👤 ABOUT",
        "💼 PROJECTS",
        "🛠️ SKILLS",
        "🎓 EXPERIENCE",
        "🏆 ACHIEVEMENTS",
        "📧 CONTACT",
        "📊 ANALYTICS"
    ]

    selected = st.radio(
        "Navigate to:",
        nav_options,
        index=nav_options.index(
            st.session_state.selected) if st.session_state.selected in nav_options else 0,
        label_visibility="collapsed"
    )

    st.session_state.selected = selected

    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; padding: 20px;'>
        <p style='color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;'>
            <strong>Dheeraj Muley</strong><br>
            AI Engineer & Developer<br>
            📍 India<br>
            🌐 Open to Opportunities<br><br>
            <span style='color: #86efac;'>● Active</span><br>
            <span style='color: #94a3b8; font-size: 0.8rem;'>Updated: January 2026</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Detailed Projects Data
detailed_projects = [
    {
        "name": "Medical Image Analyzer",
        "category": "Healthcare AI",
        "badge": "FEATURED",
        "description": """
This advanced AI-powered platform revolutionizes medical diagnostics through comprehensive analysis of X-rays, CT scans, and MRIs. The system provides instant disease detection and diagnostic support to healthcare professionals.

**The Problem:** Healthcare professionals face significant challenges in accurately diagnosing diseases from medical images. Manual analysis is time-consuming, often requiring multiple consultations and expert opinions, leading to delayed treatment decisions.

**The Solution:** I developed a sophisticated deep learning system using custom CNN architecture that analyzes medical images with 94% accuracy. The platform provides instant preliminary diagnoses, highlights areas of concern, and generates detailed diagnostic reports with confidence scores.

**Key Features:**
- Multi-modal medical image processing supporting X-ray, CT, and MRI formats
- Disease detection with 94% accuracy using ensemble deep learning models
- Region of Interest (ROI) highlighting and automated annotation
- Comparative analysis with historical patient data for trend identification
- Detailed diagnostic reports with confidence scores and recommendations
- DICOM format support ensuring compatibility with medical imaging standards
- Real-time processing with GPU acceleration for instant results
- Seamless integration with hospital management systems

**Technology Stack:** Python, TensorFlow, PyTorch, OpenCV, Flask, Docker, PostgreSQL, NumPy, Pandas

**Measurable Impact:**
- Reduced diagnosis time by 60%, enabling faster treatment decisions
- Achieved 94% accuracy in disease detection across multiple conditions
- Successfully processed over 10,000 medical images
- Deployed in 2 pilot healthcare facilities with positive feedback
        """,
    },
    {
        "name": "AI Voice Assistant",
        "category": "NLP",
        "badge": "NEW",
        "description": """
An intelligent voice-activated assistant featuring advanced NLP capabilities, multi-language support, and real-time speech processing for seamless human-computer interaction.

**The Problem:** Traditional voice assistants struggle with contextual understanding, lack robust multi-language support, and fail to maintain coherent conversations across complex flows. Users often experience frustration with repetitive commands and limited customization.

**The Solution:** I built an advanced AI assistant using state-of-the-art transformer models (BERT) that truly understands context, maintains comprehensive conversation history, and supports multiple languages with industry-leading speech recognition accuracy of 95%.

**Key Features:**
- Real-time speech-to-text conversion with 95% accuracy
- Natural language understanding powered by BERT transformers
- Multi-language support including English, Hindi, and Spanish
- Context-aware conversations with full memory of previous interactions
- Advanced intent recognition and entity extraction
- Natural text-to-speech synthesis for human-like responses
- Wake word detection enabling hands-free operation
- Custom command creation and home automation integration

**Technology Stack:** Python, PyTorch, Transformers, FastAPI, WebSockets, spaCy, Whisper, Redis

**Measurable Impact:**
- Achieved 95% speech recognition accuracy across supported languages
- Successfully supports 3+ languages with seamless switching
- Sub-second response time for real-time conversations
- 1000+ active test users providing positive feedback
        """,
    },
    {
        "name": "Stock Prediction Engine",
        "category": "FinTech",
        "badge": "LIVE",
        "description": """
A sophisticated financial forecasting system that combines LSTM neural networks with real-time sentiment analysis for accurate stock price predictions and comprehensive market trend analysis.

**The Problem:** Stock market prediction is extremely challenging due to high volatility, multiple influencing factors, and the critical need for real-time data processing. Traditional methods fail to account for sentiment and social trends that significantly impact market movements.

**The Solution:** I created a hybrid prediction model that combines LSTM networks for time series analysis with NLP-based sentiment analysis from news sources and social media. The system processes real-time market data and generates actionable predictions with 85% directional accuracy.

**Key Features:**
- LSTM-based price prediction achieving 85% directional accuracy
- Real-time market data integration via financial APIs
- News sentiment analysis using advanced NLP techniques
- Social media trend monitoring and impact assessment
- Technical indicator calculations (RSI, MACD, Bollinger Bands, Moving Averages)
- Portfolio optimization recommendations based on risk tolerance
- Comprehensive risk assessment and volatility predictions
- Interactive visualizations with Plotly for data exploration

**Technology Stack:** Python, TensorFlow, LSTM, Pandas, NumPy, Plotly, Redis, Kafka, Beautiful Soup

**Measurable Impact:**
- 85% directional accuracy in stock price predictions
- Simultaneous processing of 100+ stocks in real-time
- Real-time updates every 5 minutes during market hours
- Users reported 15% average improvement in portfolio returns
        """,
    },
    {
        "name": "Smart IoT Dashboard",
        "category": "IoT",
        "badge": "PRODUCTION",
        "description": """
Enterprise-grade real-time monitoring and control dashboard for industrial IoT sensors with highly scalable architecture capable of handling thousands of concurrent connections.

**The Problem:** Industrial environments require continuous monitoring of numerous sensors, but existing solutions lack scalability, suffer from lag in data visualization, and provide limited customization options for different operational needs.

**The Solution:** I developed a highly scalable IoT dashboard using MQTT protocol and InfluxDB time-series database, enabling real-time monitoring of 5000+ sensors with sub-second data refresh rates and zero lag in visualization.

**Key Features:**
- Real-time sensor data visualization with customizable widgets
- Support for 5000+ concurrent MQTT connections
- Time-series data storage optimized with InfluxDB
- Fully customizable widget-based dashboard interface
- Intelligent alert and notification system with threshold configuration
- Historical data analysis with advanced reporting capabilities
- Comprehensive device management and remote configuration
- Role-based access control for enterprise security

**Technology Stack:** React, Node.js, MQTT, InfluxDB, Chart.js, WebSockets, Docker, Nginx

**Measurable Impact:**
- Successfully handles 5000+ concurrent sensor connections
- Sub-second data refresh rate ensuring real-time monitoring
- 99.9% uptime in production environment
- Deployed across 3 industrial facilities improving operational efficiency
        """,
    },
    {
        "name": "Face Recognition System",
        "category": "Computer Vision",
        "badge": "DEPLOYED",
        "description": """
High-security face detection and recognition system with advanced anti-spoofing and liveness detection capabilities designed for critical authentication and access control applications.

**The Problem:** Traditional security systems are highly vulnerable to spoofing attacks using printed photos, video playback, or even 3D masks, compromising security in critical access control scenarios such as data centers and restricted facilities.

**The Solution:** I implemented a multi-layered security system that combines real-time face detection, recognition with 98% accuracy, and sophisticated liveness detection to prevent all forms of spoofing attacks. The system uses advanced algorithms to detect subtle facial movements and texture analysis.

**Key Features:**
- Real-time face detection using MTCNN (Multi-task Cascaded Convolutional Networks)
- Face recognition with 98% accuracy using deep neural networks
- Advanced liveness detection preventing photo and video spoofing
- Multi-face tracking in video streams with position prediction
- Age and emotion estimation for enhanced analytics
- Scalable database supporting 10,000+ registered faces
- Fast processing at 30 FPS on GPU-enabled systems
- RESTful API for seamless integration with existing systems

**Technology Stack:** Python, OpenCV, DeepFace, TensorFlow, Flask, Redis, PostgreSQL, Docker

**Measurable Impact:**
- Achieved 98% face recognition accuracy in real-world conditions
- Zero successful spoofing attacks during comprehensive testing
- Processing speed of 30 frames per second enabling smooth operation
- Successfully deployed in 5 high-security checkpoints
        """,
    },
    {
        "name": "E-Commerce Platform",
        "category": "Web Apps",
        "badge": "SCALABLE",
        "description": """
Full-stack marketplace featuring AI-powered product recommendations, intelligent search functionality, and comprehensive seller/buyer management system for seamless online shopping experiences.

**The Problem:** Generic e-commerce platforms suffer from poor personalization, ineffective search functionality, and struggle with scaling to handle large product catalogs. Users often abandon shopping due to inability to find relevant products quickly.

**The Solution:** I built a modern, scalable e-commerce platform with AI-driven recommendations, Elasticsearch-powered intelligent search, and microservices architecture capable of efficiently managing 50,000+ products with lightning-fast performance.

**Key Features:**
- AI-powered product recommendations using collaborative filtering
- Intelligent search with advanced filters, facets, and auto-suggestions
- Comprehensive seller dashboard with real-time analytics
- Multi-vendor marketplace support with vendor management
- Secure payment integration with Stripe supporting multiple methods
- Real-time order tracking and comprehensive management
- Customer reviews and ratings system with moderation
- Fully responsive design optimized for all devices

**Technology Stack:** React, Node.js, MongoDB, Stripe, AWS S3, Redis, Elasticsearch, JWT

**Measurable Impact:**
- Successfully managing 50,000+ products with instant search
- Supporting 100+ active sellers with dedicated dashboards
- Processing 1,000+ daily transactions securely
- 30% increase in conversion rate due to improved UX
        """,
    },
    {
        "name": "Document Q&A System",
        "category": "NLP",
        "badge": "AI-POWERED",
        "description": """
Intelligent document analysis system leveraging RAG (Retrieval Augmented Generation) architecture with vector embeddings for accurate question answering from large document collections.

**The Problem:** Finding specific information within large document collections is extremely time-consuming, requiring manual reading through hundreds of pages. Traditional search fails to understand context and semantic meaning.

**The Solution:** I created a sophisticated RAG-based system using FAISS vector embeddings and large language models to enable natural language queries over documents. The system provides accurate, cited answers by retrieving relevant context and generating precise responses.

**Key Features:**
- Support for multiple file formats including PDF, DOCX, and TXT
- Vector embedding using FAISS for semantic search
- Intelligent semantic search across entire document collections
- Context-aware answer generation with source attribution
- Automatic source citation for every answer provided
- Multi-document comparison and cross-referencing capabilities
- Full conversation history maintenance for context
- Efficient batch document processing for large uploads

**Technology Stack:** Python, LangChain, FAISS, OpenAI GPT, Streamlit, PyPDF2, ChromaDB

**Measurable Impact:**
- 95% answer relevance and accuracy rate
- Capability to process documents exceeding 1000 pages
- 80% reduction in information retrieval time
- Support for 10+ concurrent users with maintained performance
        """,
    },
    {
        "name": "Automated Data Pipeline",
        "category": "Web Apps",
        "badge": "AUTOMATED",
        "description": """
Robust ETL (Extract, Transform, Load) pipeline for automated data extraction, transformation, and loading with integrated ML model training workflows and comprehensive monitoring capabilities.

**The Problem:** Manual data processing is error-prone, extremely time-consuming, and doesn't scale effectively for large datasets that require regular updates, transformations, and quality checks. This leads to data inconsistencies and delayed insights.

**The Solution:** I developed a fully automated pipeline using Apache Airflow that orchestrates end-to-end data workflows, from initial extraction through transformation to ML model training and deployment, with built-in error handling and quality assurance.

**Key Features:**
- Scheduled data extraction from multiple heterogeneous sources
- Automated data transformation and cleaning pipelines
- Comprehensive automated quality checks and validation rules
- Integrated ML model training and retraining workflows
- Automated report generation and distribution
- Robust error handling with intelligent retry mechanisms
- Real-time pipeline monitoring and alerting system
- Complete version control for both data and models

**Technology Stack:** Apache Airflow, Python, PostgreSQL, Docker, Pandas, scikit-learn, Jupyter

**Measurable Impact:**
- 100% automation of previously manual data workflows
- Processing 1 million+ records daily with zero errors
- 90% reduction in manual effort and human errors
- Zero data quality incidents since deployment
        """,
    }
]

# HOME
if selected == "🏠 HOME":
    st.markdown(f"""
    <div class="hero-wrapper">
        <div class="hero-name">DHEERAJ MULEY</div>
        <div class="hero-role">AI Engineer & Full Stack Developer</div>
        <div class="hero-tagline">
            Building intelligent solutions with cutting-edge AI, Machine Learning, and Modern Web Technologies
        </div>
        <div style="text-align: center; margin-top: 20px;">
            <span class="availability-badge">
                <span class="pulse-dot"></span>
                Open for Freelance & Full-Time Opportunities
            </span>
        </div>
        <div style="text-align: center;">
            <span class="hero-highlight">
                🎯 35+ Projects | 12+ Technologies | 6+ Domains
            </span>
        </div>
        <div class="social-container">
            <a href="mailto:dheerajmuley006@gmail.com" class="social-link">📧 Email</a>
            <a href="https://github.com/dheeraj815" target="_blank" class="social-link">💻 GitHub</a>
            <a href="https://www.linkedin.com/in/dheeraj-muley" target="_blank" class="social-link">🔗 LinkedIn</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            '<div class="stat-box"><div class="stat-num">35+</div><div class="stat-text">Projects Delivered</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(
            '<div class="stat-box"><div class="stat-num">12+</div><div class="stat-text">Tech Stack</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(
            '<div class="stat-box"><div class="stat-num">6+</div><div class="stat-text">Domains</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(
            '<div class="stat-box"><div class="stat-num">1.5+</div><div class="stat-text">Years Coding</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ABOUT
elif selected == "👤 ABOUT":
    st.markdown('<div class="section-title">ABOUT ME</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="about-content">
            <p class="about-para">
                I'm an <strong>AI Engineer</strong> and <strong>Full Stack Developer</strong> passionate about creating intelligent systems that solve real-world problems. With expertise spanning multiple domains, I specialize in transforming complex challenges into elegant, scalable solutions.
            </p>
            <p class="about-para">
                My journey in technology encompasses <strong>Healthcare AI</strong>, <strong>Financial Technology</strong>, <strong>Computer Vision</strong>, <strong>Natural Language Processing</strong>, and <strong>Modern Web Development</strong>. I thrive on building end-to-end solutions that combine powerful AI capabilities with seamless user experiences.
            </p>
            <p class="about-para">
                With <strong>35+ projects</strong> across diverse domains, I've developed expertise in creating production-ready applications—from AI-powered medical imaging systems to real-time stock prediction engines, from intelligent chatbots to IoT dashboards.
            </p>
            <p class="about-para">
                I'm continuously expanding my knowledge in emerging technologies like <strong>Large Language Models</strong>, <strong>Generative AI</strong>, <strong>Advanced Neural Architectures</strong>, and <strong>Cloud-Native Development</strong>, staying at the forefront of technological innovation.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="skill-container">
            <div class="skill-header">🎯 Expertise</div>
            <div class="skill-list">
                <span class="skill-chip">AI & ML</span>
                <span class="skill-chip">Deep Learning</span>
                <span class="skill-chip">Computer Vision</span>
                <span class="skill-chip">NLP</span>
                <span class="skill-chip">Full Stack</span>
                <span class="skill-chip">Healthcare AI</span>
                <span class="skill-chip">FinTech</span>
                <span class="skill-chip">IoT</span>
                <span class="skill-chip">Cloud</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# PROJECTS - CLEAN PARAGRAPH VERSION
elif selected == "💼 PROJECTS":
    st.markdown('<div class="section-title">FEATURED PROJECTS</div>',
                unsafe_allow_html=True)

    project_filter = st.selectbox(
        "🔍 Filter by Category",
        ["All Projects", "Healthcare AI", "Computer Vision",
            "NLP", "FinTech", "Web Apps", "IoT"],
        key="project_filter"
    )

    if project_filter != "All Projects":
        filtered_projects = [
            p for p in detailed_projects if p["category"] == project_filter]
    else:
        filtered_projects = detailed_projects

    for idx, project in enumerate(filtered_projects):
        st.markdown(f"""
        <div class="project-card">
            <div class="project-header">
                <div class="project-title">{project["name"]}</div>
                <div class="project-badges">
                    <span class="category-badge">{project["category"]}</span>
                    <span class="status-badge">{project["badge"]}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Use st.markdown for clean paragraph formatting
        st.markdown(project["description"])

        # Add divider between projects
        if idx < len(filtered_projects) - 1:
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# SKILLS
elif selected == "🛠️ SKILLS":
    st.markdown('<div class="section-title">TECHNICAL SKILLS</div>',
                unsafe_allow_html=True)

    skills_data = {
        "🤖 AI & Machine Learning": [
            "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "XGBoost",
            "MLflow", "Weights & Biases"
        ],
        "🧠 Deep Learning": [
            "CNN", "RNN", "LSTM", "Transformers", "GANs",
            "Transfer Learning", "Fine-tuning"
        ],
        "👁️ Computer Vision": [
            "OpenCV", "YOLO", "ResNet", "EfficientNet",
            "MediaPipe", "Image Processing"
        ],
        "💬 NLP & LLMs": [
            "BERT", "GPT", "LangChain", "Hugging Face", "spaCy",
            "RAG", "Vector Databases"
        ],
        "🌐 Full Stack Development": [
            "React", "Node.js", "FastAPI", "Flask",
            "Django", "Streamlit", "Next.js"
        ],
        "🗄️ Databases": [
            "PostgreSQL", "MongoDB", "Redis", "MySQL",
            "Pinecone", "ChromaDB", "Firebase"
        ],
        "☁️ Cloud & DevOps": [
            "AWS", "Docker", "Kubernetes", "CI/CD",
            "GitHub Actions", "Linux"
        ],
        "📊 Data Science": [
            "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly",
            "Jupyter", "Apache Spark"
        ]
    }

    for category, skills in skills_data.items():
        skill_chips = "".join(
            [f'<span class="skill-chip">{skill}</span>' for skill in skills])

        st.markdown(f"""
        <div class="skill-container">
            <div class="skill-header">{category}</div>
            <div class="skill-list">{skill_chips}</div>
        </div>
        """, unsafe_allow_html=True)

# EXPERIENCE
elif selected == "🎓 EXPERIENCE":
    st.markdown('<div class="section-title">EXPERIENCE</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-year">📅 June 2024 - Present</div>
        <div class="timeline-title">🚀 Freelance AI Engineer & Full Stack Developer</div>
        <div class="timeline-desc">
            <strong>Self-Employed | Remote</strong><br><br>
            Building and deploying AI-powered solutions for diverse clients:<br><br>
            • Developed healthcare AI systems for medical image analysis and diagnostics<br>
            • Created full-stack applications using React, Node.js, and Python frameworks<br>
            • Implemented NLP solutions including chatbots and document analysis systems<br>
            • Built computer vision applications for security and automation<br>
            • Designed scalable cloud architectures on AWS and GCP<br>
            • Delivered end-to-end solutions from concept to production deployment
        </div>
        <div class="achievement-box">
            <div class="achievement-text">
                ✨ Key Achievements:<br>
                • Successfully delivered 35+ projects across multiple domains<br>
                • Achieved 94%+ accuracy in AI/ML models<br>
                • Built systems handling 5K+ concurrent users<br>
                • Reduced deployment time by 50% through automation
            </div>
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-year">📅 January 2024 - May 2024</div>
        <div class="timeline-title">💻 AI/ML Developer & Researcher</div>
        <div class="timeline-desc">
            <strong>Independent Projects | Remote</strong><br><br>
            Focused on learning and building AI/ML expertise:<br><br>
            • Completed intensive courses in Deep Learning and Computer Vision<br>
            • Built 15+ personal projects covering various AI domains<br>
            • Developed proficiency in TensorFlow, PyTorch, and modern frameworks<br>
            • Created full-stack applications integrating AI capabilities<br>
            • Contributed to open-source projects on GitHub<br>
            • Participated in online coding challenges and hackathons
        </div>
        <div class="achievement-box">
            <div class="achievement-text">
                ✨ Learning Highlights:<br>
                • Mastered 12+ core technologies<br>
                • Built strong foundation in MLOps and deployment<br>
                • Completed multiple technical certifications<br>
                • Developed practical problem-solving skills
            </div>
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-year">📅 2021 - 2023</div>
        <div class="timeline-title">🎓 Education & Foundation Building</div>
        <div class="timeline-desc">
            <strong>Computer Science Studies</strong><br><br>
            Built foundational knowledge in computer science:<br><br>
            • Studied core CS fundamentals and programming<br>
            • Learned data structures, algorithms, and software engineering<br>
            • Completed projects in web development<br>
            • Started exploring AI/ML through online courses<br>
            • Developed interest in practical application development
        </div>
    </div>
    """, unsafe_allow_html=True)

# ACHIEVEMENTS
elif selected == "🏆 ACHIEVEMENTS":
    st.markdown('<div class="section-title">ACHIEVEMENTS</div>',
                unsafe_allow_html=True)

    achievements = [
        {
            "icon": "🎯",
            "title": "35+ Projects Delivered",
            "desc": "Successfully built diverse applications across Healthcare, FinTech, Computer Vision, and Web Development"
        },
        {
            "icon": "⭐",
            "title": "12+ Technologies",
            "desc": "Expert proficiency in modern frameworks including TensorFlow, React, PyTorch, and cloud platforms"
        },
        {
            "icon": "🏅",
            "title": "High-Performance AI",
            "desc": "Developed models achieving 94%+ accuracy in medical diagnosis and 92% in prediction tasks"
        },
        {
            "icon": "🚀",
            "title": "Scalable Systems",
            "desc": "Built production applications handling 5K+ concurrent users with 99% uptime"
        },
        {
            "icon": "💡",
            "title": "Healthcare Innovation",
            "desc": "Created AI diagnostic tools for real-world medical image analysis applications"
        },
        {
            "icon": "🔧",
            "title": "Open Source",
            "desc": "Active contributor with well-documented projects and technical tutorials"
        },
        {
            "icon": "📚",
            "title": "Continuous Learning",
            "desc": "Completed 15+ technical certifications in AI, ML, and Full Stack Development"
        },
        {
            "icon": "⚡",
            "title": "Fast Development",
            "desc": "Reduced project delivery time by 50% through automation and efficient workflows"
        },
        {
            "icon": "🎨",
            "title": "UI/UX Focus",
            "desc": "Created intuitive interfaces with modern design and excellent user experience"
        },
        {
            "icon": "🔐",
            "title": "Security First",
            "desc": "Implemented robust security with encryption, authentication, and privacy protocols"
        },
        {
            "icon": "📈",
            "title": "Business Impact",
            "desc": "Delivered solutions improving operational efficiency and generating measurable ROI"
        },
        {
            "icon": "🌍",
            "title": "Global Reach",
            "desc": "Worked with diverse clients delivering custom AI and web solutions"
        }
    ]

    cols = st.columns(3)
    for idx, achievement in enumerate(achievements):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="contact-card">
                <div class="contact-emoji">{achievement["icon"]}</div>
                <div class="timeline-title" style="margin-bottom: 12px; font-size: 1.3rem;">{achievement["title"]}</div>
                <div class="timeline-desc">{achievement["desc"]}</div>
            </div>
            """, unsafe_allow_html=True)

# CONTACT
elif selected == "📧 CONTACT":
    st.markdown('<div class="section-title">GET IN TOUCH</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-tagline" style="text-align: center; margin-bottom: 45px;">
        Open to discussing new projects, collaborations, or opportunities. Let's build something great together!
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="contact-card">
            <div class="contact-emoji">📧</div>
            <div class="contact-label">Email</div>
            <div class="contact-info">dheerajmuley006@gmail.com</div>
            <a href="mailto:dheerajmuley006@gmail.com" class="social-link">Send Email</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="contact-card">
            <div class="contact-emoji">💻</div>
            <div class="contact-label">GitHub</div>
            <div class="contact-info">@dheeraj815</div>
            <a href="https://github.com/dheeraj815" target="_blank" class="social-link">View Profile</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="contact-card">
            <div class="contact-emoji">🔗</div>
            <div class="contact-label">LinkedIn</div>
            <div class="contact-info">Dheeraj Muley</div>
            <a href="https://www.linkedin.com/in/dheeraj-muley" target="_blank" class="social-link">Connect</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="font-size: 2.5rem; margin-top: 70px;">💼 SERVICES</div>',
                unsafe_allow_html=True)

    services = [
        {
            "icon": "🤖",
            "title": "AI/ML Solutions",
            "desc": "Custom AI models, Computer Vision, NLP systems, and LLM integration"
        },
        {
            "icon": "🌐",
            "title": "Full Stack Development",
            "desc": "End-to-end web applications, APIs, and scalable solutions"
        },
        {
            "icon": "🏥",
            "title": "Healthcare AI",
            "desc": "Medical imaging analysis and diagnostic systems"
        },
        {
            "icon": "💰",
            "title": "FinTech Solutions",
            "desc": "Stock prediction, fraud detection, and financial analytics"
        },
        {
            "icon": "🔍",
            "title": "Computer Vision",
            "desc": "Object detection, face recognition, and video analytics"
        },
        {
            "icon": "💬",
            "title": "NLP & Chatbots",
            "desc": "Conversational AI, document analysis, and RAG systems"
        }
    ]

    cols = st.columns(3)
    for idx, service in enumerate(services):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="contact-card" style="padding: 32px;">
                <div class="contact-emoji">{service["icon"]}</div>
                <div class="timeline-title" style="margin-bottom: 10px; font-size: 1.2rem;">{service["title"]}</div>
                <div class="timeline-desc" style="font-size: 0.95rem;">{service["desc"]}</div>
            </div>
            """, unsafe_allow_html=True)

# ANALYTICS
elif selected == "📊 ANALYTICS":
    st.markdown('<div class="section-title">PORTFOLIO ANALYTICS</div>',
                unsafe_allow_html=True)

    st.markdown('<div class="skill-container">', unsafe_allow_html=True)
    st.markdown('<div class="skill-header">📈 Skills Distribution</div>',
                unsafe_allow_html=True)

    skills_chart_data = {
        'Category': ['AI/ML', 'Web Dev', 'Computer Vision', 'NLP', 'Cloud', 'Data Science', 'DevOps'],
        'Proficiency': [92, 88, 90, 85, 82, 86, 78],
        'Projects': [12, 10, 8, 7, 11, 9, 8]
    }

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        name='Proficiency %',
        x=skills_chart_data['Category'],
        y=skills_chart_data['Proficiency'],
        marker_color='#6366f1'
    ))
    fig1.add_trace(go.Bar(
        name='Projects',
        x=skills_chart_data['Category'],
        y=skills_chart_data['Projects'],
        marker_color='#a855f7'
    ))

    fig1.update_layout(
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e7ff'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(129, 140, 248, 0.15)'),
        height=400
    )

    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="skill-container">', unsafe_allow_html=True)
    st.markdown('<div class="skill-header">📅 Project Timeline</div>',
                unsafe_allow_html=True)

    timeline_data = {
        'Period': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q1 2026'],
        'Projects': [4, 6, 8, 10, 5, 2],
        'Skills': [2, 3, 3, 2, 1, 1]
    }

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=timeline_data['Period'],
        y=timeline_data['Projects'],
        mode='lines+markers',
        name='Projects',
        line=dict(color='#6366f1', width=3),
        marker=dict(size=10)
    ))
    fig2.add_trace(go.Scatter(
        x=timeline_data['Period'],
        y=timeline_data['Skills'],
        mode='lines+markers',
        name='New Skills',
        line=dict(color='#a855f7', width=3),
        marker=dict(size=10)
    ))

    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e7ff'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(129, 140, 248, 0.15)'),
        height=400
    )

    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="skill-container">', unsafe_allow_html=True)
        st.markdown(
            '<div class="skill-header">🎯 Domain Distribution</div>', unsafe_allow_html=True)

        domain_data = {
            'Domain': ['Healthcare AI', 'FinTech', 'Computer Vision', 'NLP', 'Web Apps', 'IoT', 'Other'],
            'Count': [7, 5, 8, 6, 4, 3, 2]
        }

        fig3 = px.pie(
            values=domain_data['Count'],
            names=domain_data['Domain'],
            color_discrete_sequence=[
                '#6366f1', '#a855f7', '#818cf8', '#c084fc', '#2dd4bf', '#f472b6', '#fbbf24']
        )

        fig3.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e7ff'),
            height=400
        )

        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="skill-container">', unsafe_allow_html=True)
        st.markdown(
            '<div class="skill-header">⚡ Tech Stack Usage</div>', unsafe_allow_html=True)

        tech_data = {
            'Technology': ['Python', 'React', 'TensorFlow', 'PyTorch', 'Node.js', 'MongoDB', 'Docker'],
            'Usage %': [95, 82, 78, 72, 75, 68, 80]
        }

        fig4 = go.Figure(go.Bar(
            x=tech_data['Usage %'],
            y=tech_data['Technology'],
            orientation='h',
            marker=dict(
                color=tech_data['Usage %'],
                colorscale=[[0, '#a855f7'], [1, '#6366f1']],
                line=dict(width=0)
            )
        ))

        fig4.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e7ff'),
            xaxis=dict(showgrid=True, gridcolor='rgba(129, 140, 248, 0.15)'),
            yaxis=dict(showgrid=False),
            height=400
        )

        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 70px; padding: 30px; border-top: 1px solid rgba(129, 140, 248, 0.2);">
    <div class="hero-tagline" style="margin-bottom: 15px; font-size: 1rem;">
        Built with ❤️ using Streamlit • © 2026 Dheeraj Muley
    </div>
    <div class="availability-badge" style="display: inline-flex;">
        <span class="pulse-dot"></span>
        Open for New Opportunities
    </div>
</div>
""", unsafe_allow_html=True)
