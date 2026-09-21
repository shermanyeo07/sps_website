import streamlit as st

st.set_page_config(page_title="SPS | Home", layout="wide")

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

<div class="hero-grid">
    <div class="quarter" style="background-image: url('https://images.unsplash.com/photo-1532094349884-543bc11b234d');"><h2>Quarter 1 Text</h2></div>
    <div class="quarter" style="background-image: url('https://images.unsplash.com/photo-1518152006812-edab29b069ac');"><h2>Quarter 2 Text</h2></div>
    <div class="quarter" style="background-image: url('https://images.unsplash.com/photo-1507413245164-6160d8298b31');"><h2>Quarter 3 Text</h2></div>
    <div class="quarter" style="background-image: url('https://images.unsplash.com/photo-1503694978374-8a2fa686963a');"><h2>Quarter 4 Text</h2></div>
    <div class="center-logo">SPS LOGO<br>IMAGE HERE</div>
</div>

<div class="polygon-container">
    <div class="polygon-img"><img src="https://via.placeholder.com/350x350?text=Insert+Image" style="width:100%; height:100%; object-fit:cover;" /></div>
    <div>
        <h3 style="color: var(--sps-gold);">More Home Page Content</h3>
        <p>Text for the dynamic focus section on the main page goes here.</p>
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