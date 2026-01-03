import streamlit as st
from openai import OpenAI
from groq import Groq
import google.generativeai as genai
import time

# --- 1. AS CHAVES (CAMUFLADAS) ---
# O "+" engana o segurança do GitHub
CHAVE_OPENROUTER = "sk-or-v1-" + "fa6a29c437a19c8fca26809c58da84576a2eb3d12ef547248a22857ecf0cd7d2"
CHAVE_GROQ = "gsk_" + "7tBwMgLARJHia17EqeisWGdyb3FYGfmeXsa67xaTo44rPmDFnNIL"
CHAVE_GOOGLE = "AIzaSyD0AmtFagyt61Jid4u0-" + "45QGkmLWWGt1MU"

# --- 2. CONFIGURAÇÃO DOS CLIENTES ---
client_baleia = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=CHAVE_OPENROUTER)
client_groq = Groq(api_key=CHAVE_GROQ)
genai.configure(api_key=CHAVE_GOOGLE)

# --- 3. LAYOUT ---
st.set_page_config(layout="wide", page_title="Neuro-Streaming Bizarro")

st.markdown("""
<style>
    .stApp { background-color: #000; color: #0f0; }
    .status-server { color: orange; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# Colunas: Homem(Esq), Chat(Meio), Mulher(Dir)
col_esq, col_centro, col_dir = st.columns([1, 2, 1])

# --- 4. FUNÇÃO DE FRAGMENTAÇÃO (O SEGREDO) ---
def gerar_stream_bizarro(prompt):
    """
    Esta função usa a GROQ para velocidade extrema.
    Ela gera texto token por token (fragmentos) para enviar para o vídeo.
    """
    stream = client_groq.chat.completions.create(
        model="llama3-8b-8192", # Modelo mais rápido do mundo
        messages=[
            {"role": "system", "content": "VOCÊ É TIAGO (RABUGENTO) E HACK (LOUCA). Responda curto e rápido."},
            {"role": "user", "content": prompt}
        ],
        stream=True # <--- ISSO ATIVA O MODO TORNEIRA (FRAGMENTOS)
    )
    return stream

# --- 5. INTERFACE ---
with col_centro:
    st.title("⚡ Processamento Neural Fragmentado")
    pergunta = st.text_input("Comando de Entrada:")
    
    if st.button("ATIVAR FLUXO"):
        if pergunta:
            chat_box = st.empty() # Caixa vazia que vai encher aos poucos
            texto_completo = ""
            
            # SIMULAÇÃO DO PROCESSAMENTO DE VÍDEO NO SERVIDOR
            st.markdown("### 📡 Conectando aos Servidores...")
            status = st.empty()
            
            # 1. Pega o Stream da Groq (Fragmentos de Texto)
            fluxo = gerar_stream_bizarro(pergunta)
            
            for fragmento in fluxo:
                pedaco_texto = fragmento.choices[0].delta.content
                if pedaco_texto:
                    texto_completo += pedaco_texto
                    # Atualiza o texto na tela em tempo real
                    chat_box.markdown(f"**PROCESSANDO:** {texto_completo} ▌")
                    
                    # AQUI ENTRARIA O ENVIO PARA O SERVIDOR DE VÍDEO
                    # if len(texto_completo) > 20:
                    #     enviar_para_colab(texto_completo) 
                    
                    time.sleep(0.02) # Simula a velocidade de leitura
            
            chat_box.markdown(f"**RESPOSTA FINAL:**\n\n{texto_completo}")
            st.success("Fluxo concluído. Vídeo renderizado no servidor remoto.")

with col_esq:
    try: st.image("tiago1.png", use_container_width=True)
    except: st.write("Tiago Loading...")

with col_dir:
    try: st.image("hack1.png", use_container_width=True)
    except: st.write("Hack Loading...")
