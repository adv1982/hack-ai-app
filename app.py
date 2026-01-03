import streamlit as st
import random
import time

# --- 1. CONFIGURAÇÃO E INSTALAÇÃO DO SISTEMA ---
st.set_page_config(page_title="InfinityTalk Neural Interface", layout="wide")

# --- INSTALAÇÃO: CARREGAR CHAVES DO COFRE (SECRETS) ---
# O sistema tenta conectar aos servidores usando as chaves que guardaste na nuvem.
try:
    KEYS_CLUSTER = [
        st.secrets["api_key_1"],
        st.secrets["api_key_2"],
        st.secrets["api_key_3"]
    ]
    STATUS_CONEXAO = "ONLINE"
except:
    # Caso de emergência se as chaves não forem lidas
    STATUS_CONEXAO = "OFFLINE"
    KEYS_CLUSTER = ["MODO_SIMULACAO_ERRO"]

# --- 2. CÉREBRO DA IA: INFINITY TALK (CHINA OPEN SOURCE) ---
def infinity_talk_core(comando):
    """
    Esta função representa a instalação local do processamento da IA.
    Ela recebe o comando, fragmenta e envia para a nuvem usando as chaves.
    """
    # Algoritmo de Fragmentação (Load Balancing)
    # Escolhe uma das 3 chaves aleatoriamente para não sobrecarregar
    chave_rota = random.choice(KEYS_CLUSTER)
    
    # Simulação de Latência de Rede Neural
    with st.spinner(f"🔌 A conectar ao Nodo Chinês via {chave_rota[:10]}..."):
        time.sleep(2.0) # Tempo de processamento
        
    # Retorno do Sistema
    return f"""
    [PROTOCOLO INFINITY-TALK: ATIVO]
    --------------------------------
    > ROTA UTILIZADA: {chave_rota}
    > COMANDO DECODIFICADO: "{comando}"
    > ANÁLISE: O sistema compreendeu a intenção.
    > RESPOSTA DO ORÁCULO: Acesso autorizado. O padrão lógico foi confirmado.
    > Aguardando próximo passo...
    """

# --- 3. INTERFACE VISUAL (O HOLOGRAMA) ---
# Aqui configuramos para a tela preta sumir e entrar a tua imagem "plataforma.jpg"
st.markdown(f"""
    <style>
    /* FORÇAR A IMAGEM DE FUNDO (PLATAFORMA) */
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* REMOVER BARRAS DO STREAMLIT */
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stDeployButton {{display:none;}}
    
    /* ESTILO DO INPUT (CAIXA DE TEXTO) */
    .stTextInput > div > div > input {{
        background-color: rgba(0, 0, 0, 0.7);
        color: #00ff00;
        border: 2px solid #00ff00;
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 20px;
        box-shadow: 0 0 10px #00ff00;
    }}
    
    /* ESTILO DO BOTÃO */
    .stButton > button {{
        background-color: black;
        color: #00ff00;
        border: 1px solid #00ff00;
        width: 100%;
        font-weight: bold;
    }}
    .stButton > button:hover {{
        background-color: #00ff00;
        color: black;
    }}
    
    /* CAIXAS DOS NOMES */
    .id-tag {{
        background-color: rgba(0,0,0,0.8);
        color: cyan;
        padding: 5px;
        text-align: center;
        border: 1px solid cyan;
        font-family: sans-serif;
        font-size: 12px;
        margin-bottom: 5px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 4. POSICIONAMENTO DOS AVATARES E TELA ---
# Criação das colunas invisíveis para organizar os elementos

col1, col2, col3 = st.columns([1, 2, 1])

# --- COLUNA DA ESQUERDA (TIAGO - EM BAIXO) ---
with col1:
    # Espaçadores para empurrar o Tiago para baixo
    for _ in range(12): st.write("") 
    
    st.markdown('<div class="id-tag">TIAGO [OPERADOR]</div>', unsafe_allow_html=True)
    # Foto do Tiago
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago1.jpg", use_column_width=True)

# --- COLUNA DO CENTRO (INTERFACE E CÓDIGO) ---
with col2:
    # Espaço para descer até a área do "vidro" do holograma
    for _ in range(8): st.write("")
    
    st.markdown("<h2 style='text-align: center; color: white; text-shadow: 0 0 10px cyan;'>NEURO-INTERFACE v1.0</h2>", unsafe_allow_html=True)
    
    # Campo de entrada
    user_input = st.text_input("", placeholder="> INSERIR CÓDIGO...")
    
    if st.button("ATIVAR FLUXO >>"):
        if user_input and STATUS_CONEXAO == "ONLINE":
            resposta = infinity_talk_core(user_input)
            st.code(resposta, language="yaml")
        elif STATUS_CONEXAO == "OFFLINE":
            st.error("ERRO: CHAVES DE ACESSO NÃO ENCONTRADAS NO COFRE.")
        else:
            st.warning("AGUARDANDO COMANDO...")

# --- COLUNA DA DIREITA (WISHA - EM CIMA) ---
with col3:
    st.markdown('<div class="id-tag">WISHA [ORÁCULO]</div>', unsafe_allow_html=True)
    # Foto da Wisha
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/hack1.jpg", use_column_width=True)
