public class Produto {
    private String nome, descricao;
    private double valor;
    private int quantidade;
    
    public Produto (String nome, double valor, String descricao, int quantidade){
        this.nome = nome;
        this.valor = valor;
        this.descricao = descricao;
        this.quantidade = quantidade;
    }
    
    public Produto(String nome, double valor){
        this.nome = nome;
        this.valor = valor;
    
    }
}