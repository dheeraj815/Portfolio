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

# Premium Custom CSS
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
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(99, 102, 241, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(168, 85, 247, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 40% 60%, rgba(59, 130, 246, 0.05) 0%, transparent 40%);
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .block-container {
        padding: 2rem 1.5rem;
        max-width: 1400px;
        position: relative;
        z-index: 1;
    }
    
    .hero-wrapper {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.95) 0%, rgba(31, 41, 55, 0.9) 100%);
        backdrop-filter: blur(20px);
        padding: 70px 50px;
        border-radius: 32px;
        margin: 30px 0 70px 0;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 
                    0 0 0 1px rgba(99, 102, 241, 0.2),
                    inset 0 1px 0 rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(99, 102, 241, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .hero-wrapper::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.12) 0%, transparent 70%);
        animation: pulse 6s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.4; }
        50% { transform: scale(1.15); opacity: 0.7; }
    }
    
    .hero-name {
        font-size: 5.5rem;
        font-weight: 900;
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #818cf8 0%, #6366f1 30%, #a855f7 70%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        line-height: 1.1;
        letter-spacing: -3px;
        position: relative;
        z-index: 2;
        animation: fadeInUp 0.8s ease-out;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .hero-role {
        font-size: 2.2rem;
        color: #818cf8;
        margin: 28px 0;
        font-weight: 700;
        position: relative;
        z-index: 2;
        animation: fadeInUp 0.8s ease-out 0.15s both;
    }
    
    .hero-tagline {
        font-size: 1.25rem;
        color: #cbd5e1;
        max-width: 850px;
        margin: 28px auto;
        line-height: 1.9;
        position: relative;
        z-index: 2;
        animation: fadeInUp 0.8s ease-out 0.3s both;
    }
    
    .hero-highlight {
        display: inline-flex;
        align-items: center;
        gap: 15px;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        padding: 15px 32px;
        border-radius: 50px;
        font-size: 1.1rem;
        color: #e0e7ff;
        font-weight: 600;
        margin: 20px 0;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        position: relative;
        z-index: 2;
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
        animation: pulse 2s ease-in-out infinite;
    }
    
    .pulse-dot {
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
        box-shadow: 0 0 10px rgba(34, 197, 94, 0.8);
    }
    
    .social-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 40px;
        flex-wrap: wrap;
        position: relative;
        z-index: 2;
    }
    
    .social-link {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        padding: 14px 36px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.3);
        display: inline-flex;
        align-items: center;
        gap: 10px;
    }
    
    .social-link:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0 16px 40px rgba(99, 102, 241, 0.5);
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 25px;
        margin: 40px 0;
    }
    
    .stat-box {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 45px 30px;
        border-radius: 24px;
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
        font-size: 4rem;
        font-weight: 900;
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #818cf8 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
    }
    
    .stat-text {
        font-size: 1.1rem;
        color: #cbd5e1;
        margin-top: 15px;
        font-weight: 600;
    }
    
    .section-title {
        font-size: 3.5rem;
        font-weight: 900;
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #818cf8 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin: 80px 0 50px 0;
        letter-spacing: -2px;
    }
    
    .section-title::after {
        content: '';
        display: block;
        width: 140px;
        height: 6px;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        margin: 25px auto 0;
        border-radius: 3px;
        box-shadow: 0 4px 16px rgba(99, 102, 241, 0.4);
    }
    
    .project-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
        gap: 28px;
        margin: 35px 0;
    }
    
    .project-item {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 38px;
        border-radius: 24px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.2);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .project-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    
    .project-item:hover::before {
        transform: scaleX(1);
    }
    
    .project-item:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 64px rgba(99, 102, 241, 0.3);
        border-color: #6366f1;
    }
    
    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: start;
        margin-bottom: 15px;
        gap: 15px;
    }
    
    .project-name {
        font-size: 1.7rem;
        font-weight: 800;
        color: #e0e7ff;
        margin: 0;
        line-height: 1.3;
    }
    
    .project-badge {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.25) 0%, rgba(168, 85, 247, 0.25) 100%);
        color: #c4b5fd;
        padding: 8px 18px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        border: 1.5px solid rgba(129, 140, 248, 0.4);
        white-space: nowrap;
    }
    
    .project-cat {
        font-size: 1rem;
        color: #818cf8;
        font-weight: 600;
        margin: 10px 0 18px 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .project-desc {
        font-size: 1.05rem;
        color: #cbd5e1;
        line-height: 1.7;
        margin-bottom: 22px;
    }
    
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 20px;
    }
    
    .tech-badge {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        color: #e0e7ff;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        transition: all 0.3s;
    }
    
    .tech-badge:hover {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        transform: translateY(-2px);
    }
    
    .skill-container {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.2);
        margin-bottom: 30px;
    }
    
    .skill-header {
        font-size: 2rem;
        font-weight: 800;
        color: #e0e7ff;
        margin-bottom: 28px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .skill-list {
        display: flex;
        flex-wrap: wrap;
        gap: 14px;
    }
    
    .skill-chip {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        color: #e0e7ff;
        padding: 12px 26px;
        border-radius: 25px;
        font-size: 1rem;
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
    
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 28px;
        margin: 40px 0;
    }
    
    .contact-card {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 45px 35px;
        border-radius: 24px;
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
        font-size: 3.5rem;
        margin-bottom: 20px;
    }
    
    .contact-label {
        font-size: 1rem;
        color: #94a3b8;
        margin-bottom: 12px;
        font-weight: 600;
    }
    
    .contact-info {
        font-size: 1.2rem;
        color: #e0e7ff;
        font-weight: 700;
        margin-bottom: 24px;
        word-break: break-word;
    }
    
    .about-content {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.7) 100%);
        backdrop-filter: blur(15px);
        padding: 45px;
        border-radius: 24px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.2);
        margin-bottom: 30px;
    }
    
    .about-para {
        font-size: 1.2rem;
        color: #cbd5e1;
        line-height: 1.9;
        margin-bottom: 22px;
        text-align: justify;
    }
    
    .timeline-item {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.7) 0%, rgba(31, 41, 55, 0.6) 100%);
        backdrop-filter: blur(12px);
        padding: 32px;
        border-radius: 20px;
        margin-bottom: 22px;
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
        font-size: 1.15rem;
        font-weight: 700;
        color: #818cf8;
        margin-bottom: 10px;
    }
    
    .timeline-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #e0e7ff;
        margin-bottom: 10px;
    }
    
    .timeline-desc {
        font-size: 1.05rem;
        color: #cbd5e1;
        line-height: 1.7;
    }
    
    .achievement-box {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.08) 0%, rgba(59, 130, 246, 0.08) 100%);
        border: 1.5px solid rgba(34, 197, 94, 0.25);
        padding: 20px;
        border-radius: 16px;
        margin-top: 12px;
    }
    
    .achievement-text {
        color: #86efac;
        font-size: 1rem;
        font-weight: 600;
        line-height: 1.6;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 14, 39, 0.95) 0%, rgba(26, 29, 58, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(129, 140, 248, 0.2);
    }
    
    .stRadio > label {
        color: #e0e7ff;
        font-weight: 700;
        font-size: 1.3rem;
        margin-bottom: 18px;
    }
    
    .stRadio > div > label {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        padding: 14px 28px;
        border-radius: 16px;
        color: #e0e7ff;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        cursor: pointer;
        transition: all 0.3s;
        font-weight: 600;
        font-size: 1.05rem;
    }
    
    .stRadio > div > label:hover {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        transform: translateX(8px);
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.4);
    }
    
    h1, h2, h3 {
        color: #e0e7ff !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
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

# Sidebar
st.sidebar.markdown("## 🎯 NAVIGATION")
selected = st.sidebar.radio(
    "",
    ["🏠 HOME", "👤 ABOUT", "💼 PROJECTS", "🛠️ SKILLS", "🎓 EXPERIENCE",
        "🏆 ACHIEVEMENTS", "📧 CONTACT", "📊 ANALYTICS"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
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

current_year = datetime.now().year

# HOME
if selected == "🏠 HOME":
    st.markdown(f"""
    <div class="hero-wrapper">
        <div class="hero-name">DHEERAJ MULEY</div>
        <div class="hero-role">AI Engineer & Full Stack Developer</div>
        <div class="hero-tagline">
            Building intelligent solutions with cutting-edge AI, Machine Learning, and Modern Web Technologies
        </div>
        <div style="text-align: center; margin-top: 25px;">
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

# PROJECTS
elif selected == "💼 PROJECTS":
    st.markdown('<div class="section-title">FEATURED PROJECTS</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        project_filter = st.selectbox("🔍 Filter by Category",
                                      ["All Projects", "Healthcare AI", "Computer Vision", "NLP", "FinTech", "Web Apps", "IoT"])

    projects = [
        {
            "name": "Medical Image Analyzer",
            "category": "Healthcare AI",
            "badge": "FEATURED",
            "desc": "Deep learning platform for analyzing X-rays, CT scans, and MRIs. Achieved 94% accuracy in disease detection using custom CNN architecture.",
            "tech": ["TensorFlow", "PyTorch", "OpenCV", "Flask", "Docker"]
        },
        {
            "name": "AI Voice Assistant",
            "category": "NLP",
            "badge": "NEW",
            "desc": "Advanced voice recognition system with NLP capabilities. Supports multi-language processing and real-time speech-to-text conversion.",
            "tech": ["Python", "PyTorch", "Transformers", "FastAPI", "WebSockets"]
        },
        {
            "name": "Stock Prediction Engine",
            "category": "FinTech",
            "badge": "LIVE",
            "desc": "LSTM-based system for stock price forecasting with sentiment analysis. Processes real-time market data and news feeds.",
            "tech": ["Python", "LSTM", "Pandas", "Plotly", "Redis"]
        },
        {
            "name": "Smart IoT Dashboard",
            "category": "IoT",
            "badge": "PRODUCTION",
            "desc": "Real-time monitoring dashboard for industrial sensors. Handles 5K+ concurrent connections with MQTT protocol.",
            "tech": ["React", "Node.js", "MQTT", "InfluxDB", "Chart.js"]
        },
        {
            "name": "Face Recognition System",
            "category": "Computer Vision",
            "badge": "DEPLOYED",
            "desc": "Real-time face detection and recognition with anti-spoofing. Features liveness detection for enhanced security.",
            "tech": ["Python", "OpenCV", "DeepFace", "Flask", "Redis"]
        },
        {
            "name": "E-Commerce Platform",
            "category": "Web Apps",
            "badge": "SCALABLE",
            "desc": "Full-stack marketplace with AI recommendations. Manages 50K+ products with intelligent search and filtering.",
            "tech": ["React", "Node.js", "MongoDB", "Stripe", "AWS"]
        },
        {
            "name": "Document Q&A System",
            "category": "NLP",
            "badge": "AI-POWERED",
            "desc": "RAG-based intelligent document analysis using vector embeddings. Supports PDF, DOCX, and multiple file formats.",
            "tech": ["LangChain", "FAISS", "Streamlit", "OpenAI", "Python"]
        },
        {
            "name": "Automated Data Pipeline",
            "category": "Web Apps",
            "badge": "AUTOMATED",
            "desc": "End-to-end ETL pipeline for large-scale data processing. Automated reporting and ML model training workflows.",
            "tech": ["Apache Airflow", "Python", "PostgreSQL", "Docker", "Pandas"]
        }
    ]

    if project_filter != "All Projects":
        filtered_projects = [
            p for p in projects if p["category"] == project_filter]
    else:
        filtered_projects = projects

    st.markdown('<div class="project-grid">', unsafe_allow_html=True)

    for project in filtered_projects:
        tech_badges = "".join(
            [f'<span class="tech-badge">{tech}</span>' for tech in project["tech"]])

        st.markdown(f"""
        <div class="project-item">
            <div class="project-header">
                <div class="project-name">{project["name"]}</div>
                <span class="project-badge">{project["badge"]}</span>
            </div>
            <div class="project-cat">{project["category"]}</div>
            <div class="project-desc">{project["desc"]}</div>
            <div class="tech-stack">{tech_badges}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

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
    <div class="hero-tagline" style="text-align: center; margin-bottom: 50px;">
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

    st.markdown('<div class="section-title" style="font-size: 2.8rem; margin-top: 80px;">💼 SERVICES</div>',
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
            <div class="contact-card" style="padding: 35px;">
                <div class="contact-emoji">{service["icon"]}</div>
                <div class="timeline-title" style="margin-bottom: 12px; font-size: 1.25rem;">{service["title"]}</div>
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
<div style="text-align: center; margin-top: 80px; padding: 35px; border-top: 1px solid rgba(129, 140, 248, 0.2);">
    <div class="hero-tagline" style="margin-bottom: 18px; font-size: 1.1rem;">
        Built with ❤️ using Streamlit • © 2026 Dheeraj Muley
    </div>
    <div class="availability-badge" style="display: inline-flex;">
        <span class="pulse-dot"></span>
        Open for New Opportunities
    </div>
</div>
""", unsafe_allow_html=True)
