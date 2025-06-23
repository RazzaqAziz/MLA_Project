mkdir -p ~/.streamlit/

echo "\
[server]
headless = true
enableCORS=false
port = $PORT
\n\
" > ~/.streamlit/config.toml
