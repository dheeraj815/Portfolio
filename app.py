
import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Dheeraj Muley - AI/ML Engineering Student",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Professional & Clean
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
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
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(99, 102, 241, 0.2);
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
        font-size: 1.4rem;
        color: #cbd5e1;
        margin: 15px 0;
        font-weight: 600;
        text-align: center;
    }
    
    .hero-tagline {
        font-size: 1.05rem;
        color: #94a3b8;
        max-width: 750px;
        margin: 15px auto;
        line-height: 1.7;
        text-align: center;
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
        padding: 12px 28px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.3);
        display: inline-block;
    }
    
    .social-link:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0 16px 40px rgba(99, 102, 241, 0.5);
    }
    
    /* Stats Grid */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 20px;
        margin: 40px 0;
    }
    
    .stat-box {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 35px 25px;
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
        font-size: 2.8rem;
        font-weight: 900;
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #818cf8 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
    }
    
    .stat-text {
        font-size: 0.95rem;
        color: #cbd5e1;
        margin-top: 12px;
        font-weight: 600;
    }
    
    /* Section Title */
    .section-title {
        font-size: 2.5rem;
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
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        margin: 18px auto 0;
        border-radius: 3px;
        box-shadow: 0 4px 16px rgba(99, 102, 241, 0.4);
    }
    
    /* Content Styling */
    .main h2 {
        color: #e0e7ff !important;
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        margin: 25px 0 15px 0 !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    .main h3 {
        color: #818cf8 !important;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        margin: 25px 0 15px 0 !important;
        padding-left: 15px !important;
        border-left: 4px solid #6366f1 !important;
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
    
    .main code {
        background: rgba(99, 102, 241, 0.15) !important;
        color: #c4b5fd !important;
        padding: 3px 8px !important;
        border-radius: 4px !important;
        font-size: 0.9rem !important;
    }
    
    /* Project Card */
    .project-card {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.9) 0%, rgba(31, 41, 55, 0.85) 100%);
        backdrop-filter: blur(20px);
        padding: 35px;
        border-radius: 18px;
        margin-bottom: 30px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(129, 140, 248, 0.25);
        border-left: 4px solid #6366f1;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3);
        border-left-color: #a855f7;
    }
    
    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 18px;
        gap: 20px;
        flex-wrap: wrap;
    }
    
    .project-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #e0e7ff;
        font-family: 'Space Grotesk', sans-serif;
        margin: 0;
    }
    
    .project-meta {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        align-items: center;
    }
    
    .tech-badge {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        color: #c4b5fd;
        padding: 6px 14px;
        border-radius: 16px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        display: inline-block;
    }
    
    .status-badge {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.2) 0%, rgba(16, 185, 129, 0.2) 100%);
        color: #86efac;
        padding: 6px 14px;
        border-radius: 16px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1.5px solid rgba(34, 197, 94, 0.4);
    }
    
    .project-link {
        color: #818cf8;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9rem;
        transition: color 0.3s;
    }
    
    .project-link:hover {
        color: #a855f7;
    }
    
    /* Skills */
    .skill-container {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.2);
        margin-bottom: 20px;
    }
    
    .skill-header {
        font-size: 1.6rem;
        font-weight: 800;
        color: #e0e7ff;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .skill-list {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    
    .skill-chip {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        color: #e0e7ff;
        padding: 8px 18px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        transition: all 0.3s;
    }
    
    .skill-chip:hover {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
    }
    
    /* Timeline */
    .timeline-item {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.7) 0%, rgba(31, 41, 55, 0.6) 100%);
        backdrop-filter: blur(12px);
        padding: 28px;
        border-radius: 16px;
        margin-bottom: 18px;
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
        font-size: 0.95rem;
        font-weight: 700;
        color: #818cf8;
        margin-bottom: 8px;
    }
    
    .timeline-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #e0e7ff;
        margin-bottom: 10px;
    }
    
    .timeline-desc {
        font-size: 1rem;
        color: #cbd5e1;
        line-height: 1.6;
    }
    
    /* Contact Cards */
    .contact-card {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 35px 28px;
        border-radius: 18px;
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
        font-size: 2.8rem;
        margin-bottom: 16px;
    }
    
    .contact-label {
        font-size: 0.9rem;
        color: #94a3b8;
        margin-bottom: 8px;
        font-weight: 600;
    }
    
    .contact-info {
        font-size: 1.1rem;
        color: #e0e7ff;
        font-weight: 700;
        margin-bottom: 18px;
        word-break: break-word;
    }
    
    /* Certification Badge */
    .cert-badge {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(99, 102, 241, 0.15) 100%);
        padding: 12px 20px;
        border-radius: 12px;
        margin: 8px;
        display: inline-block;
        border: 1.5px solid rgba(59, 130, 246, 0.3);
        transition: all 0.3s;
    }
    
    .cert-badge:hover {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        transform: translateY(-3px);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 14, 39, 0.95) 0%, rgba(26, 29, 58, 0.95) 100%) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(129, 140, 248, 0.2);
    }
    
    .stRadio > label {
        color: #e0e7ff !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        margin-bottom: 15px !important;
    }
    
    .stRadio > div > label {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%) !important;
        padding: 12px 22px !important;
        border-radius: 12px !important;
        color: #e0e7ff !important;
        border: 1.5px solid rgba(129, 140, 248, 0.3) !important;
        cursor: pointer !important;
        transition: all 0.3s !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    .stRadio > div > label:hover {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        transform: translateX(6px);
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.4);
    }
    
    .stRadio > div > label[aria-checked="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
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
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected' not in st.session_state:
    st.session_state.selected = "🏠 Home"

# Sidebar Navigation
with st.sidebar:
    st.markdown("## Navigation")

    nav_options = [
        "🏠 Home",
        "👤 About",
        "💼 Projects",
        "🎓 Education",
        "🛠️ Skills",
        "📜 Certifications",
        "🏆 Achievements",
        "📧 Contact"
    ]

    selected = st.radio(
        "Navigate to:",
        nav_options,
        index=nav_options.index(st.session_state.selected) if st.session_state.selected in nav_options else 0,
        label_visibility="collapsed"
    )

    st.session_state.selected = selected

    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; padding: 20px;'>
        <p style='color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;'>
            <strong>Dheeraj Muley</strong><br>
            BTech AIML Student<br>
            📍 India<br><br>
            <span style='color: #86efac;'>● Actively Seeking Internships</span><br>
            <span style='color: #94a3b8; font-size: 0.8rem;'>Updated: January 2026</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Updated Projects Data - More Authentic
authentic_projects = [
    {
        "name": "Medical Image Analysis System",
        "category": "Healthcare AI",
        "tech": "TensorFlow • OpenCV • Flask",
        "github": "https://github.com/dheeraj815",
        "description": """
A deep learning system for analyzing chest X-rays to detect potential abnormalities. Built as part of my academic project.

**What I built:** CNN-based classifier trained on publicly available chest X-ray datasets to identify common lung conditions.

**Technical approach:**
- Implemented transfer learning using ResNet50 pre-trained on ImageNet
- Data augmentation to improve model generalization (rotation, zoom, flip)
- Achieved 89% validation accuracy on test set
- Built Flask API for model serving
- Created simple web interface for image upload and prediction

**Key learnings:**
- Working with medical imaging data and DICOM formats
- Handling class imbalance in datasets
- Model interpretability using Grad-CAM visualization
- Deploying ML models as web services

**Challenges faced:**
- Limited computational resources - trained on Google Colab with session limits
- Overfitting on small dataset - solved with aggressive data augmentation
- Converting model predictions into meaningful insights for non-technical users
        """,
    },
    {
        "name": "AI Chatbot with RAG",
        "category": "NLP",
        "tech": "LangChain • FAISS • Streamlit",
        "github": "https://github.com/dheeraj815",
        "description": """
Question-answering chatbot that can answer questions from uploaded PDF documents using Retrieval Augmented Generation.

**What I built:** Document Q&A system where users upload PDFs and ask questions in natural language.

**Technical implementation:**
- Used LangChain for document processing and chain orchestration
- Implemented FAISS vector database for semantic search
- Integrated OpenAI's GPT-3.5 for answer generation
- Built user interface with Streamlit
- Added conversation memory to maintain context

**Key features:**
- Supports multiple PDF uploads simultaneously
- Chunks documents intelligently for better retrieval
- Shows source citations for answers
- Maintains chat history within session

**What I learned:**
- Understanding embeddings and vector similarity search
- Prompt engineering for accurate answer generation
- Managing API costs and rate limits
- Building conversational interfaces

**Limitations:**
- Requires OpenAI API key (not free)
- Performance depends on document quality and structure
- Context window limitations for very long documents
        """,
    },
    {
        "name": "Stock Price Predictor",
        "category": "FinTech",
        "tech": "LSTM • yfinance • Plotly",
        "github": "https://github.com/dheeraj815",
        "description": """
Time series forecasting model to predict stock prices using historical data and technical indicators.

**What I built:** LSTM neural network trained on historical stock data to predict next-day closing prices.

**Implementation details:**
- Fetched real-time stock data using yfinance API
- Feature engineering: Moving averages, RSI, MACD indicators
- Built LSTM model with PyTorch
- Interactive visualizations with Plotly
- Streamlit dashboard for predictions

**Model performance:**
- Achieved RMSE of 3.2% on test data for major stocks
- Better performance on stable stocks vs volatile ones
- Directional accuracy around 65% (better than random guess)

**What this taught me:**
- Time series analysis and feature engineering
- LSTM architecture and sequence modeling
- Financial data analysis and technical indicators
- The difficulty of stock market prediction (humbling!)

**Honest limitations:**
- Cannot predict major market events or news impact
- Past performance doesn't guarantee future results
- Model works better for trending markets than volatile periods
- Not suitable for actual trading decisions
        """,
    },
    {
        "name": "Face Recognition Attendance System",
        "category": "Computer Vision",
        "tech": "OpenCV • face_recognition • SQLite",
        "github": "https://github.com/dheeraj815",
        "description": """
Automated attendance system using face recognition to mark student attendance in real-time.

**What I built:** Desktop application that detects faces from webcam feed and marks attendance automatically.

**How it works:**
- Students register by capturing multiple face images
- Face encodings stored in SQLite database
- Real-time face detection using OpenCV
- Face recognition using face_recognition library (dlib)
- Automatic attendance marking with timestamp
- Excel export for attendance records

**Technical details:**
- Pre-processing: face detection, alignment, and normalization
- Face encoding using 128-dimensional vectors
- Matching threshold tuned to balance accuracy and false positives
- Multi-face detection for classroom scenarios

**Real-world testing:**
- Tested with 20 friends in controlled environment
- 95% recognition accuracy in good lighting
- Performance drops with poor lighting or masks

**Challenges:**
- Handling variations in lighting conditions
- Detecting faces at different angles
- Preventing false positives with similar-looking faces
- Optimizing for real-time performance on CPU
        """,
    },
    {
        "name": "Sentiment Analysis Dashboard",
        "category": "NLP",
        "tech": "BERT • Streamlit • Pandas",
        "github": "https://github.com/dheeraj815",
        "description": """
Web dashboard for analyzing sentiment in product reviews and customer feedback using transformer models.

**What I built:** Tool that analyzes sentiment (positive/negative/neutral) from text input or CSV upload.

**Implementation:**
- Fine-tuned DistilBERT on IMDB movie review dataset
- Built REST API using FastAPI
- Created interactive dashboard with Streamlit
- Batch processing for analyzing multiple reviews
- Visualizations showing sentiment distribution

**Technical approach:**
- Started with pre-trained DistilBERT model
- Fine-tuned on domain-specific data (product reviews)
- Achieved 91% accuracy on test set
- Optimized model for inference speed using ONNX

**Features:**
- Single text analysis with confidence scores
- Bulk analysis from CSV files
- Export results to Excel
- Word cloud visualization for positive/negative words
- Aspect-based sentiment (experimental)

**Learnings:**
- Transfer learning with transformer models
- Handling different text lengths and formats
- Model quantization for faster inference
- Building production-ready ML applications
        """,
    },
    {
        "name": "Personal Portfolio Website",
        "category": "Web Development",
        "tech": "Streamlit • Plotly • Python",
        "github": "https://github.com/dheeraj815",
        "description": """
This interactive portfolio website you're currently viewing! Built entirely with Python and Streamlit.

**Why I built this:** To showcase my projects in an interactive way and learn web development with Python.

**What I implemented:**
- Custom CSS styling for professional look
- Multi-page navigation with session state
- Interactive charts using Plotly
- Responsive design for mobile devices
- Project filtering and categorization

**Technical stack:**
- Streamlit for web framework
- Plotly for data visualizations
- Custom CSS for styling
- Deployed on Streamlit Cloud (free tier)

**What I learned:**
- Web development fundamentals (HTML, CSS)
- Creating interactive dashboards
- UI/UX design principles
- Deploying web applications
- Writing clean, maintainable code

**Future improvements:**
- Add blog section for technical writing
- Integrate GitHub API for live stats
- Add project demo videos
- Implement contact form
        """,
    }
]

# HOME
if selected == "🏠 Home":
    st.markdown(f"""
    <div class="hero-wrapper">
        <div class="hero-name">Dheeraj Muley</div>
        <div class="hero-role">BTech AI/ML Engineering Student</div>
        <div class="hero-tagline">
            3rd year student passionate about AI, Machine Learning, and building practical solutions to real-world problems
        </div>
        <div style="text-align: center; margin-top: 20px;">
            <span class="availability-badge">
                <span class="pulse-dot"></span>
                Actively Seeking AI/ML Internships
            </span>
        </div>
        <div class="social-container">
            <a href="mailto:dheerajmuley006@gmail.com" class="social-link">Email Me</a>
            <a href="https://github.com/dheeraj815" target="_blank" class="social-link">GitHub</a>
            <a href="https://www.linkedin.com/in/dheeraj-muley" target="_blank" class="social-link">LinkedIn</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="stat-box"><div class="stat-num">15+</div><div class="stat-text">Major Projects</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-box"><div class="stat-num">10+</div><div class="stat-text">Technologies</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-box"><div class="stat-num">3.5</div><div class="stat-text">Years of Study</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-box"><div class="stat-num">5+</div><div class="stat-text">Certifications</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Quick highlights
    st.markdown('<div class="section-title" style="font-size: 2rem; margin-top: 60px;">What I\'m Currently Working On</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="skill-container">
            <div class="skill-header">📚 Learning</div>
            <div class="timeline-desc">
                • Advanced Deep Learning techniques<br>
                • MLOps and model deployment<br>
                • Cloud platforms (AWS, GCP)<br>
                • Production-grade ML systems
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="skill-container">
            <div class="skill-header">🚀 Building</div>
            <div class="timeline-desc">
                • LLM-powered applications<br>
                • Computer vision projects<br>
                • Full-stack ML pipelines<br>
                • Contributing to open source
            </div>
        </div>
        """, unsafe_allow_html=True)

# ABOUT
elif selected == "👤 About":
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## Who I Am
        
        I'm a third-year **BTech AI/ML** student with a genuine passion for artificial intelligence and its applications. I love the challenge of turning theoretical concepts into working solutions.
        
        ## My Journey
        
        My interest in AI started in my first year when I took an introductory ML course. Since then, I've been consistently building projects, taking online courses, and pushing myself to learn more. I've completed **15+ major projects** across various domains including computer vision, NLP, and web development.
        
        What excites me most is seeing my models actually work in practice - whether it's correctly classifying an image, answering a question, or making a useful prediction.
        
        ## What I'm Looking For
        
        I'm actively seeking **AI/ML internship opportunities** where I can:
        - Work on real-world ML problems
        - Learn from experienced practitioners
        - Contribute to production systems
        - Develop industry-relevant skills
        
        ## My Approach
        
        I believe in learning by doing. Every project I build teaches me something new - sometimes it's a technical skill, sometimes it's about problem-solving, and often it's about what doesn't work (which is equally valuable).
        
        I'm comfortable with:
        - Reading research papers and implementing algorithms
        - Debugging stubborn bugs at 2 AM
        - Asking for help when stuck
        - Documenting my work for others
        
        ## Beyond Code
        
        When I'm not coding, I enjoy:
        - Reading ML research papers and blogs
        - Participating in online coding communities
        - Exploring new technologies and tools
        - Staying updated with AI trends
        """)

    with col2:
        st.markdown("""
        <div class="skill-container">
            <div class="skill-header">🎯 Current Focus</div>
            <div class="skill-list">
                <span class="skill-chip">Deep Learning</span>
                <span class="skill-chip">LLM Applications</span>
                <span class="skill-chip">Computer Vision</span>
                <span class="skill-chip">MLOps</span>
            </div>
        </div>
        
        <div class="skill-container">
            <div class="skill-header">💪 Strengths</div>
            <div class="timeline-desc">
                • Quick learner<br>
                • Problem solver<br>
                • Self-motivated<br>
                • Team player<br>
                • Strong fundamentals
            </div>
        </div>
        
        <div class="skill-container">
            <div class="skill-header">🌱 Growing</div>
            <div class="timeline-desc">
                • Production ML<br>
                • System design<br>
                • Cloud platforms<br>
                • Team collaboration
            </div>
        </div>
        """, unsafe_allow_html=True)

# PROJECTS
elif selected == "💼 Projects":
    st.markdown('<div class="section-title">My Projects</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero-tagline" style="text-align: center; margin-bottom: 40px;">
        Here are some of my favorite projects. Each one taught me something valuable about AI/ML and software development.
    </div>
    """, unsafe_allow_html=True)

    project_filter = st.selectbox(
        "Filter by Category",
        ["All Projects", "Healthcare AI", "Computer Vision", "NLP", "FinTech", "Web Development"],
        key="project_filter"
    )

    if project_filter != "All Projects":
        filtered_projects = [p for p in authentic_projects if p["category"] == project_filter]
    else:
        filtered_projects = authentic_projects

    for idx, project in enumerate(filtered_projects):
        st.markdown(f"""
        <div class="project-card">
            <div class="project-header">
                <div class="project-title">{project["name"]}</div>
                <div class="project-meta">
                    <span class="tech-badge">{project["tech"]}</span>
                    <a href="{project["github"]}" target="_blank" class="project-link">View on GitHub →</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(project["description"])

        if idx < len(filtered_projects) - 1:
            st.markdown("---")

# EDUCATION
elif selected == "🎓 Education":
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-year">2022 - 2026 (Expected)</div>
        <div class="timeline-title">Bachelor of Technology in AI & Machine Learning</div>
        <div class="timeline-desc">
            <strong>Current Status:</strong> 3rd Year Student<br><br>
            
            <strong>Relevant Coursework:</strong><br>
            • Machine Learning & Deep Learning<br>
            • Data Structures & Algorithms<br>
            • Database Management Systems<br>
            • Computer Vision<br>
            • Natural Language Processing<br>
            • Statistical Methods<br>
            • Software Engineering<br><br>
            
            <strong>Academic Projects:</strong><br>
            • Medical Image Classification System (Major Project)<br>
            • Face Recognition Attendance System<br>
            • Sentiment Analysis of Social Media Data<br>
            • Predictive Modeling for Stock Prices<br><br>
            
            <strong>Skills Developed:</strong><br>
            • Strong foundation in ML algorithms and mathematics<br>
            • Practical experience with modern ML frameworks<br>
            • Software development and project management<br>
            • Research paper reading and implementation
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-year">2020 - 2022</div>
        <div class="timeline-title">Higher Secondary Education (12th Grade)</div>
        <div class="timeline-desc">
            <strong>Stream:</strong> Science (PCM - Physics, Chemistry, Mathematics)<br><br>
            
            <strong>Achievements:</strong><br>
            • Strong foundation in Mathematics and Physics<br>
            • First exposure to programming (Python basics)<br>
            • Developed interest in technology and problem-solving
        </div>
    </div>
    """, unsafe_allow_html=True)

