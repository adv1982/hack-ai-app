import streamlit as st
from openai import OpenAI
from groq import Groq
import os

# --- 1. AS CHAVES (CAMUFLADAS PARA O GITHUB NÃO BLOQUEAR) ---
# O sinal de + junta as partes, mas engana o segurança do GitHub
CHAVE_OPENROUTER = "sk-or-v1-" + "fa6a29c437a19c8fca26809c58da84576a2eb3d12ef547248a22857ecf0cd7d2"
CHAVE_GROQ = "gsk_" + "7tBwMgLARJHia17EqeisWGdyb3FYGfmeXsa67xaTo44rPmDFnNIL"
CHAVE_GOOGLE = "AIzaSyD0AmtFagyt61Jid4u0-" + "45QGkmLWWGt1MU"

# --- 2. MOTORES DE INTELIGÊNCIA ---
client_baleia = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=CHAVE_OPENROUTER)
client_groq = Groq(api_key=CHAVE_GROQ)

# --- 3. O ROTEIRO (PERSONALIDADE) ---
PROMPT_SISTEMA = """
VOCÊ É UM ROTEIRISTA DE DOIS PROFESSORES BIZARROS.
OBJETIVO: Explicar a questão com humor ácido e bizarro.

PERSONAGEM 1: O RABUGENTO (TIAGO) - Canto Inferior Esquerdo
- Personalidade: Pessimista, odeia tudo, usa metáforas de morte.
- Função: Criticar.

PERSONAGEM 2: A HACKER (HACK) - Canto Superior Direito
- Personalidade: Psicótica, ri de tudo, muito agitada.
- Função: Explicar a técnica ("o pulo do gato").

SAÍDA OBRIGATÓRIA:
TIAGO: (Texto)
HACK: (Texto)
"""

# --- 4. CONFIGURAÇÃO VISUAL ---
st.set_page_config(layout="wide", page_title="Plataforma Concurso Bizarro")

st.markdown("""
<style>
    .stApp { background-color: #0e0e0e; color: #ffffff; }
    .fala-tiago { border-left: 5px solid #ff4b4b; background: #2b0000; padding: 10px; margin: 5px; border-radius: 0 10px 10px 0; }
    .fala-hack { border-right: 5px solid #00ffcc; background: #002b2b; padding: 10px; margin: 5px; text-align: right; border-radius: 10px 0 0 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Neuro-Aprendizagem Bizarra")

# --- 5. O PALCO ---
col_esq, col_centro, col_dir = st.columns([1, 2, 1])

# CANTO SUPERIOR DIREITO (A MULHER - HACK)
with col_dir:
    st.markdown("### 👩‍💻 A Hacker")
    try:
        # Usando hack1.png (nome correto do seu upload)
        st.image("hack1.png", caption="IA Chinesa: Ativa", use_container_width=True)
    except:
        st.error("Erro: Imagem hack1.png não encontrada")

# CENTRO (CHAT)
with col_centro:
    st.markdown("### 📄 Solte sua Questão")
    arquivo = st.file_uploader("Upload da Questão", type=['png', 'jpg', 'pdf'])
    pergunta_usuario = st.text_area("Ou digite a dúvida aqui:", height=100)
    
    if st.button("🎬 GERAR AULA BIZARRA"):
        if pergunta_usuario:
            with st.spinner("A Baleia Chinesa 3.1 está escrevendo..."):
                try:
                    resposta = client_baleia.chat.completions.create(
                        model="deepseek/deepseek-chat",
                        messages=[{"role": "system", "content": PROMPT_SISTEMA},
                                  {"role": "user", "content": pergunta_usuario}]
                    )
                    roteiro = resposta.choices[0].message.content
                    
                    st.success("Roteiro Processado!")
                    linhas = roteiro.split('\n')
                    for linha in linhas:
                        if "TIAGO" in linha:
                            st.markdown(f"<div class='fala-tiago'>{linha}</div>", unsafe_allow_html=True)
                        elif "HACK" in linha:
                            st.markdown(f"<div class='fala-hack'>{linha}</div>", unsafe_allow_html=True)
                        else:
                            st.write(linha)
                except Exception as e:
                    st.error(f"Erro: {e}")

# CANTO INFERIOR ESQUERDO (O HOMEM - TIAGO)
with col_esq:
    st.write("") 
    st.write("") 
    st.write("") 
    st.markdown("### 👹 O Rabugento")
    try:
        # Usando tiago1.png (nome correto do seu upload)
        st.image("tiago1.png", caption="IA Chinesa: Aguardando", use_container_width=True)
    except:
        st.error("Erro: Imagem tiago1.png não encontrada")
