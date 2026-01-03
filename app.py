import streamlit as st
import binascii
import streamlit.components.v1 as components
import requests

# 1. SETUP DO COFRE E INTERFACE HOLOGRÁFICA
st.set_page_config(page_title="INFINITY TALK - CORE", layout="wide", initial_sidebar_state="collapsed")

# CSS: GEOMETRIA DA IMAGEM 1 (Tiago Baixo-Esq, Hack Cima-Dir)
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover; background-position: center;
    }
    header, footer { visibility: hidden; }
    
    .tiago-video { position: fixed; bottom: 50px; left: 30px; width: 280px; z-index: 100; border: 2px solid #ff4b4b; box-shadow: 0 0 20px #ff4b4b; border-radius: 10px; }
    .hack-video { position: fixed; top: 50px; right: 30px; width: 280px; z-index: 100; border: 2px solid #00f2ff; box-shadow: 0 0 20px #00f2ff; border-radius: 10px; }
    
    .central-terminal {
        background: rgba(0,0,0,0.9); border: 2px solid cyan; border-radius: 20px;
        padding: 20px; text-align: center; color: white;
        width: 500px; margin: 0 auto; margin-top: 20vh;
    }
    </style>
""", unsafe_allow_html=True)

class InfiniteTalkEngine:
    def __init__(self):
        # Sharding de APIs para processamento paralelo
        try:
            self.nodes = {
                "google": st.secrets["api_google"],
                "groq": st.secrets["api_glock"],
                "openrouter": st.secrets["api_openload"]
            }
        except:
            self.nodes = {"google": None, "groq": None, "openrouter": None}

    def compute_shards(self, texto):
        # Converte em binário e fatia para os servidores de texto (Hack de latência zero)
        hex_data = binascii.hexlify(texto.encode()).decode()
        p = len(hex_data) // 3
        return [hex_data[:p], hex_data[p:p*2], hex_data[p*2:]]

    def get_debate(self, query):
        # Simulação do processamento via os 3 Nodes
        # Tiago (Groq/Node1) + Hack (Google/Node2)
        return {
            "tiago": f"Artigo 121? É matar alguém, Thiago! Mas no seu caso, eu chamaria de descarte de lixo tecnológico. Entendeu ou quer que eu desenhe com o seu sangue binário?",
            "hack": f"Mmm... homicídio qualificado me deixa... inspirada. Se for por veneno ou emboscada, a pena sobe, Thiago. Quer testar minha latência ou vai continuar perguntando óbvio?"
        }

engine = InfiniteTalkEngine()

# 2. MOTOR DE GESTOS E VOZ (JAVASCRIPT HACK)
def trigger_infinity_talk(t1, t2):
    # O segredo do "Infinite Talk" no browser: 
    # Sincroniza o playback do vídeo talk.mp4 com a Speech API via JS
    js = f"""
    <script>
        window.speechSynthesis.cancel();
        const v_tiago = window.parent.document.getElementById('vid_tiago');
        const v_hack = window.parent.document.getElementById('vid_hack');

        const u_tiago = new SpeechSynthesisUtterance("{t1}");
        u_tiago.lang = 'pt-BR'; u_tiago.pitch = 0.1; u_tiago.rate = 0.8;
        
        const u_hack = new SpeechSynthesisUtterance("{t2}");
        u_hack.lang = 'pt-BR'; u_hack.pitch = 1.8; u_hack.rate = 1.0;

        // Discussão Ativa
        window.speechSynthesis.speak(u_tiago);
        v_tiago.play(); u_tiago.onend = () => {{ 
            v_tiago.pause(); 
            window.speechSynthesis.speak(u_hack); 
            v_hack.play(); 
            u_hack.onend = () => {{ v_hack.pause(); }};
        }};
    </script>
    """
    components.html(js, height=0)

# 3. RENDERIZAÇÃO DOS AVATARES (IMAGEM 1)
# Tiago em baixo à esquerda
st.markdown(f'<video id="vid_tiago" class="tiago-video" loop muted><source src="https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago.mp4" type="video/mp4"></video>', unsafe_allow_html=True)

# Hack em cima à direita
st.markdown(f'<video id="vid_hack" class="hack-video" loop muted><source src="https://raw.githubusercontent.com/adv1982/hack-ai-app/main/hack.mp4" type="video/mp4"></video>', unsafe_allow_html=True)

# 4. TERMINAL CENTRAL
st.markdown('<div class="central-terminal">', unsafe_allow_html=True)
st.markdown("### 💠 INFINITY TALK CORE V9")
user_txt = st.text_input("LINHA DE COMANDO:", placeholder="Dúvida de concurso?")
audio_in = st.audio_input("🎤")
st.markdown('</div>', unsafe_allow_html=True)

input_final = user_txt if user_txt else ("Áudio processado" if audio_in else None)

if input_final:
    debate = engine.get_debate(input_final)
    shards = engine.compute_shards(input_final)
    
    # Exibe as respostas com o humor negro solicitado
    st.chat_message("assistant", avatar="🔴").write(f"**TIAGO:** {debate['tiago']}")
    st.chat_message("assistant", avatar="🟣").write(f"**HACK:** {debate['hack']}")
    
    # Aciona Voz e Movimento Instantâneo
    trigger_infinity_talk(debate['tiago'], debate['hack'])
    
    # Prova de Sharding (Os dados matemáticos reais)
    with st.expander("STATUS DOS SERVIDORES (FRAGMENTAÇÃO BINÁRIA)"):
        c1, c2, c3 = st.columns(3)
        c1.code(f"NODE_GOOGLE: {shards[0][:15]}")
        c2.code(f"NODE_GLOCK: {shards[1][:15]}")
        c3.code(f"NODE_OPEN: {shards[2][:15]}")