# SKILLS
elif selected == "🛠️ Skills":
    st.markdown('<div class="section-title">Technical Skills</div>', unsafe_allow_html=True)

    skills_data = {
        "🤖 Machine Learning": {
            "skills": ["TensorFlow", "PyTorch", "Scikit-learn", "Keras", "XGBoost"],
            "proficiency": "Intermediate - Working knowledge through academic and personal projects"
        },
        "🧠 Deep Learning": {
            "skills": ["CNN", "RNN", "LSTM", "Transfer Learning", "Transformers"],
            "proficiency": "Intermediate - Built multiple DL projects, still learning advanced architectures"
        },
        "👁️ Computer Vision": {
            "skills": ["OpenCV", "Image Classification", "Object Detection", "Face Recognition"],
            "proficiency": "Intermediate - Completed several CV projects"
        },
        "💬 Natural Language Processing": {
            "skills": ["BERT", "Text Classification", "Sentiment Analysis", "LangChain", "RAG"],
            "proficiency": "Beginner-Intermediate - Working on expanding NLP knowledge"
        },
        "🐍 Programming Languages": {
            "skills": ["Python (Strong)", "SQL", "JavaScript (Basic)", "C++ (Academic)"],
            "proficiency": "Python is my primary language; comfortable with others for specific tasks"
        },
        "🌐 Web Development": {
            "skills": ["Streamlit", "FastAPI", "Flask", "HTML/CSS", "Git"],
            "proficiency": "Intermediate - Can build functional web apps and deploy ML models"
        },
        "📊 Data Science": {
            "skills": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Jupyter"],
            "proficiency": "Intermediate - Comfortable with data analysis and visualization"
        },
        "☁️ Cloud & Tools": {
            "skills": ["Google Colab", "Git/GitHub", "VS Code", "Docker (Learning)"],
            "proficiency": "Beginner - Using cloud platforms for training; learning DevOps"
        }
    }

    for category, data in skills_data.items():
        skill_chips = "".join([f'<span class="skill-chip">{skill}</span>' for skill in data["skills"]])

        st.markdown(f"""
        <div class="skill-container">
            <div class="skill-header">{category}</div>
            <div class="skill-list">{skill_chips}</div>
            <div class="timeline-desc" style="margin-top: 15px; font-size: 0.9rem; color: #94a3b8;">
                <em>{data["proficiency"]}</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Soft Skills
    st.markdown('<div class="section-title" style="font-size: 2rem; margin-top: 50px;">Soft Skills</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="skill-container">
            <div class="skill-list">
                <span class="skill-chip">Problem Solving</span>
                <span class="skill-chip">Quick Learning</span>
                <span class="skill-chip">Self-Motivated</span>
                <span class="skill-chip">Research Skills</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="skill-container">
            <div class="skill-list">
                <span class="skill-chip">Documentation</span>
                <span class="skill-chip">Team Collaboration</span>
                <span class="skill-chip">Time Management</span>
                <span class="skill-chip">Adaptability</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# CERTIFICATIONS
elif selected == "📜 Certifications":
    st.markdown('<div class="section-title">Certifications & Courses</div>', unsafe_allow_html=True)

    certifications = [
        {
            "name": "Machine Learning Specialization",
            "provider": "Coursera (Stanford University)",
            "date": "2024",
            "skills": "Supervised Learning, Neural Networks, ML Best Practices"
        },
        {
            "name": "Deep Learning Specialization",
            "provider": "Coursera (deeplearning.ai)",
            "date": "2024",
            "skills": "CNNs, RNNs, LSTMs, Transformers, Optimization"
        },
        {
            "name": "Python for Data Science",
            "provider": "DataCamp / Udemy",
            "date": "2023",
            "skills": "Pandas, NumPy, Matplotlib, Data Analysis"
        },
        {
            "name": "TensorFlow Developer Certificate",
            "provider": "Google (In Progress)",
            "date": "Expected 2026",
            "skills": "TensorFlow, Keras, Model Deployment"
        },
        {
            "name": "AWS Cloud Practitioner",
            "provider": "Amazon Web Services (Preparing)",
            "date": "Expected 2026",
            "skills": "Cloud Computing, AWS Services"
        }
    ]

    for cert in certifications:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-year">{cert["date"]}</div>
            <div class="timeline-title">{cert["name"]}</div>
            <div class="timeline-desc">
                <strong>Provider:</strong> {cert["provider"]}<br>
                <strong>Skills Covered:</strong> {cert["skills"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="font-size: 2rem; margin-top: 50px;">Online Learning</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-container">
        <div class="timeline-desc">
            Beyond formal certifications, I regularly learn from:<br><br>
            
            <strong>📺 YouTube Channels:</strong><br>
            • Sentdex (Python & ML)<br>
            • CodeWithHarry (Web Development)<br>
            • Krish Naik (Data Science & ML)<br>
            • StatQuest (ML Concepts)<br><br>
            
            <strong>📚 Resources:</strong><br>
            • Kaggle Learn & Competitions<br>
            • Medium & Towards Data Science articles<br>
            • Research papers on arXiv<br>
            • Official documentation (TensorFlow, PyTorch, etc.)<br><br>
            
            <strong>👥 Communities:</strong><br>
            • Stack Overflow<br>
            • GitHub Discussions<br>
            • Reddit (r/MachineLearning, r/learnmachinelearning)<br>
            • Discord ML communities
        </div>
    </div>
    """, unsafe_allow_html=True)

