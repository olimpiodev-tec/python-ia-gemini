# Python IA Gemini
- Projeto que simula uma IA integrado com API do Gemini desenvolvido com python e flask.
- Neste exemplo fui utilizado como contexto o tema: ``Culinária Italiana``
- Está publicado na plataforma render [neste link](https://python-ia-gemini.onrender.com/)

### Objetivos
- Aprender a utilizar o framework flask.
- Realizar integração com API do Google Gemini.

### Desenvolvimento
- O design das páginas (HTML, CSS, JS) foram criadas usando o ChatGPT.

### Execução do projeto
- Realize o clone do projeto.
- Crie o ambiente virtual do python no seu sistema operacional.
- Instalar dependências do projeto usando o comando: ```pip install -r req.txt```
- O projeto faz uso da biblioteca [python-dotenv](https://pypi.org/project/python-dotenv/) para armazenar de forma segurar a chave do Google Gemini, para isso crie crie na raiz do projeto um arquivo com nome de ``.env`` e dentro dele coloque uma variável com nome ``GEMINI_API_KEY='sua-chave-da-google-gemini-aqui'``
- Para gerar a chave acesse o site [Google Studio](https://aistudio.google.com/welcome) e crie sua api key.

### Bibliotecas utilizadas
```pip install google-generativeai```
```pip install Flask```
```pip install python-dotenv```

### Render
- O gunicorn é usado para publicação do projeto na plataforma [render](https://render.com/)
- [Clique aqui](https://drive.google.com/file/d/15SeTfW8IAC_v_EDvTtgv9cu1cHAKj9WM/view?usp=sharing) para visualizar o manual de apoio para publicar projetos python no render.

