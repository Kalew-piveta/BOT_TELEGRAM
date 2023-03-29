import telebot

CHAVE_API = 'SUA CHAVE'

bot = telebot.TeleBot(CHAVE_API) # Conexão com o bot

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa: Tempo de espera de 20 min.")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10 min chega aí!")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, 'Não tem salada não, clique aqui para iniciar: /iniciar')




@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer (Clique em uma opção):
        /pizza Pizza
        /hamburguer Hamburguer
        /salada Salada
    """
    bot.send_message(mensagem.chat.id, texto)



@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um email para reclamacao@blablabla.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    #bot.reply_to(mensagem,'Valeu! Abraço de volta pra você!')
    bot.send_message(mensagem.chat.id, "Valeu! Abraço de volta pra você!")









def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
        /opcao1 Fazer pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Mandar um abraço
        Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, texto)



bot.polling() # "looping infinito do bot"

