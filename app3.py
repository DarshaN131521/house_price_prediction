import streamlit as st
import pandas as pd
import joblib
import os
from datetime import date



# ===========================================================
# PAGE CONFIG
# ===========================================================
st.set_page_config(
    page_title="Architectural Valuation System",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================================================
# THEME / CSS  ("Architectural Blueprint" design system)
# ===========================================================
NAVY_BG     = "#0B2E4F"
PANEL_NAVY  = "#0E3A5C"
LINE_CYAN   = "#6FA8C9"
PAPER_CREAM = "#F4F1E8"
BRASS       = "#C9A227"
INK         = "#1B2B3A"
MUTE_SLATE  = "#3B5772"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

/* Blueprint grid background */
.stApp {{
    background-color: {NAVY_BG};
    background-image:
        linear-gradient(rgba(111,168,201,0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(111,168,201,0.08) 1px, transparent 1px),
        linear-gradient(rgba(111,168,201,0.14) 1px, transparent 1px),
        linear-gradient(90deg, rgba(111,168,201,0.14) 1px, transparent 1px);
    background-size: 20px 20px, 20px 20px, 100px 100px, 100px 100px;
}}

/* Sidebar = "specification sheet" */
section[data-testid="stSidebar"] {{
    background-color: {PANEL_NAVY};
    border-right: 2px solid {LINE_CYAN}55;
}}
section[data-testid="stSidebar"] * {{
    color: {PAPER_CREAM} !important;
}}
section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {{
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-size: 0.95rem !important;
    color: {LINE_CYAN} !important;
    border-bottom: 1px dashed {LINE_CYAN}55;
    padding-bottom: 6px;
}}

/* Title block */
.eyebrow {{
    font-family: 'JetBrains Mono', monospace;
    color: {LINE_CYAN};
    font-size: 0.78rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    border: 1px solid {LINE_CYAN}55;
    display: inline-block;
    padding: 4px 12px;
    border-radius: 2px;
    margin-right: 8px;
}}
.title-main {{
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 2.4rem;
    color: {PAPER_CREAM};
    letter-spacing: 0.01em;
    margin: 14px 0 2px 0;
}}
.subtitle {{
    color: {LINE_CYAN};
    font-size: 1rem;
    font-family: 'Inter', sans-serif;
    margin-bottom: 18px;
}}

/* Paper spec-sheet cards */
.paper-card {{
    background-color: {PAPER_CREAM};
    color: {INK};
    border-radius: 4px;
    padding: 22px 26px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.28);
    border-top: 4px solid {BRASS};
}}
.paper-card h3, .paper-card h4 {{
    font-family: 'Space Grotesk', sans-serif;
    color: {INK};
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: 0.95rem;
    margin-bottom: 10px;
}}

/* Brass valuation plaque */
.plaque {{
    background: linear-gradient(145deg, #dcb948, {BRASS} 55%, #a8811b);
    border-radius: 6px;
    padding: 26px 30px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.35);
    border: 1px solid #8a6a15;
}}
.plaque .label {{
    font-family: 'JetBrains Mono', monospace;
    color: #3a2c05;
    letter-spacing: 0.18em;
    font-size: 0.78rem;
    text-transform: uppercase;
}}
.plaque .value {{
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 2.6rem;
    color: #241b03;
    margin: 6px 0 0 0;
}}

/* Buttons */
.stButton > button {{
    font-family: 'Space Grotesk', sans-serif;
    background-color: {BRASS};
    color: {INK};
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border: none;
    border-radius: 3px;
    padding: 10px 18px;
    transition: all 0.15s ease;
}}
.stButton > button:hover {{
    background-color: #dcb948;
    color: #000;
    box-shadow: 0 4px 14px rgba(201,162,39,0.4);
}}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    gap: 4px;
}}
.stTabs [data-baseweb="tab"] {{
    background-color: {PANEL_NAVY};
    color: {LINE_CYAN};
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-size: 0.85rem;
    border-radius: 3px 3px 0 0;
    padding: 8px 18px;
}}
.stTabs [aria-selected="true"] {{
    background-color: {BRASS} !important;
    color: {INK} !important;
}}

