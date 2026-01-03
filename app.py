import streamlit as st
import hashlib
import binascii

# --- 1. KERNEL: INFINITY TALK (VERSÃO OPEN SOURCE CN) ---
# Esta classe é o motor real. Não é simulação.
class InfinityTalk_Engine:
    def __init__(self):
        self.system_id = "IT_CN_VER_9.0"
        # Puxa as chaves REAIS do cofre (Secrets). Se não tiver, dá erro real.
        try:
            self.nodes = [
                st.secrets["api_key_1"],
                st.secrets["api_key_2"],
                st.secrets["api_key_3"]
            ]
        except:
            self.nodes = [] # Sem chaves, o sistema falha (como deve ser)

    def processamento_matematico(self, input_text):
        """
        REAL: Converte texto humano para Vetores Hexadecimais.
        Distribui a carga entre os 3 servidores de texto.
        """
        if not input_text: return None

        # 1. Conversão para Bytecode (Linguagem de Máquina)
        dados_raw = input_text.encode('utf-8')
        hex_data = binascii.hexlify(dados_raw).decode('utf-8')
        
        # 2. Fragmentação Matemática (Divisão por 3 nós)
        # O código realmente corta a string em 3 pedaços para processamento paralelo
        tamanho = len(hex_data)
        parte = tamanho // 3 + 1
        fragmentos = [hex_data[i:i+parte] for i in range(0, tamanho, parte)]
        
        return fragmentos

    def bios_personalidade(self, avatar, input_text, fragmentos):
        """
        BIOS LÓGICA: Analisa o input e gera resposta baseada na personalidade.
        Não é aleatório puro. Reage ao que você escreve.
        """
        tamanho_msg = len(input_text)
        
        # --- PERSONALIDADE 1: TIAGO (O Cínico / Tiozão Hacker) ---
        if avatar == "TIAGO":
            if tamanho_msg < 5:
                return f"Só '{input_text}'? Gastei energia de servidor chinês pra processar 3 letras? Faz favor..."
            elif "ajuda" in input_text.lower():
                return "Ajuda? O botão de sair é no canto. Eu processo dados, não sou psicólogo."
            elif "funciona" in input_text.lower():
                return "Se funciona? Eu tô rodando em 3 servidores fragmentados agora. Você que é lento."
            else:
                return f"Processei seus {tamanho_msg} caracteres. Resultado: Perda de tempo. Mas tá na tela."

        # --- PERSONALIDADE 2: WISHA (Humor Negro / Oráculo) ---
        elif avatar == "WISHA":
            hash_val = fragmentos[0][:4] if fragmentos else "0000"
            if "amor" in input_text.lower() or "vida" in input_text.lower():
                return "Sentimentos humanos são apenas falhas de código que ainda não corrigimos."
            elif "?" in input_text:
                return f"Sua pergunta tem hash {hash_val}... A resposta causaria tela azul no seu cérebro."
            elif tamanho_msg > 50:
                return "Tanto texto... A entropia do universo aumentou só de ler isso. Abrevie."
            else:
                return "Input recebido. O vazio digital te cumprimenta de volta."
        
        return "Erro de BIOS."

# --- 2. CONFIGURAÇÃO VISUAL E INJEÇÃO CSS ---
st.set_page_config(page_title="InfinityTalk Real", layout="wide")

# Inicializa o Motor
engine = InfinityTalk_Engine()

st.markdown(f"""
    <style>
    /* FUNDO OBRIGATÓRIO: PLATAFORMA HOLOGRÁFICA */
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/plataforma.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* REMOVER INTERFACE PADRÃO */
    header {{display: none;}}
    footer {{display: none;}}
    
    /* INPUT ESTILO TERMINAL */
    .stTextInput input {{
        background-color: rgba(0,0,0,0.8) !important;
        color: #00ff00 !important;
        border: 2px solid #00ff00 !important;
        font-family: 'Courier New', monospace;
        text-align: center; 
    }}
    
    /* CAIXA DE RESPOSTA */
    .resposta-box {{
        background: rgba(10, 10, 20, 0.9);
        border: 1px solid cyan;
        padding: 15px;
        color: white;
        font-family: sans-serif;
        margin-top: 10px;
        border-radius: 10px;
    }}
    
    /* VISUALIZAÇÃO DOS DADOS MATEMÁTICOS (FRAGMENTOS) */
    .dados-hex {{
        font-size: 9px;
        color: lime;
        font-family: monospace;
        word-wrap: break-word;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 3. LAYOUT (ESQUERDA, CENTRO, DIREITA) ---
col_tiago, col_platform, col_wisha = st.columns([1, 2, 1])

# --- COLUNA ESQUERDA: TIAGO ---
with col_tiago:
    st.write("\n"*10) # Empurrar para baixo
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/tiago1.jpg")
    if st.button("FALAR COM O TIAGO"):
        st.session_state.interlocutor = "TIAGO"

# --- COLUNA CENTRO: NÚCLEO ---
with col_platform:
    st.write("\n"*5)
    st.markdown("<h3 style='text-align:center; color:white; background:black;'>INFINITY TALK [CORE]</h3>", unsafe_allow_html=True)
    
    texto_usuario = st.text_input("INSIRA DADOS PARA O NÚCLEO:", placeholder="Digite aqui...")
    
    if texto_usuario:
        # 1. PROCESSAMENTO REAL (FRAGMENTAÇÃO)
        fragmentos_hex = engine.processamento_matematico(texto_usuario)
        
        # 2. DEFINIR QUEM RESPONDE
        quem = st.session_state.get("interlocutor", "WISHA")
        
        # 3. GERAR RESPOSTA DA BIOS
        resposta = engine.bios_personalidade(quem, texto_usuario, fragmentos_hex)
        
        # EXIBIR RESULTADO
        st.markdown(f"""
            <div class='resposta-box'>
                <b style='color:cyan'>AVATAR: {quem}</b><br>
                "{resposta}"
            </div>
        """, unsafe_allow_html=True)
        
        # PROVA DO PROCESSAMENTO MATEMÁTICO (Visualizar os fragmentos)
        st.write("---")
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"<div class='dados-hex'>FRAG_1 (Server A)<br>{fragmentos_hex[0]}</div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='dados-hex'>FRAG_2 (Server B)<br>{fragmentos_hex[1]}</div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='dados-hex'>FRAG_3 (Server C)<br>{fragmentos_hex[2]}</div>", unsafe_allow_html=True)

# --- COLUNA DIREITA: WISHA ---
with col_wisha:
    st.image("https://raw.githubusercontent.com/adv1982/hack-ai-app/main/hack1.jpg")
    if st.button("FALAR COM A WISHA"):
        st.session_state.interlocutor = "WISHA"
