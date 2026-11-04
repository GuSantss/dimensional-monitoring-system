# Dashboard de Monitoramento de Cotas Dimensionais

## 📋 Sobre o Projeto

Este projeto foi desenvolvido em Python com o objetivo de automatizar a análise de cotas dimensionais a partir de planilhas Excel.

A aplicação realiza a leitura dos limites de cada cota, calcula automaticamente as faixas de alerta e classifica cada medição conforme regras pré-definidas de controle dimensional.

O projeto surgiu como uma forma de eliminar cálculos manuais, reduzir erros e facilitar a identificação rápida de desvios em processos produtivos.

---

## 🎯 Objetivos

- Automatizar a análise de medições dimensionais.
- Identificar rapidamente cotas em situação crítica.
- Reduzir o tempo gasto com verificações manuais.
- Disponibilizar os resultados em uma interface simples e intuitiva.

---

## 🚀 Funcionalidades

✅ Leitura automática de arquivos Excel (.xlsx)

✅ Cálculo automático dos limites de alerta

✅ Classificação das medições em:

- OK
- ALERTA
- VERMELHO

✅ Geração de uma tabela processada

✅ Dashboard interativo utilizando Streamlit

✅ Indicadores de desempenho e quantidade de ocorrências

✅ Filtros para análise rápida das cotas

---

## 🧮 Regra de Negócio

Para cada cota são informados:

- Limite Máximo
- Limite Mínimo
- Valor Medido

### Cálculo da Faixa

Faixa = Limite Máximo - Limite Mínimo

### Cálculo da Margem de Alerta

Margem = Faixa × 16%

### Cálculo dos Alertas

Alerta Máximo = Limite Máximo - Margem

Alerta Mínimo = Limite Mínimo + Margem

### Classificação

#### 🔴 VERMELHO

Quando:

- Medido > Limite Máximo

ou

- Medido < Limite Mínimo

#### 🟠 ALERTA

Quando:

- Medido ≥ Alerta Máximo

ou

- Medido ≤ Alerta Mínimo

#### 🟢 OK

Quando a medição estiver dentro da faixa segura.

---

## 📊 Estrutura Esperada da Planilha

|  COTA | LIM MAX | LIM MIN | MEDIDO |
|-------|---------|---------|--------|
|  14A  |  0.70   |  -0.70  |  0.45  |
|  14B  |  0.70   |  -0.70  |  0.62  |
|  14C  |  0.70   |  -0.70  |  0.80  |

---

## 📈 Exemplo de Resultado

| COTA | MEDIDO | ALERTA MAX | ALERTA MIN |  STATUS |
|------|--------|------------|------------|---------|
| 14A  | 0.45   | 0.476      | -0.476     | OK      |
| 14B  | 0.62   | 0.476      | -0.476     | ALERTA  |
| 14C  | 0.80   | 0.476      | -0.476     | VERMELHO|

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- OpenPyXL
- Streamlit
- Excel

---

## 📂 Estrutura do Projeto

```text
Projeto_Cotas/
│
├── ex_test.py
├── exercicio.xlsx
├── requirements.txt
├── README.md
│
└── imagens/
    └── dashboard.png
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Acesse a pasta:

```bash
cd seu-repositorio
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o Projeto

Para iniciar a aplicação:

```bash
streamlit run ex_test.py
```

Após a execução, o dashboard será aberto automaticamente no navegador.

---

## 📸 Dashboard

Adicione aqui uma captura de tela do projeto.

```text
imagens/dashboard.png
```

---

## 🔮 Melhorias Futuras

- Exportação automática de relatórios
- Histórico de medições
- Gráficos de tendência
- Integração com banco de dados
- Controle Estatístico de Processo (CEP)
- Comparação entre medições históricas
- Monitoramento em tempo real

---

## 💡 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- Lógica de programação
- Estruturas condicionais
- Manipulação de dados com Pandas
- Automação de planilhas Excel
- Desenvolvimento de dashboards
- Tratamento de dados industriais
- Desenvolvimento de aplicações Python

---

## 👨‍💻 Autor

**Gustavo Cordeiro**

Estudante de Engenharia Mecatrônica.

Interesses:

- Automação Industrial
- Análise de Dados
- Qualidade
- Desenvolvimento em Python
- Indústria 4.0

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo, aprendizado e demonstração de competências técnicas.