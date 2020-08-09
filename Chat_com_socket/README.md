<h2>Passo a passo de execução do módulo de comunicação serial</h2>

<h3> Preparações: </h3>

Para começar, você precisa instalar algumas libs do python para funcionamento do código. Tais como: websockets e pyserial.

No windows:

```bash
$ python -m pip install websockets pyserial
```
No linux ou MacOS:

```bash
$ python3 -m pip install websockets pyserial
```

Agora você deverá criar um arquivo de configuração (.json) que contenha os parâmetros de comunicação serial.

<p>
<b>Obs: É aconselhável que o nome do arquivo (.json) não contenha caracteres especiais.</b>
</p>

Exemplo do formato do arquivo a ser seguido:

```json
{"parametros": 
    {"baudrate":9600, "bytesize":8, "parity": "N", "stopbits":1, 
        "timeout":2, "xonxoff":0, "rtscts":0, "dsrdtr":0}}
```

Você também precisa ter um arduino configurado para responder comandos enviados via serial.  (Protocolo de comunicação à sua escolha)


<h3> Executando o código: </h3>

Com o arquivo de configuração criado (.json), você deve executar no terminal o seguinte comando.

<p><b>Obs: Antes de executar o comando abaixo, verfique se o arquivo functions.py está no mesmo repositório (pasta) que o modulo_de_comunicacao.py .</b></p>

Linux ou MacOS:

```bash
$ python3 modulo_de_comunicacao.py
```

Windows:

```bash
$ python modulo_de_comunicacao.py
```

Na tela inicial do código você deverá colocar o caminho do arquivo de configuração (.json) criado anteriormente:

```bash
Configuração serial:

Digite o nome do arquivo .json que contém os parametros seriais de comunicação. 

Exemplo: parametros.json    -  (Evite caracteres especiais)

Nome do arquivo:
```

Logo em seguida vem a tela com a listagem dos dispositivos conectados na serial:

```bash
Listas de dispositivos conectados na serial:
1 - Arduino Uno (COM4)
2 - Porta de comunicação (COM1)

Digite o número que representa o dispositivo escolhido: 
```

Depois vem a tela de espera da conexão com o web site:

```bash
Tudo pronto por aqui :)

Para realizar o teste de bancada, envie o telecomando pela página web.

Esperando conexão com o servidor web...
```


-----------------------------------------------------------------------

Caso tudo ocorra bem, será mostrado na tela o telecomando enviado via serial e a sua respectiva resposta.

```bash
Comunicação estabelecida - Telecomando enviado para a serial: temperatura


Resposta do satélite: Temperatura atual: 70° 


Esperando próximo telecomando...  
```

Essa informação também poderá ser visualizada via web.
