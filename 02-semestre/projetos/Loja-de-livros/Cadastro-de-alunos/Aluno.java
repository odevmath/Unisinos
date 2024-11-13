public class Aluno{
    private String nome;
    private String matricula;
    private double grauA;
    private double grauB;
    
    // Construtor
    public Aluno(String nome, String matricula, int grauA, int grauB){
        this.nome = nome;
        this.matricula = matricula;
        this.grauA = grauA;
        this.grauB = grauB;
    }
    
    // Getters e Setters
    public String getNome(){
        return nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public String getMatricula(){
        return matricula;
    }
    public void setMatricula(String matricula){
        this.matricula = matricula;
    }
    
    public double getGrauA(){
        return grauA;
    }
    public void setGrauA(double grauA){
        this.grauA = grauA;
    }
    
    public double getGrauB(){
        return grauB;
    }
    public void setGrauB(double grauB){
        this.grauB = grauB;
    }
    
     // Método para calcular a média final
    public double calculaMediaFinal() {
        double media = (grauA * 0.33) + (grauB * 0.67); // A variável media agora tem esse nome
        return media;
    }
    
    // Método para imprimir informações do aluno
    public void imprimeInfo() {
        double mediaFinal = calculaMediaFinal(); // Calculando a média usando o método
        System.out.printf("Nome: %s\n", nome);
        System.out.printf("Matrícula: %s\n", matricula);
        System.out.printf("Nota Grau A: %.2f\n", grauA);
        System.out.printf("Nota Grau B: %.2f\n", grauB);
        System.out.printf("Média Final: %.2f\n", mediaFinal);
    }
}



