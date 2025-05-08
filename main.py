from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'não_era_para_estar_aqui'

contatos = []

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        codigo = len(contatos)
        contatos.append([codigo, nome, telefone, email])
        flash(f'Contato {nome} adicionado com sucesso!')
        return redirect('/')
    else:
        return render_template('/adicionar_contato.html')

@app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
def editar_contato(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        contatos[codigo] = [codigo, nome, telefone, email]
        flash(f'Contato {nome} atualizado com sucesso!')
        return redirect('/')
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato=contato)

@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    del contatos[codigo]
    flash(f'Contato excluído com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)