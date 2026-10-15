# 🍔 Streamlit + Supabase

## Configuração local

1. No painel do Supabase, copie `SUPABASE_URL` em **Connect → Python - Flask → .env**.
2. Copie `SUPABASE_KEY` em **Project Settings → API Keys → Secret keys → default**.
3. Preencha os valores em `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "https://SEU-PROJETO.supabase.co"
SUPABASE_KEY = "SUA_SECRET_KEY_DO_SUPABASE"
```

4. Instale as dependências com `uv sync`.
5. Execute `uv run streamlit run app.py`.

O botão **Testar conexão** chama a API do Supabase Storage para verificar se a URL e a chave funcionam. Esse teste não exige que exista uma tabela de negócio, mas a chave precisa ter permissão para listar buckets. Se sua política de segurança não permitir essa operação, o teste poderá falhar mesmo que outras APIs do projeto estejam acessíveis.

## Publicação no Streamlit Community Cloud

Em **Settings → Secrets** da aplicação, cole os mesmos campos TOML, usando os valores reais do projeto Supabase. Não é necessário enviar `secrets.toml` ao GitHub.

## Segurança

- `.streamlit/secrets.toml` está listado no `.gitignore`.
- Não publique `SUPABASE_KEY` nem a chave secreta `sb_secret_...`.
- Use a secret key apenas no backend; nunca a exponha em componentes executados no navegador.


## Exemplos de consultas no Supabase

| SQL | Supabase com Python |
|---|---|
| `SELECT * FROM clientes` | `supabase.table("clientes").select("*").execute()` |
| `SELECT nome FROM clientes` | `supabase.table("clientes").select("nome").execute()` |
| `SELECT * FROM clientes WHERE id = 1` | `supabase.table("clientes").select("*").eq("id", 1).execute()` |
| `SELECT * FROM clientes ORDER BY nome` | `supabase.table("clientes").select("*").order("nome").execute()` |
| `SELECT * FROM clientes LIMIT 10` | `supabase.table("clientes").select("*").limit(10).execute()` |

## Operadores de comparação — WHERE

| SQL | Supabase com Python | Significado |
|---|---|---|
| `WHERE id = 1` | `.eq("id", 1)` | Igual a |
| `WHERE id <> 1` | `.neq("id", 1)` | Diferente de |
| `WHERE idade > 18` | `.gt("idade", 18)` | Maior que |
| `WHERE idade < 60` | `.lt("idade", 60)` | Menor que |
| `WHERE idade >= 18` | `.gte("idade", 18)` | Maior ou igual |
| `WHERE idade <= 60` | `.lte("idade", 60)` | Menor ou igual |
