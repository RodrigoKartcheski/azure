FROM ubuntu:20.04


WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip

# Copie o conteúdo do diretório src para o diretório de trabalho no contêiner
COPY src/ src/

# Instale as dependências do Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Atualizar os pacotes e instalar dependências
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release && \
    curl -sL https://aka.ms/InstallAzureCLIDeb | bash && \
    rm -rf /var/lib/apt/lists/*

# Comando padrão
CMD ["bash"]

#docker build -t mazure:1.0 .
#docker run -v /home/jobs/azure/src:/app mazure:1.0
#docker run -v /home/jobs/azure/src:/app mazure:1.0
#docker run -it mazure:1.0 bash
#az login

# salve os arquivos na pasta src do host
#https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
