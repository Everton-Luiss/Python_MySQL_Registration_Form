from PyQt5 import uic, QtWidgets#QtWidgets é pra poder mostrar os coponentes na tela
#import mysql.connector

#banco = mysql.connector.connect(
 #   host = "localhost",
  #  user = "root",
   # passwd = "299792",
    #database = "Cadastro_produtos"
#)

def funcao_principal():#função que será acionada pelo botão
    linha1 = formulario.lineEdit.text()#lê o que foi digitado no formulário
    print('Código: ', linha1)
    linha2 = formulario.lineEdit_2.text()
    print('Descrição: ', linha2)
    linha3 = formulario.lineEdit_3.text()
    print('Preço: ', linha3)

    categoria = ""
    if formulario.radioButton.isChecked():
        print('Categoria informática foi selecionada')
        categoria = "Informática"
    elif formulario.radioButton_3.isChecked():
        print('Categoria alimentos foi selecionada')
        categoria = 'alimentos'
    elif formulario.radioButton_4.isChecked():
        print('Categoria eletrônicos foi selecionada')
        categoria = 'eletrônicos'
    # vamos colocar o código dentro da função principal pois ieremos que seja enviado
    # ao banco na hora de clicar no botão

    cursor = banco.cursor()#criamos um cursor e usamos nossa instancia do banco -> variavel criada fora da função principal
    comando_sql = 'insert into produtos(codigo, descricao, preco, categoria) values(%s, %s, %s, %s)'
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_sql, dados)
    banco.commit()

    linha1 = formulario.lineEdit.setText("")
    linha2 = formulario.lineEdit_2.setText("")
    linha3 = formulario.lineEdit_3.setText("")

def chama_lista():
    lista_produtos.show()

app=QtWidgets.QApplication([])#inicializando a aplicação
formulario=uic.loadUi("cadastro.ui")#importando o arquivo.ui pra variável formulário
lista_produtos=uic.loadUi("lista_produtos.ui")
formulario.pushButton.clicked.connect(funcao_principal)#quando clicar no botão formulário ele chama a função principal
formulario.pushButton_2.clicked.connect(chama_lista)

formulario.show()#mostra o  formulario
app.exec()#execura a aplicação