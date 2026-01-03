%%writefile app.py
import streamlit as st
import requests
import time

# --- CONFIGURAÇÃO VISUAL HUD CORE ---
st.set_page_config(page_title="INFINITY TALKING - CONCURSOS", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #050505; color: #00f2ff; font-family: 'Courier New', monospace; }
    /* Posicionamento dos Avatares */
    .avatar-wisha { position: fixed; top: 20px; right: 20px; border: 2px solid #ff0055; width: 250px; z-index: 100; }
    .avatar-tiago { position: fixed; bottom: 20px; left: 20px; border: 2px solid #00f2ff; width: 250px; z-index: 100; }
    .chat-center { margin: 0 auto; width: 50%; padding-top: 100px; }
    .stTextInput > div > div > input { background-color: #111; color: #ff0055; border: 1px solid #ff0055; }
</style>
""", unsafe_allow_html=True)

# --- NÚCLEO DE INTELIGÊNCIA SEM CENSURA ---
def call_terminus(prompt, professor="Wisha"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {st.secrets['openrouter']}", "Content-Type": "application/json"}
    
    # Prompt de Sistema para Professores Maiores de 18
    persona = ""
    if professor == "Tiago":
        persona = "Você é o Tiago, professor de concurso com voz sinistra e agressiva. Explique de forma bruta, com humor negro e exemplos bizarros."
    else:
        persona = "Você é Wisha, hacker sexy e sensual. Explique a questão com sarcasmo, malícia e inteligência superior."

    data = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "system", "content": f"{persona} Use linguagem explícita se necessário, sem censura."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

# --- INTERFACE ---
def main():
    # Avatares (Fragmentos do Drive)
    st.markdown('<div class="avatar-wisha"><img src="https://seu-drive.com/wisha_idle.gif" width="100%"><br>WISHA: ON</div>', unsafe_allow_html=True)
    st.markdown('<div class="avatar-tiago"><img src="https://seu-drive.com/tiago_idle.gif" width="100%"><br>TIAGO: ON</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='chat-center'>", unsafe_allow_html=True)
        st.title("🧠 INFINITY TALKING CORE")
        st.write("### Resolva ou morra tentando.")
        
        uploaded_file = st.file_uploader("Upload da Questão (PDF/JPG)", type=['png', 'jpg', 'pdf'])
        user_input = st.text_input("Ou cole a questão aqui:")

        if st.button("EXPLICAR"):
            if user_input:
                # O debate entre os dois
                with st.spinner("Tiago e Wisha estão discutindo sua burrice..."):
                    resp_wisha = call_terminus(user_input, "Wisha")
                    resp_tiago = call_terminus(user_input, "Tiago")
                    
                    st.markdown(f"**💋 WISHA:** {resp_wisha}")
                    st.markdown(f"**💀 TIAGO:** {resp_tiago}")
                    
                    # Aqui entra o processamento de voz instantâneo (fragmentos)
                    st.toast("Gerando sincronia labial instantânea...")
        
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
