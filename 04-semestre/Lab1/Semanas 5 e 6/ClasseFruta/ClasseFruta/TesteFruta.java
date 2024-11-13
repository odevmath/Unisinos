public class TesteFruta{
    public static void main (String [] args){
        Fruta f1 = new Fruta ("Maça", 1.80);
        System.out.println("O preço da " +f1.getNome()+ " é R$" + String.format("%.2f", f1.getPreco()));
        
        f1.setNome("Uva");
        f1.setPreco(3.40);
        System.out.println("O produto foi alterado para " + f1.getNome() + " e o seu valor é R$" + String.format("%.2f", f1.getPreco()));
                
        Fruta f2 = new Fruta ("Banana", 5.90);
        System.out.println("O preço da " +f2.getNome()+ " é R$" + String.format("%.2f", f2.getPreco()));

          
        Fruta f3 = new Fruta ("Laranja", 2.50);
        System.out.println("O preço da " +f3.getNome()+ " é R$" + String.format("%.2f", f3.getPreco()));
        
        System.out.println("\nVeja abaixo o preço das frutas com imposto de 12% incluso:");
        double imposto = 0.12;
        
        System.out.println("-> " + f1.getNome() + ": R$" + String.format("%.2f", f1.calculaPreco(imposto)));
        System.out.println("-> " + f2.getNome() + ": R$" + String.format("%.2f", f2.calculaPreco(imposto)));
        System.out.println("-> " + f3.getNome() + ": R$" + String.format("%.2f", f3.calculaPreco(imposto)));
    }
}