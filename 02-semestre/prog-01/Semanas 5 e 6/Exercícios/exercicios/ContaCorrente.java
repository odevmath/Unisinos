public class ContaCorrente{
    private int numConta;
    private double saldo;

    public int getNumConta(){
        return numConta;
    }
    public void setNumConta(int numConta){
        this.numConta = numConta;
        
    }
    
    public double getSaldo(){
        return saldo;
    }
    public void setSaldo (double saldo){
        this.saldo = saldo;
        
    }
    
     public String toString(){
          return "Numero da conta: " + getNumConta() + "\nSaldo atual: " + getSaldo();
          }
}