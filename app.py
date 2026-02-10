import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Dheeraj Muley - AI/ML Engineer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS - Market-Level Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    :root {
        --primary: #3b82f6;
        --primary-dark: #2563eb;
        --secondary: #8b5cf6;
        --accent: #06b6d4;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --dark-bg: #0f172a;
        --card-bg: #1e293b;
        --card-hover: #334155;
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --text-muted: #94a3b8;
        --border: #334155;
        --border-light: #475569;
    }
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        letter-spacing: -0.01em;
    }
    
    /* Main Background */
    .main {
        background: linear-gradient(to bottom, #0f172a 0%, #1e293b 100%);
        position: relative;
    }
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 30%, rgba(59, 130, 246, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(139, 92, 246, 0.08) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    
    .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
        position: relative;
        z-index: 1;
    }
    
    /* Typography - Professional & Consistent */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        line-height: 1.2 !important;
        margin: 0 !important;
    }
    
    /* Main Heading */
    h1 {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem !important;
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Section Headings */
    h2 {
        font-size: 1.875rem !important;
        margin: 3rem 0 1.5rem 0 !important;
        padding-bottom: 0.75rem !important;
        border-bottom: 2px solid var(--border);
        position: relative;
    }
    
    h2::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 60px;
        height: 2px;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
    }
    
    /* Subsection Headings */
    h3 {
        font-size: 1.25rem !important;
        color: var(--text-primary) !important;
        margin: 2rem 0 1rem 0 !important;
        font-weight: 600 !important;
    }
    
    h4 {
        font-size: 1.125rem !important;
        color: var(--text-secondary) !important;
        margin: 1.5rem 0 0.75rem 0 !important;
        font-weight: 600 !important;
    }
    
    /* Body Text */
    p, li, span, div {
        color: var(--text-secondary) !important;
        font-size: 1rem !important;
        line-height: 1.7 !important;
        font-weight: 400 !important;
    }
    
    strong {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    
    code {
        background: rgba(59, 130, 246, 0.1) !important;
        color: #93c5fd !important;
        padding: 0.2rem 0.5rem !important;
        border-radius: 0.375rem !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.875rem !important;
        border: 1px solid rgba(59, 130, 246, 0.2);
    }
    
    /* Professional Cards */
    .stAlert {
        background: var(--card-bg) !important;
        border: 1px solid var(--border) !important;
        border-left: 3px solid var(--primary) !important;
        border-radius: 0.75rem !important;
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .stAlert:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(59, 130, 246, 0.15);
        border-left-color: var(--accent);
    }
    
    /* Premium Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 0.5rem !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25) !important;
        cursor: pointer !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.35) !important;
        background: linear-gradient(135deg, var(--primary-dark) 0%, var(--secondary) 100%) !important;
    }
    
    /* Metric Cards */
    [data-testid="stMetric"] {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 0.75rem;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(59, 130, 246, 0.15);
        border-color: var(--primary);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2.25rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
        border-right: 1px solid var(--border) !important;
    }
    
    [data-testid="stSidebar"] .block-container {
        padding: 2rem 1rem;
    }
    
    /* Radio Buttons - Navigation */
    .stRadio > label {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        font-size: 0.875rem !important;
        margin-bottom: 1rem !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    .stRadio > div {
        gap: 0.5rem !important;
    }
    
    .stRadio > div > label {
        background: rgba(30, 41, 59, 0.6) !important;
        padding: 0.875rem 1rem !important;
        border-radius: 0.5rem !important;
        border: 1px solid var(--border) !important;
        color: var(--text-secondary) !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        font-weight: 500 !important;
    }
    
    .stRadio > div > label:hover {
        background: rgba(59, 130, 246, 0.1) !important;
        border-color: var(--primary) !important;
        transform: translateX(4px);
        color: var(--text-primary) !important;
    }
    
    .stRadio > div > label[aria-checked="true"] {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
        border-color: var(--primary) !important;
        color: white !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: var(--card-bg) !important;
        border-radius: 0.75rem !important;
        border: 1px solid var(--border) !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        padding: 1rem 1.25rem !important;
        transition: all 0.3s ease !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: var(--card-hover) !important;
        border-color: var(--primary) !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid var(--border);
        border-top: none;
        border-radius: 0 0 0.75rem 0.75rem;
        padding: 1.5rem;
    }
    
    /* Links */
    a {
        color: var(--accent) !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    a:hover {
        color: var(--primary) !important;
        text-decoration: underline !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: rgba(30, 41, 59, 0.6);
        border-radius: 0.75rem;
        padding: 0.5rem;
        border: 1px solid var(--border);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 0.5rem !important;
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(59, 130, 246, 0.1) !important;
        color: var(--text-primary) !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25);
    }
    
    /* Professional Badge System */
    .badge {
        display: inline-block;
        padding: 0.4rem 0.875rem;
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 0.5rem;
        color: #93c5fd !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        margin: 0.25rem;
        transition: all 0.3s ease;
    }
    
    .badge:hover {
        background: rgba(59, 130, 246, 0.2);
        border-color: var(--primary);
        transform: translateY(-2px);
    }
    
    .badge-success {
        background: rgba(16, 185, 129, 0.1);
        border-color: rgba(16, 185, 129, 0.3);
        color: #86efac !important;
    }
    
    .badge-warning {
        background: rgba(245, 158, 11, 0.1);
        border-color: rgba(245, 158, 11, 0.3);
        color: #fcd34d !important;
    }
    
    /* Lists */
    ul, ol {
        margin: 1rem 0 !important;
        padding-left: 1.5rem !important;
    }
    
    li {
        margin-bottom: 0.75rem !important;
        color: var(--text-secondary) !important;
    }
    
    ul li::marker {
        color: var(--primary);
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }
    
    /* Status Dot */
    .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--success);
        margin-right: 0.5rem;
        animation: pulse 2s ease-in-out infinite;
        box-shadow: 0 0 8px var(--success);
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark-bg);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--primary), var(--secondary));
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #60a5fa, #a78bfa);
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border), transparent);
        margin: 2.5rem 0;
    }
    
    /* Selection */
    ::selection {
        background: rgba(59, 130, 246, 0.3);
        color: var(--text-primary);
    }
    
    /* Professional Info Cards */
    .info-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .info-card:hover {
        border-color: var(--primary);
        box-shadow: 0 8px 16px rgba(59, 130, 246, 0.15);
    }
    
    /* Hero Section */
    .hero-section {
        padding: 3rem 0;
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Stat Box */
    .stat-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
        border: 1px solid var(--border);
        border-radius: 0.75rem;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(59, 130, 246, 0.2);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: var(--text-muted);
        font-size: 0.875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)

