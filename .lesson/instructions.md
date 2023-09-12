<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# Assessment

## Exercício 12

À medida que seus barcos se aproximam da terra, os elfos começam a fazer um inventário de seus suprimentos. Uma consideração importante é a comida - em particular, o número de calorias que cada elfo carrega.

Os elfos se revezam anotando o número de calorias contidas nas várias refeições, lanches, rações, etc. que trouxeram consigo, um item por linha. Cada elfo separa seu próprio inventário do inventário do elfo anterior (se houver) por uma linha em branco.

Por exemplo, suponha que os elfos terminem de escrever as calorias de seus itens e terminem com a seguinte lista:
```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```
Esta lista representa as calorias da comida transportada por cinco elfos:

- O 1º elfo está carregando comida com 1000, 2000, e 3000 calorias, um total de 6000 calorias.
- O 2º elfo está carregando um alimento com 4000 calorias.
- O 3º elfo está carregando comida com 5000 e 6000 calorias, um total de 11000 calorias.
- O 4º elfo está carregando comida com 7000, 8000, e 9000 calorias, um total de 24000 calorias.
- O 5º elfo está carregando um alimento com 10000 calorias.

Caso os elfos fiquem com fome e precisem de lanches extras, eles precisam saber a qual elfo perguntar: eles gostariam de saber quantas calorias estão sendo transportadas pelo elfo que carrega mais calorias. No exemplo acima, é 24000 (4º elfo).

Encontre o elfo carregando mais calorias. Quantas calorias totais ele está carregando?

A entrada para seu programa será um arquivo contendo uma lista no formato especificado acima.
Teste seu programa com os arquivos ```exemplo1.txt``` e ```exemplo2.txt```