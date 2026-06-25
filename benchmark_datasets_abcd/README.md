# Unified Federated Learning (FL) Benchmark Pipeline — CSAI-4-CPS

[English](#english) | [Português](#português)

---

## English

Welcome to the official repository for the **CSAI-4-CPS** Unified Federated Learning (FL) Benchmark Pipeline. This project introduces a standardized framework designed to evaluate the robustness of various FL aggregation algorithms under diverse adversarial cyberattacks across multiple Cyber-Physical Systems (CPS) and Internet of Things (IoT) environments.

### 🚀 Overview
Federated Learning is highly susceptible to poisoning and manipulation attacks. This benchmark provides a rigorous environment to test security compliances and mitigation strategies by injecting precise, synthetic malicious behaviors (`Cumulative`, `Scaling`, `Sybil`, and `OnOff`) into the local model training phases of distributed edge clients.

### 📁 Repository Structure
* `Unified_FL_Benchmark_Pipeline_CSAI4CPS.ipynb`: The core pipeline notebook containing the simulation orchestrator, client-server topology, model definitions, threat injection layers, and federated defenses (`FedAvg`, `Krum`, `FLAME`, `FLTrust`, and `Adaptive_Ultimate`).
* `Organização Nomes e Geração de Figuras v2.ipynb`: Analytical toolkit dedicated to processing raw outputs, aggregating benchmarking runs, computing multi-metric comparative matrices, and plotting visual curves.
* **Curated CPS/IoT Datasets**:
    * `Dataset_A_CPS-NetFlow-IDS.csv`: Network flow intrusion detection patterns.
    * `Dataset_B_Packet-Level Botnet Set.csv`: Fine-grained network packet botnet traces.
    * `Dataset_C_MQTT-IoT-Flood.csv`: Machine-to-machine telemetry flooding events.
    * `Dataset_D_Aggregated Traffic Set.csv`: Statistically aggregated industrial traffic.

---

### 🛠️ Execution Instructions

#### Method 1: Interactive Execution via Google Colab (Highly Recommended)
1.  Import the notebook `Unified_FL_Benchmark_Pipeline_CSAI4CPS.ipynb` into your Google Colab instance.
2.  Execute the initial setup and pipeline cells sequentially. 
3.  When prompted by the file management system (`"Faça o upload dos datasets CSV curados."`), multi-select and upload the four companion CSV datasets (`Dataset_A`, `Dataset_B`, `Dataset_C`, and `Dataset_D`).
4.  The orchestrator will iteratively evaluate defenses under diverse random seeds (e.g., 42, 43, 44), assessing target indicators like F1-Score, Execution Latency, and Attack Success Rate (ASR).
5.  Upon final iteration, the system compiles logs into an `execution_report.csv` and auto-downloads a consolidated `unified_results.zip`.

#### Method 2: Local Environment Deployment
1.  Clone this repository to your target machine:
    ```bash
    git clone https://github.com/your-username/csai4cps.git
    cd csai4cps
    ```
2.  Install the exact ecosystem prerequisites:
    ```bash
    pip install pandas numpy scikit-learn jupyter notebook
    ```
3.  Boot your local notebook environment:
    ```bash
    jupyter notebook
    ```
4.  Open the pipeline script, ensuring your dataset CSV elements reside within the workspace or root subdirectory path.

### 📊 Analytics & Performance Plots
To map global defense efficacy boundaries:
1.  Boot the secondary notebook: `Organização Nomes e Geração de Figuras v2.ipynb`.
2.  Provide the compressed analytical bundle (`unified_results.zip`) when requested by the workbook.
3.  The workflow automatically exports high-fidelity visualizations isolating defense resilience curves under every adversarial vector.

---

## Português

Bem-vindo ao repositório oficial do pipeline unificado de benchmark de Aprendizado Federado (FL) do projeto **CSAI-4-CPS**. Este framework padronizado foi concebido para testar e quantificar a resiliência de algoritmos de agregação federada contra múltiplos cenários de ciberataques em ambientes de Sistemas Ciber-Físicos (CPS) e Internet das Coisas (IoT).

### 🚀 Visão Geral
O Aprendizado Federado é vulnerável a envenenamento e manipulação de atualizações locais. Este benchmark oferece um ecossistema rigoroso para avaliar estratégias de mitigação através da injeção controlada de vetores maliciosos (`Cumulative`, `Scaling`, `Sybil` e `OnOff`) aplicados diretamente em clientes distribuídos na borda da rede.

### 📁 Estrutura do Repositório
* `Unified_FL_Benchmark_Pipeline_CSAI4CPS.ipynb`: Notebook central do pipeline contendo o orquestrador, topologia cliente-servidor, camadas de injeção de ameaças e algoritmos defensivos (`FedAvg`, `Krum`, `FLAME`, `FLTrust` e `Adaptive_Ultimate`).
* `Organização Nomes e Geração de Figuras v2.ipynb`: Utilitário analítico voltado ao pós-processamento, consolidação de métricas comparativas multi-critério e plotagem gráfica automatizada.
* **Datasets Curados de CPS/IoT**:
    * `Dataset_A_CPS-NetFlow-IDS.csv`: Padrões de intrusão baseados em fluxos de rede.
    * `Dataset_B_Packet-Level Botnet Set.csv`: Tráfego granular de botnets ao nível de pacotes.
    * `Dataset_C_MQTT-IoT-Flood.csv`: Eventos de inundação de telemetria em protocolos M2M.
    * `Dataset_D_Aggregated Traffic Set.csv`: Agregações estatísticas de tráfego industrial.

---

### 🛠️ Instruções de Execução

#### Método 1: Execução Interativa via Google Colab (Recomendado)
1.  Importe o arquivo `Unified_FL_Benchmark_Pipeline_CSAI4CPS.ipynb` no seu ambiente Google Colab.
2.  Execute as células de configuração e inicialização do pipeline.
3.  Quando solicitado pelo widget nativo (`"Faça o upload dos datasets CSV curados."`), selecione e envie simultaneamente os quatro arquivos CSV (`Dataset_A`, `Dataset_B`, `Dataset_C` e `Dataset_D`).
4.  O orquestrador executará as simulações cobrindo múltiplas sementes aleatórias (Ex: 42, 43, 44), medindo indicadores essenciais como F1-Score, Latência de Execução e Taxa de Sucesso do Ataque (ASR).
5.  Ao finalizar as rodadas, o sistema compila o relatório de auditoria `execution_report.csv` e força o download automático do arquivo condensado `unified_results.zip`.

#### Método 2: Implantação em Ambiente Local
1.  Clone este repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/seu-usuario/csai4cps.git
    cd csai4cps
    ```
2.  Instale as dependências mandatórias da pilha de ciência de dados:
    ```bash
    pip install pandas numpy scikit-learn jupyter notebook
    ```
3.  Inicie o servidor local do Jupyter:
    ```bash
    jupyter notebook
    ```
4.  Abra o notebook principal e garanta que os arquivos dos datasets CSV estejam posicionados na mesma pasta ou subdiretório de trabalho.

### 📊 Análise de Métricas e Geração de Gráficos
Para traçar as curvas de eficiência e gerar rankings analíticos das defesas:
1.  Inicie o notebook complementar `Organização Nomes e Geração de Figuras v2.ipynb`.
2.  Submeta o arquivo comprimido de métricas coletadas (`unified_results.zip`).
3.  O script gerará de forma automatizada figuras de alta resolução expondo as barreiras de tolerância a falhas e ataques de cada algoritmo testado.
