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

# Custom CSS - Ultra Professional Design with Fixed Gradients
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');
    
    :root {
        --primary: #2563eb;
        --secondary: #7c3aed;
        --accent: #06b6d4;
        --success: #10b981;
        --warning: #f59e0b;
        --dark-bg: #0a0f1e;
        --card-bg: #111827;
        --card-hover: #1f2937;
        --text-primary: #f9fafb;
        --text-secondary: #d1d5db;
        --text-muted: #9ca3af;
        --border: rgba(37, 99, 235, 0.2);
    }
    
    * {
        font-family: 'Sora', sans-serif;
        letter-spacing: -0.01em;
    }
    
    /* Main Background with Animated Gradient */
    .main {
        background: linear-gradient(135deg, #0a0f1e 0%, #1a1f35 25%, #0f1629 50%, #1a1f35 75%, #0a0f1e 100%);
        background-size: 400% 400%;
        animation: gradientFlow 15s ease infinite;
        position: relative;
        overflow-x: hidden;
    }
    
    @keyframes gradientFlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 50%, rgba(37, 99, 235, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 50%, rgba(124, 58, 237, 0.1) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    
    .block-container {
        padding: 3rem 2rem;
        max-width: 1400px;
        position: relative;
        z-index: 1;
    }
    
    /* Fix for text truncation in markdown */
    .stMarkdown {
        overflow: visible !important;
        width: 100% !important;
    }
    
    .stMarkdown > div {
        overflow: visible !important;
        width: 100% !important;
    }
    
    [data-testid="stMarkdownContainer"] {
        overflow: visible !important;
        width: 100% !important;
    }
    
    /* Typography System */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Sora', sans-serif !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        line-height: 1.2 !important;
        overflow: visible !important;
        display: block !important;
        width: 100% !important;
    }
    
    /* FIXED H1 - with fallback color and proper display */
    h1 {
        font-size: 3.75rem !important;
        font-weight: 800 !important;
        color: #60a5fa !important;  /* Fallback color - bright blue */
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem !important;
        animation: fadeInUp 0.8s ease-out;
        display: block !important;
        width: 100% !important;
        overflow: visible !important;
        white-space: normal !important;
        word-wrap: break-word !important;
    }
    
    /* Fallback for browsers that don't support background-clip: text */
    @supports not (background-clip: text) or not (-webkit-background-clip: text) {
        h1 {
            color: #60a5fa !important;
            background: none !important;
            -webkit-text-fill-color: #60a5fa !important;
        }
    }
    
    h2 {
        font-size: 2.25rem !important;
        margin: 3.5rem 0 1.5rem 0 !important;
        padding-bottom: 1rem !important;
        border-bottom: 2px solid var(--primary);
        position: relative;
        animation: fadeInUp 0.6s ease-out;
    }
    
    h2::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 100px;
        height: 2px;
        background: linear-gradient(90deg, var(--secondary), var(--accent));
        box-shadow: 0 0 10px var(--secondary);
    }
    
    h3 {
        font-size: 1.5rem !important;
        color: var(--accent) !important;
        margin: 2rem 0 1rem 0 !important;
        font-weight: 600 !important;
    }
    
    p, li, span {
        color: var(--text-secondary) !important;
        font-size: 1.0625rem !important;
        line-height: 1.75 !important;
        font-weight: 400 !important;
    }
    
    strong {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    
    code {
        background: rgba(37, 99, 235, 0.15) !important;
        color: #93c5fd !important;
        padding: 0.25rem 0.5rem !important;
        border-radius: 0.375rem !important;
        font-family: 'Fira Code', monospace !important;
        font-size: 0.9375rem !important;
        border: 1px solid rgba(37, 99, 235, 0.3);
    }
    
    /* Enhanced Lists */
    ul, ol {
        margin: 1.25rem 0 1.75rem 1.5rem !important;
        padding-left: 0.5rem !important;
    }
    
    li {
        margin-bottom: 0.875rem !important;
        padding-left: 0.75rem !important;
        position: relative;
    }
    
    ul li::before {
        content: '▹';
        position: absolute;
        left: -1rem;
        color: var(--primary);
        font-weight: bold;
        font-size: 1.25rem;
    }
    
    /* Professional Card System */
    .stAlert {
        background: linear-gradient(135deg, var(--card-bg) 0%, rgba(31, 41, 55, 0.95) 100%) !important;
        border: 1px solid var(--border) !important;
        border-left: 3px solid var(--primary) !important;
        border-radius: 0.75rem !important;
        padding: 1.75rem !important;
        margin: 1.5rem 0 !important;
        backdrop-filter: blur(12px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeIn 0.5s ease-out;
    }
    
    .stAlert:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(37, 99, 235, 0.2);
        border-left-color: var(--accent);
    }
    
    /* Premium Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 0.5rem !important;
        padding: 0.875rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3) !important;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4) !important;
    }
    
    /* Metric Cards with Glassmorphism - FIXED with fallback */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8), rgba(31, 41, 55, 0.6));
        backdrop-filter: blur(10px);
        border: 1px solid var(--border);
        border-radius: 0.75rem;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.2);
        border-color: var(--primary);
    }
    
    /* FIXED Metric Value - with fallback */
    [data-testid="stMetricValue"] {
        font-size: 2.75rem !important;
        font-weight: 800 !important;
        color: #60a5fa !important;  /* Fallback color */
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    @supports not (background-clip: text) or not (-webkit-background-clip: text) {
        [data-testid="stMetricValue"] {
            color: #60a5fa !important;
            background: none !important;
            -webkit-text-fill-color: #60a5fa !important;
        }
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-size: 0.9375rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    [data-testid="stMetricDelta"] {
        color: var(--success) !important;
        font-size: 0.875rem !important;
    }
    
    /* Elegant Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--dark-bg) 0%, #141b2d 100%) !important;
        border-right: 1px solid var(--border) !important;
        box-shadow: 4px 0 12px rgba(0, 0, 0, 0.3);
    }
    
    [data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }
    
    .stRadio > label {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        font-size: 1.125rem !important;
        margin-bottom: 1.25rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stRadio > div {
        gap: 0.625rem !important;
    }
    
    .stRadio > div > label {
        background: rgba(17, 24, 39, 0.6) !important;
        padding: 0.875rem 1.5rem !important;
        border-radius: 0.5rem !important;
        border: 1px solid var(--border) !important;
        color: var(--text-secondary) !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-weight: 500 !important;
        position: relative;
        overflow: hidden;
    }
    
    .stRadio > div > label::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        width: 3px;
        background: var(--primary);
        transform: scaleY(0);
        transition: transform 0.3s ease;
    }
    
    .stRadio > div > label:hover {
        background: rgba(37, 99, 235, 0.15) !important;
        border-color: var(--primary) !important;
        transform: translateX(8px);
        color: var(--text-primary) !important;
    }
    
    .stRadio > div > label:hover::before {
        transform: scaleY(1);
    }
    
    .stRadio > div > label[aria-checked="true"] {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
        border-color: var(--primary) !important;
        color: white !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    
    .stRadio > div > label[aria-checked="true"]::before {
        transform: scaleY(1);
        background: white;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, var(--card-bg), rgba(31, 41, 55, 0.9)) !important;
        border-radius: 0.75rem !important;
        border: 1px solid var(--border) !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        padding: 1.25rem 1.5rem !important;
        transition: all 0.3s ease !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(37, 99, 235, 0.15) !important;
        border-color: var(--primary) !important;
        transform: translateX(4px);
    }
    
    .streamlit-expanderContent {
        background: rgba(17, 24, 39, 0.5);
        border: 1px solid var(--border);
        border-top: none;
        border-radius: 0 0 0.75rem 0.75rem;
        padding: 1.5rem;
    }
    
    /* Enhanced Links */
    a {
        color: var(--accent) !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        position: relative;
    }
    
    a::after {
        content: '';
        position: absolute;
        width: 0;
        height: 2px;
        bottom: -2px;
        left: 0;
        background: var(--accent);
        transition: width 0.3s ease;
    }
    
    a:hover {
        color: var(--primary) !important;
    }
    
    a:hover::after {
        width: 100%;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.75rem;
        background: rgba(17, 24, 39, 0.6);
        border-radius: 0.75rem;
        padding: 0.625rem;
        border: 1px solid var(--border);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 0.5rem !important;
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
        padding: 0.875rem 1.75rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(37, 99, 235, 0.15) !important;
        color: var(--text-primary) !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    
    /* Badge System */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.4rem 0.875rem;
        background: rgba(37, 99, 235, 0.15);
        border: 1px solid rgba(37, 99, 235, 0.3);
        border-radius: 0.5rem;
        color: #93c5fd !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        margin: 0.25rem;
        transition: all 0.3s ease;
        backdrop-filter: blur(8px);
    }
    
    .badge:hover {
        background: rgba(37, 99, 235, 0.25);
        border-color: var(--primary);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(37, 99, 235, 0.2);
    }
    
    .badge-success {
        background: rgba(16, 185, 129, 0.15);
        border-color: rgba(16, 185, 129, 0.3);
        color: #86efac !important;
    }
    
    .badge-success:hover {
        background: rgba(16, 185, 129, 0.25);
        border-color: var(--success);
    }
    
    .badge-warning {
        background: rgba(245, 158, 11, 0.15);
        border-color: rgba(245, 158, 11, 0.3);
        color: #fcd34d !important;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
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
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.6;
        }
    }
    
    /* Status Indicator */
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
        width: 12px;
        height: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark-bg);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--primary), var(--secondary));
        border-radius: 6px;
        border: 2px solid var(--dark-bg);
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
    
    /* Plotly Chart Styling */
    .js-plotly-plot {
        border-radius: 0.75rem;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* Selection Styling */
    ::selection {
        background: rgba(37, 99, 235, 0.3);
        color: var(--text-primary);
    }
    
    /* Focus Styling */
    *:focus {
        outline: 2px solid var(--primary);
        outline-offset: 2px;
    }
</style>
""", unsafe_allow_html=True)

# GitHub Repository Data
GITHUB_REPOS = {
    "AI Medical Diagnosis & Health Assistant": {
        "url": "https://github.com/dheeraj815/AI-Medical-Diagnosis-Health-Assitant",
        "description": "Intelligent medical diagnosis system leveraging machine learning to analyze symptoms and provide evidence-based health recommendations with natural language interface.",
        "tech_stack": ["Python", "TensorFlow", "NLP", "Streamlit", "Medical AI"],
        "category": "Healthcare AI",
        "highlights": [
            "Advanced symptom-based disease prediction using ensemble ML models",
            "Natural language processing for medical query understanding and context",
            "Interactive conversational AI interface for health consultation",
            "Integration with comprehensive medical knowledge databases",
            "Real-time diagnosis confidence scoring and explanation system"
        ],
        "status": "Active",
        "impact": "Potential to assist in preliminary medical screening",
        "metrics": {"Accuracy": "87%", "Response Time": "<2s"}
    },
    "Rock Paper Scissors AI": {
        "url": "https://github.com/dheeraj815/RPS-AI",
        "description": "Intelligent game AI that learns and adapts to player patterns using machine learning for strategic prediction in Rock-Paper-Scissors gameplay.",
        "tech_stack": ["Python", "Scikit-learn", "Pattern Recognition", "Markov Chains"],
        "category": "Game AI",
        "highlights": [
            "Advanced pattern recognition algorithm for move prediction",
            "Reinforcement learning implementation with Q-learning",
            "Statistical analysis engine for gameplay pattern detection",
            "Real-time prediction accuracy tracking and visualization",
            "Adaptive strategy adjustment based on player behavior"
        ],
        "status": "Completed",
        "impact": "Demonstrates practical application of ML in game theory",
        "metrics": {"Win Rate": "65%", "Adaptation Speed": "10 moves"}
    },
    "Movie Recommender System": {
        "url": "https://github.com/dheeraj815/Movie-RecommenderNLP",
        "description": "Sophisticated NLP-based recommendation engine using content-based filtering and semantic similarity for personalized movie suggestions.",
        "tech_stack": ["Python", "NLP", "NLTK", "Cosine Similarity", "TF-IDF"],
        "category": "Recommendation Systems",
        "highlights": [
            "Content-based filtering using movie plots, genres, and metadata",
            "TF-IDF vectorization for advanced text similarity computation",
            "Cosine similarity algorithm for precise recommendation matching",
            "Interactive web interface with search and filter capabilities",
            "Genre-aware recommendation with user preference learning"
        ],
        "status": "Completed",
        "impact": "Personalized content discovery system",
        "metrics": {"Precision": "82%", "Dataset": "5000+ movies"}
    },
    "House Price Predictor": {
        "url": "https://github.com/dheeraj815/House-Price-Predictor",
        "description": "Comprehensive real estate price prediction system using multiple regression algorithms and extensive feature engineering for accurate market analysis.",
        "tech_stack": ["Python", "Pandas", "Scikit-learn", "Regression", "Feature Engineering"],
        "category": "Predictive Analytics",
        "highlights": [
            "Multi-algorithm comparison (Linear, Ridge, Lasso, Ensemble methods)",
            "Advanced feature engineering with domain-specific insights",
            "Robust data preprocessing and outlier detection pipeline",
            "Cross-validation for model reliability assessment",
            "Interactive prediction interface with confidence intervals"
        ],
        "status": "Completed",
        "impact": "Real estate market analysis tool",
        "metrics": {"RMSE": "3.2%", "R² Score": "0.89"}
    },
    "Portfolio Website": {
        "url": "https://github.com/dheeraj815/Portfolio",
        "description": "Professional portfolio platform showcasing AI/ML projects with interactive visualizations and modern design principles.",
        "tech_stack": ["Streamlit", "Python", "Plotly", "CSS", "Web Design"],
        "category": "Web Development",
        "highlights": [
            "Responsive design with custom CSS and modern aesthetics",
            "Interactive project showcase with filtering and search",
            "Dynamic data visualizations using Plotly",
            "Professional UI/UX following industry best practices",
            "Optimized performance and cross-browser compatibility"
        ],
        "status": "Active",
        "impact": "Professional online presence and project showcase",
        "metrics": {"Load Time": "<1s", "Responsive": "100%"}
    },
    "GitHub Profile": {
        "url": "https://github.com/dheeraj815/dheeraj815",
        "description": "Automated GitHub profile README featuring dynamic statistics, activity tracking, and professional presentation.",
        "tech_stack": ["Markdown", "GitHub Actions", "APIs", "Automation"],
        "category": "Developer Tools",
        "highlights": [
            "Automated GitHub statistics generation and updates",
            "Dynamic skill badges and technology showcase",
            "Project highlights with direct repository links",
            "Professional profile presentation and branding",
            "Continuous integration for real-time updates"
        ],
        "status": "Active",
        "impact": "Enhanced GitHub presence and visibility",
        "metrics": {"Update Frequency": "Daily", "API Calls": "Optimized"}
    }
}

# Skills Data with Proficiency Levels
SKILLS = {
    "Machine Learning & AI": {
        "skills": ["TensorFlow", "PyTorch", "Scikit-learn", "Keras", "XGBoost", "Model Deployment"],
        "proficiency": 80,
        "level": "Intermediate-Advanced",
        "description": "Strong foundation in supervised/unsupervised learning, neural networks, and model optimization with production deployment experience"
    },
    "Deep Learning": {
        "skills": ["CNN", "RNN", "LSTM", "Transfer Learning", "Computer Vision", "NLP Models"],
        "proficiency": 75,
        "level": "Intermediate",
        "description": "Hands-on experience with various deep learning architectures for image and text processing tasks"
    },
    "Programming Languages": {
        "skills": ["Python (Advanced)", "SQL", "JavaScript", "C++", "HTML/CSS"],
        "proficiency": 90,
        "level": "Advanced",
        "description": "Expert-level Python programming for ML/AI development and data processing with full-stack capabilities"
    },
    "Data Science & Analytics": {
        "skills": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Data Visualization"],
        "proficiency": 85,
        "level": "Advanced",
        "description": "Proficient in data manipulation, statistical analysis, and creating insightful visualizations"
    },
    "Web Development": {
        "skills": ["Streamlit", "Flask", "FastAPI", "React (Basic)", "REST APIs"],
        "proficiency": 75,
        "level": "Intermediate",
        "description": "Full-stack development capabilities with focus on ML model deployment and API development"
    },
    "NLP & Text Processing": {
        "skills": ["NLTK", "spaCy", "TF-IDF", "Sentiment Analysis", "Text Classification"],
        "proficiency": 70,
        "level": "Intermediate",
        "description": "Experience with various NLP tasks including recommendation systems, chatbots, and text analysis"
    },
    "Tools & Platforms": {
        "skills": ["Git/GitHub", "Jupyter", "Google Colab", "VS Code", "Docker"],
        "proficiency": 80,
        "level": "Intermediate-Advanced",
        "description": "Proficient with modern development tools, version control, and containerization"
    },
    "Cloud & Deployment": {
        "skills": ["Streamlit Cloud", "Heroku", "AWS", "Model Serving", "CI/CD"],
        "proficiency": 60,
        "level": "Intermediate",
        "description": "Learning cloud platforms and MLOps best practices for production deployment"
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
        "Active participation in coding communities"
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
    st.markdown("### 🧭 Navigation")

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

    st.markdown(f"""
    <div style='text-align: center; padding: 1.5rem 0;'>
        <h3 style='color: var(--text-primary); margin-bottom: 0.5rem;'>Dheeraj Muley</h3>
        <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
            AI/ML Engineering Student
        </p>
        <p style='color: var(--text-muted); font-size: 0.875rem; line-height: 1.6;'>
            📍 India<br>
            🎓 BTech AIML (3rd Year)<br>
            💼 Seeking Internships
        </p>
        <div style='margin: 1.5rem 0;'>
            <span class='badge badge-success'>
                <span class='status-dot'></span>
                Available for Opportunities
            </span>
        </div>
        <div style='margin-top: 1.5rem;'>
            <a href='https://github.com/dheeraj815' target='_blank' style='margin: 0 0.5rem;'>GitHub</a>
            <a href='https://linkedin.com/in/dheeraj-muley' target='_blank' style='margin: 0 0.5rem;'>LinkedIn</a>
            <a href='mailto:dheerajmuley006@gmail.com' style='margin: 0 0.5rem;'>Email</a>
        </div>
        <p style='color: var(--text-muted); font-size: 0.75rem; margin-top: 1.5rem;'>
            Updated: January 2026
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== HOME PAGE ====================
if st.session_state.page == "Home":

    # Hero Section
    col1, col2 = st.columns([2, 1])

    with col1:
        # Using HTML for better rendering consistency across platforms
        st.markdown("""
        <h1 style='font-size: 3.75rem; font-weight: 800; color: #60a5fa; 
                   margin-bottom: 1rem; display: block; width: 100%; 
                   background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #06b6d4 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                   background-clip: text; overflow: visible;'>
        Dheeraj Muley
        </h1>
        """, unsafe_allow_html=True)

        st.markdown(
            "### AI/ML Engineering Student | Building Intelligent Solutions")

        st.markdown("""
        Passionate **3rd-year BTech AI/ML student** specializing in building practical machine learning 
        applications. I transform complex problems into elegant solutions through artificial intelligence, 
        with a focus on healthcare AI, NLP, and computer vision. **50+ projects completed** across diverse domains.
        """)

        st.info(
            "🟢 **Currently Available** for AI/ML internships and collaborative projects")

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
        <div style='padding: 2rem; background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(124, 58, 237, 0.1)); border-radius: 1rem; border: 1px solid var(--border);'>
            <h4 style='color: var(--text-primary); margin-bottom: 1rem;'>🎯 Quick Stats</h4>
            <div style='line-height: 2;'>
                <strong style='color: var(--accent);'>50+</strong> Projects Completed<br>
                <strong style='color: var(--accent);'>30+</strong> Technologies<br>
                <strong style='color: var(--accent);'>3</strong> Certifications<br>
                <strong style='color: var(--accent);'>1.5</strong> Years Experience
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Detailed Metrics
    st.markdown("## 📊 Portfolio Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Projects Completed", "50+", "Active on GitHub")
    with col2:
        st.metric("Technologies Mastered", "30+", "Growing")
    with col3:
        st.metric("Certifications", "3", "Verified")
    with col4:
        st.metric("Learning Duration", "1.5 Years", "Continuous")

    st.markdown("---")

    # Core Competencies
    st.markdown("## 💡 Core Competencies")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🎯 Technical Expertise
        
        **Machine Learning Development**
        - Building predictive models and classification systems
        - End-to-end ML pipeline development
        - Model optimization and hyperparameter tuning
        
        **Deep Learning**
        - Neural networks for computer vision and NLP
        - Transfer learning and fine-tuning
        - Custom architecture design
        
        **Data Science**
        - Exploratory data analysis and visualization
        - Statistical modeling and hypothesis testing
        - Feature engineering and selection
        """)

    with col2:
        st.markdown("""
        ### 🚀 Domain Specialization
        
        **Healthcare AI**
        - Medical diagnosis and health recommendation systems
        - Clinical decision support tools
        - Healthcare data analysis
        
        **NLP Applications**
        - Chatbots and conversational AI
        - Recommendation engines
        - Text classification and sentiment analysis
        
        **Computer Vision**
        - Image classification and object detection
        - Pattern recognition systems
        - Face recognition applications
        """)

    st.markdown("---")

    # Featured Projects
    st.markdown("## ⭐ Featured Projects")

    featured_projects = ["AI Medical Diagnosis & Health Assistant",
                         "Movie Recommender System", "House Price Predictor"]

    for project_name in featured_projects:
        project = GITHUB_REPOS[project_name]

        with st.expander(f"**{project_name}** - {project['category']}", expanded=False):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**{project['description']}**")

                st.markdown("**Key Highlights:**")
                for highlight in project['highlights'][:3]:
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

    # Current Focus
    st.markdown("## 🔭 Current Focus")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 📚 Learning
        
        - Advanced Deep Learning
        - MLOps & Model Deployment
        - Cloud Platforms (AWS, GCP)
        - Production ML Systems
        - Large Language Models
        """)

    with col2:
        st.markdown("""
        ### 🛠️ Building
        
        - LLM-powered applications
        - Healthcare AI systems
        - Computer vision projects
        - Full-stack ML pipelines
        - Open source contributions
        """)

    with col3:
        st.markdown("""
        ### 🎯 Goals
        
        - Secure AI/ML internship
        - Build production systems
        - Contribute to research
        - Expand technical skills
        - Network with professionals
        """)

