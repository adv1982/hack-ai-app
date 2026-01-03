import streamlit as st
import random
import time

# --- 1. CONFIGURAÇÃO OBRIGATÓRIA (PRIMEIRA LINHA) ---
st.set_page_config(page_title="InfinityTalk Interface", layout="wide")

# --- 2. FORÇAR O VISUAL HOLOGRÁFICO (CSS AVANÇADO) ---
# Este bloco obriga o navegador a substituir o fundo preto pela tua imagem
st.markdown(f"""
    <style>
    /* 1. FUNDO GERAL - APLICADO A TUDO */
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* 2. REMOVER O FUNDO PRETO PADRÃO DOS MENUS */
    header {{visibility: hidden;}}
    .css-1dp5vir {{background-image: none;}}
    
    /* 3. CAIXA DE TEXTO CENTRAL (ESTILO NEON) */
    .stTextInput > div > div > input {{
        background-color: rgba(0, 10, 20, 0.8);
        color: cyan; 
        border: 2px solid cyan;
        text-align: center;
        font-size: 20px;
        border-radius: 10px;
        box-shadow: 0 0 15px cyan;
    }}

    /* 4. BOTÃO DE AÇÃO */
    .stButton > button {{
        background-color: #000000;
        color: cyan;
        border: 1px solid cyan;
        font-weight: bold;
        text-transform: uppercase;
        width: 100%;
        transition: 0.3s;
    }}
    .stButton > button:hover {{
        background-color: cyan;
        color: black;
        box-shadow: 0 0 20px cyan;
    }}
    
    /* 5. TAGS DOS NOMES (Tiago e Wisha) */
    .name-tag {{
        background-color: black;
        color: #00ff00;
        padding: 5px;
        text-align: center;
        border: 1px solid #00ff00;
        font-family: monospace;
        margin-bottom: 5px;
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 3. CONEXÃO COM O COFRE (SECRETS) ---
try:
    # Tenta ler as chaves reais que guardaste
    chaves = [st.secrets["api_key_1"], st.secrets["api_key_2"], st.secrets["api_key_3"]]
    sistema_status = "ONLINE"
except:
    # Se der erro, não quebra o site (Modo de Segurança)
    chaves = ["DEMO_KEY_001"]
    sistema_status = "MODO_DEMO"

# --- 4. CÉREBRO DA IA (INFINITY TALK) ---
def processar_comando(comando):
    chave_usada = random.choice(chaves)
    # Simula o tempo de "pensar" da IA
    with st.spinner(f"📡 A acessar servidor chinês via {chave_usada[:8]}..."):
        time.sleep(2.5) 
    
    return f"""
    >>> PROTOCOLO INFINITY: ATIVO
    >>> ROTA SEGURA: {chave_usada}
    >>> COMANDO: "{comando}"
    >>> RESPOSTA: Acesso validado. O sistema aguarda instruções complexas.
    """

# --- 5. LAYOUT DA TELA (GRELHA) ---

# Criamos 3 colunas para organizar: Esquerda (Tiago), Centro (Chat), Direita (Wisha)
col_esq, col_centro, col_dir = st.columns([1, 3, 1])

# COLUNA ESQUERDA: TIAGO
with col_esq:
    for _ in range(15): st.write("") # Empurra para baixo
    st.markdown('<div class="name-tag">TIAGO [ADMIN]</div>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago1.jpg")

# COLUNA CENTRAL: COMANDOS
with col_centro:
    for _ in range(10): st.write("") # Empurra para o centro do vidro do holograma
    
    st.markdown("<h2 style='text-align: center; color: white; text-shadow: 0 0 10px cyan;'>INFINITY TALK v2.0</h2>", unsafe_allow_html=True)
    
    comando = st.text_input("", placeholder="DIGITE O COMANDO AQUI...")
    
    if st.button("ENVIAR DADOS >>"):
        if comando:
            resultado = processar_comando(comando)
            st.code(resultado, language="yaml")

# COLUNA DIREITA: WISHA
with col_dir:
    st.markdown('<div class="name-tag">WISHA [IA]</div>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/hack1.jpg")
