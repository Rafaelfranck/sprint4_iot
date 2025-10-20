# 🧠 Projeto IoT + Reconhecimento Facial

### 👥 Integrantes
- **Rafael Franck** (RM550875)  
- **Gabriela Trevisan** (RM99500)  
- **Eduardo Araujo** (RM99758)  
- **Leonardo Bonini** (RM551716)

---

## 🎯 Objetivo

Integrar um módulo de **reconhecimento facial** desenvolvido em **Python (Flask + OpenCV)** com uma **aplicação mobile/web React Native (Expo)**, permitindo que o usuário seja autenticado por meio da câmera.

Quando o rosto é reconhecido, o sistema:
1. Registra automaticamente a presença no **Firebase Firestore**.  
2. Redireciona o usuário para a **tela principal da aplicação**.

---

## 🧩 Tecnologias Utilizadas

| Camada | Tecnologias |
|:--|:--|
| **Frontend (App)** | React Native (Expo) + TypeScript |
| **Backend** | Python + Flask + OpenCV |
| **Banco de Dados** | Firebase Firestore |
| **Reconhecimento Facial** | Modelo Haar Cascade |

---

## ⚙️ Passo a Passo para Executar a Solução Final

### 🖥️ 1. Iniciar o servidor Flask

1. Abra o terminal dentro da pasta:
   ```bash
   cd iot_project/src
   
2. Ative o ambiente virtual:
   ```bash
   .venv\Scripts\activate

3. Execute o servidor:
   ```bash
   python api.py

O servidor Flask será iniciado localmente (exemplo: http://127.0.0.1:5000).

📱 2. Iniciar o aplicativo React Native

No terminal do projeto React Native, execute:

npx expo start


O navegador abrirá automaticamente a aplicação.

Clique em “Iniciar Reconhecimento Facial” e aguarde alguns segundos.

O app se conectará ao servidor Flask, processará a imagem e validará o rosto.

Após a validação, o usuário será redirecionado para a tela principal da aplicação.

🔁 Fluxo de Funcionamento

O app captura a imagem da câmera (via CameraView ou getUserMedia).

A imagem é convertida em Base64 e enviada via POST para o servidor Flask.

O Flask decodifica e processa a imagem com o modelo Haar Cascade.

Se um rosto for detectado:

O servidor retorna:

{ "recognized": true, "user": "Rafael" }


O app grava no Firestore:

Nome do usuário

Data e hora do reconhecimento

Status de sucesso

O app redireciona automaticamente para a tela principal (Tabs).

🔗 Integração com o Resto da Aplicação

O reconhecimento facial atua como etapa inicial de autenticação.

Após o rosto ser reconhecido:

O app grava o log de presença no Firebase.

Em seguida, abre as telas principais do aplicativo:

Perfil

Carteira

Ativos

Recomendações

Dessa forma, o reconhecimento facial está diretamente integrado ao fluxo de login e navegação, oferecendo uma autenticação prática e automatizada.

🗂 Estrutura Completa do Projeto
iot_project/
│
├── src/
│   ├── api.py              # Servidor Flask com endpoint /recognize
│   ├── detect_haar.py      # Script de reconhecimento facial (modelo Haar Cascade)
│   ├── data/               # Base de imagens de referência
│   ├── templates/          # (Opcional) Páginas HTML auxiliares
│   └── __init__.py
│
├── .venv/                  # Ambiente virtual Python
├── requirements.txt        # Dependências do backend
│
└── react_app/              # Projeto React Native (Expo)
    ├── App.tsx
    ├── package.json
    ├── assets/
    ├── screens/
    └── components/

🧱 Instalação das Dependências
🐍 Backend (Python)

Dentro da pasta iot_project/src, execute:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

📱 Frontend (React Native)

Dentro da pasta do projeto React Native (ex: react_app/), execute:

npm install
npx expo start

🎥 Demonstração em Vídeo

👉 Assista ao vídeo de demonstração no Google Drive

🧾 Observações Finais

Certifique-se de ter todas as dependências instaladas corretamente (requirements.txt e package.json).

Verifique se o servidor Flask está rodando antes de abrir o aplicativo Expo.

O sistema foi desenvolvido para fins acadêmicos, mas pode ser facilmente expandido para:

Controle de acesso físico ou digital;

Registro automatizado de presença;

Sistemas de autenticação facial em tempo real.