/* Dimension callout footer */
.stamp {{
    font-family: 'JetBrains Mono', monospace;
    color: {LINE_CYAN}aa;
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    border-top: 1px dashed {LINE_CYAN}55;
    padding-top: 10px;
    margin-top: 30px;
    display: flex;
    justify-content: space-between;
}}
</style>
""", unsafe_allow_html=True)

# ===========================================================
# HEADER / TITLE BLOCK
# ===========================================================
st.markdown(f"""
<span class="eyebrow">DWG NO. 0147</span>
<span class="eyebrow">SCALE 1:100</span>
<span class="eyebrow">REV A</span>
<div class="title-main">Architectural Valuation System</div>
<div class="subtitle">Structural specification → predicted market value, via Linear Regression</div>
""", unsafe_allow_html=True)

# ===========================================================
# LOAD MODEL & FEATURES
# ===========================================================
MODEL_PATH = "house_price_model.pkl"
FEATURES_PATH = "feature_names.pkl"

@st.cache_resource
def load_artifacts():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(FEATURES_PATH):
        return None, None
    model = joblib.load(MODEL_PATH)
    feature_names = joblib.load(FEATURES_PATH)
    return model, feature_names

model, feature_names = load_artifacts()

if model is None:
    st.error(
        f"Could not find `{MODEL_PATH}` and/or `{FEATURES_PATH}` in this folder. "
        "Place both files alongside app.py before running."
    )
    st.stop()

# ===========================================================
# SIDEBAR — "SPECIFICATION SHEET"
# ===========================================================
st.sidebar.markdown("## Specification Sheet")

st.sidebar.markdown("### Dimensions")
area = st.sidebar.number_input("Area (sq ft)", min_value=100, max_value=20000, value=3000, step=50)
bedrooms = st.sidebar.number_input("Bedrooms", min_value=1, max_value=10, value=3, step=1)
bathrooms = st.sidebar.number_input("Bathrooms", min_value=1, max_value=10, value=2, step=1)
stories = st.sidebar.number_input("Stories", min_value=1, max_value=5, value=2, step=1)
parking = st.sidebar.number_input("Parking spaces", min_value=0, max_value=5, value=1, step=1)

st.sidebar.markdown("### Features")
mainroad = st.sidebar.selectbox("Main road access", ["yes", "no"])
guestroom = st.sidebar.selectbox("Guest room", ["yes", "no"])
basement = st.sidebar.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.sidebar.selectbox("Hot water heating", ["yes", "no"])
airconditioning = st.sidebar.selectbox("Air conditioning", ["yes", "no"])
prefarea = st.sidebar.selectbox("Preferred area", ["yes", "no"])

st.sidebar.markdown("### Finish")
furnishingstatus = st.sidebar.selectbox(
    "Furnishing status",
    ["furnished", "semi-furnished", "unfurnished"]
)

predict_clicked = st.sidebar.button("Generate Valuation", use_container_width=True)

# ===========================================================
# PREPROCESSING (mirrors training pipeline exactly)
# ===========================================================
def build_feature_row(feature_names):
    yes_no_map = {"yes": 1, "no": 0}
    row = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": yes_no_map[mainroad],
        "guestroom": yes_no_map[guestroom],
        "basement": yes_no_map[basement],
        "hotwaterheating": yes_no_map[hotwaterheating],
        "airconditioning": yes_no_map[airconditioning],
        "parking": parking,
        "prefarea": yes_no_map[prefarea],
        "furnishingstatus_semi-furnished": 1 if furnishingstatus == "semi-furnished" else 0,
        "furnishingstatus_unfurnished": 1 if furnishingstatus == "unfurnished" else 0,
    }
    input_df = pd.DataFrame([row])
    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0
    return input_df[feature_names]

input_df = build_feature_row(feature_names)

# ===========================================================
# SIGNATURE ELEMENT — live blueprint floor-plan schematic
# ===========================================================
def c(active):
    return BRASS if active else MUTE_SLATE

def blueprint_svg():
    mr  = c(mainroad == "yes")
    gr  = c(guestroom == "yes")
    bsm = c(basement == "yes")
    hw  = c(hotwaterheating == "yes")
    ac  = c(airconditioning == "yes")
    pa  = c(prefarea == "yes")
    park = c(parking > 0)
    furn_dashes = {"furnished": "0", "semi-furnished": "6,4", "unfurnished": "2,6"}[furnishingstatus]

    return f"""
    <svg viewBox="0 0 640 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
      <!-- basement hatch (underlay) -->
      <rect x="70" y="70" width="360" height="220" fill="none" stroke="{bsm}" stroke-width="6"
            stroke-dasharray="4,6" opacity="0.55"/>
      <text x="80" y="63" font-family="JetBrains Mono" font-size="11" fill="{bsm}">BASEMENT</text>

      <!-- outer walls -->
      <rect x="90" y="90" width="320" height="180" fill="none" stroke="{PAPER_CREAM}" stroke-width="3"/>

      <!-- room divisions -->
      <line x1="230" y1="90" x2="230" y2="270" stroke="{LINE_CYAN}" stroke-width="1.5"/>
      <line x1="90" y1="180" x2="230" y2="180" stroke="{LINE_CYAN}" stroke-width="1.5"/>
      <line x1="230" y1="200" x2="410" y2="200" stroke="{LINE_CYAN}" stroke-width="1.5"/>

      <!-- living room (furnishing indicated by dashed furniture outline) -->
      <rect x="105" y="105" width="110" height="60" fill="none" stroke="{PAPER_CREAM}"
            stroke-width="1.5" stroke-dasharray="{furn_dashes}"/>
      <text x="110" y="125" font-family="JetBrains Mono" font-size="10" fill="{PAPER_CREAM}">LIVING</text>

      <!-- bedroom -->
      <text x="110" y="200" font-family="JetBrains Mono" font-size="10" fill="{PAPER_CREAM}">BED x{bedrooms}</text>
      <rect x="105" y="205" width="110" height="45" fill="none" stroke="{PAPER_CREAM}"
            stroke-width="1.5" stroke-dasharray="{furn_dashes}"/>

      <!-- guestroom -->
      <rect x="245" y="105" width="150" height="80" fill="none" stroke="{gr}" stroke-width="2"/>
      <text x="250" y="125" font-family="JetBrains Mono" font-size="10" fill="{gr}">GUEST ROOM</text>

      <!-- bathroom -->
      <text x="245" y="235" font-family="JetBrains Mono" font-size="10" fill="{PAPER_CREAM}">BATH x{bathrooms}</text>
      <rect x="245" y="215" width="150" height="40" fill="none" stroke="{PAPER_CREAM}" stroke-width="1.5"/>

      <!-- stories marker -->
      <text x="330" y="90" font-family="JetBrains Mono" font-size="10" fill="{LINE_CYAN}">{stories} STORY</text>

      <!-- garage / parking -->
      <rect x="440" y="150" width="90" height="70" fill="none" stroke="{park}" stroke-width="2"/>
      <text x="448" y="145" font-family="JetBrains Mono" font-size="10" fill="{park}">PARKING x{parking}</text>

      <!-- AC unit -->
      <rect x="440" y="90" width="30" height="20" fill="{ac}" opacity="0.85"/>
      <text x="475" y="105" font-family="JetBrains Mono" font-size="9" fill="{ac}">A/C</text>

      <!-- hot water heater -->
      <circle cx="530" cy="100" r="12" fill="none" stroke="{hw}" stroke-width="2.5"/>
      <text x="500" y="80" font-family="JetBrains Mono" font-size="9" fill="{hw}">WATER HTG</text>

      <!-- prefarea flag -->
      <line x1="560" y1="230" x2="560" y2="270" stroke="{pa}" stroke-width="2"/>
      <polygon points="560,230 590,240 560,250" fill="{pa}"/>
      <text x="540" y="285" font-family="JetBrains Mono" font-size="9" fill="{pa}">PREF. AREA</text>

      <!-- main road -->
      <rect x="0" y="330" width="640" height="18" fill="none" stroke="{mr}" stroke-width="2"/>
      <line x1="0" y1="339" x2="640" y2="339" stroke="{mr}" stroke-width="1" stroke-dasharray="10,8"/>
      <text x="10" y="365" font-family="JetBrains Mono" font-size="10" fill="{mr}">MAIN ROAD ACCESS</text>
    </svg>
    """

st.markdown('<div class="paper-card">', unsafe_allow_html=True)
st.markdown("#### Site Plan — Live Schematic")
st.markdown(blueprint_svg(), unsafe_allow_html=True)
st.markdown(
    f'<p style="font-size:0.8rem;color:{MUTE_SLATE};margin-top:8px;">'
    'Brass = feature active · Slate = feature inactive · Dashes on Living/Bed = furnishing level'
    '</p>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ===========================================================
# TABS — Valuation / Model Insights
# ===========================================================
tab1, tab2 = st.tabs(["🏠  Valuation", "📐  Model Insights"])

with tab1:
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<div class="paper-card">', unsafe_allow_html=True)
        st.markdown("#### Input Specification")
        st.dataframe(input_df.T.rename(columns={0: "Value"}), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if predict_clicked:
            prediction = model.predict(input_df)[0]
            st.markdown(f"""
            <div class="plaque">
                <div class="label">Estimated Market Value</div>
                <div class="value">₹ {prediction:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="plaque" style="opacity:0.5;">
                <div class="label">Estimated Market Value</div>
                <div class="value">— — —</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(
                f'<p style="color:{PAPER_CREAM};font-size:0.85rem;margin-top:10px;">'
                'Set your specification in the sidebar, then press <b>Generate Valuation</b>.'
                '</p>',
                unsafe_allow_html=True
            )

with tab2:
    st.markdown('<div class="paper-card">', unsafe_allow_html=True)
    st.markdown("#### Feature Coefficients — Linear Regression")
    st.markdown(
        f'<p style="font-size:0.85rem;color:{MUTE_SLATE};">'
        'How each unit of a feature shifts the predicted price, holding others constant.'
        '</p>',
        unsafe_allow_html=True
    )

    coef_df = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": model.coef_
    }).sort_values("Coefficient")

    colors = [BRASS if v >= 0 else MUTE_SLATE for v in coef_df["Coefficient"]]

    fig = go.Figure(go.Bar(
        x=coef_df["Coefficient"],
        y=coef_df["Feature"],
        orientation="h",
        marker_color=colors,
        marker_line_color=INK,
        marker_line_width=0.5,
    ))
    fig.update_layout(
        plot_bgcolor=PAPER_CREAM,
        paper_bgcolor=PAPER_CREAM,
        font=dict(family="JetBrains Mono", color=INK, size=11),
        margin=dict(l=10, r=10, t=10, b=10),
        height=420,
        xaxis=dict(gridcolor="#00000022", zerolinecolor=INK),
        yaxis=dict(gridcolor="#00000000"),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ===========================================================
# FOOTER — drafting stamp
# ===========================================================
st.markdown(f"""
<div class="stamp">
    <span>MODEL: LINEAR REGRESSION</span>
    <span>FEATURES: {len(feature_names)}</span>
    <span>GENERATED: {date.today().isoformat()}</span>
</div>
""", unsafe_allow_html=True)