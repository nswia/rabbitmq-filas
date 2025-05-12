# 🐰 RabbitMQ com Python - Projeto de Filas

Este projeto demonstra como criar e consumir filas usando **RabbitMQ** e **Python**, ideal para aprendizado de mensageria e sistemas assíncronos.

## 📦 Pré-requisitos

- Docker Desktop instalado e rodando com WSL2
- Container do RabbitMQ rodando com a imagem `rabbitmq:3-management`
- Python 3.8+ instalado
- `pip` instalado
- VSCode (opcional, mas recomendado)

## 🚀 Como rodar o projeto

Execução classica em python execute nessa ordem:
Aba 1:
python consumer.py 
fica aguardando a mensagens

Aba 2:
python producer.py
envia as mensagens

### 1. Clone o repositório

```bash
git clone https://github.com/nswia/rabbitmq-filas.git
cd rabbitmq-filas

## 🚀 Docker Compose

Usei o WSL no Windows em uma maquina virtual Ubuntu 22.04

docker-compose.yml
nsw@Walcow:/opt/rabbitmq$ cat docker-compose.yml
version: '3.8'

services:
  rabbitmq:
    image: rabbitmq:3-management
    container_name: rabbitmq
    hostname: rabbitmq
    ports:
      - "5672:5672"
      - "15672:15672"
      - "15692:15692"
    environment:
      RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS: "-rabbitmq_prometheus true"
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
    restart: always

  prometheus:
    image: prom/prometheus
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    restart: always

  grafana:
    image: grafana/grafana
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    restart: always

volumes:
  rabbitmq_data:
  grafana_data:



*** Também para efeito de registro o prometheus.yml tem que estar no mesmo diretorio que o docker-compose.yml para trazer as configurações dos endpoints

prometheus.yml

global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'rabbitmq'
    static_configs:
      - targets: ['rabbitmq:15692']
    metrics_path: /metrics
    scheme: http