# ==================== ABOUT PAGE ====================
elif st.session_state.page == "About":

    st.markdown("# About Me")

    st.markdown("""
    I'm a dedicated AI/ML engineering student with a passion for building intelligent systems that solve 
    real-world problems. My journey combines academic excellence with hands-on project experience.
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
        - Strong programming skills with focus on Python and data science
        - Hands-on experience with modern ML frameworks and tools
        - Project-based learning across multiple AI domains
        
        **Practical Experience**
        - 50+ complete projects across multiple domains
        - Experience with healthcare AI, NLP, and computer vision
        - Model deployment and production considerations
        - Clean code practices and documentation
        
        ## 🚀 My Approach
        
        **Learning by Building**: I believe in practical, hands-on learning. With **50+ projects completed**, 
        each one teaches me something new about AI/ML in real-world applications - from small experiments to 
        production-ready systems.
        
        **Problem-First Mindset**: I start with understanding the problem deeply before jumping into solutions, 
        ensuring my ML models address actual needs.
        
        **Continuous Improvement**: Technology evolves rapidly. I stay updated through research papers, online 
        courses, and active participation in ML communities.
        
        **Quality Focus**: I prioritize code quality, documentation, and best practices in all my projects, 
        making them production-ready and maintainable.
        """)

    with col2:
        st.markdown("""
        ### 🎯 Technical Strengths
        
        **Programming**
        - Python (Advanced)
        - SQL, JavaScript
        - Algorithm Design
        - Problem Solving
        
        **ML/AI**
        - Supervised/Unsupervised Learning
        - Deep Learning (CNN, RNN)
        - NLP & Computer Vision
        - Model Optimization
        
        **Development**
        - Web Applications
        - API Development
        - Model Deployment
        - Version Control
        
        **Tools**
        - TensorFlow, PyTorch
        - Scikit-learn, Pandas
        - Git/GitHub
        - Jupyter, VS Code
        
        ### 🌱 Currently Learning
        
        - MLOps & Production ML
        - Advanced NLP (Transformers)
        - Cloud Platforms (AWS)
        - System Design for ML
        - Large Language Models
        
        ### 🎯 Career Objectives
        
        **Immediate**
        - Secure AI/ML internship
        - Gain industry experience
        
        **Short-term**
        - Build production systems
        - Contribute to open source
        
        **Long-term**
        - ML Engineer role
        - Impactful AI applications
        """)

    st.markdown("---")

    st.markdown("## 🏆 What Sets Me Apart")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🔨 Hands-On Builder
        
        - 50+ complete projects across domains
        - End-to-end implementations
        - Production-ready code
        - Comprehensive documentation
        - Real-world problem solving
        """)

    with col2:
        st.markdown("""
        ### 📚 Self-Directed Learner
        
        - Multiple verified certifications
        - Active in ML communities
        - Regular research paper reading
        - Continuous skill development
        - Experimental mindset
        """)

    with col3:
        st.markdown("""
        ### 🎯 Results-Oriented
        
        - Strong analytical thinking
        - Systematic problem approach
        - Attention to detail
        - Quality-focused delivery
        - Adaptable to challenges
        """)

    st.markdown("---")

    st.markdown("## 💼 Internship Readiness")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### What I'm Seeking
        
        **Position Type:**
        - AI/ML Engineering Intern
        - Data Science Intern
        - ML Research Intern
        - Applied AI Intern
        
        **Duration:** 2-6 months (Flexible)
        
        **Mode:** Remote, Hybrid, or On-site
        
        **Start Date:** Immediate to Flexible
        
        **Availability:** Full-time commitment during internship
        
        **Work Authorization:** Available for work in India
        """)

    with col2:
        st.markdown("""
        ### What I Bring
        
        **Technical Skills:**
        - Strong Python & ML fundamentals
        - Hands-on project experience
        - Quick learner & adaptable
        - Good documentation practices
        - Understanding of ML lifecycle
        
        **Soft Skills:**
        - Excellent problem-solving abilities
        - Strong written & verbal communication
        - Collaborative team player
        - Self-motivated & proactive
        - Eager to learn from experts
        
        **Portfolio:** 50+ complete ML projects with real impact
        """)

    st.markdown("---")

    st.markdown("""
    ## 🎓 Learning Philosophy
    
    I believe in **continuous learning** and **practical application**. My approach involves:
    
    - **Understanding Fundamentals**: Deep dive into ML theory and mathematics
    - **Hands-On Practice**: Building projects to solidify learning
    - **Community Engagement**: Learning from and contributing to the ML community
    - **Reading Research**: Staying updated with latest advancements
    - **Teaching Others**: Documenting and sharing knowledge
    
    This philosophy has helped me grow from a curious beginner to a confident ML practitioner ready 
    to contribute to professional projects and teams.
    """)

