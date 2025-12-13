# QA Reporter DSL

**QA Reporter DSL** é uma Linguagem de Domínio Específico (DSL) projetada para automatizar a criação, análise e estilização de relatórios de Garantia de Qualidade (QA). Ela permite definir regras de formatação em um script simples e legível, aplicando-as a dados CSV brutos para gerar relatórios Excel profissionais e visuais automaticamente.

## 🎓 Informações do Projeto

| Categoria | Detalhe |
| :--- | :--- |
| **Equipe** | Luiz Daros e Guilherme Valença |
| **Disciplina** | Compiladores |
| **Professor** | Luis Carlos Menezes |

## 🎯 Motivação e Descrição Informal da Linguagem

A criação de relatórios de Garantia de Qualidade (QA) é fundamental, mas a estilização condicional (ex: pintar linhas falhas de vermelho) é um processo manual e repetitivo. A **QA Reporter DSL** foi desenvolvida para eliminar essa complexidade.

É uma Linguagem de Domínio Específico (DSL) que permite ao engenheiro de QA ou Analista de Dados escrever **regras de formatação legíveis por humanos** em um script simples (`test.txt`).

O **Compilador/Interpretador** processa esse script, analisa os dados de um arquivo CSV e aplica as regras de estilo de forma inteligente, gerando um relatório Excel visualmente profissional e pronto para ser compartilhado. O compilador atua como um tradutor de regras de negócio em formatação.

## 🚀 Funcionalidades

* **Sintaxe Legível**: Defina estilos e lógica usando comandos simples (`LOAD`, `STYLE`, `APPLY`).
* **Formatação Condicional Avançada**: Aplique estilos baseados nos valores dos dados usando operadores lógicos e de comparação (`AND`, `OR`, `NOT`, `==`, `>`, `CONTAINS`, etc.).
* **Estilização Flexível**: Defina cores de fundo e negrito dinamicamente. Escolha entre pintar a linha inteira ou apenas uma coluna específica.
* **Saída em Excel**: Salve relatórios diretamente como arquivos Excel (`.xlsx`) prontos para envio.
* **Visualização Multi-Plataforma**: Escolha como deseja ver o resultado final: transformado em um dashboard HTML no **navegador** (`BROWSER`) ou nativamente no **Excel** (`EXCEL`).

## 🛠️ Instalação

Siga os passos abaixo para configurar o ambiente de execução.

### 1. Pré-requisitos
Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado em sua máquina.

### 2. Configurar Ambiente Virtual (Recomendado)
A criação de uma `venv` isola as dependências do projeto, evitando conflitos com outras bibliotecas do seu sistema.

* **No Windows:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```

* **No Linux / macOS:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Instalar Dependências
Com o ambiente virtual ativado, instale os pacotes necessários listados no arquivo de requisitos:

```bash
pip install -r requirements.txt
```

## 💻 Guia de Execução do Compilador/Interpretador

### Parte A: Execução Local

1.  **Gerar Parser e Lexer:**
    Primeiro, o ANTLR precisa gerar os arquivos Python a partir da gramática (`.g4`):
    ```bash
    python -m antlr4_tool -Dlanguage=Python3 -visitor QAReporterDSL.g4
    ```

2.  **Preparar Arquivos:** Coloque os arquivos `data.csv` e `test.txt` na raiz do projeto.

3.  **Executar o Interpretador:**
    ```bash
    python main.py
    ```

### Parte B: Execução no GitHub Codespaces

O Codespaces é configurado via `.devcontainer.json` para realizar a instalação de dependências e a geração do Parser/Lexer automaticamente no *startup*.

1.  **Inicie o Codespace:** Abra o projeto no GitHub Codespaces (Botão "Code" -> "Create codespace").
2.  **Preparar Arquivos:** Coloque os arquivos `data.csv` e `test.txt` na raiz do projeto.
3.  **Executar o Interpretador:** No terminal integrado:
    ```bash
    python main.py
    ```
4.  **Visualização:** O sistema adaptará a saída:
    * **BROWSER:** Instruirá o usuário a clicar com o botão direito no arquivo `.html` gerado e selecionar **"Open Preview"** no VS Code.
    * **EXCEL:** Instruirá o usuário a **baixar** o arquivo `.xlsx` gerado.

## 📝 Guia de Sintaxe da DSL

### 1. Carregando Dados
Comece carregando seu arquivo CSV de origem.
```text
LOAD "data.csv"
```

### 2. Definindo Estilos
Crie estilos nomeados com propriedades específicas.
*   **Propriedades**: `background` (red, green, yellow), `bold` (true, false).

```text
STYLE Sucesso {
    background: green,
    bold: false
}

STYLE Critico {
    background: red,
    bold: true
}
```

### 3. Aplicando Estilos
Aplique estilos às linhas que atendem a condições específicas.
*   **Operadores**: `==`, `!=`, `>`, `<`, `>=`, `<=`, `CONTAINS`.
*   **Lógica**: `AND`, `OR`, `NOT`.

```text
APPLY STYLE Sucesso WHERE Status == "Passed"
APPLY STYLE Critico WHERE Priority == "High" AND ExecutionTime > 500
```

### 4. Salvando e Visualizando
Salve os dados processados em um arquivo Excel e opcionalmente abra-o.

```text
SAVE "relatorio.xlsx"
VISUALIZE EXCEL
```

## 📂 Estrutura do Projeto

*   **`QAReporterDSL.g4`**: Definição da gramática ANTLR4.
*   **`interpreter.py`**: Lógica principal que lida com o processamento de dados (Pandas) e estilização (OpenPyXL).
*   **`main.py`**: Ponto de entrada que analisa o script e executa o interpretador.
*   **`test.txt`**: Exemplo de script de uso.

## 🔧 Construído Com
*   [ANTLR4](https://www.antlr.org/) - Gerador de parser.
*   [Pandas](https://pandas.pydata.org/) - Manipulação de dados.
*   [OpenPyXL](https://openpyxl.readthedocs.io/) - Geração de arquivos Excel.
