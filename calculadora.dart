
void main() {  
  Tela tela = new Tela();
  String imput = 'm'.toUpperCase();
  List <num> nume = [1,2];
  String cont='s'.toUpperCase();
  
  tela.mostrar(imput,nume,cont);
  
}

class Tela {     
  void mostrar(String imput, List nume,String cont){
    Calculadora calc = new Calculadora();
    
    print('-------------Menu-------------'); 
    print('Escolha uma das opçoes a baixo'); 
    print('S) somar');
    print('SU) subtraçao');
    print('D) divisão');
    print('M) Multiplicação');
    print('------------------------------');
    print('digite o primeiro numero');
    print('digite o segundo numero');
    print('-------------------------------');
    switch (imput){
        case'S':{print('Somando..... ${calc.somar(nume.first,nume.last)}');}
          break;
        case'SU':{print('Subtraindo...... ${calc.subtrair(nume.first,nume.last)}');}
          break;
        case'D':{print('Dividindo........ ${calc.divi(nume.first,nume.last)}');}
          break;
        case'M':{print('Multiplicando......... ${calc.divi(nume.first,nume.last)}');}
          break;
      default:{
        print('digite uma das opçoes do menu');
      }
    }
  }
}





class Calculadora {
 num somar(num valor1, num valor2) {
   return valor1 + valor2;
  }
 num subtrair(num valor1, num valor2) {
   return valor1 - valor2;
 }
 num mult(num valor1,num valor2) {
   return valor1 * valor2;
 }
 num divi(num valor1,num valor2) {
   return valor1 / valor2;
 }
}