# GitHub Repository Data
GITHUB_REPOS = {
    "AI-Powered Trading Bot with ML": {
        "url": "https://github.com/dheeraj815/AI-Powered-Trading-Bot-with-ML",
        "description": "Sophisticated AI-powered trading bot leveraging ensemble machine learning models to generate real-time buy/sell signals from live market data, featuring advanced technical analysis and comprehensive portfolio management.",
        "tech_stack": ["Python", "Scikit-learn", "yfinance", "Streamlit", "Plotly", "TA-Lib", "Ensemble ML"],
        "category": "Financial AI",
        "highlights": [
            "Ensemble ML model combining Random Forest, Gradient Boosting, and Logistic Regression for robust predictions",
            "70+ advanced technical indicators including RSI, MACD, Bollinger Bands, and custom engineered features",
            "Real-time trading signal generation with confidence scoring and probability metrics",
            "Interactive portfolio management dashboard with live P&L tracking and risk analytics",
            "Comprehensive backtesting engine with Sharpe ratio, maximum drawdown, and win rate analysis",
            "Professional financial charting with candlestick patterns and technical overlays",
            "Time-series cross-validation ensuring robust model generalization"
        ],
        "status": "Active",
        "impact": "Automated trading system enabling data-driven investment decisions with quantified risk management",
        "metrics": {"Validation Accuracy": "72%", "Features Engineered": "70+", "Backtesting": "Complete"}
    },
    "AI Medical Diagnosis & Health Assistant": {
        "url": "https://github.com/dheeraj815/AI-Medical-Diagnosis-Health-Assitant",
        "description": "Intelligent medical diagnosis system utilizing machine learning to analyze symptoms and provide evidence-based health recommendations through an intuitive natural language interface.",
        "tech_stack": ["Python", "TensorFlow", "NLP", "Streamlit", "Medical AI", "Classification Models"],
        "category": "Healthcare AI",
        "highlights": [
            "Advanced symptom-based disease prediction using ensemble classification algorithms",
            "Natural language processing for medical query understanding and contextual analysis",
            "Interactive conversational AI interface for health consultation and triage",
            "Integration with comprehensive medical knowledge databases and symptom taxonomies",
            "Real-time diagnosis confidence scoring with detailed explanations and recommendations"
        ],
        "status": "Active",
        "impact": "Healthcare accessibility tool with potential for preliminary medical screening and health education",
        "metrics": {"Prediction Accuracy": "87%", "Response Time": "<2s", "Diseases Covered": "100+"}
    },
    "Rock Paper Scissors AI": {
        "url": "https://github.com/dheeraj815/RPS-AI",
        "description": "Intelligent game AI that learns and adapts to player patterns using machine learning algorithms for strategic prediction in Rock-Paper-Scissors gameplay.",
        "tech_stack": ["Python", "Scikit-learn", "Pattern Recognition", "Markov Chains", "Reinforcement Learning"],
        "category": "Game AI",
        "highlights": [
            "Advanced pattern recognition algorithm for move prediction and strategy adaptation",
            "Reinforcement learning implementation with Q-learning for optimal gameplay",
            "Statistical analysis engine for detecting and exploiting player behavior patterns",
            "Real-time prediction accuracy tracking with visual performance analytics",
            "Adaptive strategy adjustment based on historical move sequences"
        ],
        "status": "Completed",
        "impact": "Practical demonstration of ML in game theory and adaptive AI systems",
        "metrics": {"Win Rate": "65%", "Adaptation Speed": "10 moves", "Pattern Detection": "Real-time"}
    },
    "Movie Recommender System": {
        "url": "https://github.com/dheeraj815/Movie-RecommenderNLP",
        "description": "Sophisticated NLP-based recommendation engine employing content-based filtering and semantic similarity algorithms for personalized movie suggestions.",
        "tech_stack": ["Python", "NLP", "NLTK", "Cosine Similarity", "TF-IDF", "Pandas"],
        "category": "Recommendation Systems",
        "highlights": [
            "Content-based filtering utilizing movie plots, genres, cast, and comprehensive metadata",
            "TF-IDF vectorization for advanced text similarity computation and feature extraction",
            "Cosine similarity algorithm for precise recommendation matching and ranking",
            "Interactive web interface with intelligent search and multi-criteria filtering",
            "Genre-aware recommendation system with user preference learning capabilities"
        ],
        "status": "Completed",
        "impact": "Personalized content discovery platform enhancing user engagement and satisfaction",
        "metrics": {"Precision@10": "82%", "Dataset Size": "5000+ movies", "Avg Response": "<500ms"}
    },
    "House Price Predictor": {
        "url": "https://github.com/dheeraj815/House-Price-Predictor",
        "description": "Comprehensive real estate price prediction system utilizing multiple regression algorithms and extensive feature engineering for accurate market valuation analysis.",
        "tech_stack": ["Python", "Pandas", "Scikit-learn", "Regression Models", "Feature Engineering"],
        "category": "Predictive Analytics",
        "highlights": [
            "Multi-algorithm comparison including Linear, Ridge, Lasso, and Ensemble regression methods",
            "Advanced feature engineering with domain-specific real estate insights",
            "Robust data preprocessing pipeline with outlier detection and treatment",
            "Cross-validation strategy for reliable model performance assessment",
            "Interactive prediction interface with confidence intervals and feature importance"
        ],
        "status": "Completed",
        "impact": "Data-driven real estate valuation tool for informed property investment decisions",
        "metrics": {"RMSE": "3.2%", "R² Score": "0.89", "Features": "25+"}
    },
    "Portfolio Website": {
        "url": "https://github.com/dheeraj815/Portfolio",
        "description": "Professional portfolio platform showcasing AI/ML projects with interactive visualizations, modern design principles, and responsive user experience.",
        "tech_stack": ["Streamlit", "Python", "Plotly", "CSS", "Web Design", "UI/UX"],
        "category": "Web Development",
        "highlights": [
            "Responsive design with custom CSS and modern aesthetic principles",
            "Interactive project showcase with dynamic filtering and search capabilities",
            "Data visualizations using Plotly for engaging presentations",
            "Professional UI/UX following industry best practices and accessibility standards",
            "Optimized performance with cross-browser compatibility"
        ],
        "status": "Active",
        "impact": "Professional online presence establishing credibility and showcasing technical capabilities",
        "metrics": {"Load Time": "<1s", "Mobile Responsive": "100%", "Accessibility": "WCAG 2.1"}
    },
    "GitHub Profile": {
        "url": "https://github.com/dheeraj815/dheeraj815",
        "description": "Automated GitHub profile README featuring dynamic statistics, activity tracking, technology showcase, and professional presentation.",
        "tech_stack": ["Markdown", "GitHub Actions", "APIs", "Automation", "CI/CD"],
        "category": "Developer Tools",
        "highlights": [
            "Automated GitHub statistics generation with real-time updates",
            "Dynamic skill badges and comprehensive technology showcase",
            "Project highlights with direct repository links and descriptions",
            "Professional profile branding and visual identity",
            "Continuous integration for automated daily updates"
        ],
        "status": "Active",
        "impact": "Enhanced GitHub presence and professional visibility in developer community",
        "metrics": {"Update Frequency": "Daily", "API Integration": "GitHub Stats", "Uptime": "99.9%"}
    }
}

