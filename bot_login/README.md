# Login automático no Instagram

Um script em Python para fazer login automático na rede social [instagram](https://www.instagram.com/).


## Começando

<details>
  <summary><strong>Certifique-se de ter o Python 3.3 ou posterior e o pip instalados em sua máquina</strong></summary><br />
  
* Para verificar se você tem o `python` e o `pip`
  ```bash
  python3 --version && pip --version
  ```
* A saída deve ser similar a algo assim:
  ```
  Python 3.8.10
  pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
  ```
</details>

<br>

1. Faça um clone do repositório e entre nele

```bash
git clone git@github.com:luandersonalvesdev/instagram-bots.git
cd instagram-bots
```

2. Crie um ambiente virtual separado com o `venv`

```bash
python3 -m venv nome_do_ambiente
```

3. Ative o ambiente virtual:

- Windows:
    ```bash
    nome_do_ambiente\Scripts\activate
    ```

- Linux:
    ```bash
    source nome_do_ambiente/bin/activate
    ```

4. Instale as dependências a partir do `requirements.txt`
```bash
pip install -r requirements.txt
```

5. Crie o arquivo com suas informações de login na rede [instagram](https://www.instagram.com/)
```bash
touch user.json
```
- Exemplo:
    ```
    {
      "username": "luaoderson",
      "password": "senha123",
      "max_retries": 5,
      "wait_time": 2
    }
    ```
    > `username`: seu usuário instagram sem "@".

    > `password`: senha da sua conta.

    > `max_retries`: quantidade de tentativas que o bot fará para capturar o elemento no navegador. Aumente caso queira mais tentativas.

    > `wait_time`: quantos **segundos** o bot irá esperar para uma nova tentativa de capturar o elemento no navegador. Aumente caso seu navegador demore para carregar as paǵinas.


6. Execute o script
```bash
python3 bot_login.py
```

7. No mesmo terminal que iniciou, pressione "Enter" para encerrar o script.

---
## Contact

#### [Linkedin](https://linkedin.com/in/luandersonalvesdev)