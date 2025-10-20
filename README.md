# 🧠 Projeto IoT com Reconhecimento Facial

Este projeto integra um sistema de **reconhecimento facial** desenvolvido em Python com uma **aplicação mobile em React Native**. O objetivo é permitir a autenticação de um usuário através da câmera, registrando sua presença e liberando o acesso ao aplicativo.

### 👥 Integrantes
- **Rafael Franck** (RM550875)
- **Gabriela Trevisan** (RM99500)
- **Eduardo Araujo** (RM99758)
- **Leonardo Bonini** (RM551716)

---

## 🎥 Demonstração em Vídeo

👉 Assista ao vídeo de demonstração no Google Drive *[aqui](https://drive.google.com/file/d/11PDbrhh8zY-XkbxwcXM17NDy-8RBYob2/view?usp=drive_link)*.

---

## ✨ Funcionalidades Principais

* **Autenticação Facial**: O usuário inicia o aplicativo e utiliza a câmera para ser autenticado.
* **Comunicação via API**: O aplicativo envia a imagem capturada (em formato Base64) para um servidor Flask, que realiza o processamento.
* **Detecção de Rosto**: O backend utiliza a biblioteca OpenCV e o modelo Haar Cascade para detectar a presença de um rosto na imagem.
* **Registro no Firebase**: Após o reconhecimento, a presença do usuário é registrada automaticamente no Firebase Firestore, incluindo nome e timestamp.
* **Navegação Automática**: Uma vez autenticado, o usuário é redirecionado para a tela principal da aplicação.

---

## 🛠️ Tecnologias Utilizadas

| Camada                  | Tecnologias                               | Descrição                                                                      |
| :---------------------- | :---------------------------------------- | :----------------------------------------------------------------------------- |
| **Frontend (Mobile App)** | `React Native (Expo)` + `TypeScript`      | Para a construção da interface do usuário e captura da câmera.                 |
| **Backend (API)** | `Python` + `Flask` + `OpenCV`             | Para o processamento da imagem, detecção facial e comunicação com o app.         |
| **Banco de Dados** | `Firebase Firestore`                      | Para armazenar os registros de presença (logs de autenticação).                |
| **Reconhecimento Facial** | `Haar Cascade`                            | Modelo pré-treinado do OpenCV para detecção de objetos (neste caso, rostos). |

---

## 📂 Estrutura do Projeto
```bash
iot_project/
│
├── .venv/                  # Ambiente virtual do Python
├── src/                    # Código-fonte do backend
│   ├── api.py              # Servidor Flask com o endpoint de reconhecimento
│   └── __init__.py
│
├── requirements.txt        # Dependências do backend (Python)
└── react_app/              # (Exemplo) Projeto React Native (Expo)
    ├── App.tsx             # Arquivo principal do app
    ├── package.json        # Dependências do frontend
    ├── assets/
    ├── screens/
    └── components/
```
---

## 🚀 Como Executar a Solução

Siga os passos abaixo para configurar e executar o ambiente localmente.

### 1. Backend (Servidor Flask)

**Pré-requisitos**: Python 3.x instalado.

1.  **Navegue até a pasta do projeto e crie o ambiente virtual:**
    ```bash
    cd iot_project
    python -m venv .venv
    ```

2.  **Ative o ambiente virtual:**
    * No Windows:
        ```bash
        .venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

3.  **Instale as dependências do Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie o servidor Flask:**
    ```bash
    cd src
    python api.py
    ```
    O servidor será iniciado em `http://<seu-ip-local>:5000`. Anote o endereço IP, pois ele será usado no aplicativo.

### 2. Frontend (Aplicativo React Native)

**Pré-requisitos**: Node.js, npm/yarn e Expo CLI instalados.

1.  **Navegue até a pasta do aplicativo:**
    ```bash
    cd react_app
    ```

2.  **Instale as dependências do Node.js:**
    ```bash
    npm install
    ```

3.  **Configure o IP do servidor no código do aplicativo:**
    * Abra o arquivo onde a chamada à API é feita (ex: `App.tsx`).
    * Substitua o endereço da API pelo IP local do seu servidor Flask (ex: `http://192.168.1.10:5000/recognize`).

4.  **Inicie o aplicativo com Expo:**
    ```bash
    npx expo start
    ```

5.  Abra o aplicativo **Expo Go** em seu smartphone e escaneie o QR Code exibido no terminal.

---

## 🔄 Fluxo de Funcionamento

1.  O aplicativo React Native captura uma imagem da câmera do usuário.
2.  A imagem é convertida para o formato **Base64**.
3.  Uma requisição `POST` é enviada para o endpoint `/recognize` do servidor Flask, contendo a imagem em Base64.
4.  O servidor Flask decodifica a imagem e a processa com o modelo **Haar Cascade** para detectar um rosto.
5.  **Se um rosto for detectado**, o servidor retorna uma resposta de sucesso:
    ```json
    {
      "recognized": true,
      "user": "Rafael",
      "timestamp": "2023-10-27T10:00:00.000Z"
    }
    ```
6.  O aplicativo recebe a resposta, grava o log de presença no **Firebase Firestore** e redireciona o usuário para a tela principal (Tabs).
7.  **Caso nenhum rosto seja detectado**, o servidor retorna:
    ```json
    {
      "recognized": false,
      "user": null,
      "timestamp": "2023-10-27T10:00:05.123Z"
    }
    ```

---

## ⚙️ Endpoints da API

O servidor Flask expõe os seguintes endpoints:

* **`GET /`**
    * **Descrição**: Verifica o status do servidor.
    * **Resposta de Sucesso**:
        ```json
        {
          "status": "Servidor de Reconhecimento Facial ativo 🚀"
        }
        ```

* **`POST /recognize`**
    * **Descrição**: Recebe uma imagem em Base64 para realizar o reconhecimento facial.
    * **Corpo da Requisição (Body)**:
        ```json
        {
          "image": "<sua-imagem-em-base64>"
        }
        ```
    * **Respostas Possíveis**: JSON indicando se o reconhecimento foi bem-sucedido ou não (conforme detalhado no *Fluxo de Funcionamento*).

---

## 📝 Observações Finais

* Certifique-se de que o servidor Flask esteja rodando e acessível na rede local antes de iniciar o aplicativo.
* Este projeto foi desenvolvido para fins acadêmicos, mas pode ser expandido para cenários como:
    * Controle de acesso físico ou digital.
    * Sistemas de ponto eletrônico automatizado.
    * Autenticação facial em tempo real para aplicações de segurança.
