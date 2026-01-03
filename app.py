import streamlit as st
import requests
import base64
from gtts import gTTS
from pydub import AudioSegment
import io

# 1. Recuperar Chaves do Cofre (Secrets do Streamlit)
OPENROUTER_KEY = st.secrets["openrouter"]

# --- LAYOUT HUD CYBERPUNK ---
st.set_page_config(page_title="INFINITY TALK CORE V9", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #050505; color: #00f2ff; font-family: 'Courier New', monospace; }
    /* Avatar Wisha (Hacker) - Canto Superior Direito */
    .avatar-hacker { position: fixed; top: 10px; right: 10px; border: 2px solid #ff0055; width: 220px; z-index: 1000; background: rgba(0,0,0,0.8); }
    /* Avatar Tiago - Canto Inferior Esquerdo */
    .avatar-tiago { position: fixed; bottom: 80px; left: 10px; border: 2px solid #00f2ff; width: 220px; z-index: 1000; background: rgba(0,0,0,0.8); }
    .main-box { margin: 0 auto; width: 55%; padding-top: 50px; }
</style>
""", unsafe_allow_html=True)

# --- CÉREBRO DEEPSEEK 3.1 TERMINUS ---
def call_professors(tema, prof):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_KEY}", "Content-Type": "application/json"}
    
    if prof == "Tiago":
        sys_msg = "Você é o Professor Tiago. Voz sinistra, agressiva, direta. Explique o tema jurídico com humor negro e exemplos bizarros para maiores de 18 anos. Sem censura."
    else:
        sys_msg = "Você é a Hacker Wisha. Sensual, sarcástica, inteligente. Deboche da dúvida do aluno e explique com malícia acadêmica."

    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [{"role": "system", "content": sys_msg}, {"role": "user", "content": tema}]
    }
    res = requests.post(url, headers=headers, json=payload).json()
    return res['choices'][0]['message']['content']

# --- INTERFACE ---
def main():
    # Renderização dos Professores
    st.markdown('<div class="avatar-hacker"><img src="https://i.imgur.com/link_da_wisha.gif" width="100%"><center>HACKER: ATIVA</center></div>', unsafe_allow_html=True)
    st.markdown('<div class="avatar-tiago"><img src="https://i.imgur.com/link_do_tiago.gif" width="100%"><center>TIAGO: SINISTRO</center></div>', unsafe_allow_html=True)

    st.markdown("<div class='main-box'>", unsafe_allow_html=True)
    st.title("🛡️ INFINITY TALK V9: TERMINUS")
    
    questao = st.text_area("COLE A QUESTÃO DO CONCURSO AQUI:", placeholder="Ex: Artigo 121 CP...")
    
    if st.button("HACKEAR EXPLICAÇÃO"):
        col_a, col_b = st.columns(2)
        
        with st.spinner("DeepSeek 3.1 fritando os servidores..."):
            resp_t = call_professors(questao, "Tiago")
            resp_h = call_professors(questao, "Hacker")
            
            with col_a:
                st.error(f"💀 TIAGO DIZ: {resp_t}")
                # Gerar Voz Agressiva (Pitch baixo)
                tts = gTTS(resp_t, lang='pt', tld='com.br')
                tts.save("tiago.mp3")
                st.audio("tiago.mp3")

            with col_b:
                st.warning(f"💋 HACKER DIZ: {resp_h}")
                # Gerar Voz Sexy (Pitch normal/agudo)
                tts = gTTS(resp_h, lang='pt', tld='com.pt')
                tts.save("hacker.mp3")
                st.audio("hacker.mp3")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
