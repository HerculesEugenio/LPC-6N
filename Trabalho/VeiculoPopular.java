package Classes;

public class VeiculoPopular extends Veiculo {

    public VeiculoPopular() {
    }

    public VeiculoPopular(int codigo, String placa, String modelo) {
        super(codigo, placa, modelo);
    }

    @Override
    public String toString() {
        return "VeiculoPopular{" + super.toString();
    }
    
    @Override
    public double valorDaDiaria(){
      return getValorBase();
    };
}
