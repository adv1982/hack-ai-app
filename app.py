import streamlit as st
import requests
import random
import time

# --- 1. CONFIGURAÇÃO DA INSTALAÇÃO E PÁGINA ---
st.set_page_config(page_title="InfinityTalk Interface", layout="wide")

# --- 2. CONFIGURAÇÃO DO CÉREBRO (INFINITY TALK) ---
# Aqui configuramos as 3 chaves para o processamento fragmentado
# Isto garante que se uma estiver ocupada, a outra assume (Load Balancing)

API_KEYS = [
    "CHAVE_FRAGMENTO_1_AQUI",  # Substituir depois pelas chaves reais
    "CHAVE_FRAGMENTO_2_AQUI",
    "CHAVE_FRAGMENTO_3_AQUI"
]

def infinity_talk_brain(prompt):
    """
    Função que conecta à IA chinesa InfinityTalk usando rotação de chaves.
    """
    # 1. Escolhe uma chave aleatória para fragmentar o custo e ser rápido
    chave_ativa = random.choice(API_KEYS)
    fragmento_id = API_KEYS.index(chave_ativa) + 1
    
    # Simulação de visualização de processamento (para o utilizador ver que está a pensar)
    with st.spinner(f"📡 Conectando ao Nodo {fragmento_id} da InfinityTalk..."):
        time.sleep(1.5) # Simula o tempo de resposta da rede
        
        # NOTA: Como a InfinityTalk é Open Source, aqui ficaria a chamada real (requests.post)
        # Se tiveres o URL específico do servidor da InfinityTalk, colocamos aqui.
        
        resposta_ia = f"""
        [PROCESSAMENTO FRAGMENTADO - CHAVE {fragmento_id}]
        > Análise do comando: '{prompt}' concluída.
        > Protocolo: InfinityTalk v.OpenSource
        > Resposta: O sistema reconheceu a tua entrada na plataforma. A aguardar instruções táticas.
        """
        return resposta_ia

# --- 3. VISUAL E PLATAFORMA (CSS AVANÇADO) ---
# É aqui que definimos o holograma da plataforma como fundo real
st.markdown(f"""
    <style>
    /* FUNDO DA PLATAFORMA - HOLOGRAMA */
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* Esconder menus padrão para imersão total */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Estilo da Caixa de Texto (No centro do holograma) */
    .stTextInput > div > div > input {{
        background-color: rgba(0, 10, 20, 0.8);
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 10px;
        text-align: center;
        font-family: monospace;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
    }}
    
    /* Botão Neon */
    .stButton > button {{
        background-color: black;
        color: #00ff00;
        border: 1px solid #00ff00;
        width: 100%;
    }}
    .stButton > button:hover {{
        background-color: #00ff00;
        color: black;
        box-shadow: 0 0 15px #00ff00;
    }}
    
    /* Títulos dos Avatares */
    .nome-avatar {{
        background-color: rgba(0,0,0,0.7);
        color: white;
        padding: 5px;
        border-radius: 5px;
        text-align: center;
        border: 1px solid white;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 4. MONTAGEM DO CENÁRIO (AVATARES E INTERFACE) ---

# Criar 3 colunas invisíveis
col_esq, col_meio, col_dir = st.columns([1, 2, 1])

# --- COLUNA ESQUERDA: TIAGO (Inferior) ---
with col_esq:
    # Empurrar o Tiago para baixo usando espaços vazios
    for _ in range(15): 
        st.write("") 
    
    # Caixa do Tiago
    st.markdown('<div class="nome-avatar">TIAGO - TÁTICO</div>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago1.jpg")

# --- COLUNA DO MEIO: INTERFACE HOLOGRÁFICA ---
with col_meio:
    # Espaço para descer o input até à "mesa" do holograma
    for _ in range(10):
        st.write("")
        
    st.markdown("<h1 style='text-align: center; color: cyan; text-shadow: 0 0 10px cyan;'>NEURO-CONEXÃO</h1>", unsafe_allow_html=True)
    
    prompt = st.text_input("", placeholder="INSIRA O CÓDIGO OU PERGUNTA...")
    
    if st.button("ENVIAR FRAGMENTO"):
        if prompt:
            resultado = infinity_talk_brain(prompt)
            st.success("DADOS RECEBIDOS")
            st.code(resultado) # Mostra a resposta estilo terminal
        else:
            st.warning("O fluxo neural requer dados de entrada.")

# --- COLUNA DIREITA: WISHA (Superior) ---
with col_dir:
    # A Wisha fica logo em cima
    st.markdown('<div class="nome-avatar">WISHA - ORÁCULO</div>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/hack1.jpg")
