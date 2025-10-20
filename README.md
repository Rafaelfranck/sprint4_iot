Rafael Franck (RM550875), Gabriela Trevisan (RM99500), Eduardo Araujo (RM99758) e Leonardo Bonini (RM551716)


PROJETO IOT + RECONHECIMENTO FACIAL

Objetivo:
Integrar um módulo de reconhecimento facial desenvolvido em Python (Flask + OpenCV) com a aplicação mobile/web React Native (Expo), permitindo que o usuário seja autenticado por meio da câmera. Quando o rosto é reconhecido, o sistema registra automaticamente a presença no Firebase Firestore e abre a tela principal da aplicação.

Tecnologias utilizadas:

Frontend (App): React Native (Expo) + TypeScript

Backend: Python + Flask + OpenCV

Banco de dados: Firebase Firestore

Reconhecimento facial: modelo Haar Cascade

PASSO A PASSO PARA EXECUTAR A SOLUÇÃO FINAL

Iniciar o servidor Flask
Abra o terminal dentro da pasta:
iot_project/src

Ative o ambiente virtual:
.venv\Scripts\activate

Execute o servidor:
python api.py

Iniciar o aplicativo React Native
No terminal do projeto React Native, execute:
npx expo start

O navegador abrirá a aplicação.
Clique em “Iniciar Reconhecimento Facial” e aguarde alguns segundos.

Fluxo de funcionamento

O app captura a imagem da câmera (via CameraView ou getUserMedia).

A imagem é convertida em Base64 e enviada via POST para o servidor Flask.

O Flask decodifica e processa a imagem com o modelo Haar Cascade.

Se um rosto for detectado:

O servidor retorna recognized: true e user: “Rafael”

O app grava no Firestore o nome do usuário, data e hora do reconhecimento e o status de sucesso

O app redireciona automaticamente para a tela principal (Tabs).

INTEGRAÇÃO COM O RESTANTE DA APLICAÇÃO

O reconhecimento facial atua como etapa inicial de autenticação.
Após o rosto ser reconhecido:

O app grava o log de presença no Firebase.

Em seguida, abre as telas principais do aplicativo (perfil, carteira, ativos e recomendações).

Dessa forma, o reconhecimento facial está conectado diretamente ao fluxo principal de login e navegação do app, funcionando como uma forma prática e automatizada de acesso.

ESTRUTURA

iot_project/
│
├── src/
│ ├── api.py → Servidor Flask com endpoint /recognize

Link Video de demonstração:
https://drive.google.com/file/d/11PDbrhh8zY-XkbxwcXM17NDy-8RBYob2/view?usp=drive_link