# Skills Data with Proficiency Levels
SKILLS = {
    "Machine Learning & AI": {
        "skills": ["TensorFlow", "PyTorch", "Scikit-learn", "Keras", "XGBoost", "Model Deployment"],
        "proficiency": 85,
        "level": "Advanced",
        "description": "Strong foundation in supervised/unsupervised learning, neural networks, ensemble methods, and model optimization with production deployment experience",
        "icon": "🤖"
    },
    "Deep Learning": {
        "skills": ["CNN", "RNN", "LSTM", "Transfer Learning", "Computer Vision", "NLP Models"],
        "proficiency": 75,
        "level": "Intermediate-Advanced",
        "description": "Hands-on experience with various deep learning architectures for image and text processing tasks",
        "icon": "🧠"
    },
    "Programming Languages": {
        "skills": ["Python (Expert)", "SQL", "JavaScript", "C++", "HTML/CSS"],
        "proficiency": 90,
        "level": "Advanced",
        "description": "Expert-level Python programming for ML/AI development and data processing with full-stack capabilities",
        "icon": "💻"
    },
    "Data Science & Analytics": {
        "skills": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Statistical Analysis"],
        "proficiency": 85,
        "level": "Advanced",
        "description": "Proficient in data manipulation, statistical analysis, and creating insightful visualizations",
        "icon": "📊"
    },
    "Web Development": {
        "skills": ["Streamlit", "Flask", "FastAPI", "React (Basic)", "REST APIs"],
        "proficiency": 75,
        "level": "Intermediate-Advanced",
        "description": "Full-stack development capabilities with focus on ML model deployment and API development",
        "icon": "🌐"
    },
    "NLP & Text Processing": {
        "skills": ["NLTK", "spaCy", "TF-IDF", "Sentiment Analysis", "Text Classification"],
        "proficiency": 70,
        "level": "Intermediate",
        "description": "Experience with various NLP tasks including recommendation systems, chatbots, and text analysis",
        "icon": "💬"
    },
    "Financial Analysis & Trading": {
        "skills": ["TA-Lib", "yfinance", "Algorithmic Trading", "Technical Indicators", "Risk Management"],
        "proficiency": 75,
        "level": "Intermediate-Advanced",
        "description": "Proficient in quantitative finance, technical analysis, and building algorithmic trading systems",
        "icon": "💰"
    },
    "Tools & Platforms": {
        "skills": ["Git/GitHub", "Jupyter", "Google Colab", "VS Code", "Docker"],
        "proficiency": 80,
        "level": "Advanced",
        "description": "Proficient with modern development tools, version control, and containerization",
        "icon": "🛠️"
    },
    "Cloud & Deployment": {
        "skills": ["Streamlit Cloud", "Heroku", "AWS (Learning)", "Model Serving", "CI/CD"],
        "proficiency": 60,
        "level": "Intermediate",
        "description": "Learning cloud platforms and MLOps best practices for production deployment",
        "icon": "☁️"
    }
}

# Education Data
EDUCATION = {
    "degree": "Bachelor of Technology in Artificial Intelligence & Machine Learning",
    "institution": "Engineering College",
    "duration": "2024 - 2027",
    "status": "3rd Year Student",
    "gpa": "Strong Academic Performance",
    "coursework": [
        "Machine Learning & Deep Learning",
        "Data Structures & Algorithms",
        "Natural Language Processing",
        "Computer Vision",
        "Database Management Systems",
        "Statistical Methods for Data Science",
        "Software Engineering Principles",
        "Pattern Recognition"
    ],
    "achievements": [
        "Completed 50+ projects across diverse ML domains",
        "Strong foundation in AI/ML theory and practice",
        "Active participation in coding communities",
        "Consistent academic excellence"
    ]
}

# Certifications
CERTIFICATIONS = [
    {
        "name": "Machine Learning Specialization",
        "provider": "Coursera (Stanford University)",
        "instructor": "Andrew Ng",
        "date": "2024",
        "skills": ["Supervised Learning", "Neural Networks", "Best Practices"],
        "credential": "Verified Certificate",
        "status": "Completed"
    },
    {
        "name": "Deep Learning Specialization",
        "provider": "Coursera (deeplearning.ai)",
        "instructor": "Andrew Ng",
        "date": "2024",
        "skills": ["CNNs", "RNNs", "Transformers", "Optimization"],
        "credential": "Verified Certificate",
        "status": "Completed"
    },
    {
        "name": "Python for Data Science",
        "provider": "DataCamp",
        "instructor": "Multiple Instructors",
        "date": "2023",
        "skills": ["Pandas", "NumPy", "Data Visualization"],
        "credential": "Verified Certificate",
        "status": "Completed"
    }
]

