
# 🧰 Sistema de Gestão de Estoque (Desafio SAEP - SENAI)

## 📋 Descrição do Projeto
Este projeto foi desenvolvido como **desafio prático SAEP (SENAI)**, com o objetivo de aplicar os conhecimentos em **desenvolvimento web full stack**.  
A proposta foi criar um **sistema de controle de estoque** funcional utilizando **Flask (Python)** e **PostgreSQL**, simulando um ambiente real de uma fabricante de ferramentas e equipamentos manuais.

O sistema permite o **cadastro de produtos**, **registro de entradas e saídas**, e **monitoramento automático do nível de estoque mínimo**, emitindo alertas quando um item, está abaixo do limite configurado.  
O objetivo é oferecer uma **solução web simples, funcional e responsiva**, garantindo **organização**, **rastreabilidade** e **eficiência** na gestão de materiais.

---

## 🚀 Funcionalidades
- Login e autenticação de usuários (almoxarifes);
- CRUD completo de produtos (criar, visualizar, editar e excluir);
- Registro de movimentações de estoque (entrada e saída);
- Atualização automática de quantidades em estoque;
- Alertas automáticos para estoque mínimo;
- Histórico completo de movimentações (data, tipo, quantidade e responsável);
- Painel web simples e responsivo feito com TailwindCSS.

---

## 🧱 Tecnologias Utilizadas
- **Backend:** Flask (Python)
- **Frontend:** HTML + Tailwind CSS
- **Banco de Dados:** PostgreSQL
- **ORM:** SQLAlchemy
- **Autenticação:** Flask-Login
- **Hospedagem local:** Flask dev server

---

## ⚙️ Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/juanpfr/saep-estoque-flask/

# Acesse a pasta do projeto
cd saep-estoque-flask

# Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate  # (Windows)
# ou source venv/bin/activate (Linux/Mac)

# Caso ocorra algum erro no comando acima, tente este comando para liberar ambientes virtuais:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Instale as dependências
pip install -r requirements.txt

# Execute o projeto
python app.py
```

A aplicação ficará disponível em:  
👉 http://localhost:5000

---

## 🧑‍💻 Desenvolvedores
- **Juan**  
  GitHub: [https://github.com/juanpfr](https://github.com/juanpfr)

- **Bruno**  
  GitHub: [https://github.com/br7trindade](https://github.com/br7trindade)

---

## 🧾 Licença
Este projeto foi desenvolvido para fins **educacionais** (SAEP - SENAI) e pode ser adaptado livremente.  
Criado por **Juan** e **Bruno**.
