# queue-simulator

#### Requisitos
- Python 3.6+


#### Instalação (Linux e macOS)
```sh
$ pip install -r requirements.txt
```

Ou utilizando [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```sh
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

#### Execução
```sh
$ python3 -m queue_simulator <arquivo.yml>
``` 
Exemplo:
```sh
$ python3 -m queue_simulator ./files/class-model.yml
``` 

#### Arquivo de entrada
O arquivo de entrada deve estar no formato yaml e possuir a mesma estrutura utilizada pelo simulador disponibilizado no moodle da disciplina, com exceção da chave *rndnumbers*, utilizada para definir os números aleatórios que serão utilizados na simulação, que será ignorada caso seja enviada.   
Na pasta *files* já existem dois arquivos de exemplo, o arquivo *simulator-model.yml* é o mesmo gerado pelo simulador disponibilizado.
O arquivo *class-model* contém o [exemplo solicitado para teste do trabalho](./assets/class-model.jpg).  

#### Resultados
##### class-model.yml
    Fila: Q1 | G/G/1 | arrival: 1.0..4.0 | service: 1.0..1.5
    State           Time    Probability
        0     14271.2821       35.3611%
        1     20635.2082       51.1294%
        2      4905.0393       12.1536%
        3       524.3922        1.2993%
        4        22.5553        0.0559%
        5          0.278        0.0007%
    Losses: 0
    Total time: 40358.7552
    
    Fila: Q2 | G/G/3/5 | service: 5.0..10.0
    State           Time    Probability
        0         33.414        0.0828%
        1       409.1626        1.0138%
        2      2576.7122        6.3845%
        3      8611.8437       21.3382%
        4     15119.0348       37.4616%
        5      13608.588        33.719%
    Losses: 4788
    Total time: 40358.7552
    
    Fila: Q3 | G/G/2/8 | service: 10.0..20.0
    State           Time    Probability
        0        10.2735        0.0255%
        1          5.071        0.0126%
        2         0.8881        0.0022%
        3         6.8368        0.0169%
        4        21.8931        0.0542%
        5       152.0356        0.3767%
        6      2975.5332        7.3727%
        7     12832.7643       31.7967%
        8     24353.4597       60.3424%
    Losses: 6602
    Total time: 40358.7552

<br/>

##### simulator-model.yml
    G/G/1/5 | arrival: 20.0..40.0 | service: 10.0..12.0
    State           Time    Probability
        0    294131.6796       60.5493%
        1    186329.8257       38.3575%
        2       5283.227        1.0876%
        3        27.3629        0.0056%
    Losses: 0
    Total time: 485772.0952
    
    G/G/2/5 | service: 30.0..120.0
    State           Time    Probability
        0       4682.199        0.9639%
        1     31773.7501        6.5409%
        2     84463.2935       17.3874%
        3    132243.6274       27.2234%
        4    147956.1449       30.4579%
        5     84653.0802       17.4265%
    Losses: 1193
    Total time: 485772.0952
    
    G/G/2/5 | service: 15.0..60.0
    State           Time    Probability
        0    310688.7478       63.9577%
        1    145965.2908       30.0481%
        2     26940.9677         5.546%
        3      2113.7308        0.4351%
        4        62.0458        0.0128%
        5         1.3123        0.0003%
    Losses: 0
    Total time: 485772.0952
    
    G/G/3 | service: 5.0..15.0
    State           Time    Probability
        0    365290.0081       75.1978%
        1    108827.0118       22.4029%
        2     11204.6697        2.3066%
        3       447.3772        0.0921%
        4         3.0283        0.0006%
    Losses: 0
    Total time: 485772.0952


