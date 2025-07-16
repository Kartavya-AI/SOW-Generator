import streamlit as st
from datetime import datetime
from src.sow.crew import Sow
import os

# Page configuration with custom styling
st.set_page_config(
    page_title="📚 Scope of Work Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Sidebar for API and AI settings
with st.sidebar:
    st.header("⚙️ AI & API Settings")

    # Gemini API Key input
    gemini_api_key = st.text_input(
        "Gemini API Key",
        type="password",
        value=st.session_state.get("GEMINI_API_KEY", ""),
        help="Enter your Gemini (Google AI) API key"
    )

    # Serper API Key input
    serper_api_key = st.text_input(
        "Serper API Key",
        type="password",
        value=st.session_state.get("SERPER_API_KEY", ""),
        help="Enter your Serper (Google Search) API key"
    )

    # AI Model selection dropdown
    model_options = ["gemini/gemini-2.5-flash-preview-05-20", "", "gemini-pro", "mistral-medium"]
    default_model = st.session_state.get("MODEL", model_options[0])

    model_choice = st.selectbox(
        "Select AI Model",
        model_options,
        index=model_options.index(default_model),
        help="Choose which AI model to use"
    )

    # Save button
    if st.button("💾 Save Settings"):
        updated = False

        if gemini_api_key:
            st.session_state["GEMINI_API_KEY"] = gemini_api_key
            os.environ["GEMINI_API_KEY"] = gemini_api_key
            updated = True

        if serper_api_key:
            st.session_state["SERPER_API_KEY"] = serper_api_key
            os.environ["SERPER_API_KEY"] = serper_api_key
            updated = True

        if model_choice:
            st.session_state["MODEL"] = model_choice
            os.environ["MODEL"] = model_choice
            updated = True

        if updated:
            st.success("✅ Settings saved successfully!")
        else:
            st.error("❌ Please enter at least one API key or model selection.")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .main-header h1 {
        color: white !important;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #f0f0f0;
        margin-bottom: 0;
    }
    
    .form-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin-bottom: 2rem;
    }
    
    .output-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 5px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .status-success {
        background: #d4edda;
        color: #155724;
    }
    
    .status-error {
        background: #f8d7da;
        color: #721c24;
    }
    
    .status-warning {
        background: #fff3cd;
        color: #856404;
    }
    
    .metric-container {
        display: flex;
        justify-content: space-around;
        margin: 1rem 0;
    }
    
    .metric-box {
        text-align: center;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: bold;
        color: #667eea;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #6c757d;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>📝 Scope of Work Generator</h1>
    <p class="subtitle">Powered by CrewAI • Generate Professional SoW Documents in Minutes</p>
</div>
""", unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns([2, 1])

with col2:
    st.markdown("""
    <style>
    ul {
    padding-left: 20px;
    list-style-type: disc;
    }
    li {
    margin-bottom: 8px;
    font-size: 1rem;
    }
    h3 {
    color: #2c3e50;
    margin-bottom: 10px;
    }
    </style>

    <h3>Features</h3>
    <ul>
        <li><strong>Smart Parsing:</strong> Automatically extracts project details from simple text inputs.</li>
        <li><strong>Comprehensive Coverage:</strong> Includes all essential sections such as deliverables, timelines, IP terms, and payment clauses.</li>
        <li><strong>Customizable Output:</strong> Tailor content to fit your project’s unique needs.</li>
        <li><strong>Legal Best Practices:</strong> Includes standard clauses to protect both parties.</li>
        <li><strong>Ready-to-Share Documents:</strong> Export clean, polished Markdown files or PDFs effortlessly.</li>
    </ul>

    <h3>Tips for Best Results</h3>
    <ul>
        <li>Provide clear, concise descriptions of project goals and scope.</li>
        <li>Include timelines and deliverables wherever possible.</li>
        <li>Specify any special requirements or constraints upfront.</li>
        <li>Review generated drafts and customize sections as needed.</li>
    </ul>
    """, unsafe_allow_html=True)


with col1:
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    # Input form with better organization
    with st.form("input_form", clear_on_submit=False):
        st.subheader("📋 Project Details")
        
        # Client and Contractor in columns
        client_col, contractor_col = st.columns(2)
        
        with client_col:
            client = st.text_input(
                "👤 Client Name",
                value="Alice from BrandCo",
                placeholder="Enter client name or company",
                help="The name of the client or client company"
            )
        
        with contractor_col:
            contractor = st.text_input(
                "🏢 Contractor Name",
                value="Bob from DevGuru",
                placeholder="Enter contractor name or company",
                help="The name of the contractor or contracting company"
            )
        
        # Project description with better formatting
        st.markdown("### 📝 Project Description")
        raw_description = st.text_area(
            "",
            value=(
                "We are planning to develop a modern Shopify-based e-commerce site that supports "
                "responsive design, payment gateway integration, SEO, and product listing features. "
                "The project should be completed in 4 weeks, with a clear deliverables list and limited revision rounds."
            ),
            height=150,
            placeholder="Describe the project scope, goals, timelines, deliverables, and any special conditions or requirements...",
            help="Provide a detailed description of the project including objectives, requirements, timeline, and deliverables"
        )
        
        # # Additional options in expander
        # with st.expander("⚙️ Advanced Options", expanded=False):
        #     priority = st.selectbox(
        #         "Project Priority",
        #         ["Standard", "High", "Urgent"],
        #         help="Set the priority level for the project"
        #     )
            
        #     include_legal = st.checkbox(
        #         "Include Legal Terms",
        #         value=True,
        #         help="Include standard legal terms and conditions"
        #     )
            
        #     include_timeline = st.checkbox(
        #         "Include Detailed Timeline",
        #         value=True,
        #         help="Generate a detailed project timeline with milestones"
        #     )
        
        # Submit button with better styling
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🚀 Generate Scope of Work", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Initialize report state
if 'report_md' not in st.session_state:
    st.session_state['report_md'] = ""

# Form processing
if submitted:
    # Validation with better error handling
    errors = []
    if not client.strip():
        errors.append("Client name is required")
    if not contractor.strip():
        errors.append("Contractor name is required")
    if not raw_description.strip():
        errors.append("Project description is required")
    if len(raw_description.strip()) < 50:
        errors.append("Project description should be at least 50 characters")
    
    if errors:
        for error in errors:
            st.error(f"⚠️ {error}")
    else:
        inputs = {
            'Client': client,
            'Contractor': contractor,
            'raw_description': raw_description,
            'current_year': str(datetime.now().year),
        }

        # Progress indicator
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            status_text.text("🔄 Initializing AI crew...")
            progress_bar.progress(20)
            
            status_text.text("🤖 Analyzing project requirements...")
            progress_bar.progress(40)
            
            status_text.text("📝 Generating scope of work...")
            progress_bar.progress(60)
            
            # Run the crew
            Sow().crew().kickoff(inputs=inputs)
            
            progress_bar.progress(80)
            status_text.text("📄 Formatting document...")
            
            # Check for output file
            report_file = "scope_of_work.md"
            if os.path.exists(report_file):
                with open(report_file, "r", encoding="utf-8") as f:
                    st.session_state['report_md'] = f.read()
                
                progress_bar.progress(100)
                status_text.empty()
                progress_bar.empty()
                
                st.markdown('<div class="status-badge status-success">✅ Successfully Generated</div>', unsafe_allow_html=True)
                st.balloons()
                
            else:
                st.markdown('<div class="status-badge status-warning">⚠️ Output file not found</div>', unsafe_allow_html=True)
                st.warning("Could not find the generated Scope of Work document. Please check the file path.")

        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.markdown('<div class="status-badge status-error">❌ Generation Failed</div>', unsafe_allow_html=True)
            st.error(f"Error during generation: {str(e)}")

# Display generated report
if st.session_state['report_md']:
    st.markdown("---")
    
    # Output controls
    output_col1, output_col2, output_col3 = st.columns([2, 1, 1])
    
    with output_col1:
        st.subheader("📄 Generated Scope of Work Document")
    
    with output_col2:
        if st.button("📋 Copy to Clipboard", help="Copy the generated document"):
            st.success("Document copied to clipboard!")
    
    with output_col3:
        if st.button("🗑️ Clear Output", help="Clear the generated document"):
            st.session_state['report_md'] = ""
            st.rerun()
    
    # Display the document in a styled container
    st.markdown('<div class="output-container">', unsafe_allow_html=True)
    st.markdown(st.session_state['report_md'], unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Download button
    st.download_button(
        label="💾 Download as Markdown",
        data=st.session_state['report_md'],
        file_name=f"scope_of_work_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
        mime="text/markdown",
        use_container_width=True
    )

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6c757d; padding: 2rem;">
    <p>Built with ❤️ using Streamlit and CrewAI • Generate professional documents with AI assistance</p>
</div>
""", unsafe_allow_html=True)