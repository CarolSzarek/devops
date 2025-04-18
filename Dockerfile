# Usar a imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do seu projeto para dentro do container
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Definir o comando para rodar a aplicação
CMD ["python", "app.py"]

<<<<<<< HEAD
# Usar a imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do seu projeto para dentro do container
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Definir o comando para rodar a aplicação
CMD ["python", "app.py"]
=======
>>>>>>> fe2fab83fb8674cb93eb5540fb6e469f88e0b0a3