# Session State
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h3 style='text-align: center; margin-bottom: 1.5rem;'>🧭 Navigation</h3>",
                unsafe_allow_html=True)

    pages = ["Home", "About", "Projects", "Skills",
             "Education", "Certifications", "Contact"]

    selected_page = st.radio(
        "Navigate to:",
        pages,
        index=pages.index(st.session_state.page),
        label_visibility="collapsed"
    )

    st.session_state.page = selected_page

    st.markdown("---")

    # Sidebar Profile Card
    st.markdown(f"""
    <div style='text-align: center; padding: 1.5rem 0;'>
        <div style='width: 100px; height: 100px; margin: 0 auto 1rem; background: linear-gradient(135deg, #3b82f6, #8b5cf6); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 3rem;'>
            👨‍💻
        </div>
        <h3 style='color: var(--text-primary); margin-bottom: 0.5rem; font-size: 1.25rem !important;'>Dheeraj Muley</h3>
        <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
            AI/ML Engineering Student
        </p>
        <div style='margin: 1rem 0;'>
            <p style='color: var(--text-muted); font-size: 0.875rem; line-height: 1.8;'>
                📍 India<br>
                🎓 BTech AIML (3rd Year)<br>
                💼 Seeking Internships
            </p>
        </div>
        <div style='margin: 1.5rem 0;'>
            <span class='badge badge-success' style='display: inline-flex; align-items: center;'>
                <span class='status-dot'></span>
                Available for Opportunities
            </span>
        </div>
        <div style='margin-top: 1.5rem; display: flex; justify-content: center; gap: 1rem;'>
            <a href='https://github.com/dheeraj815' target='_blank' style='font-size: 0.9rem;'>GitHub</a>
            <a href='https://linkedin.com/in/dheeraj-muley' target='_blank' style='font-size: 0.9rem;'>LinkedIn</a>
            <a href='mailto:dheerajmuley006@gmail.com' style='font-size: 0.9rem;'>Email</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==================== HOME PAGE ====================
if st.session_state.page == "Home":

    # Hero Section
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("# Dheeraj Muley")
        st.markdown(
            "### AI/ML Engineering Student | Building Intelligent Solutions")

        st.markdown("""
        Passionate **3rd-year BTech AI/ML student** specializing in building practical machine learning 
        applications. I transform complex problems into elegant solutions through artificial intelligence, 
        with expertise in **financial AI, healthcare systems, NLP, and computer vision**. 
        
        With **50+ completed projects** and a strong foundation in both theory and practice, I'm ready 
        to contribute to innovative teams and drive impactful AI solutions.
        """)

        st.info(
            "🟢 **Currently Available** for AI/ML internships and collaborative projects")

        # Action Buttons
        col_btn1, col_btn2, col_btn3 = st.columns(3)

        with col_btn1:
            if st.button("📧 Contact Me", use_container_width=True):
                st.session_state.page = "Contact"
                st.rerun()

        with col_btn2:
            if st.button("💼 View Projects", use_container_width=True):
                st.session_state.page = "Projects"
                st.rerun()

        with col_btn3:
            if st.button("🎓 Education", use_container_width=True):
                st.session_state.page = "Education"
                st.rerun()

    with col2:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>50+</div>
            <div class='stat-label'>Projects Completed</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>35+</div>
            <div class='stat-label'>Technologies Mastered</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>1.5</div>
            <div class='stat-label'>Years Experience</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Portfolio Metrics
    st.markdown("## 📊 Portfolio Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Projects Completed", "50+", "Active Development")
    with col2:
        st.metric("Technologies", "35+", "Continuously Growing")
    with col3:
        st.metric("Certifications", "3", "Verified & Complete")
    with col4:
        st.metric("GitHub Repos", "7+", "Featured Projects")

    st.markdown("---")

    # Core Competencies
    st.markdown("## 💡 Core Competencies")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🎯 Technical Expertise
        
        **Machine Learning Development**
        - Building predictive models and classification systems
        - End-to-end ML pipeline development and optimization
        - Advanced model evaluation and hyperparameter tuning
        - Feature engineering and data preprocessing
        
        **Deep Learning**
        - Neural network architectures for CV and NLP
        - Transfer learning and model fine-tuning
        - Custom architecture design and implementation
        
        **Financial AI & Algorithmic Trading**
        - Ensemble ML models for market prediction
        - Technical analysis and feature engineering
        - Real-time trading systems with backtesting
        - Risk management and portfolio optimization
        """)

    with col2:
        st.markdown("""
        ### 🚀 Domain Specialization
        
        **Healthcare AI**
        - Medical diagnosis and recommendation systems
        - Clinical decision support tools
        - Healthcare data analysis and visualization
        
        **Financial Technology**
        - Algorithmic trading systems
        - Portfolio optimization strategies
        - Market prediction and signal generation
        
        **NLP & Computer Vision**
        - Recommendation engines and chatbots
        - Image classification and pattern recognition
        - Sentiment analysis and text processing
        
        **Web Development & Deployment**
        - Full-stack ML application development
        - API design and microservices
        - Cloud deployment and MLOps
        """)

    st.markdown("---")

    # Featured Projects
    st.markdown("## ⭐ Featured Projects")

    featured_projects = [
        "AI-Powered Trading Bot with ML",
        "AI Medical Diagnosis & Health Assistant",
        "Movie Recommender System"
    ]

    for project_name in featured_projects:
        project = GITHUB_REPOS[project_name]

        with st.expander(f"**{project_name}** - {project['category']}", expanded=False):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**{project['description']}**")

                st.markdown("**Key Highlights:**")
                for highlight in project['highlights'][:4]:
                    st.markdown(f"- {highlight}")

            with col2:
                st.markdown(f"**Status:** `{project['status']}`")
                st.markdown(f"**Category:** `{project['category']}`")

                for metric_name, metric_value in project['metrics'].items():
                    st.markdown(f"**{metric_name}:** `{metric_value}`")

            tech_badges = " ".join(
                [f'<span class="badge">{tech}</span>' for tech in project['tech_stack']])
            st.markdown(tech_badges, unsafe_allow_html=True)

            st.markdown(f"[View on GitHub →]({project['url']})")

    st.markdown("---")

    # Current Focus Areas
    st.markdown("## 🔭 Current Focus & Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 📚 Learning
        
        - Advanced Deep Learning architectures
        - Quantitative Finance & Trading strategies
        - MLOps & Production ML systems
        - Cloud Platforms (AWS, GCP, Azure)
        - Large Language Models & Transformers
        - Reinforcement Learning algorithms
        """)

    with col2:
        st.markdown("""
        ### 🛠️ Building
        
        - Financial AI trading applications
        - LLM-powered intelligent systems
        - Healthcare AI diagnostic tools
        - End-to-end ML production pipelines
        - Open source project contributions
        - Research paper implementations
        """)

    with col3:
        st.markdown("""
        ### 🎯 Goals
        
        - Secure impactful AI/ML internship
        - Build production-ready ML systems
        - Contribute to open source AI projects
        - Expand cloud & MLOps expertise
        - Network with industry professionals
        - Publish technical blog posts
        """)

# ==================== ABOUT PAGE ====================
elif st.session_state.page == "About":

    st.markdown("# About Me")

    st.markdown("""
    Dedicated AI/ML engineering student with a passion for building intelligent systems that solve 
    real-world problems. My journey combines rigorous academic excellence with extensive hands-on 
    project experience across diverse domains.
    """)

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## 👋 Introduction
        
        I'm **Dheeraj Muley**, a third-year BTech student specializing in **Artificial Intelligence and Machine Learning**. 
        My journey into AI began with curiosity about how machines learn and make decisions, evolving into a 
        genuine passion for building intelligent systems that create meaningful impact.
        
        ## 🎓 Academic Journey
        
        Currently pursuing my **BTech in AI/ML** (3rd Year, 2024-2027), I've developed:
        
        **Technical Foundation**
        - Deep understanding of ML algorithms and mathematical foundations
        - Strong programming skills with expertise in Python and data science stack
        - Hands-on experience with modern ML frameworks (TensorFlow, PyTorch, Scikit-learn)
        - Project-based learning across financial AI, healthcare, NLP, and computer vision
        
        **Practical Experience**
        - **50+ complete projects** spanning multiple AI/ML domains
        - Experience with financial AI, healthcare diagnostics, NLP, and computer vision
        - End-to-end model development, deployment, and production considerations
        - Clean code practices, comprehensive documentation, and version control
        
        ## 🚀 My Approach
        
        **Learning by Building**: I believe in practical, hands-on learning. With **50+ projects completed**, 
        each one teaches me something new about real-world AI/ML applications - from small experiments to 
        production-ready systems with actual users.
        
        **Problem-First Mindset**: I start with deep understanding of the problem domain before jumping into solutions, 
        ensuring my ML models address actual needs and deliver measurable value.
        
        **Continuous Improvement**: Technology evolves rapidly in AI/ML. I stay current through research papers, 
        online courses, technical blogs, and active participation in ML communities.
        
        **Quality Focus**: I prioritize code quality, comprehensive documentation, testing, and industry best 
        practices in all my projects, making them production-ready and maintainable.
        
        ## 🌟 What Drives Me
        
        I'm fascinated by the potential of AI to transform industries and improve lives. Whether it's building 
        trading algorithms that make data-driven investment decisions, creating diagnostic tools that could assist 
        healthcare professionals, or developing recommendation systems that enhance user experience - I'm driven 
        by the real-world impact of intelligent systems.
        """)

    with col2:
        st.markdown("""
        ### 🎯 Technical Strengths
        
        **Core Programming**
        - Python (Advanced)
        - SQL, JavaScript
        - Algorithm Design
        - Data Structures
        
        **Machine Learning**
        - Supervised Learning
        - Unsupervised Learning
        - Ensemble Methods
        - Model Optimization
        
        **Deep Learning**
        - CNNs, RNNs, LSTMs
        - Transfer Learning
        - NLP Models
        - Computer Vision
        
        **Financial AI**
        - Algorithmic Trading
        - Technical Analysis
        - Risk Management
        - Market Prediction
        
        **Development**
        - Web Applications
        - API Development
        - Model Deployment
        - Version Control (Git)
        
        **Tools & Frameworks**
        - TensorFlow, PyTorch
        - Scikit-learn, Pandas
        - Streamlit, Flask
        - Plotly, Matplotlib
        
        ### 🌱 Currently Exploring
        
        - MLOps & Production ML
        - Large Language Models
        - Reinforcement Learning
        - Cloud Platforms (AWS)
        - Advanced NLP
        - Quantitative Finance
        
        ### 🏆 Key Achievements
        
        - 50+ ML projects completed
        - 3 verified certifications
        - Active GitHub contributor
        - Strong academic record
        - Multiple domain expertise
        """)

    st.markdown("---")

    st.markdown("## 🏆 What Sets Me Apart")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🔨 Hands-On Builder
        
        - **50+ complete projects** across domains
        - End-to-end implementations
        - Production-ready code quality
        - Comprehensive documentation
        - Real-world problem solving
        - Continuous iteration and improvement
        """)

    with col2:
        st.markdown("""
        ### 📚 Self-Directed Learner
        
        - Multiple verified certifications
        - Active in ML communities
        - Regular research paper reading
        - Continuous skill development
        - Experimental mindset
        - Knowledge sharing through documentation
        """)

    with col3:
        st.markdown("""
        ### 🎯 Results-Oriented
        
        - Strong analytical thinking
        - Systematic problem approach
        - Attention to detail
        - Quality-focused delivery
        - Adaptable to challenges
        - Data-driven decision making
        """)

    st.markdown("---")

    st.markdown("## 💼 Internship Readiness")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### What I'm Seeking
        
        **Position Types:**
        - AI/ML Engineering Intern
        - Quantitative Research Intern
        - Data Science Intern
        - Financial ML Intern
        - Applied AI Research Intern
        
        **Preferences:**
        - **Duration:** 2-6 months (Flexible)
        - **Mode:** Remote, Hybrid, or On-site
        - **Start Date:** Immediate to Flexible
        - **Commitment:** Full-time during internship
        - **Location:** India (Open to relocation)
        
        **Ideal Opportunity:**
        - Work on real-world ML problems
        - Learn from experienced professionals
        - Contribute to production systems
        - Exposure to industry best practices
        - Collaborative team environment
        """)

    with col2:
        st.markdown("""
        ### What I Bring
        
        **Technical Skills:**
        - Strong Python & ML fundamentals
        - 50+ hands-on project portfolio
        - Financial AI & trading expertise
        - Quick learner & adaptable
        - Clean code & documentation
        - Problem-solving abilities
        
        **Professional Qualities:**
        - Excellent communication skills
        - Collaborative team player
        - Self-motivated & proactive
        - Strong work ethic
        - Eager to learn from experts
        - Adaptable to new technologies
        
        **Proven Track Record:**
        - Diverse project portfolio
        - Academic excellence
        - Continuous learning
        - Community engagement
        """)

    st.markdown("---")

    st.markdown("""
    ## 🎓 Learning Philosophy
    
    My approach to continuous professional development is built on four pillars:
    
    **1. Structured Learning**
    - Following well-designed courses from reputable institutions
    - Ensuring comprehensive coverage of fundamentals
    - Building strong theoretical foundation
    - Verified certifications demonstrating expertise
    
    **2. Practical Application**
    - Immediately applying concepts to real projects
    - Reinforcing learning through hands-on implementation
    - Building portfolio of working applications
    - Iterating based on results and feedback
    
    **3. Community Engagement**
    - Active participation in ML communities
    - Learning from diverse perspectives
    - Staying updated with industry trends
    - Sharing knowledge and helping others
    
    **4. Research-Oriented**
    - Regular reading of research papers
    - Understanding cutting-edge developments
    - Implementing novel approaches
    - Staying ahead of the curve
    
    This philosophy has helped me grow from a curious beginner to a confident ML practitioner ready 
    to contribute to professional projects and collaborate with experienced teams.
    """)

