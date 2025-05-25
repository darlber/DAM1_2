public class Circulo {

    /**
     * 
     */
    private double radio;
    private String color;
    public static int numCirculos;

    //metodo constructor
    /**
     * 
     * @param radio
     * @param color 
     */
    
    public Circulo(double radio, String color) {
        this.radio = radio;
        this.color = color;
    }

    //encapsulación
    /**
     * 
     * @return get radio
     */
    public double getRadio() {
        return radio;
    }
/**
 * 
 * @param radio 
 */
    public void setRadio(double radio) {
        this.radio = radio;
    }
/**
 * 
 * @return get color
 */
    public String getColor() {
        return color;
    }
/**
 * 
 * @param color 
 */
    public void setColor(String color) {
        this.color = color;
    }

    /**
     * 
     * @return int numCirculos
     */
    public static int getNumCirculos() {
        return numCirculos;
    }

    /**
     * 
     * @param numCirculos 
     */
    public static void setNumCirculos(int numCirculos) {
        Circulo.numCirculos = numCirculos;
    }
    
    /**
     * 
     * @return AreaCalculada
     */
    public double calculoArea(){
        if (this.radio<0)
            throw new IllegalArgumentException("Radio negativo");
        return (Math.pow(radio, 2)*Math.PI);
    }
    /**
     * 
     * @return Perimetro Calculado
     * @throws Exception 
     */
    public double calculoPerimetro()throws Exception{
        if (this.radio<0)
            throw new Exception ("Radio negativo");
        else if(radio>=100)
            throw new Exception ("Radio muy grande");
        else 
            return (2*Math.PI*this.radio);
    }
    
    /**
     * 
     * @return Si el color es aceptable
     * @throws Exception 
     */
    public boolean colorAceptable() throws Exception {
        if(color.length()>20){
            return false;
        }
        else{
            if(color.length()<=0){
                throw new Exception ("Color no existente");
            }
            return true;
        }       
    }
    
    
}
