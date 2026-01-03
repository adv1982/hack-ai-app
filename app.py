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
            self.nodes = [st.secrets["api_key_1"], st.secrets["api_key_2"], st.secrets["api_key_3"]]
        except Exception:
            # Fallback para as chaves Google/Glock/Openload se os nomes forem diferentes
            try:
                self.nodes = [st.secrets["api_google"], st.secrets["api_glock"], st.secrets["api_openload"]]
            except Exception:
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

engine = InfinityTalk_Engine()

# 2. INJEÇÃO DE VOZ NEURAL (SAÍDA DE ÁUDIO)
def voice_engine(texto, avatar):
    # cuidado: SpeechSynthesis é do browser, comportamento pode variar entre navegadores
    pitch = 0.1 if avatar == "TIAGO" else 1.8  # Sinistro vs Sexy
    rate = 0.8 if avatar == "TIAGO" else 1.0
    # Escapar o texto usando json.dumps para evitar quebrar o JS
    safe_text = json.dumps(texto)
    js = f"""
    <script>
        try {{
            window.speechSynthesis.cancel();
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
    # height mínimo > 0 evita issues em alguns navegadores/Streamlit
    components.html(js, height=1)

# 3. INTERFACE HOLOGRÁFICA (CSS)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover; background-position: center;
    }
    header, footer { visibility: hidden; }
    .terminal-main {
        background: rgba(0,0,0,0.85); border: 2px solid cyan; border-radius: 20px;
        padding: 20px; text-align: center; color: white;
    }
    .avatar-video {
        border-radius: 10px; border: 2px solid cyan; box-shadow: 0 0 15px cyan;
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

with col_esq:
    # TIAGO (EM BAIXO) - mantive o vídeo remoto (podes substituir por componente customizado)
    st.markdown("<div style='height:420px; display:flex; align-items:flex-end;'>", unsafe_allow_html=True)
    # video via HTML para permitir classe personalizada
    components.html(
        f"""
        <div style="position:relative; height:100%;">
            <video class="avatar-video" width="220" controls>
                <source src="https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago.mp4" type="video/mp4">
                Seu navegador não suporta o elemento de vídeo.
            </video>
        </div>
        """,
        height=420,
    )
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("CANAL: TIAGO"):
        st.session_state.target = "TIAGO"

with col_dir:
    # WISHA / HACK (EM CIMA)
    components.html(
        f"""
        <div style="height:220px; display:flex; align-items:flex-start; justify-content:flex-end;">
            <video class="avatar-video" width="220" controls>
                <source src="https://raw.githubusercontent.com/adv1982/hack-ai-app/main/hack.mp4" type="video/mp4">
                Seu navegador não suporta o elemento de vídeo.
            </video>
        </div>
        """,
        height=220,
    )
    if st.button("CANAL: WISHA"):
        st.session_state.target = "WISHA"
    st.markdown("<br>" * 6, unsafe_allow_html=True)

with col_mid:
    # CORE CENTRAL
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="terminal-main">', unsafe_allow_html=True)
    st.markdown("### 💠 INFINITY TALK CN-9")

    # ENTRADA DE TEXTO
    user_txt = st.text_input("LINHA DE COMANDO:", placeholder="Digita ou envia um ficheiro de áudio...")

    # ENTRADA DE ÁUDIO (UPLOAD) - substitui captura directa do microfone
    st.markdown("**Ou faz upload de um ficheiro de áudio (wav/mp3/m4a):**")
    audio_file = st.file_uploader("", type=["wav", "mp3", "m4a"])

    st.markdown(
        "<small>Nota: captura de microfone em tempo real exige bibliotecas adicionais (ex.: streamlit-webrtc). Se quiser, eu te mostro como integrar.</small>",
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # Usa arquivo de áudio se enviado, senão o texto
    input_final = None
    if user_txt and user_txt.strip():
        input_final = user_txt.strip()
    elif audio_file is not None:
        # aqui podes salvar/encaminhar o audio_file.read() para um ASR (Whisper/serviço)
        # por enquanto usamos um marcador
        input_final = "Comando por voz recebido (arquivo)"
        # se quiseres, podes extrair texto com ASR local aqui

    if input_final:
        avatar = st.session_state.get("target", "WISHA")
        shards = engine.sharding(input_final)
        resposta = engine.bios(avatar, input_final)

        # Feedback Visual e Áudio
        st.success(f"**{avatar}:** {resposta}")
        voice_engine(resposta, avatar)

        # Prova de Fragmentação (Nodes do Cofre)
        with st.expander("STATUS DOS SERVIDORES (SHARDING)"):
            c1, c2, c3 = st.columns(3)
            c1.code(f"NODE_1: ONLINE\n{shards[0][:24]}")
            c2.code(f"NODE_2: ONLINE\n{shards[1][:24]}")
            c3.code(f"NODE_3: ONLINE\n{shards[2][:24]}")
