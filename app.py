from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Usuario, Produto, Movimentacao
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_simples'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:22994433@localhost/saep_db'
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# 🔥 Cria tabelas se ainda não existirem
with app.app_context():
    db.create_all()

# ----------------- ROTAS -----------------

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = Usuario.query.filter_by(email=email).first()
        if user and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Email ou senha incorretos.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])
        if Usuario.query.filter_by(email=email).first():
            flash('Email já cadastrado.')
            return redirect(url_for('register'))
        novo = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo)
        db.session.commit()
        flash('Conta criada! Faça login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    produtos = Produto.query.filter_by(usuario_id=current_user.id).all()
    movimentacoes = Movimentacao.query.filter_by(usuario_id=current_user.id).order_by(Movimentacao.data.desc()).limit(10).all()
    return render_template('dashboard.html', produtos=produtos, movimentacoes=movimentacoes)

@app.route('/add_produto', methods=['POST'])
@login_required
def add_produto():
    nome = request.form['nome']
    quantidade = int(request.form['quantidade'])
    minimo = int(request.form['estoque_minimo'])
    novo = Produto(nome=nome, quantidade=quantidade, estoque_minimo=minimo, usuario_id=current_user.id)
    db.session.add(novo)
    db.session.commit()
    flash('Produto adicionado!')
    return redirect(url_for('dashboard'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    produto = Produto.query.get_or_404(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.quantidade = int(request.form['quantidade'])
        produto.estoque_minimo = int(request.form['estoque_minimo'])
        db.session.commit()
        flash('Produto atualizado!')
        return redirect(url_for('dashboard'))
    return render_template('editar_produto.html', produto=produto)

@app.route('/deletar/<int:id>')
@login_required
def deletar(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto removido.')
    return redirect(url_for('dashboard'))

# registrar entrada ou saída
@app.route('/movimentar/<int:id>', methods=['GET', 'POST'])
@login_required
def movimentar(id):
    produto = Produto.query.get_or_404(id)
    if request.method == 'POST':
        tipo = request.form['tipo']
        quantidade = int(request.form['quantidade'])
        if tipo == 'entrada':
            produto.quantidade += quantidade
        elif tipo == 'saida':
            if produto.quantidade < quantidade:
                flash('Quantidade insuficiente em estoque!')
                return redirect(url_for('movimentar', id=id))
            produto.quantidade -= quantidade
        mov = Movimentacao(tipo=tipo, quantidade=quantidade, produto_id=id, usuario_id=current_user.id)
        db.session.add(mov)
        db.session.commit()
        flash(f'Movimentação registrada ({tipo})!')
        return redirect(url_for('dashboard'))
    return render_template('movimentar.html', produto=produto)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
