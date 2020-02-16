package Classes;

public class VeiculoUtilitario extends Veiculo {

    public VeiculoUtilitario() {
    }

    public VeiculoUtilitario(int codigo, String placa, String modelo) {
        super(codigo, placa, modelo);
    }

    @Override
    public String toString() {
        return "VeiculoUtilitario{" + super.toString();
    }
    
    @Override
    public double valorDaDiaria(){
      return getValorBase()*1.3;
    };

}