# ==================== PROJECTS PAGE ====================
elif st.session_state.page == "Projects":

    st.markdown("# Projects Portfolio")

    st.markdown("""
    Comprehensive showcase of my AI/ML work spanning **50+ projects**. Featured below are my most significant 
    projects that demonstrate end-to-end implementation, from problem definition to deployment, showcasing 
    practical application of machine learning across healthcare, NLP, computer vision, and more.
    """)

    # Project Overview Box
    st.info("""
    **📌 Portfolio Overview:** I've completed 50+ projects spanning various domains of AI/ML. This page 
    features 6 major projects that best represent my capabilities. The complete collection includes 
    experimental projects, tutorials implementations, Kaggle competitions, hackathon submissions, and 
    production-ready applications - all available on my [GitHub](https://github.com/dheeraj815).
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

            st.markdown("### 📊 Metrics")
            for metric_name, metric_value in project['metrics'].items():
                st.markdown(f"**{metric_name}:** `{metric_value}`")

        st.markdown("---")

    # Project Statistics
    st.markdown("## 📊 Project Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Projects", "50+", "Across All Domains")

    with col2:
        active_count = sum(1 for p in GITHUB_REPOS.values()
                           if p['status'] == "Active")
        st.metric("Featured Projects", len(GITHUB_REPOS), "Highlighted Here")

    with col3:
        tech_count = len(
            set([tech for proj in GITHUB_REPOS.values() for tech in proj['tech_stack']]))
        st.metric("Technologies Used", "30+", "Diverse Stack")

    st.markdown("---")

    # Project Breakdown
    st.markdown("## 📁 Complete Project Portfolio (50+ Projects)")

    st.markdown("""
    Beyond the featured projects above, my portfolio includes extensive work across multiple domains:
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🏥 Healthcare & Medical AI
        - Medical diagnosis systems
        - Health recommendation engines
        - Clinical data analysis
        - Medical image classification
        - Patient prediction models
        
        **Count:** 10+ projects
        """)

    with col2:
        st.markdown("""
        ### 💬 NLP & Text Processing
        - Chatbots & conversational AI
        - Sentiment analysis systems
        - Recommendation engines
        - Text classification models
        - Language processing tools
        
        **Count:** 15+ projects
        """)

    with col3:
        st.markdown("""
        ### 👁️ Computer Vision
        - Image classification systems
        - Object detection models
        - Face recognition apps
        - Pattern recognition systems
        - Image processing projects
        
        **Count:** 12+ projects
        """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 📊 Data Science & Analytics
        - Predictive analytics models
        - Time series forecasting
        - Statistical analysis tools
        - Visualization dashboards
        - Business intelligence
        
        **Count:** 8+ projects
        """)

    with col2:
        st.markdown("""
        ### 🎮 Game AI & RL
        - Game playing agents
        - Strategy optimization
        - Pattern learning systems
        - Competitive AI models
        - Simulation environments
        
        **Count:** 5+ projects
        """)

    with col3:
        st.markdown("""
        ### 🌐 Development & Deployment
        - ML model deployment
        - REST API development
        - Full-stack applications
        - Portfolio websites
        - Interactive dashboards
        
        **Count:** 8+ projects
        """)

    st.info("""
    **💡 Note:** The 6 featured projects above represent my most significant and well-documented work. 
    My complete portfolio of 50+ projects includes experimental implementations, tutorial completions, 
    Kaggle competitions, hackathon submissions, and various learning exercises - all available on 
    [GitHub](https://github.com/dheeraj815).
    """)

    st.markdown("---")

    # Technology Distribution Chart
    st.markdown("## 📈 Technology Distribution")

    tech_counter = {}
    for project in GITHUB_REPOS.values():
        for tech in project['tech_stack']:
            tech_counter[tech] = tech_counter.get(tech, 0) + 1

    fig = go.Figure(data=[
        go.Bar(
            x=list(tech_counter.values()),
            y=list(tech_counter.keys()),
            orientation='h',
            marker=dict(
                color=list(tech_counter.values()),
                colorscale='Blues',
                showscale=False
            ),
            text=list(tech_counter.values()),
            textposition='auto',
        )
    ])

    fig.update_layout(
        title="Technologies Used Across Projects",
        xaxis_title="Number of Projects",
        yaxis_title="Technology",
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#d1d5db', family='Sora'),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True,
                    key="tech_distribution_chart")

