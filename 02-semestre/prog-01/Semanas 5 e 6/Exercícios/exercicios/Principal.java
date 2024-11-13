public class Principal{
  public static void main(String[] args){
      //Conta 1
      ContaCorrente c1 = new ContaCorrente();
      c1.setNumConta(1234);
      c1.setSaldo (100.00);
      
      //Conta 1
      ContaCorrente c2 = new ContaCorrente();
      c2.setNumConta(8765);
      c2.setSaldo (-98.00);
      
      //Conta 1
      ContaCorrente c3 = new ContaCorrente();
      c3.setNumConta(3342);
      c3.setSaldo (3445.80);
      
      //Exibindo as informaão
      System.out.println(c1);
      System.out.println(c2);
      System.out.println(c3);
  }
  
 
  
 
}