# ==================== PROJECTS PAGE ====================
elif st.session_state.page == "Projects":

    st.markdown("# Projects Portfolio")

    st.markdown("""
    Comprehensive showcase of my AI/ML work spanning **50+ projects**. Featured below are my most significant 
    projects demonstrating end-to-end implementation, from problem definition to deployment, across financial AI, 
    healthcare, NLP, computer vision, and more.
    """)

    st.info("""
    **📌 Portfolio Overview:** I've completed 50+ projects across various AI/ML domains. This page features  
    7 major projects that best represent my capabilities. The complete collection is available on my 
    [GitHub](https://github.com/dheeraj815).
    """)

    st.markdown("---")

    # Project Filters
    col1, col2 = st.columns([3, 1])

    with col1:
        categories = ["All Projects"] + \
            list(set([proj['category'] for proj in GITHUB_REPOS.values()]))
        selected_category = st.selectbox("**Filter by Category:**", categories)

    with col2:
        sort_by = st.selectbox(
            "**Sort by:**", ["Recent", "Category", "Status"])

    st.markdown("---")

    # Display Projects
    for project_name, project in GITHUB_REPOS.items():

        if selected_category != "All Projects" and project['category'] != selected_category:
            continue

        st.markdown(f"## {project_name}")

        # Status and Category
        col1, col2, col3 = st.columns([2, 2, 1])

        with col1:
            status_class = "badge-success" if project['status'] == "Active" else "badge"
            st.markdown(
                f'<span class="{status_class}">{project["status"]}</span>', unsafe_allow_html=True)

        with col2:
            st.markdown(
                f'<span class="badge">{project["category"]}</span>', unsafe_allow_html=True)

        with col3:
            st.markdown(f"[GitHub →]({project['url']})")

        st.markdown(f"### 📝 Overview")
        st.markdown(project['description'])

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("### ✨ Key Highlights")
            for highlight in project['highlights']:
                st.markdown(f"- {highlight}")

            st.markdown(f"### 🎯 Impact")
            st.markdown(project['impact'])

        with col2:
            st.markdown("### 🛠️ Tech Stack")
            for tech in project['tech_stack']:
                st.markdown(
                    f'<span class="badge">{tech}</span>', unsafe_allow_html=True)

            st.markdown("### 📊 Performance Metrics")
            for metric_name, metric_value in project['metrics'].items():
                st.markdown(f"**{metric_name}:** `{metric_value}`")

        st.markdown("---")

    # Project Statistics
    st.markdown("## 📊 Project Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Projects", "50+", "Across All Domains")

    with col2:
        st.metric("Featured Projects", len(GITHUB_REPOS), "Highlighted Here")

    with col3:
        active_count = sum(1 for p in GITHUB_REPOS.values()
                           if p['status'] == "Active")
        st.metric("Active Projects", active_count, "Ongoing Development")

    with col4:
        tech_count = len(
            set([tech for proj in GITHUB_REPOS.values() for tech in proj['tech_stack']]))
        st.metric("Technologies", "35+", "Diverse Stack")

    st.markdown("---")

    # Technology Distribution Chart
    st.markdown("## 📈 Technology Distribution")

    tech_counter = {}
    for project in GITHUB_REPOS.values():
        for tech in project['tech_stack']:
            tech_counter[tech] = tech_counter.get(tech, 0) + 1

    sorted_tech = sorted(tech_counter.items(),
                         key=lambda x: x[1], reverse=True)

    fig = go.Figure(data=[
        go.Bar(
            x=[v for k, v in sorted_tech],
            y=[k for k, v in sorted_tech],
            orientation='h',
            marker=dict(
                color=[v for k, v in sorted_tech],
                colorscale='Blues',
                showscale=False
            ),
            text=[v for k, v in sorted_tech],
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>Projects: %{x}<extra></extra>'
        )
    ])

    fig.update_layout(
        title="Technologies Used Across Projects",
        xaxis_title="Number of Projects",
        yaxis_title="Technology",
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#cbd5e1', family='Inter'),
        showlegend=False,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    st.plotly_chart(fig, use_container_width=True,
                    key="tech_distribution_chart")

# ==================== SKILLS PAGE ====================
elif st.session_state.page == "Skills":

    st.markdown("# Technical Skills")

    st.markdown("""
    Comprehensive overview of my technical capabilities, developed through academic coursework, personal 
    projects, professional certifications, and continuous self-learning. Each skill area represents hands-on 
    experience and practical application.
    """)

    st.markdown("---")

    # Skills Overview with Icons
    for skill_category, details in SKILLS.items():
        st.markdown(f"## {details['icon']} {skill_category}")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(
                f"**Proficiency Level:** {details['level']} ({details['proficiency']}%)")
            st.markdown(f"*{details['description']}*")

            st.markdown("**Technologies & Tools:**")
            skills_badges = " ".join(
                [f'<span class="badge">{skill}</span>' for skill in details['skills']])
            st.markdown(skills_badges, unsafe_allow_html=True)

        with col2:
            # Proficiency gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=details['proficiency'],
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Proficiency", 'font': {
                    'color': '#cbd5e1', 'size': 14}},
                gauge={
                    'axis': {'range': [0, 100], 'tickcolor': '#cbd5e1'},
                    'bar': {'color': "#3b82f6"},
                    'bgcolor': "rgba(0,0,0,0)",
                    'borderwidth': 2,
                    'bordercolor': "#475569",
                    'steps': [
                        {'range': [0, 50],
                            'color': 'rgba(59, 130, 246, 0.15)'},
                        {'range': [50, 75],
                            'color': 'rgba(59, 130, 246, 0.25)'},
                        {'range': [75, 100],
                            'color': 'rgba(59, 130, 246, 0.35)'}
                    ],
                }
            ))

            fig.update_layout(
                height=200,
                margin=dict(l=20, r=20, t=40, b=20),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1', family='Inter', size=12)
            )

            st.plotly_chart(fig, use_container_width=True,
                            key=f"skill_gauge_{skill_category}")

        st.markdown("---")

    # Overall Skills Radar Chart
    st.markdown("## 📊 Skills Proficiency Overview")

    categories = list(SKILLS.keys())
    values = [SKILLS[cat]['proficiency'] for cat in categories]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Proficiency',
        fillcolor='rgba(59, 130, 246, 0.25)',
        line=dict(color='#3b82f6', width=3)
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='#475569',
                tickfont=dict(color='#cbd5e1', size=10)
            ),
            angularaxis=dict(
                gridcolor='#475569',
                tickfont=dict(color='#cbd5e1', size=11)
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=False,
        height=600,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#cbd5e1', family='Inter')
    )

    st.plotly_chart(fig, use_container_width=True, key="skills_radar_chart")

    st.markdown("---")

    # Professional Competencies
    st.markdown("## 🤝 Professional Competencies")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Technical Competencies
        
        **Problem Solving**
        - Analytical thinking and systematic approach
        - Breaking down complex challenges
        - Creative solution design
        
        **Quick Learning**
        - Rapidly acquire new technologies
        - Adapt to changing requirements
        - Self-directed learning
        
        **Research Skills**
        - Reading and implementing papers
        - Understanding cutting-edge techniques
        - Experimental validation
        
        **Code Quality**
        - Clean, maintainable code
        - Comprehensive documentation
        - Best practices adherence
        
        **Testing & Debugging**
        - Systematic issue identification
        - Unit testing and validation
        - Performance optimization
        """)

    with col2:
        st.markdown("""
        ### Collaboration & Communication
        
        **Team Collaboration**
        - Group project experience
        - Coding community engagement
        - Knowledge sharing
        
        **Technical Communication**
        - Explaining complex concepts clearly
        - Documentation and presentations
        - Code reviews and feedback
        
        **Adaptability**
        - Learning new tools quickly
        - Flexible to different methodologies
        - Open to feedback
        
        **Time Management**
        - Balancing multiple projects
        - Meeting deadlines consistently
        - Prioritizing effectively
        
        **Self-Motivation**
        - Proactive learning
        - Independent project completion
        - Continuous improvement mindset
        """)

    st.markdown("---")

    # Learning Resources
    st.markdown("## 📚 Continuous Learning Ecosystem")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### Online Platforms
        
        - **Coursera** - Specializations
        - **DataCamp** - Data Science
        - **Kaggle** - Competitions & Learn
        - **YouTube** - Technical Tutorials
        - **Fast.ai** - Practical Deep Learning
        - **QuantInsti** - Algorithmic Trading
        - **Udacity** - Nanodegrees
        - **edX** - University Courses
        """)

    with col2:
        st.markdown("""
        ### Reading & Research
        
        - **arXiv** - Research Papers
        - **Medium** - Technical Blogs
        - **Towards Data Science** - Tutorials
        - **Official Documentation**
        - **ML Conference Papers**
        - **Tech Company Blogs**
        - **Quantitative Finance Journals**
        - **GitHub Trending**
        """)

    with col3:
        st.markdown("""
        ### Community Engagement
        
        - **Stack Overflow** - Q&A
        - **Reddit** - r/MachineLearning
        - **Discord** - ML Communities
        - **LinkedIn** - Professional Groups
        - **GitHub** - Discussions
        - **Kaggle** - Competitions
        - **Twitter** - ML Researchers
        - **Local Meetups**
        """)