# ==================== SKILLS PAGE ====================
elif st.session_state.page == "Skills":

    st.markdown("# Technical Skills")

    st.markdown("""
    Comprehensive overview of my technical capabilities, developed through academic coursework, personal 
    projects, and continuous self-learning. Each skill area represents hands-on experience and practical application.
    """)

    st.markdown("---")

    # Skills Overview
    for skill_category, details in SKILLS.items():
        st.markdown(f"## {skill_category}")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(
                f"**Proficiency Level:** {details['level']} ({details['proficiency']}%)")
            st.markdown(f"*{details['description']}*")

            st.markdown("**Technologies:**")
            skills_badges = " ".join(
                [f'<span class="badge">{skill}</span>' for skill in details['skills']])
            st.markdown(skills_badges, unsafe_allow_html=True)

        with col2:
            # Proficiency gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=details['proficiency'],
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Proficiency", 'font': {'color': '#d1d5db'}},
                gauge={
                    'axis': {'range': [0, 100], 'tickcolor': '#d1d5db'},
                    'bar': {'color': "#2563eb"},
                    'bgcolor': "rgba(0,0,0,0)",
                    'borderwidth': 2,
                    'bordercolor': "#374151",
                    'steps': [
                        {'range': [0, 50], 'color': 'rgba(37, 99, 235, 0.2)'},
                        {'range': [50, 75], 'color': 'rgba(37, 99, 235, 0.3)'},
                        {'range': [75, 100], 'color': 'rgba(37, 99, 235, 0.4)'}
                    ],
                }
            ))

            fig.update_layout(
                height=200,
                margin=dict(l=20, r=20, t=40, b=20),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#d1d5db', family='Sora', size=12)
            )

            st.plotly_chart(fig, use_container_width=True,
                            key=f"skill_gauge_{skill_category}")

        st.markdown("---")

    # Overall Proficiency Radar Chart
    st.markdown("## 📊 Skills Proficiency Overview")

    categories = list(SKILLS.keys())
    values = [SKILLS[cat]['proficiency'] for cat in categories]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Proficiency',
        fillcolor='rgba(37, 99, 235, 0.3)',
        line=dict(color='#2563eb', width=2)
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='#374151',
                tickfont=dict(color='#d1d5db')
            ),
            angularaxis=dict(
                gridcolor='#374151',
                tickfont=dict(color='#d1d5db', size=11)
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=False,
        height=600,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#d1d5db', family='Sora')
    )

    st.plotly_chart(fig, use_container_width=True, key="skills_radar_chart")

    st.markdown("---")

    # Soft Skills
    st.markdown("## 🤝 Professional Competencies")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Technical Competencies
        
        - **Problem Solving**: Analytical thinking and systematic approach to complex challenges
        - **Quick Learning**: Rapidly acquire and apply new technologies and frameworks
        - **Research Skills**: Comfortable reading and implementing research papers
        - **Code Quality**: Focus on clean, maintainable, and well-documented code
        - **Debugging**: Systematic approach to identifying and resolving issues
        - **Testing**: Understanding of unit testing and validation practices
        """)

    with col2:
        st.markdown("""
        ### Collaboration & Communication
        
        - **Team Collaboration**: Experience in academic group projects and coding communities
        - **Technical Communication**: Ability to explain complex concepts clearly
        - **Documentation**: Comprehensive project documentation and README files
        - **Adaptability**: Flexible in learning new tools and methodologies
        - **Time Management**: Balancing academics, projects, and continuous learning
        - **Self-Motivation**: Proactive in seeking knowledge and completing projects
        """)

    st.markdown("---")

    # Learning Resources
    st.markdown("## 📚 Continuous Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### Online Platforms
        
        - Coursera (Specializations)
        - DataCamp (Data Science)
        - Kaggle (Competitions)
        - YouTube (Tutorials)
        - Fast.ai (Deep Learning)
        - Google Codelabs
        """)

    with col2:
        st.markdown("""
        ### Reading & Research
        
        - arXiv (Research Papers)
        - Medium/Towards Data Science
        - Official Documentation
        - Technical Blogs
        - ML Conference Papers
        - GitHub Repositories
        """)

    with col3:
        st.markdown("""
        ### Community Engagement
        
        - Stack Overflow
        - Reddit ML Communities
        - Discord Servers
        - LinkedIn Groups
        - GitHub Discussions
        - Coding Forums
        """)

