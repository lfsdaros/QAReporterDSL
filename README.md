# QA Reporter DSL

**QA Reporter DSL** é uma Linguagem de Domínio Específico (DSL) projetada para automatizar a criação e estilização de relatórios de Garantia de Qualidade (QA). Ela permite definir regras de formatação em um script simples e legível, aplicando-as a dados CSV para gerar relatórios Excel profissionais automaticamente.

## 🚀 Funcionalidades

*   **Sintaxe Legível**: Defina estilos e lógica usando comandos simples (`LOAD`, `STYLE`, `APPLY`).
*   **Formatação Condicional**: Aplique estilos baseados nos valores dos dados usando operadores lógicos (`AND`, `OR`, `NOT`, `==`, `>`, etc.).
*   **Estilização Automática**: Defina cores de fundo e negrito dinamicamente.
*   **Saída em Excel**: Salve relatórios diretamente como arquivos Excel (`.xlsx`).
*   **Visualização Instantânea**: Abra os relatórios gerados automaticamente no Excel ou no Navegador.

## 🛠️ Instalação

1.  **Pré-requisitos**: Certifique-se de ter o Python 3.x instalado.
2.  **Instalar Dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## 📖 Como Usar

1.  **Prepare os Dados**: Coloque seus dados brutos em um arquivo `.csv` (ex: `data.csv`).
2.  **Escreva o Script**: Crie um arquivo de texto (ex: `test.txt`) com suas regras de estilo.
3.  **Execute**:
    ```bash
    python main.py
    ```

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
