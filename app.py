from __future__ import annotations

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
        
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1f2e 0%, #0f1419 100%);
        }
        
        .main .block-container {
            padding-top: 2rem;
            max-width: 1400px;
        }
        
        .stExpander {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
        }
        
        .stButton > button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        
        [data-testid="stFileUploader"] {
            border: 2px dashed #4a5568;
            border-radius: 12px;
            padding: 2rem;
            background-color: #1a202c;
            transition: all 0.3s ease;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #10b981;
            background-color: #1e293b;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: #1e293b;
            padding: 0.5rem;
            border-radius: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: transparent;
            border-radius: 6px;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #10b981;
        }
        
        .stProgress > div > div {
            background-color: #10b981;
        }
        
        .stSelectbox, .stTextInput {
            margin-bottom: 1rem;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .element-container {
            animation: fadeIn 0.3s ease;
        }
        
        .logo-link {
            cursor: pointer;
            text-decoration: none;
        }
        
        .logo-link:hover h1 {
            color: #059669 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Logo with clickable link
    if st.button("StudyMate AI", key="logo_button", use_container_width=True, type="primary"):
        st.session_state.current_page = "Home"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation section
    st.markdown("""
        <div style='padding: 0 0.5rem;'>
            <p style='color: #64748b; font-size: 0.75rem; text-transform: uppercase; 
                      letter-spacing: 1px; margin-bottom: 0.5rem; font-weight: 600;'>
                Navigation
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"
    
    pages = {
        "Home": """<svg class="nav-icon" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/>
        </svg>""",
        "Study": """<svg class="nav-icon" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z"/>
        </svg>""",
        "Community": """<svg class="nav-icon" fill="currentColor" viewBox="0 0 20 20">
            <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"/>
        </svg>""",
        "History": """<svg class="nav-icon" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"/>
        </svg>"""
    }
    
    for page_name, icon_svg in pages.items():
        is_selected = st.session_state.current_page == page_name
        
        if st.button(
            page_name, 
            key=f"nav_{page_name}",
            use_container_width=True,
            type="primary" if is_selected else "secondary"
        ):
            st.session_state.current_page = page_name
            st.rerun()
    
    # Footer
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='position: fixed; bottom: 0; left: 0; right: 0; padding: 1.5rem; 
                    border-top: 1px solid #334155; 
                    background: linear-gradient(180deg, transparent 0%, #0f1419 100%);
                    width: inherit;'>
            <p style='color: #64748b; font-size: 0.75rem; text-align: center; margin: 0;'>
                Made with ❤️ for Education
            </p>
            <p style='color: #475569; font-size: 0.7rem; text-align: center; margin-top: 0.25rem;'>
                Powered by Onyx Team
            </p>
        </div>
    """, unsafe_allow_html=True)

# Main content
page = st.session_state.current_page

if page == "Home":
    from pages import home
    home.show()
elif page == "Study":
    from pages import study
    study.show()
elif page == "Community":
    from pages import community
    community.show()
elif page == "History":
    from pages import history
    history.show()
