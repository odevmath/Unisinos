public class Fruta{
    //Atributos da classe
    private String nome;
    private double preco;
    
    /*Construtor da classe Fruta, que recebe dois parâmetros: nome e preço
    e inicializa os atributos correspondentes*/
    public Fruta(String nome, double preco){
        this.nome = nome;
        this.preco = preco;
    }
    
    //Getters e Setters:
    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }
    
    public double getPreco(){
        return preco;
    }

    public void setPreco(double preco){
        this.preco = preco;
    }
    
    public double calculaPreco(double imposto){
        return preco + (preco * imposto);
    }
}
