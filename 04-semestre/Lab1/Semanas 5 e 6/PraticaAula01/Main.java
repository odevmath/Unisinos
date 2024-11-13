public class Main{
    public static void main(String[] args){
        int x; // declara uma variavel denominada "x"
        String nome; //declara uma variavel do tipo String chamada "nome"
        double altura; //declara uma variavel chamada altura do tipo double
        char opcao; //declara uma variavel do tipo char chamada opcao
        
        x = 10;
        nome = "Matheus";
        altura = 1.69;
        opcao = 'M';
        
        System.out.println ("Texto aleatorio");
        System.out.println(x);
        System.out.println(nome);
        System.out.println(altura);
        System.out.println("A opçao escolhida foi " + opcao);
        System.out.println("A pessoa de nome " + nome + " possui " + altura + " metros de altura");
    }
}