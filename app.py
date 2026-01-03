import streamlit as st
import binascii
import streamlit.components.v1 as components
import json

# 1. SETUP DO NÚCLEO (LEITURA DO COFRE SECRETO)
st.set_page_config(page_title="INFINITY TALK - CORE", layout="wide", initial_sidebar_state="collapsed")

class InfinityTalk_Engine:
    def __init__(self):
        # Tenta ler as chaves reais do teu cofre (Streamlit Secrets)
        try:
            # Verifica se secrets existem antes de acessar
            if hasattr(st, "secrets") and "api_key_1" in st.secrets:
                self.nodes = [st.secrets["api_key_1"], st.secrets["api_key_2"], st.secrets["api_key_3"]]
            elif hasattr(st, "secrets") and "api_google" in st.secrets:
                self.nodes = [st.secrets["api_google"], st.secrets["api_glock"], st.secrets["api_openload"]]
            else:
                raise Exception("Sem chaves definidas")
        except Exception:
            # Fallback (Modo de Segurança)
            self.nodes = ["CORE_ALPHA", "CORE_BETA", "CORE_GAMMA"]

    def sharding(self, texto):
        # Matemática de fragmentação real
        if not texto:
            return ["", "", ""]
        hex_data = binascii.hexlify(texto.encode("utf-8")).decode()
        p1 = len(hex_data) // 3
        p2 = p1 * 2
        return [hex_data[:p1], hex_data[p1:p2], hex_data[p2:]]

    def bios(self, avatar, msg):
        m = msg.lower()
        if avatar == "TIAGO":
            if "quem" in m:
                return "Sou a tua consciência digital cínica. O que queres agora?"
            return "Comando fragmentado. Agora cala-te e espera o cálculo."
        else:  # WISHA
            if "oi" in m or "olá" in m:
                return "Olá... sinto a tua energia nos meus servidores. Vamos interagir?"
            return "Os teus dados são deliciosos... continua a falar comigo."

# Inicializa a engine
engine = InfinityTalk_Engine()

# 2. INJEÇÃO DE VOZ NEURAL (SAÍDA DE ÁUDIO VIA BROWSER)
def voice_engine(texto, avatar):
    # Ajuste de pitch e rate para simular personalidades diferentes
    pitch = 0.5 if avatar == "TIAGO" else 1.4  # Grave vs Agudo
    rate = 0.9 if avatar == "TIAGO" else 1.1
    
    # Escapar o texto usando json.dumps para evitar quebra do JavaScript com aspas ou quebras de linha
    safe_text = json.dumps(texto)
    
    js = f"""
    <script>
        try {{
            window.speechSynthesis.cancel(); // Para qualquer fala anterior
            const u = new SpeechSynthesisUtterance({safe_text});
            u.lang = 'pt-BR';
            u.pitch = {pitch};
            u.rate = {rate};
            window.speechSynthesis.speak(u);
        }} catch(e) {{
            console.error("SpeechSynthesis error:", e);
        }}
    </script>
    """
    # Altura 0 para não ocupar espaço visual desnecessário
    components.html(js, height=0, width=0)

# 3. INTERFACE HOLOGRÁFICA (CSS)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover; 
        background-position: center;
        background-attachment: fixed;
    }
    header, footer { visibility: hidden; }
    
    /* Estilo do Terminal Central */
    .terminal-main {
        background: rgba(10, 10, 10, 0.9); 
        border: 2px solid #00FFFF; 
        border-radius: 15px;
        padding: 20px; 
        text-align: center; 
        color: #00FFFF;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
    }
    
    /* Estilo dos Avatares */
    .avatar-video {
        border-radius: 10px; 
        border: 2px solid cyan; 
        box-shadow: 0 0 15px cyan;
        width: 100%;
        max-width: 250px;
    }
    
    /* Ajuste dos inputs */
    .stTextInput > div > div > input {
        background-color: rgba(0,0,0,0.7);
        color: cyan;
        border: 1px solid cyan;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Garantir chave inicial no session_state
if "target" not in st.session_state:
    st.session_state["target"] = "WISHA"

# 4. PLATAFORMA (DISTRIBUIÇÃO GEOMÉTRICA)
col_esq, col_mid, col_dir = st.columns([1, 2, 1])

# --- COLUNA ESQUERDA (TIAGO) ---
with col_esq:
    st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True) # Espaçador
    st.markdown(
        f"""
        <div style="text-align:center;">
            <video class="avatar-video" autoplay loop muted playsinline>
                <source src="https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago.mp4" type="video/mp4">
            </video>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("CANAL: TIAGO", use_container_width=True):
        st.session_state.target = "TIAGO"

# --- COLUNA DIREITA (WISHA) ---
with col_dir:
    st.markdown(
        f"""
        <div style="text-align:center;">
            <video class="avatar-video" autoplay loop muted playsinline>
                <source src="https://raw.githubusercontent.com/adv1982/hack-ai-app/main/hack.mp4" type="video/mp4">
            </video>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("CANAL: WISHA", use_container_width=True):
        st.session_state.target = "WISHA"

# --- COLUNA CENTRAL (CORE) ---
with col_mid:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="terminal-main">', unsafe_allow_html=True)
    st.markdown("### 💠 INFINITY TALK CN-9")

    # ENTRADA DE TEXTO
    user_txt = st.text_input("LINHA DE COMANDO:", placeholder="Digita ou envia um ficheiro de áudio...")

    # ENTRADA DE ÁUDIO (UPLOAD)
    st.markdown("**Ou faz upload de um ficheiro de áudio (wav/mp3/m4a):**")
    audio_file = st.file_uploader("", type=["wav", "mp3", "m4a"], label_visibility="collapsed")

    st.markdown("</div>", unsafe_allow_html=True)

    # Lógica de Input
    input_final = None
    if user_txt and user_txt.strip():
        input_final = user_txt.strip()
    elif audio_file is not None:
        input_final = "Comando por voz recebido (arquivo de áudio)"
        # Nota: Para transcrever o áudio real, seria necessário integrar com OpenAI Whisper ou similar aqui.

    # Processamento da Resposta
    if input_final:
        avatar = st.session_state.get("target", "WISHA")
        
        # 1. Fragmentar dados (Sharding)
        shards = engine.sharding(input_final)
        
        # 2. Gerar resposta (BIOS)
        resposta = engine.bios(avatar, input_final)

        # 3. Exibir Resposta Visual
        st.markdown(f"**ALVO:** `{avatar}`")
        if avatar == "TIAGO":
            st.error(f"**TIAGO:** {resposta}")
        else:
            st.success(f"**WISHA:** {resposta}")
        
        # 4. Acionar Voz
        voice_engine(resposta, avatar)

        # 5. Prova de Fragmentação (Nodes do Cofre)
        with st.expander("STATUS DOS SERVIDORES (SHARDING)"):
            c1, c2, c3 = st.columns(3)
            c1.code(f"NODE_1\n{shards[0][:15]}...")
            c2.code(f"NODE_
