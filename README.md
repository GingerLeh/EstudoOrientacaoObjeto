## Estudo Orientação Objeto
> Exercicio feito para o curso de Analise e Desenvolvimento de Sistemas no 4º semestre, na matéria de orientação a objetos. Desenvolvido em python.
### Item 1
    Desenvolva em Python a classe de nome CodigoPostal, cujo objetos sejam capazes de guardar o código postal de uma dada rua. Note que cada Código Postal é constituído por dois números inteiros, que designaremos respectivamente por "indicativo" e "extensão" e o nome da rua (Ex: 38408-046 Armando Lombardi).
    Implemente também o método mostra(), cuja evocação, permita visualizar a informação relativa a um determinado código postal no formato:  CEP: 38408 - 046 Armando Lombardi
    Escreva um programa de teste para a classe CodigoPostal. Crie várias instâncias da classe e teste o objeto.
### Item 2 
    Escreva uma classe em Python para representar um Horário. Esta classe deve conter dois atributos do tipo inteiro denominados de hora e minuto. Faça também:
    a. Um método para incrementar o horário em uma hora, note que se a hora for 23, passamos para o próximo dia, portanto a hora deverá ser 0.
    b. Método para decrementar o horário em uma hora, note que se a hora for 0 ela deverá voltar às 23 horas.
    c. Método para decrementar o horário em um minuto. Faça as consistências necessárias.
    d. Método para incrementar o horário em um minuto. Faça as consistências necessárias.
    e. Método para retornar o horário na forma de string (hh:mm).
    f. Método que verifica se o horário representa um valor “antes do meio dia” ou “após o meio dia”. O método retorna “AM” ou “PM”
### Item 3 
    Escreva uma classe em Python que represente um voo. O voo possui no máximo 100 passageiros e a classe deve controlar a ocupação das vagas. Os dados do voo devem ser: o número do voo, o horário do voo (pode ser uma string) e uma forma para representar os assentos livres e ocupados (pode ser lista, string ou alguma outra estrutura). Faça ainda os seguintes métodos:

    * getProximoAssento() – retorna o número do assento livre mais próximo, a partir do assento número 1;
    * veficarAssento(numassento) – verifica se o número do assento recebido como parâmetro está ocupado, retorna um booleano;
    ocupar(numassento) – ocupa determinado assento do voo cujo número é recebido como parâmetro e retorna o resultado – 
    se o assento ainda não estiver ocupado retorna verdadeiro indicando operação bem sucedida, caso contrário retorna falso;
    * getVagas() – retorna o número de assentos vagos disponíveis (não ocupados) no voo;
    * getVoo() – retorna o número do voo;
    * getHoraVoo() – retorna a data do voo;
    * getMapaAssentos() – retorna uma string representando todos os 100 assentos do avião. Os assentos ocupados deverão ser representados por ‘0’ 
    e os livres por ‘1‘. Considere que os assentos estão disponibilizados em 4 fileiras com 25 assentos cada uma. 

* Alessa Baptista dos Santos