# ==================== EDUCATION PAGE ====================
elif st.session_state.page == "Education":

    st.markdown("# Education & Academic Background")

    st.markdown("""
    My academic journey in AI/ML, combining rigorous coursework with hands-on project experience and 
    continuous skill development through certifications and self-learning.
    """)

    st.markdown("---")

    # Main Education
    st.markdown(f"## {EDUCATION['degree']}")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"**Institution:** {EDUCATION['institution']}")
        st.markdown(f"**Duration:** {EDUCATION['duration']}")
        st.markdown(f"**Current Status:** {EDUCATION['status']}")
        st.markdown(f"**Academic Performance:** {EDUCATION['gpa']}")

    with col2:
        st.markdown("""
        <div style='padding: 1.5rem; background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(124, 58, 237, 0.15)); border-radius: 0.75rem; border: 1px solid var(--border);'>
            <h4 style='color: var(--text-primary); margin-bottom: 1rem;'>🎯 Academic Highlights</h4>
            <p style='color: var(--text-secondary); font-size: 0.9rem; line-height: 1.6;'>
                ✓ Strong foundation in AI/ML<br>
                ✓ 6+ major projects completed<br>
                ✓ Active coding community member<br>
                ✓ Consistent academic excellence
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📚 Relevant Coursework")

    col1, col2 = st.columns(2)

    mid_point = len(EDUCATION['coursework']) // 2

    with col1:
        for course in EDUCATION['coursework'][:mid_point]:
            st.markdown(f"- {course}")

    with col2:
        for course in EDUCATION['coursework'][mid_point:]:
            st.markdown(f"- {course}")

    st.markdown("---")

    # Academic Projects
    st.markdown("## 🔬 Major Academic Projects")

    academic_projects = [
        {
            "title": "Medical Image Classification System",
            "course": "Deep Learning Lab",
            "description": "CNN-based system for chest X-ray analysis",
            "tech": "TensorFlow, OpenCV, ResNet50",
            "outcome": "89% validation accuracy"
        },
        {
            "title": "Sentiment Analysis System",
            "course": "Natural Language Processing",
            "description": "Transformer-based sentiment classifier",
            "tech": "BERT, PyTorch, NLTK",
            "outcome": "91% test accuracy"
        },
        {
            "title": "Face Recognition Attendance",
            "course": "Computer Vision",
            "description": "Automated attendance system",
            "tech": "OpenCV, face_recognition, SQLite",
            "outcome": "95% recognition accuracy"
        },
        {
            "title": "Stock Price Prediction",
            "course": "ML Applications",
            "description": "LSTM-based time series forecasting",
            "tech": "PyTorch, yfinance, Technical Indicators",
            "outcome": "65% directional accuracy"
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
        """)

    with col2:
        st.markdown("""
        ### ML/AI Expertise
        
        - ML Algorithms & Theory
        - Deep Learning Architectures
        - Computer Vision Techniques
        - NLP & Text Processing
        - Model Optimization
        - Statistical Methods
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
        """)

    st.markdown("---")

    # Timeline Visualization
    st.markdown("## 📈 Academic Timeline")

    timeline_data = pd.DataFrame({
        'Year': ['2024', '2025', '2026', '2027'],
        'Semester': ['Sem 1-2', 'Sem 3-4', 'Sem 5-6', 'Sem 7-8'],
        'Focus': ['Foundations', 'Core ML/AI', 'Advanced Topics', 'Specialization'],
        'Projects': [2, 3, 5, 8]
    })

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=timeline_data['Year'],
        y=timeline_data['Projects'],
        mode='lines+markers+text',
        name='Projects Completed',
        line=dict(color='#2563eb', width=3),
        marker=dict(size=12, color='#2563eb',
                    line=dict(color='white', width=2)),
        text=timeline_data['Focus'],
        textposition='top center',
        textfont=dict(color='#d1d5db', size=12)
    ))

    fig.update_layout(
        title='Project Growth Throughout Academic Journey',
        xaxis_title='Academic Year',
        yaxis_title='Cumulative Projects',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#d1d5db', family='Sora'),
        hovermode='x unified'
    )

    st.plotly_chart(fig, use_container_width=True,
                    key="education_timeline_chart")

