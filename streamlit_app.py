import streamlit as st
from PIL import Image, ImageDraw
import io
import os
from datetime import datetime

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="JGAN Designer - Sports Graphic Design Portfolio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================
css_code = """
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%) !important;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    [data-testid="stMainBlockContainer"] {
        background: transparent !important;
        padding-top: 0 !important;
    }

    /* SCROLLBAR */
    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #0a0a0a;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00d9ff, #ff006e);
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #ff006e, #00d9ff);
    }

    /* HEADINGS */
    h1 {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00d9ff, #ff006e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(0, 217, 255, 0.3);
        letter-spacing: 2px;
        margin-bottom: 10px;
    }

    h2 {
        font-size: 2.5rem;
        color: #00d9ff;
        text-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
        margin-bottom: 30px;
        font-weight: 800;
        border-bottom: 3px solid #ff006e;
        padding-bottom: 15px;
        display: inline-block;
    }

    h3 {
        color: #ffffff;
        font-size: 1.5rem;
        margin-bottom: 15px;
    }

    p {
        line-height: 1.8;
        font-size: 1.1rem;
        color: #e0e0e0;
    }

    /* CONTAINERS */
    .hero-container {
        min-height: 90vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 60px 20px;
        text-align: center;
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.05) 0%, rgba(255, 0, 110, 0.05) 100%);
        border-bottom: 2px solid rgba(0, 217, 255, 0.2);
        box-shadow: 0 20px 60px rgba(0, 217, 255, 0.1);
    }

    .section-container {
        padding: 80px 20px;
        max-width: 1400px;
        margin: 0 auto;
    }

    .card-container {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(0, 217, 255, 0.2);
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(0, 217, 255, 0.1);
    }

    .card-container:hover {
        transform: translateY(-10px);
        border-color: #00d9ff;
        box-shadow: 0 20px 50px rgba(0, 217, 255, 0.3), 0 0 30px rgba(255, 0, 110, 0.2);
        background: rgba(0, 217, 255, 0.05);
    }

    /* SERVICE CARDS */
    .service-card {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.05), rgba(255, 0, 110, 0.05));
        border: 2px solid rgba(0, 217, 255, 0.3);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 217, 255, 0.2), transparent);
        transition: left 0.5s ease;
    }

    .service-card:hover::before {
        left: 100%;
    }

    .service-card:hover {
        transform: translateY(-15px) scale(1.05);
        border-color: #ff006e;
        box-shadow: 0 0 30px rgba(0, 217, 255, 0.4), inset 0 0 30px rgba(255, 0, 110, 0.1);
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.1), rgba(255, 0, 110, 0.1));
    }

    .service-icon {
        font-size: 3rem;
        margin-bottom: 15px;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    /* PORTFOLIO GRID */
    .portfolio-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
        margin: 30px 0;
    }

    .portfolio-item {
        position: relative;
        overflow: hidden;
        border-radius: 15px;
        aspect-ratio: 4/3;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0, 217, 255, 0.2);
        border: 2px solid rgba(0, 217, 255, 0.3);
    }

    .portfolio-item img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.4s ease;
    }

    .portfolio-item:hover img {
        transform: scale(1.15) rotate(2deg);
        filter: brightness(1.1) saturate(1.2);
    }

    .portfolio-item::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.3) 0%, rgba(255, 0, 110, 0.3) 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .portfolio-item:hover::after {
        opacity: 1;
    }

    /* BUTTONS */
    .btn-primary {
        display: inline-block;
        background: linear-gradient(135deg, #00d9ff, #ff006e);
        color: #0a0a0a;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 800;
        font-size: 1.1rem;
        margin: 10px 10px 10px 0;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        cursor: pointer;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.4);
        letter-spacing: 1px;
    }

    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 40px rgba(0, 217, 255, 0.6), 0 0 30px rgba(255, 0, 110, 0.4);
        filter: brightness(1.1);
    }

    .btn-secondary {
        display: inline-block;
        background: transparent;
        color: #00d9ff;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 800;
        font-size: 1.1rem;
        margin: 10px 10px 10px 0;
        transition: all 0.3s ease;
        border: 2px solid #00d9ff;
        cursor: pointer;
        letter-spacing: 1px;
    }

    .btn-secondary:hover {
        background: rgba(0, 217, 255, 0.1);
        transform: translateY(-3px);
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
    }

    /* FOOTER */
    footer {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(255, 0, 110, 0.1) 100%);
        border-top: 2px solid rgba(0, 217, 255, 0.3);
        padding: 40px 20px;
        text-align: center;
        margin-top: 80px;
        color: #b0b0b0;
    }

    /* ANIMATIONS */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes glow {
        0%, 100% {
            text-shadow: 0 0 10px rgba(0, 217, 255, 0.5);
        }
        50% {
            text-shadow: 0 0 30px rgba(0, 217, 255, 0.8), 0 0 50px rgba(255, 0, 110, 0.5);
        }
    }

    .glow-text {
        animation: glow 3s ease-in-out infinite;
    }

    /* RESPONSIVE */
    @media (max-width: 768px) {
        h1 {
            font-size: 2.5rem;
        }
        
        h2 {
            font-size: 1.8rem;
        }

        .hero-container {
            min-height: 60vh;
            padding: 40px 20px;
        }

        .section-container {
            padding: 40px 20px;
        }

        .portfolio-grid {
            grid-template-columns: 1fr;
        }

        .service-card {
            padding: 20px;
        }
    }
</style>
"""

