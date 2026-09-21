import streamlit as st

st.set_page_config(page_title="SPS | About Us", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="custom-header">
    <div class="logo-placeholder">Logo</div>
    <div class="title-container">
        <h1>Special Programme in Science</h1>
        <div class="slogan">Your SPS Slogan Goes Here</div>
    </div>
    <div class="logo-placeholder">SPS 30</div>
</div>
<div class="navbar">
    <a href="/" target="_self">Home</a>
    <a href="/About_Us" target="_self">About Us</a>
</div>

<div class="hero-banner">
    <h1>About Us</h1>
</div>
<div style="padding: 0 10%; text-align: center; font-size: 1.1rem; line-height: 1.6;">
    <p>SPS is a vibrant academic community established to nurture talented students with a strong passion for science.</p>
</div>

<div style="padding: 0 10%;">
    <div class="circuit-container">
        <div class="circuit-node">
            <div class="icon-circle">🧬</div>
            <div class="info-box"><h4>Biology</h4><p>Details about the biology discipline...</p></div>
        </div>
        <div class="circuit-node">
            <div class="icon-circle">🧪</div>
            <div class="info-box"><h4>Chemistry</h4><p>Details about the chemistry discipline...</p></div>
        </div>
    </div>
</div>

<div class="polygon-container reverse">
    <div class="polygon-img"><img src="https://via.placeholder.com/350x350?text=Insert+Image" style="width:100%; height:100%; object-fit:cover;" /></div>
    <div>
        <h3 style="color: var(--sps-blue);">Student Spotlight</h3>
        <p>Parallelogram image style carried over to the subpage.</p>
    </div>
</div>

<div class="footer">
    <div class="footer-col">
        <h4>Quick Links</h4>
        <p>Home</p>
        <p>About Us</p>
        <p>Admissions</p>
    </div>
    <div class="footer-col">
        <h4>Location</h4>
        <p>National University of Singapore</p>
        <p>12 Science Drive 2, Singapore 117549</p>
    </div>
    <div class="footer-col">
        <h4>Contact Us</h4>
        <p>Phone: +65 6516 1234</p>
        <p>Email: sps@nus.edu.sg</p>
    </div>
</div>
""", unsafe_allow_html=True)