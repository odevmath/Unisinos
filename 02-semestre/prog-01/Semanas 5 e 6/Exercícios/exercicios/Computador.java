public class Computador {
    private String marca;
    private double velocidade;
    private int anoFabricacao;
    private boolean novo;

    // Construtor da classe
    public Computador(String marca, double velocidade, int anoFabricacao, boolean novo) {
        this.marca = marca;
        this.velocidade = velocidade;
        this.anoFabricacao = anoFabricacao;
        this.novo = novo;
    }
    
    public Computador(String marca, int anoFabricacao){
        this.marca = marca;
        this.anoFabricacao = anoFabricacao;
        
    }

    // Getter e Setter para 'marca'
    public String getMarca() {
        return marca;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }

    // Getter e Setter para 'velocidade'
    public double getVelocidade() {
        return velocidade;
    }
    public void setVelocidade(double velocidade) {
        this.velocidade = velocidade;
    }

    // Getter e Setter para 'ano'
    public int getAnoFabricacao() {
        return anoFabricacao;
    }
    public void setAnoFabricacao(int anoFabricacao) {
        this.anoFabricacao = anoFabricacao;
    }

    // Getter e Setter para 'novo'
    public boolean isNovo() {
        return novo;
    }
    public void setNovo(boolean novo) {
        this.novo = novo;
    }

    // Método para exibir as informações do computador
    public void exibirInformacoes() {
        System.out.println("Marca: " + marca);
        System.out.println("Velocidade: " + velocidade + " MHz");
        System.out.println("Ano: " + anoFabricacao);
        System.out.println("É novo: " + (novo ? "Sim" : "Não"));
    }
}