# ==================== EDUCATION PAGE ====================
elif st.session_state.page == "Education":

    st.markdown("# Education & Academic Background")

    st.markdown("""
    My academic journey in AI/ML, combining rigorous coursework with hands-on project experience and 
    continuous skill development through certifications and self-directed learning.
    """)

    st.markdown("---")

    # Main Education
    st.markdown(f"## 🎓 {EDUCATION['degree']}")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"**Institution:** {EDUCATION['institution']}")
        st.markdown(f"**Duration:** {EDUCATION['duration']}")
        st.markdown(f"**Current Status:** {EDUCATION['status']}")
        st.markdown(f"**Academic Performance:** {EDUCATION['gpa']}")

        st.markdown("### 📚 Relevant Coursework")

        col_a, col_b = st.columns(2)

        mid_point = len(EDUCATION['coursework']) // 2

        with col_a:
            for course in EDUCATION['coursework'][:mid_point]:
                st.markdown(f"- {course}")

        with col_b:
            for course in EDUCATION['coursework'][mid_point:]:
                st.markdown(f"- {course}")

    with col2:
        st.markdown("""
        <div class='info-card'>
            <h4 style='color: var(--text-primary); margin-bottom: 1rem; font-size: 1.125rem !important;'>🎯 Academic Highlights</h4>
            <p style='color: var(--text-secondary); font-size: 0.9rem; line-height: 1.8;'>
                ✓ Strong AI/ML foundation<br>
                ✓ 50+ projects completed<br>
                ✓ Active in coding communities<br>
                ✓ Consistent academic excellence<br>
                ✓ 3 professional certifications<br>
                ✓ Research paper implementations
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Academic Achievements
    st.markdown("## 🏆 Academic Achievements")

    for achievement in EDUCATION['achievements']:
        st.markdown(f"- {achievement}")

    st.markdown("---")

    # Academic Projects
    st.markdown("## 🔬 Major Academic Projects")

    academic_projects = [
        {
            "title": "AI-Powered Trading Bot",
            "course": "Financial AI & Machine Learning Lab",
            "description": "Ensemble ML-based algorithmic trading system with real-time market signals",
            "tech": "Python, Scikit-learn, yfinance, TA-Lib, Streamlit",
            "outcome": "72% validation accuracy, comprehensive backtesting framework"
        },
        {
            "title": "Medical Diagnosis System",
            "course": "Healthcare AI Applications",
            "description": "ML-powered symptom-based disease prediction with NLP interface",
            "tech": "TensorFlow, NLP, Ensemble Methods",
            "outcome": "87% prediction accuracy across 100+ diseases"
        },
        {
            "title": "Deep Learning Image Classifier",
            "course": "Computer Vision & Deep Learning",
            "description": "CNN-based image classification with transfer learning",
            "tech": "PyTorch, ResNet50, OpenCV, Data Augmentation",
            "outcome": "89% validation accuracy on custom dataset"
        },
        {
            "title": "NLP Sentiment Analyzer",
            "course": "Natural Language Processing",
            "description": "Transformer-based sentiment classification system",
            "tech": "BERT, PyTorch, NLTK, Web Scraping",
            "outcome": "91% test accuracy, real-time inference"
        }
    ]

    for project in academic_projects:
        with st.expander(f"**{project['title']}** - {project['course']}", expanded=False):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Technologies:** `{project['tech']}`")
            st.markdown(f"**Outcome:** {project['outcome']}")

    st.markdown("---")

    # Skills Developed
    st.markdown("## 💡 Skills Developed Through Education")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### Technical Foundation
        
        - Algorithm Design & Analysis
        - Data Structures
        - Software Engineering
        - Database Management
        - Operating Systems
        - Computer Networks
        - Object-Oriented Programming
        - System Design
        """)

    with col2:
        st.markdown("""
        ### ML/AI Expertise
        
        - Machine Learning Theory
        - Deep Learning Architectures
        - Computer Vision Techniques
        - Natural Language Processing
        - Model Optimization
        - Statistical Methods
        - Feature Engineering
        - Model Evaluation
        """)

    with col3:
        st.markdown("""
        ### Professional Skills
        
        - Research Methodology
        - Technical Writing
        - Project Management
        - Team Collaboration
        - Presentation Skills
        - Critical Thinking
        - Problem Solving
        - Communication
        """)