st.markdown(css_code, unsafe_allow_html=True)

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def create_placeholder_image(width=400, height=300, text="Imagem"):
    """Cria uma imagem placeholder com gradiente"""
    img = Image.new('RGB', (width, height), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Gradiente
    for y in range(height):
        ratio = y / height
        r = int(10 + (0 * ratio))
        g = int(26 + (217 * ratio))
        b = int(46 + (255 * ratio))
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))
    
    # Texto
    text_bbox = draw.textbbox((0, 0), text)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    
    draw.text((text_x, text_y), text, fill=(0, 217, 255), font=None)
    
    return img

def load_image(file_path):
    """Carrega uma imagem ou retorna placeholder"""
    if os.path.exists(file_path):
        try:
            return Image.open(file_path)
        except:
            return create_placeholder_image(text=file_path)
    return create_placeholder_image(text=file_path)

# ============================================================================
# HERO SECTION
# ============================================================================
hero_col1, hero_col2 = st.columns([1, 1])

with hero_col1:
    st.markdown("""
    <div class="hero-container" style="text-align: left;">
        <div>
            <h1 style="text-align: left; margin-bottom: 20px;">🎨 JGAN DESIGNER</h1>
            <p style="font-size: 1.8rem; color: #00d9ff; margin-bottom: 20px; font-weight: 600;">SPORTS GRAPHIC DESIGNER</p>
            <p style="font-size: 1.2rem; color: #e0e0e0; line-height: 1.6; margin-bottom: 30px;">
                Transformando visões em arte visual impactante. Design esportivo de alta performance para atletas, times e marcas.
            </p>
            <div style="margin-top: 30px;">
                <a href="https://wa.me/558396851338" class="btn-primary" style="display: inline-block;">💬 WHATSAPP</a>
                <a href="https://www.instagram.com/jgan.designer/" class="btn-primary" style="display: inline-block;">📸 INSTAGRAM</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with hero_col2:
    try:
        profile_img = load_image("minhafoto.png")
        st.image(profile_img, use_column_width=True, caption=None)
    except:
        st.image(create_placeholder_image(400, 500, "minhafoto.png"), use_column_width=True)

# ============================================================================
# ABOUT SECTION
# ============================================================================
st.markdown("""
<div class="section-container">
    <h2>👋 SOBRE MIM</h2>
    <div class="card-container">
        <p>
            Me chamo <strong>Gabriel Alves</strong>, conhecido como <strong>JGAN</strong>. Sou designer esportivo especializado em 
            <strong>artes para futebol, vôlei, basquete, posters esportivos, social media, wallpapers e matchdays</strong>. 
        </p>
        <p style="margin-top: 20px;">
            Atendo clientes do Brasil e exterior, criando conteúdo visual de alta qualidade que transcende fronteiras. 
            Meu objetivo é elevar sua marca ou projeto esportivo para o próximo nível com design inovador e impactante.
        </p>
        <p style="margin-top: 20px; color: #00d9ff;">
            💡 <strong>Diferencial:</strong> Combinação de criatividade, técnica profissional e compreensão profunda do universo esportivo.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SERVICES SECTION
# ============================================================================
st.markdown('<div class="section-container"><h2>💼 SERVIÇOS</h2></div>', unsafe_allow_html=True)

services = [
    {"icon": "⚽", "title": "Matchday", "desc": "Artes incríveis para dias de jogo"},
    {"icon": "📸", "title": "Poster Esportivo", "desc": "Pôsteres de alta performance"},
    {"icon": "📱", "title": "Social Media", "desc": "Conteúdo otimizado para redes"},
    {"icon": "🎬", "title": "Thumbs", "desc": "Thumbnails impactantes e virais"},
    {"icon": "🖼️", "title": "Wallpapers", "desc": "Fundos premium para desktops"},
    {"icon": "🎨", "title": "Identidade Visual", "desc": "Branding completo para sua marca"},
]

cols = st.columns(3)
for idx, service in enumerate(services):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{service['icon']}</div>
            <h3>{service['title']}</h3>
            <p>{service['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PORTFOLIO SECTION
# ============================================================================
st.markdown("""
<div class="section-container">
    <h2>🖼️ PORTFÓLIO</h2>
</div>
""", unsafe_allow_html=True)

portfolio_images = ["arte1.png", "arte2.png", "arte3.png", "arte4.png", "arte5.png", "arte6.png"]

cols = st.columns(3)
for idx, img_name in enumerate(portfolio_images):
    with cols[idx % 3]:
        try:
            portfolio_img = load_image(img_name)
            st.image(portfolio_img, use_column_width=True, caption=f"Trabalho {idx+1}")
        except:
            st.image(create_placeholder_image(400, 300, img_name), use_column_width=True, caption=f"Trabalho {idx+1}")

# ============================================================================
# CONTACT SECTION
# ============================================================================
st.markdown("""
<div class="section-container">
    <h2>📞 ENTRE EM CONTATO</h2>
    <div class="card-container" style="text-align: center;">
        <p style="font-size: 1.3rem; margin-bottom: 30px;">
            Pronto para elevar seu projeto? Vamos conversar!
        </p>
        <div>
            <a href="https://wa.me/558396851338" class="btn-primary">💬 ENVIAR MENSAGEM NO WHATSAPP</a>
            <a href="https://www.instagram.com/jgan.designer/" class="btn-primary">📸 SEGUIR NO INSTAGRAM</a>
            <a href="mailto:gabriel@jgandesigner.com" class="btn-primary">📧 ENVIAR EMAIL</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
<footer>
    <p>© 2026 - JGAN Designer | Sports Graphic Design | Brazil 🇧🇷</p>
    <p style="margin-top: 10px; color: #808080;">Transformando visões em arte visual profissional</p>
</footer>
""", unsafe_allow_html=True)

# ============================================================================
# HIDDEN STREAMLIT CUSTOMIZATION
# ============================================================================
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_container {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