# ==================== CERTIFICATIONS PAGE ====================
elif st.session_state.page == "Certifications":

    st.markdown("# Certifications & Professional Development")

    st.markdown("""
    Beyond academic education, I've pursued professional certifications to deepen expertise and stay 
    current with industry practices and emerging technologies.
    """)

    st.markdown("---")

    # Certification Stats
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Certifications", len(CERTIFICATIONS), "Professional")
    with col2:
        st.metric("Completed", len(CERTIFICATIONS), "Verified")
    with col3:
        st.metric("Platforms Used", "3", "Coursera, DataCamp")
    with col4:
        st.metric("Learning Hours", "500+", "Documented")

    st.markdown("---")

    # Display All Completed Certifications
    st.markdown("## ✅ Professional Certifications")

    for cert in CERTIFICATIONS:
        st.markdown(f"### {cert['name']}")

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
            <div style='padding: 1.5rem; background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(6, 182, 212, 0.15)); border-radius: 0.75rem; border: 1px solid rgba(16, 185, 129, 0.3);'>
                <p style='color: var(--success); font-weight: 600; margin-bottom: 0.5rem;'>✓ {cert['status']}</p>
                <p style='color: var(--text-secondary); font-size: 0.875rem;'>{cert['credential']}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

    st.markdown("---")

    # Learning Platforms
    st.markdown("## 📚 Continuous Learning Ecosystem")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### Online Platforms
        
        **Primary Platforms:**
        - Coursera (Specializations from top universities)
        - DataCamp (Interactive data science tracks)
        - Kaggle Learn (Hands-on ML tutorials)
        - YouTube (Technical content creators)
        
        **Supplementary:**
        - Fast.ai (Practical deep learning)
        - Google Codelabs (TensorFlow guides)
        - Udacity (Nanodegree programs)
        - edX (University courses)
        """)

    with col2:
        st.markdown("""
        ### Reading & Research
        
        **Technical Resources:**
        - arXiv (Latest ML research papers)
        - Medium/Towards Data Science
        - Official framework documentation
        - Technical blogs from industry
        
        **Industry Insights:**
        - ML conference papers (NeurIPS, ICML)
        - GitHub trending repositories
        - Tech company engineering blogs
        - AI research lab publications
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
        """)

    st.markdown("---")

    # Learning Philosophy
    st.markdown("""
    ## 🎯 Learning Philosophy
    
    My approach to continuous professional development:
    
    **Structured Learning:** Following well-designed courses from reputable institutions ensures comprehensive coverage of topics and strong theoretical foundation.
    
    **Practical Application:** Every certification is immediately applied to personal projects, reinforcing learning through hands-on implementation.
    
    **Community Learning:** Active participation in ML communities provides diverse perspectives and keeps me updated with industry trends and best practices.
    
    **Research-Oriented:** Regular reading of research papers helps understand cutting-edge developments and inspires new project ideas.
    
    **Documentation:** Maintaining detailed notes and documenting learnings helps reinforce concepts and provides reference for future projects.
    """)

# ==================== CONTACT PAGE ====================
elif st.session_state.page == "Contact":

    st.markdown("# Contact & Connect")

    st.markdown("""
    I'm actively seeking **AI/ML internship opportunities** and always open to connecting with fellow 
    developers, researchers, and professionals. Let's build something amazing together!
    """)

    st.markdown("---")

    # Contact Cards
    st.markdown("## 📬 Get In Touch")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(124, 58, 237, 0.15)); border-radius: 0.75rem; border: 1px solid var(--border);'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>📧</div>
            <h3 style='color: var(--text-primary); margin-bottom: 0.5rem;'>Email</h3>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
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
        <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(124, 58, 237, 0.15)); border-radius: 0.75rem; border: 1px solid var(--border);'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>💼</div>
            <h3 style='color: var(--text-primary); margin-bottom: 0.5rem;'>LinkedIn</h3>
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
        <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(124, 58, 237, 0.15)); border-radius: 0.75rem; border: 1px solid var(--border);'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>💻</div>
            <h3 style='color: var(--text-primary); margin-bottom: 0.5rem;'>GitHub</h3>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;'>
                github.com/dheeraj815
            </p>
            <p style='color: var(--text-muted); font-size: 0.8rem;'>Code portfolio</p>
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
        - Data Science Intern
        - Machine Learning Research Intern
        - Applied AI Intern
        - Deep Learning Intern
        
        **Preferred Duration:** 2-6 months (Flexible)
        
        **Work Mode:** Remote, Hybrid, or On-site
        
        **Start Date:** Immediate to Flexible (within 2-3 months)
        
        **Availability:** Full-time commitment during internship period
        
        **Location:** Available for work in India; Open to relocation for right opportunity
        """)

    with col2:
        st.markdown("""
        ### What I Bring
        
        **Technical Capabilities:**
        - Strong Python programming & ML fundamentals
        - 6+ complete end-to-end ML projects
        - Experience with TensorFlow, PyTorch, Scikit-learn
        - Web development & model deployment skills
        - Understanding of ML lifecycle and best practices
        
        **Professional Qualities:**
        - Excellent analytical & problem-solving skills
        - Strong written & verbal communication
        - Collaborative team player with leadership potential
        - Self-motivated with strong work ethic
        - Quick learner adaptable to new technologies
        - Attention to detail & quality-focused
        
        **Portfolio:** View my work at [github.com/dheeraj815](https://github.com/dheeraj815)
        
        **50+ Projects Completed** across diverse domains including healthcare AI, NLP, computer vision, 
        recommendation systems, predictive analytics, and more.
        """)

    st.markdown("---")

    # Contact Guidelines
    st.markdown("## 💬 Contact Guidelines")

    st.markdown("""
    ### For Internship Opportunities
    
    **Best Method:** Email (dheerajmuley006@gmail.com)
    
    **Please Include:**
    - Company/Organization name and background
    - Position details and responsibilities
    - Duration and expected timeline
    - Key technical requirements
    - Any specific projects or domains
    
    **What You'll Receive:**
    - Response within 24 hours
    - Updated resume and portfolio
    - Relevant project links and code samples
    - Availability and interview scheduling
    
    ### For Collaboration & Networking
    
    **LinkedIn:** Perfect for professional networking and staying connected
    
    **GitHub:** For technical discussions, code reviews, and collaborations
    
    **Email:** For general inquiries, learning resources sharing, or project discussions
    
    ### Response Times
    
    - **Email:** Within 24 hours (typically same day)
    - **LinkedIn:** Within 48 hours
    - **GitHub Issues:** Same day for urgent technical matters
    
    **Best Time to Contact:** Anytime! I check messages regularly throughout the day (IST timezone: GMT+5:30)
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
        
        **Languages:** English (Fluent), Hindi (Native)
        
        **Willing to Relocate:** Yes, for the right opportunity
        
        **Work Authorization:** Available for work in India
        
        **Notice Period:** Immediate (for internships)
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
        - Team player
        """)

    st.markdown("---")

    # Call to Action
    st.success("""
    💡 **Thank you for visiting my portfolio!** I'm excited about opportunities to contribute to innovative 
    AI/ML projects and learn from experienced professionals. Whether it's an internship opportunity, 
    collaboration proposal, or just a technical discussion, I'd love to hear from you!
    """)

    # Quick Actions
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 Request Resume", use_container_width=True):
            st.info(
                "Please email me at dheerajmuley006@gmail.com to request my latest resume and additional materials.")

    with col2:
        if st.button("💼 View Projects", use_container_width=True):
            st.session_state.page = "Projects"
            st.rerun()

    with col3:
        if st.button("🎓 Check Credentials", use_container_width=True):
            st.session_state.page = "Certifications"
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 0; color: var(--text-muted);'>
    <p style='font-size: 0.9rem; margin-bottom: 0.5rem;'>
        Built with passion using <strong>Streamlit</strong> and <strong>Python</strong>
    </p>
    <p style='font-size: 0.875rem; margin-bottom: 1rem;'>
        © 2026 Dheeraj Muley | Last Updated: January 2026
    </p>
    <p style='font-size: 0.875rem;'>
        <a href='https://github.com/dheeraj815' target='_blank'>GitHub</a> • 
        <a href='https://linkedin.com/in/dheeraj-muley' target='_blank'>LinkedIn</a> • 
        <a href='mailto:dheerajmuley006@gmail.com'>Email</a>
    </p>
</div>
""", unsafe_allow_html=True)
