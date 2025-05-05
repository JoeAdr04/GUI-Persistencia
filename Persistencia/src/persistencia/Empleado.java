package persistencia;

import java.io.Serializable;

public class Empleado implements Serializable{
    private String paterno;
    private String materno;
    private String nombre;
    private int item;
    public Empleado(){
        this.paterno = "";
        this.materno = "";
        this.nombre="";
        this.item = 0;
    }
    public Empleado(int i, String pat, String mat, String nom){
        this.paterno = pat;
        this.materno = mat;
        this.nombre=nom;
        this.item = i;
    }
    public String getPaterno() {return paterno;}
    public String getMaterno() {return materno;}
    public String getNombre() {return nombre;}
    public int getItem() {return item;}
    public void setPaterno(String paterno) {this.paterno = paterno;}
    public void setMaterno(String materno) {this.materno = materno;}
    public void setNombre(String nombre) {this.nombre = nombre;}
    public void setItem(int item) {this.item = item;}
    @Override
    public String toString() {
        return "Empleado{" + "paterno=" + paterno + ", materno=" + materno + ", nombre=" + nombre + ", item=" + item + '}';
    }
}