# ACHIEVEMENTS
elif selected == "🏆 Achievements":
    st.markdown('<div class="section-title">Achievements & Milestones</div>', unsafe_allow_html=True)

    achievements = [
        {
            "icon": "🎯",
            "title": "15+ Complete Projects",
            "desc": "Built diverse ML applications from healthcare to finance, each solving a specific problem"
        },
        {
            "icon": "📚",
            "title": "5+ Certifications",
            "desc": "Completed courses from Stanford, deeplearning.ai, and other reputed platforms"
        },
        {
            "icon": "💻",
            "title": "Active GitHub Profile",
            "desc": "Maintained consistent project contributions and documentation"
        },
        {
            "icon": "🏅",
            "title": "Academic Excellence",
            "desc": "Maintained strong academic performance while pursuing practical projects"
        },
        {
            "icon": "🧠",
            "title": "Research Implementation",
            "desc": "Successfully implemented algorithms from research papers in projects"
        },
        {
            "icon": "📖",
            "title": "Technical Blog Writing",
            "desc": "Documented learnings and tutorials to help fellow students"
        },
        {
            "icon": "🤝",
            "title": "Peer Collaboration",
            "desc": "Worked with classmates on group projects and study sessions"
        },
        {
            "icon": "🎓",
            "title": "Continuous Learning",
            "desc": "Consistently upgrading skills through online courses and self-study"
        },
        {
            "icon": "🔧",
            "title": "Problem Solving",
            "desc": "Successfully debugged complex issues and found creative solutions"
        }
    ]

    cols = st.columns(3)
    for idx, achievement in enumerate(achievements):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="contact-card">
                <div class="contact-emoji">{achievement["icon"]}</div>
                <div class="timeline-title" style="margin-bottom: 12px; font-size: 1.2rem;">{achievement["title"]}</div>
                <div class="timeline-desc" style="font-size: 0.95rem;">{achievement["desc"]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="font-size: 2rem; margin-top: 60px;">What I\'m Proud Of</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-container">
        <div class="timeline-desc" style="font-size: 1.05rem; line-height: 1.8;">
            <strong>🎯 Consistency:</strong> I've maintained a steady learning pace over the past 2 years, completing projects regularly and documenting my progress.<br><br>
            
            <strong>💡 Practical Focus:</strong> Every project I build has a clear purpose and teaches me something new about AI/ML in practice.<br><br>
            
            <strong>📈 Growth Mindset:</strong> I'm not afraid to tackle challenging problems or admit when I need to learn something new.<br><br>
            
            <strong>🤝 Helping Others:</strong> I enjoy sharing what I learn through documentation and helping classmates with their projects.<br><br>
            
            <strong>🔍 Attention to Detail:</strong> I take time to understand concepts deeply rather than just copying code from tutorials.
        </div>
    </div>
    """, unsafe_allow_html=True)

# CONTACT
elif selected == "📧 Contact":
    st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-tagline" style="text-align: center; margin-bottom: 45px;">
        I'm actively looking for AI/ML internship opportunities! Feel free to reach out if you'd like to discuss projects, opportunities, or just chat about AI.
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

    st.markdown('<div class="section-title" style="font-size: 2rem; margin-top: 60px;">What I\'m Looking For</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="skill-container">
            <div class="skill-header">💼 Internship Opportunities</div>
            <div class="timeline-desc">
                • AI/ML Engineering roles<br>
                • Data Science positions<br>
                • Computer Vision projects<br>
                • NLP applications<br>
                • Full-stack ML development<br><br>
                <strong>Duration:</strong> 2-6 months<br>
                <strong>Type:</strong> Remote or On-site<br>
                <strong>Start:</strong> Flexible
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="skill-container">
            <div class="skill-header">🎯 What I Can Offer</div>
            <div class="timeline-desc">
                • Strong fundamentals in ML/DL<br>
                • Practical project experience<br>
                • Quick learning ability<br>
                • Self-motivated work ethic<br>
                • Good communication skills<br><br>
                <strong>Best at:</strong> Python, TensorFlow, PyTorch<br>
                <strong>Eager to learn:</strong> MLOps, Production ML
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="font-size: 2rem; margin-top: 50px;">Quick Response</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-container">
        <div class="timeline-desc" style="text-align: center; font-size: 1.05rem;">
            I usually respond to emails within 24 hours. For urgent inquiries, feel free to connect on LinkedIn!<br><br>
            <strong>Best time to reach:</strong> Anytime! I check messages regularly.<br>
            <strong>Time zone:</strong> IST (GMT+5:30)
        </div>
    </div>
    """, unsafe_allow_html=True)

