# TubeFy 🎶➡️📺

Este script mágico clona sua playlist do Spotify para o YouTube, automaticamente encontrando as músicas correspondentes e criando uma nova playlist em sua conta do YouTube. Tudo o que você precisa são suas credenciais do Spotify e YouTube, e pronto! Vamos dar os primeiros passos para deixar sua playlist em dois mundos ao mesmo tempo.

## Como Funciona?
1. O script autentica sua conta do **Spotify** para acessar suas playlists.
2. Para cada música da playlist do Spotify, o script pesquisa no YouTube usando o **título da música** e o **nome do artista**.
3. Encontra o vídeo com mais visualizações (dentro dos parâmetros da pesquisa) e adiciona o vídeo correspondente a uma nova playlist no YouTube.
4. **Voilà!** Você tem sua playlist clonada no YouTube! 🎉

## Pré-requisitos 📋
Você precisará das seguintes bibliotecas e APIs:

- **Python 3.6+**
- Instale as bibliotecas necessárias no arquivo ***requirements.txt***

### Spotify Developer Credentials 

Acesse Spotify Developer Dashboard e crie uma aplicação para obter:

*client_id*

*client_secret*

*redirect_uri* (por exemplo, http://localhost:8888/callback)

**Passo a Passo para Obter as Credenciais do Spotify:**

* Acesse Spotify Developer Dashboard e faça login com sua conta do Spotify.
* Clique em Create an App (Criar Aplicação).
* Preencha os campos obrigatórios (nome da aplicação, descrição, etc.).
* Após a criação, você verá as informações da sua aplicação. As credenciais Client ID e Client Secret estarão disponíveis na página do app.
* No campo Redirect URIs, adicione um novo URI de redirecionamento (por exemplo, http://localhost:8888/callback).
* Salve as alterações.

### YouTube API Credentials:

* Vá até o Google Cloud Console.
* Crie um projeto.
* Ative a YouTube Data API v3.
* Vá para "Credenciais" e clique em "Criar credenciais".
* Escolha OAuth 2.0 e crie um ID de cliente OAuth.
* Baixe o arquivo credentials.json e coloque-o no mesmo diretório do script.

## Configuração 🛠️

* Clone o repositório:

```git clone https://github.com/Lari-Cassanjo/tubefy.git```

```cd tubefy```

* Configure suas credenciais no script (ou crie variáveis de ambiente):

> client_ID = 'seu_client_id'

> client_Secret = 'seu_client_secret'

* Coloque o arquivo credentials.json (que você baixou do Google Cloud) na pasta do projeto.

## Usando o Script 🚀

Execute o script:

```python main.py```

Ele pedirá a ID da sua playlist do Spotify. Para pegar essa ID:

* Vá até a playlist no Spotify.
* Clique com o botão direito e selecione "Compartilhar" -> "Copiar link da playlist".
* A ID da playlist será a parte após o playlist/ no link. Exemplo:
```https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M```
>Neste exemplo, a ID é 37i9dQZF1DXcBWIGoYBM5M.

Após isso, o script vai autenticar sua conta do YouTube, criar uma nova playlist e começar a adicionar os vídeos! 🎉

## Detalhes Técnicos ⚙️

O script usa:

* **Spotify API:** Para obter as músicas da playlist.
* **YouTube Data API:** Para criar a playlist no YouTube e adicionar vídeos.
* **YouTubeSearchPython:** Para pesquisar vídeos no YouTube.
* **Exponential Backoff:** Para lidar com erros temporários do YouTube.

## Contribuições 🤝

Contribuições são super bem-vindas! Abra um issue ou envie um pull request se tiver alguma sugestão ou melhoria.