# ==================== CERTIFICATIONS PAGE ====================
elif st.session_state.page == "Certifications":

    st.markdown("# Certifications & Professional Development")

    st.markdown("""
    Beyond academic education, I've pursued professional certifications to deepen expertise and stay 
    current with industry practices, emerging technologies, and best practices in AI/ML.
    """)

    st.markdown("---")

    # Certification Stats
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Certifications", len(CERTIFICATIONS), "Professional")
    with col2:
        st.metric("Completed", len(CERTIFICATIONS), "Verified")
    with col3:
        st.metric("Platforms", "2", "Coursera, DataCamp")
    with col4:
        st.metric("Learning Hours", "500+", "Documented")

    st.markdown("---")

    # Display Certifications
    st.markdown("## ✅ Professional Certifications")

    for cert in CERTIFICATIONS:
        st.markdown(f"### 📜 {cert['name']}")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"**Provider:** {cert['provider']}")
            st.markdown(f"**Instructor:** {cert['instructor']}")
            st.markdown(f"**Completion Date:** {cert['date']}")

            st.markdown("**Skills Covered:**")
            skills_badges = " ".join(
                [f'<span class="badge">{skill}</span>' for skill in cert['skills']])
            st.markdown(skills_badges, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class='info-card' style='background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(6, 182, 212, 0.1)); border-color: rgba(16, 185, 129, 0.3);'>
                <p style='color: var(--success); font-weight: 600; margin-bottom: 0.5rem; font-size: 1rem !important;'>✓ {cert['status']}</p>
                <p style='color: var(--text-secondary); font-size: 0.875rem !important;'>{cert['credential']}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

    # Learning Platforms
    st.markdown("## 📚 Continuous Learning Ecosystem")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### Online Platforms
        
        **Primary Learning:**
        - Coursera (Stanford, deeplearning.ai)
        - DataCamp (Interactive courses)
        - Kaggle Learn (Hands-on tutorials)
        - YouTube (Technical content)
        
        **Supplementary:**
        - Fast.ai (Practical deep learning)
        - Google Codelabs (TensorFlow)
        - Udacity (Nanodegrees)
        - edX (University courses)
        - QuantInsti (Algo trading)
        """)

    with col2:
        st.markdown("""
        ### Reading & Research
        
        **Technical Resources:**
        - arXiv (Latest ML research)
        - Medium/Towards Data Science
        - Official documentation
        - Technical blogs
        
        **Industry Insights:**
        - ML conference papers
        - GitHub trending repos
        - Tech company blogs
        - AI research lab publications
        - Academic journals
        """)

    with col3:
        st.markdown("""
        ### Community Engagement
        
        **Discussion Platforms:**
        - Stack Overflow (Q&A)
        - Reddit (r/MachineLearning)
        - Discord communities
        - LinkedIn groups
        
        **Collaboration:**
        - GitHub discussions
        - Kaggle competitions
        - Open source contributions
        - Peer study groups
        - Local meetups
        """)

    st.markdown("---")

    # Learning Philosophy
    st.markdown("""
    ## 🎓 Learning Philosophy
    
    My approach to continuous professional development is based on four key principles:
    
    ### 1. Structured Learning
    Following well-designed courses from reputable institutions ensures comprehensive topic coverage and 
    builds a strong theoretical foundation. Verified certifications demonstrate commitment and expertise.
    
    ### 2. Practical Application
    Every certification is immediately applied to personal projects, reinforcing learning through hands-on 
    implementation and building a portfolio of working applications.
    
    ### 3. Community Learning
    Active participation in ML communities provides diverse perspectives, keeps me updated with industry 
    trends, and allows knowledge sharing with peers.
    
    ### 4. Research-Oriented
    Regular reading of research papers helps understand cutting-edge developments, inspires new project 
    ideas, and maintains awareness of the field's evolution.
    
    This philosophy has enabled continuous growth from foundational knowledge to advanced expertise, 
    preparing me for professional contributions and collaborative projects.
    """)

# ==================== CONTACT PAGE ====================
elif st.session_state.page == "Contact":

    st.markdown("# Contact & Connect")

    st.markdown("""
    I'm actively seeking **AI/ML internship opportunities** and always open to connecting with fellow 
    developers, researchers, and professionals. Let's collaborate and build innovative AI solutions together!
    """)

    st.markdown("---")

    # Contact Cards
    st.markdown("## 📬 Get In Touch")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='info-card' style='text-align: center; padding: 2rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>📧</div>
            <h3 style='color: var(--text-primary); margin-bottom: 0.75rem; font-size: 1.25rem !important;'>Email</h3>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem; word-break: break-all;'>
                dheerajmuley006@gmail.com
            </p>
            <p style='color: var(--text-muted); font-size: 0.8rem;'>Response within 24 hours</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📧 Send Email", key="email_btn", use_container_width=True):
            st.markdown(
                "[Open Email Client](mailto:dheerajmuley006@gmail.com)")

    with col2:
        st.markdown("""
        <div class='info-card' style='text-align: center; padding: 2rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>💼</div>
            <h3 style='color: var(--text-primary); margin-bottom: 0.75rem; font-size: 1.25rem !important;'>LinkedIn</h3>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
                linkedin.com/in/dheeraj-muley
            </p>
            <p style='color: var(--text-muted); font-size: 0.8rem;'>Professional networking</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔗 Connect on LinkedIn", key="linkedin_btn", use_container_width=True):
            st.markdown(
                "[View Profile](https://linkedin.com/in/dheeraj-muley)")

    with col3:
        st.markdown("""
        <div class='info-card' style='text-align: center; padding: 2rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>💻</div>
            <h3 style='color: var(--text-primary); margin-bottom: 0.75rem; font-size: 1.25rem !important;'>GitHub</h3>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
                github.com/dheeraj815
            </p>
            <p style='color: var(--text-muted); font-size: 0.8rem;'>Code portfolio & projects</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("👨‍💻 View GitHub", key="github_btn", use_container_width=True):
            st.markdown("[Visit Repository](https://github.com/dheeraj815)")

    st.markdown("---")

    # Internship Opportunities
    st.markdown("## 🎯 Internship Opportunities")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### What I'm Seeking
        
        **Position Types:**
        - AI/ML Engineering Intern
        - Quantitative Research Intern
        - Data Science Intern
        - Financial ML Intern
        - Applied AI Research Intern
        - MLOps Engineering Intern
        
        **Preferences:**
        - **Duration:** 2-6 months (Flexible)
        - **Work Mode:** Remote, Hybrid, or On-site
        - **Start Date:** Immediate to within 2-3 months
        - **Commitment:** Full-time during internship
        - **Location:** India (Open to relocation)
        
        **Ideal Environment:**
        - Work on real-world ML challenges
        - Learn from experienced professionals
        - Contribute to production systems
        - Exposure to industry best practices
        - Collaborative and innovative team
        - Mentorship and growth opportunities
        """)

    with col2:
        st.markdown("""
        ### What I Bring
        
        **Technical Capabilities:**
        - Strong Python & ML fundamentals
        - 50+ hands-on project portfolio
        - Financial AI & trading experience
        - TensorFlow, PyTorch, Scikit-learn
        - Web development & deployment
        - Clean code & documentation
        
        **Professional Qualities:**
        - Excellent problem-solving skills
        - Strong communication abilities
        - Collaborative team player
        - Self-motivated & proactive
        - Quick learner & adaptable
        - Detail-oriented approach
        
        **Proven Track Record:**
        - Diverse project portfolio
        - Academic excellence
        - Professional certifications
        - Active community engagement
        - Continuous learning mindset
        """)

    st.markdown("---")

    # Contact Guidelines
    st.markdown("## 💬 Contact Guidelines")

    st.markdown("""
    ### For Internship Opportunities
    
    **Best Method:** Email (dheerajmuley006@gmail.com)
    
    **Please Include:**
    - Company/Organization name and overview
    - Position details and key responsibilities
    - Duration and expected timeline
    - Technical requirements and tech stack
    - Team structure and mentorship approach
    - Any specific projects or focus areas
    
    **What You'll Receive:**
    - Response within 24 hours
    - Updated resume and portfolio
    - Relevant project links and code samples
    - Availability and scheduling flexibility
    - References if requested
    
    ### For Collaboration & Networking
    
    **LinkedIn:** Best for professional networking and industry connections
    
    **GitHub:** Technical discussions, code reviews, and project collaborations
    
    **Email:** General inquiries, resource sharing, or detailed discussions
    
    ### Response Times
    
    - **Email:** Within 24 hours (typically same day)
    - **LinkedIn:** Within 48 hours
    - **GitHub Issues:** Same day for technical matters
    
    **Time Zone:** IST (GMT+5:30) - Available throughout the day
    """)

    st.markdown("---")

    # Additional Information
    st.markdown("## ℹ️ Additional Information")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Professional Details
        
        **Location:** India
        
        **Time Zone:** IST (GMT+5:30)
        
        **Languages:**
        - English (Fluent)
        - Hindi (Native)
        
        **Work Authorization:** Available for work in India
        
        **Willing to Relocate:** Yes, for the right opportunity
        
        **Notice Period:** Immediate availability for internships
        
        **Availability:** Full-time commitment during internship period
        """)

    with col2:
        st.markdown("""
        ### What to Expect
        
        **Communication Style:**
        - Clear and professional
        - Responsive and proactive
        - Technical yet accessible
        - Collaborative approach
        
        **Work Ethic:**
        - Punctual and reliable
        - Detail-oriented
        - Self-motivated
        - Continuous learner
        - Strong team player
        
        **Values:**
        - Quality over quantity
        - Continuous improvement
        - Knowledge sharing
        - Ethical AI practices
        """)

    st.markdown("---")

    # Call to Action
    st.success("""
    💡 **Thank you for visiting my portfolio!** I'm excited about opportunities to contribute to innovative 
    AI/ML projects and learn from experienced professionals. Whether it's an internship opportunity, 
    collaboration proposal, or technical discussion, I'd love to hear from you!
    """)

    # Quick Actions
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 Request Resume", use_container_width=True):
            st.info(
                "Please email me at dheerajmuley006@gmail.com to request my latest resume and additional materials.")

    with col2:
        if st.button("💼 View All Projects", use_container_width=True):
            st.session_state.page = "Projects"
            st.rerun()

    with col3:
        if st.button("🎓 View Credentials", use_container_width=True):
            st.session_state.page = "Certifications"
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2.5rem 0; color: var(--text-muted);'>
    <p style='font-size: 0.9rem; margin-bottom: 0.75rem; color: var(--text-secondary);'>
        Built with <strong style='color: var(--primary);'>Streamlit</strong> and <strong style='color: var(--primary);'>Python</strong>
    </p>
    <p style='font-size: 0.875rem; margin-bottom: 1rem;'>
        © 2026 Dheeraj Muley • Last Updated: February 2026
    </p>
    <p style='font-size: 0.875rem;'>
        <a href='https://github.com/dheeraj815' target='_blank'>GitHub</a> • 
        <a href='https://linkedin.com/in/dheeraj-muley' target='_blank'>LinkedIn</a> • 
        <a href='mailto:dheerajmuley006@gmail.com'>Email</a>
    </p>
</div>
""", unsafe_allow_html=True)
