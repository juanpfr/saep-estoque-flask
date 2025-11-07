
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

## 🧱 Comandos SQL_Postgree
Tabela 1: 

INSERT INTO usuario (nome, email, senha) VALUES
('Carlos Silva', 'carlos@fabrica.com', '123456'),
('Ana Oliveira', 'ana@fabrica.com', '123456'),
('João Pereira', 'joao@fabrica.com', '123456');

Tabela 2:

INSERT INTO produto (nome, quantidade, estoque_minimo, usuario_id) VALUES
('Martelo com cabo de madeira', 50, 10, 1),
('Chave de fenda ponta chata', 40, 10, 1),
('Chave de fenda ponta Philips', 35, 10, 1),
('Alicate universal 8"', 25, 5, 2),
('Trena de 5 metros', 60, 15, 2),
('Chave inglesa 10"', 30, 8, 3),
('Serrote de 20 polegadas', 20, 5, 3),
('Nível de bolha 30cm', 15, 5, 2),
('Conjunto de chaves Allen', 50, 10, 1),
('Estilete profissional', 40, 10, 2);

Tabela 3: 

INSERT INTO movimentacao (tipo, quantidade, data, produto_id, usuario_id) VALUES
('entrada', 20, NOW(), 1, 1),
('saida', 5, NOW(), 2, 1),
('entrada', 10, NOW(), 3, 1),
('saida', 8, NOW(), 4, 2),
('entrada', 15, NOW(), 5, 2),
('saida', 3, NOW(), 6, 3),
('entrada', 10, NOW(), 7, 3),
('saida', 4, NOW(), 8, 2),
('entrada', 25, NOW(), 9, 1),
('saida', 6, NOW(), 10, 2);

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
