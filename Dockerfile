# Usa imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do repositório para dentro do container
COPY . .

# Instala as bibliotecas do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 (onde a aplicação Flask roda)
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]

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
