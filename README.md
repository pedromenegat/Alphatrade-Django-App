# Alphatrade-Django-App

# Informações Gerais
Esta aplicação é uma implementação básica de formulários com Django. Nela, o usuário poderá usar as seguintes funcionalidades:
* Se registrar no site;
* Fazer login;
* Criar quantas enquetes quiser com número ilimitado de opções;
* Ver e interagir com as enquetes criadas por outros usuários;
* Acessar a página de perfil contendo todos os seus dados, incluindo todas as enquetes criadas pelo usuário;
* Alterar os dados como e-mail, username e foto de perfil; e
* Fazer logout.

# Rodando a Aplicação
Para utilizar a aplicação a nível de usuário, além de ter uma versão atualizada do Python e do Django instaladas no seu computador, é necessário instalar o Crispy Forms e a biblioteca Pillow.
Veja abaixo o passo a passo para rodar a aplicação:
* Faça o download deste repositório e extraia o arquivo zipado Alphatrade-Django-App-master.
* Abra o terminal e acesse o diretório Alphatrade-Django-App-master; em seguida acesse o diretório mysite dentro do diretório atual, digitando **cd mysite**.
* Quando estiver dentro do diretório mysite, instale o Crispy Forms e o Pillow com os seguintes comandos:
  ```
  pip3 install --user django-crispy-forms
  ```  
  ```
  pip install Pillow
  ```
* Ao completar a instalação, digite o comando "**python manage.py runserver**";
* Acesse a URL que aparecerá no terminal. Ela será parecida com esta: http://127.0.0.1:8000/
* Agora você já consegue utilizar a aplicação!
