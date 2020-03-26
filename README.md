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
$ python3 -m queue_simulator
``` 


#### Resulados
      Fila: G/G/1/5 | chegadas 2..4 | atendimento 3..5
      
      State           Time    Probability
          0         3.2088        0.0019%
          1         7.6854        0.0044%
          2         13.436        0.0078%
          3       193.5603        0.1119%
          4      69924.157       40.4415%
          5    102760.1391       59.4325%
          
  
   
      Fila: G/G/2/5 | chegadas 2..4 | atendimento 3..5
      
      State           Time    Probability
          0      2241.0699         1.488%
          1     95803.5712       63.6102%
          2     52239.1125        34.685%
          3       326.5448        0.2168%
          4            0.0           0.0%
          5            0.0           0.0%
      
<br/>

**Detalhes da execução**:  
- Chegada do primeiro cliente: 3.0  
- Números aleatórios utilizados: 100000  
- Seed: timestamp do sistema  
- Média de 5 execuções  
