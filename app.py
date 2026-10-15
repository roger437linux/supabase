import streamlit as st

from streamlit_00.db import conectar

st.title("🍔 Hamburgueria")
st.write("Teste de conexão com o Supabase")

if st.button("Testar conexão"):
    try:
        conn = conectar()
        st.success("✅ Conexão com a API do Supabase realizada com sucesso!")       

        resposta = (
            conn.table("clientes")
            .select("nome, bairro, fone")
            .lte("id_cliente", 100)
            .eq('bairro', 'Centro')
            .order("nome")
            .limit(5)
            .execute()
        )

        # Exibe os resultados
        st.title("Clientes")
        st.dataframe(resposta.data)

    except Exception as e:
        st.error("❌ Não foi possível conectar à API do Supabase.")
        st.exception(e)
