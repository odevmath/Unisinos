public class PrincipalAluno {
    public static void main(String[] args) {
        // Criando os 3 alunos
        Aluno aluno1 = new Aluno("Brandamente", "1585258", 5, 9);
        Aluno aluno2 = new Aluno("Radigunda", "2254879", 8, 2);
        Aluno aluno3 = new Aluno("Vitimado José Araújo", "0085994", 7, 1);

        // Imprimindo as informações de cada aluno
        aluno1.imprimeInfo();
        System.out.println();
        aluno2.imprimeInfo();
        System.out.println();
        aluno3.imprimeInfo();
        System.out.println();

        // Alterando a nota do Grau A de Radigunda para 9
        aluno2.setGrauA(9);

        // Imprimindo apenas a média final de Radigunda
        System.out.printf("Média Final de Radigunda: %.2f\n", aluno2.calculaMediaFinal());
        System.out.println();

        // Imprimindo somente a matrícula de Vitimado
        System.out.printf("Matrícula de Vitimado: %s\n", aluno3.getMatricula());
        System.out.println();

        // Alterando a matrícula de Brandamente para 1585228
        aluno1.setMatricula("1585228");

        // Lendo nova nota do Grau B para Radigunda usando a classe Teclado
        double novaNotaGB = Teclado.leDouble("Digite a nova nota do Grau B para Radigunda: ");
        aluno2.setGrauB(novaNotaGB);

        // Imprimindo as informações de Radigunda após as alterações
        System.out.println("\nInformações atualizadas de Radigunda:");
        aluno2.imprimeInfo();
    }
}