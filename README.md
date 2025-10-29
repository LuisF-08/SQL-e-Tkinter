
# ⚙️ Guia de Instalação e Execução — Projeto SQL + Tkinter + ORM

Bem-vindo(a)! 👋  
Este repositório reúne estudos sobre bancos de dados **SQL** e **NoSQL**, com foco em **SQLite**, **PostgreSQL**, **MongoDB**, e uma **interface gráfica feita com Tkinter**.  
Além disso, a aplicação utiliza **SQLAlchemy ORM** para manipular o banco de forma mais estruturada e moderna.

---

## 🧰 1. Pré-requisitos

Antes de começar, garanta que você possui instalado em sua máquina:

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- (Opcional) [Visual Studio Code](https://code.visualstudio.com/) ou outro editor de sua preferência

Para verificar se o Python está disponível, abra o terminal (CMD ou PowerShell) e execute:

```bash
python --version
````

Se o comando retornar algo como `Python 3.11.5`, está tudo certo ✅

---

## 📦 2. Clonar o Repositório

Faça o download do projeto localmente com o comando:

```bash
git clone https://github.com/LuisF-08/SQL-e-Tkinter.git
```

Em seguida, entre na pasta do projeto:

```bash
cd SQL-e-Tkinter
```

---

## 🧱 3. Criar o Ambiente Virtual

É recomendado usar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente:

* **Windows (PowerShell):**

  ```bash
  venv\Scripts\activate
  ```
* **Linux/Mac:**

  ```bash
  source venv/bin/activate
  ```

Ao ativar, o terminal exibirá algo como `(venv)` no início da linha.

---

## 📋 4. Instalar as Dependências

Com o ambiente virtual ativo, instale todas as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

As dependências incluem:

* **tkinter** → Interface gráfica
* **sqlite3 / psycopg2 / pymongo** → Conexão com bancos SQL e NoSQL
* **SQLAlchemy** → ORM para gerenciar o banco de dados com classes Python

---

## 🧩 5. Estrutura do Projeto

A estrutura básica é a seguinte:

```
SQL-e-Tkinter/
│
├── interface.py          # Interface gráfica com Tkinter
├── orm.py                # Configuração e ORM com SQLAlchemy
├── requirements.txt
├── README.md
└── venv/                 # Ambiente virtual (criado automaticamente)
```

---

## ▶️ 6. Executando o Projeto

Para abrir a interface e executar a aplicação:

```bash
python interface.py
```

Se tudo estiver configurado corretamente, a janela do sistema de cadastro será exibida 🎉

---

## 🧱 7. Gerando o Executável (.exe)

Caso queira transformar a aplicação em um executável para Windows, siga os passos abaixo:

1. **Instale o PyInstaller:**

   ```bash
   pip install pyinstaller
   ```

2. **Gere o arquivo `.exe`:**

   ```bash
   pyinstaller --onefile --noconsole --add-data "orm.py;." interface.py
   ```

   * `--onefile` → cria um único executável.
   * `--noconsole` → oculta o terminal.
   * `--add-data "orm.py;."` → inclui o arquivo `orm.py` dentro do executável.

3. **Após o processo, o executável estará disponível em:**

   ```
   dist/interface.exe
   ```

---

## 🧪 8. Testando o Executável

Para testar o programa gerado:

```bash
cd dist
interface.exe
```

Se a interface abrir normalmente, o build foi concluído com sucesso ✅

---

## 🧹 9. Dicas Úteis

* **Limpar builds antigos:**

  ```bash
  rmdir /s /q build dist __pycache__
  ```
* **Exibir terminal (para depuração):**

  ```bash
  pyinstaller --onefile --add-data "orm.py;." interface.py
  ```
* **Adicionar ícone personalizado:**

  ```bash
  pyinstaller --onefile --noconsole --add-data "orm.py;." --icon="icone.ico" interface.py
  ```

---

## 💡 Possíveis Erros Comuns

| Problema                      | Solução                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| `ModuleNotFoundError`         | Certifique-se de ter ativado o ambiente virtual antes de instalar as dependências. |
| Janela fecha instantaneamente | Remova `--noconsole` do comando do PyInstaller para visualizar mensagens de erro.  |
| Banco não conecta             | Verifique se o caminho ou o nome do banco está correto no arquivo `orm.py`.        |

---

## 👨‍💻 Autor

**Luís Filipe**
💡 Desenvolvedor em aprendizado contínuo.
🔗 [GitHub](https://github.com/LuisF-08)

---

## 🏷️ Tags

#Python #Tkinter #SQLAlchemy #SQLite #PostgreSQL #MongoDB #InterfaceGrafica #CRUD #Database #Learning

```

