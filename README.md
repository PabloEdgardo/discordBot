# Bot de discord feito para aprender

Fiz esse bot o bot para aprender com o video do [Lan code](https://www.youtube.com/@lan_code) o "[COMO CRIAR BOT DE DISCORD COMPLETASSO COM PYTHON](https://www.youtube.com/watch?v=Gt1BmJPme_g)"

## 1. o que o bot oferece?

o bot é apenas um teste, não tem funções reais no dia a dia, então todos os seus comandos são para testes da bliblioteca do discord 






## !aviso!

para envio publico o bot foi colocado sem IDs, caso queira rodar na propria maquina, troque os IDs,

* linha:106: bot.run((id do bot)) para rodar o bot
* linha:93, 98 e 103: canal= bot.get_channel((id do canal de bom dia)) para rodar as tasks de bom dia, boa tarde e boa noite
* linha:88: canal= bot.get_channel((id de envio de mensagens constantes))
* linha:25 e 30: canal = bot.get_channel((id de bemvindo)) para envio para o bem vindo e saida de membros

## 2. eventos

eventos são instruções executadas automaticamente quando algo de especifico acontece no servidor, e são os que eu fiz

1. sicronizar e declarar quantos comandos com interface estão carregados pelo terminal
2. iniciar as tarefaz
3. declarar o inicio de funcionamento do bot pelo terminal
4. enviar uma mensagem de bem vindo a um membro novo
5. enviar uma mensagem quando um membro saiu do grupo
6. enviar uma mensagem quando um membro reagiu a outra mensagem com emoji

## 3. tasks

tarefas que o bot pode fazer assim que inicia, como mandar mensagens em horarios especificos ou repetir a mesma mensagem

1. enviar sempre a mesma mensagem em um canal especifico enquanto o bot funcionar
2. dizer bom dia, boa tarde, boa noite no horario da inglaterra

## 4. comandos

os comandos são os inputs que são inseridos pelo usuario dentro do servidor ao bot, retornando alguma mensagem programada

1. .ola: responde "opa" + o nome do autor do input
2. .falar: repete a mensagem colocada depois da chamada do input
3. .soma: soma dois numeros colocados depois da chamada, exemplo ".soma 3 4" o bot retorna "7"
4. .embed_test: o bot retorna uma embed, uma mensagem estilizada em uma caixa que pode conter imagens e texto

### 4.1 comandos com interface

existem comandos que são chamados com "/" e apresentam todos os comandos de bots que podem ser chamados da mesma forma, ao selecionar o meu bot do servidor ele apresentará 4 comandos

1. /bobo @algum usuario do servidor: retorna o usuario mencionado no comando, o chamando de bobo
2. /falar texto:"algum texto": retorna o texto digitado pelo bot dentro do servidor
3. /oi: retorna "oi" + a menção ao autor do input, pode apenas ser visualizado pelo proprio
4. /standby_command: faz o dar um delay para processar a mensagem e enviar um "pronto"
