import streamlit as st
from supabase import Client, create_client

# Conexão com o Supabase usando secrets.toml

'''
O decorador @st.cache_resource é a escolha ideal aqui, pois o cliente do Supabase 
é um objeto de conexão (um recurso global). Isso garante que o Streamlit crie a conexão 
apenas uma vez e a reutilize em todas as recargas da página, economizando memória e evitando 
múltiplas conexões desnecessárias.
'''

@st.cache_resource()
def conectar() -> Client:    
    supabase = create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )
    return supabase
