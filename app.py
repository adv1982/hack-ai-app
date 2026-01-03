import streamlit as st
import binascii

# --- 1. CONFIGURAÇÃO DA ENGINE INFINITY TALK (REAL) ---
st.set_page_config(page_title="InfinityTalk: Neural Video Core", layout="wide")

# --- 2. CLASSE DE PROCESSAMENTO (MATEMÁTICA E BIOS) ---
class InfinityTalk_Core:
    def __init__(self):
        # Carrega chaves reais ou define modo de falha segura
        try:
            self.security_keys = [st.secrets["api_key_1"], st.secrets["api_key_2"], st.secrets["api_key_3"]]
        except:
            self.security_keys = ["NULL_KEY", "NULL_KEY", "NULL_KEY"]

    def fragmentar_matematica(self, texto):
        """
        REAL: Converte o input em Hexadecimal puro e divide a carga.
        Isso é o que faz a 'mágica' de transmissão de dados.
        """
        if not texto: return []
        # Conversão Binária/Hex
        hex_raw = binascii.hexlify(texto.encode()).decode()
        # Sharding (Fragmentação por 3 nós)
        part = len(hex_raw) // 3 + 1
        return [hex_raw[i:i+part] for i in range(0, len(hex_raw), part)]

    def bios_personalidade(self, avatar, texto):
        """
        BIOS CÍNICA: O cérebro por trás do vídeo.
        """
        if avatar == "TIAGO":
            if len(texto) < 4: return "Sério? Abri o canal de vídeo criptografado pra você digitar isso?"
            if "segredo" in texto.lower(): return "O único segredo aqui é como você ainda não foi deletado."
            return f"Pacote recebido. Hash: {hash(texto)}. Não espere que eu sorria."
        
        elif avatar == "WISHA":
            if "futuro" in texto.lower(): return "O futuro é um glitch que a gente ainda não corrigiu."
            if "ajuda" in texto.lower(): return "Sua dependência emocional é fascinante... e inútil."
            return "Estou te observando através da webcam. O processamento foi concluído."
        
        return "Conexão Instável."

engine = InfinityTalk_Core()

# --- 3. CSS PARA O LAYOUT HOLOGRÁFICO EXATO ---
st.markdown("""
    <style>
    /* FUNDO DA PLATAFORMA */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover;
        background-position: center; 
        background-attachment: fixed;
    }
    
    /* ESCONDER O HEADER PADRÃO */
    header, footer {visibility: hidden;}

    /* INPUT CENTRAL */
    .stTextInput input {
        background-color: rgba(0, 0, 0, 0.9) !important;
        color: #00ff00 !important;
        border: 2px solid #00ff00 !important;
        text-align: center;
        font-family: 'Courier New';
        font-weight: bold;
    }

    /* CAIXA DE TEXTO DOS AVATARES */
    .dialogo-box {
        background: rgba(0, 0, 0, 0.85);
        border-left: 4px solid cyan;
        padding: 15px;
        color: white;
        font-family: sans-serif;
        margin-top: 10px;
        border-radius: 0px 10px 10px 0px;
    }
    
    /* ESTILO PARA VÍDEO SEM BORDAS */
    video {
        border: 2px solid cyan;
        border-radius: 10px;
        box-shadow: 0 0 15px cyan;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. CONSTRUÇÃO DO GRID (TIAGO ESQ/BAIXO - WISHA DIR/TOPO) ---
c1, c2, c3 = st.columns([1.2, 2, 1.2])

# --- COLUNA 1: TIAGO (PREMENDO PARA BAIXO) ---
with c1:
    # Empurrar o Tiago para baixo para bater com o layout da foto
    st.write("\n" * 15) 
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True) 
    
    # VÍDEO DO TIAGO (Loop Infinito - "Infinity Talk")
    st.video("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago.mp4", format="video/mp4", start_time=0)
    
    if st.button("ATIVAR CANAL: TIAGO"):
        st.session_state.avatar = "TIAGO"

# --- COLUNA 2: CENTRO (PROCESSAMENTO) ---
with c2:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True) # Ajuste vertical
    st.markdown("<h3 style='text-align:center; color:white; background:black; border:1px solid cyan'>INFINITY TALK [CORE 9.0]</h3>", unsafe_allow_html=True)
    
    comando = st.text_input("LINHA DE COMANDO:", placeholder="Inicie o protocolo de texto...")
    
    if comando:
        # 1. Fragmentação Matemática Real
        frags = engine.fragmentar_matematica(comando)
        
        # 2. Resposta da BIOS
        quem = st.session_state.get("avatar", "WISHA")
        resposta = engine.bios_personalidade(quem, comando)
        
        # 3. Exibir Resposta Visual
        st.markdown(f"""
            <div class="dialogo-box">
                <strong style="color:cyan">>> {quem}:</strong> {resposta}
            </div>
        """, unsafe_allow_html=True)
        
        # 4. Prova Matemática (Display dos Hexadecimais)
        st.write("---")
        cols_frag = st.columns(3)
        cols_frag[0].code(frags[0], language="text")
        cols_frag[1].code(frags[1], language="text")
        cols_frag[2].code(frags[2], language="text")

# --- COLUNA 3: WISHA (TOPO DIREITO) ---
with c3:
    # Wisha fica no topo, sem espaçamento
    st.video("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/hack.mp4", format="video/mp4", start_time=0)
    
    if st.button("ATIVAR CANAL: WISHA"):
        st.session_state.avatar = "WISHA"
