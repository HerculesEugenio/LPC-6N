package Classes;

public abstract class Veiculo {
    private int codigo;
    private String placa, modelo;
    private static double valorBase;

    public Veiculo() {}

    public Veiculo(int codigo, String placa, String modelo) {
        this.codigo = codigo;
        this.placa = placa;
        this.modelo = modelo;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public static double getValorBase() {
        return valorBase;
    }

    public static void setValorBase(double valorBase) {
        Veiculo.valorBase = valorBase;
    }
    
    public String toString() {
        return "codigo=" + codigo + ", placa=" + placa + ", modelo=" + modelo + ", valorBase=" + valorBase + '}';
    }   
    public abstract double valorDaDiaria();
}