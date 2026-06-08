# 🎧 Time Travel Playlist Generator

Este projeto cria automaticamente uma playlist no Spotify baseada nas músicas que estavam no billboard numa data específica escolhida pelo utilizador. Após introduzir uma data, o sistema identifica o sábado correspondente, recolhe as músicas mais populares dessa semana e adiciona-as a uma playlist privada no Spotify.

Se a playlist para essa data já existir, é reutilizada em vez de ser criada uma nova, garantindo organização e evitando duplicados.

---

## ✨ Funcionalidades

- Validação da data introduzida pelo utilizador.
- Cálculo automático do sábado correspondente.
- Recolha das músicas mais populares dessa semana através do Billboard.
- Pesquisa das faixas no Spotify com base no título e ano.
- Criação automática de uma playlist privada com o nome da data selecionada.
- Reutilização da playlist caso já exista.
- Adição de todas as músicas encontradas diretamente na playlist.

---

## 🎯 Objetivo

Proporcionar uma forma simples e automática de revisitar musicalmente qualquer semana entre 2020 e 2026, criando playlists personalizadas que refletem os maiores sucessos da época.

---

## 📌 Fluxo do Processo

1. O utilizador escolhe uma data.
2. O sistema valida a data e determina o sábado correspondente.
3. As músicas dessa semana são recolhidas do Billboard.
4. Cada música é pesquisada no Spotify.
5. A playlist correspondente é criada ou reutilizada.
6. As músicas encontradas são adicionadas automaticamente.

---

## 📚 Notas

- Apenas músicas encontradas no Spotify são adicionadas.
- A playlist é sempre privada.
- O nome da playlist segue o formato: **Top Songs for YYYY-MM-DD**.
