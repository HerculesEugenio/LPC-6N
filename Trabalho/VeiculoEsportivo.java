package Classes;

public class VeiculoEsportivo extends Veiculo {

    public VeiculoEsportivo() {
    }

    public VeiculoEsportivo(int codigo, String placa, String modelo) {
        super(codigo, placa, modelo);
    }

    @Override
    public String toString() {
        return "VeiculoEsportivo{" + super.toString();
    }
 
    @Override
    public double valorDaDiaria(){
      return getValorBase()*1.5;
    };
}