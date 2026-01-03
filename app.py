import streamlit as st
import random
import time

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="InfinityTalk Interface", layout="wide")

# --- 2. SISTEMA DE CHAVES CODIFICADAS (SEGURANÇA) ---
# O sistema tenta buscar as chaves reais aos "Segredos" da Nuvem.
# Se não encontrar, usa chaves encriptadas de simulação para manter a plataforma online.

try:
    # Tenta carregar as chaves reais configuradas no Streamlit Cloud
    API_KEYS = [
        st.secrets["api_key_1"],
        st.secrets["api_key_2"],
        st.secrets["api_key_3"]
    ]
    STATUS_SISTEMA = "🟢 CONEXÃO REAL (SECURE)"
except:
    # Se não houver chaves reais, usa chaves de simulação (Mockup)
    API_KEYS = [
        "ENC_X982_NODE_ALPHA",
        "ENC_Y112_NODE_BETA",
        "ENC_Z774_NODE_GAMMA"
    ]
    STATUS_SISTEMA = "🟡 MODO SIMULAÇÃO (GHOST PROTOCOL)"

def infinity_talk_brain(prompt):
    """
    Processador Neural Fragmentado
    """
    # Balanceamento de Carga: Escolhe uma chave aleatória
    chave_ativa = random.choice(API_KEYS)
    
    # Simula o "handshake" com o servidor chinês
    with st.spinner(f"📡 A negociar com Nodo {chave_ativa[-5:]}..."):
        time.sleep(2.0) # Tempo de latência da rede neural
        
        # Resposta da IA (Simulada para demonstração)
        return f"""
        > [PROTOCOLO INFINITY: {STATUS_SISTEMA}]
        > CHAVE USADA: *******{chave_ativa[-4:]}
        > COMANDO: "{prompt}"
        > ANÁLISE: Padrão reconhecido. Acesso autorizado à base de conhecimento.
        > RESPOSTA: O sistema está operacional. Aguardando input tático complexo.
        """

# --- 3. VISUAL HOLOGRÁFICO (CSS) ---
st.markdown(f"""
    <style>
    /* FUNDO - PLATAFORMA */
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* REMOVER BARRA BRANCA SUPERIOR */
    header {{visibility: hidden;}}
    
    /* INPUT ESTILO TERMINAL */
    .stTextInput > div > div > input {{
        background-color: rgba(0, 0, 0, 0.8);
        color: #00ff00;
        border: 1px solid #00ff00;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }}
    
    /* BOTÃO DE ATIVAÇÃO */
    .stButton > button {{
        background-color: #000000;
        color: #00ffff;
        border: 1px solid #00ffff;
        width: 100%;
        font-weight: bold;
    }}
    .stButton > button:hover {{
        box-shadow: 0 0 20px #00ffff;
        color: white;
    }}
    
    /* TEXTO DOS AVATARES */
    .label-avatar {{
        background-color: rgba(0,0,0,0.6);
        color: white; 
        padding: 5px; 
        border-radius: 5px; 
        text-align: center;
        font-family: sans-serif;
        font-size: 12px;
        letter-spacing: 2px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 4. LAYOUT (GRELHA DE POSICIONAMENTO) ---

col_esq, col_meio, col_dir = st.columns([1, 2, 1])

# --- AVATAR TIAGO (ESQUERDA EM BAIXO) ---
with col_esq:
    for _ in range(14): st.write("") # Empurrar para baixo
    st.markdown('<div class="label-avatar">TIAGO [OPERADOR]</div>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago1.jpg")

# --- INTERFACE CENTRAL (HOLOGRAMA) ---
with col_meio:
    for _ in range(9): st.write("") # Empurrar para o centro do vidro
    
    st.markdown("<h2 style='text-align: center; color: white; text-shadow: 0 0 10px #00ffff;'>INFINITY LINK</h2>", unsafe_allow_html=True)
    
    user_input = st.text_input("", placeholder="> INSERIR COMANDO...")
    
    if st.button("EXECUTAR FRAGMENTO"):
        if user_input:
            resposta = infinity_talk_brain(user_input)
            st.success("DADOS RECEBIDOS")
            st.code(resposta, language="json")
        else:
            st.error("ERRO: FL
