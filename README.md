# queue-simulator

#### Requisitos
- Python 3.6+


#### Execução
```sh
$ python3 -m queue_simulator
``` 


#### Resulados (Filas em Tundem)
          G/G/2/3 | arrival: 2..3 | service: 2..5
          State           Time    Probability
              0      2297.5446        2.3769%
              1     57677.9253       59.6699%
              2     36390.1519       37.6469%
              3       296.0314        0.3063%
          Losses: 0

          G/G/1/3 | service: 3..5
          State           Time    Probability
              0         6.1302        0.0063%
              1       243.6503        0.2521%
              2      35854.179       37.0923%
              3     60558.1231       62.6493%
          Losses: 14679
      
<br/>

**Detalhes da execução**:  
- Chegada do primeiro cliente: 2.5  
- Números aleatórios utilizados: 100000  
- Seed: timestamp do sistema  
- Média de 5 execuções  
