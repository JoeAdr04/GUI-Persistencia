
package persistencia;

import java.io.ObjectOutputStream;
import java.io.FileOutputStream;
import java.io.Serializable;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

public class ArchEmpleado implements Serializable{
    private String nombre;
    
    public ArchEmpleado(String nombre){
        this.nombre = nombre;
    }
    
    public void crear() {
        File archivoFisico = new File(this.nombre);
        if (!archivoFisico.exists()) {//pregunta si el archivo existe
            try {//manejo de exepciones
                ObjectOutputStream archivo = new ObjectOutputStream(new FileOutputStream(this.nombre));
                archivo.close(); //cerrar archivo
                System.out.println("Archivo creado porque no existia.");
            } catch (IOException e) {
                System.out.println("Error al crear archivo: " + e.getMessage());
            }
        } else {
            System.out.println("Archivo ya existe, no se modifico.");
        }
    }

    public void adicionar(Empleado emp)throws IOException, ClassNotFoundException{
        ObjectOutputStream archivo  = null;
        try{
            if(!new File(this.nombre).exists()){
                archivo = new ObjectOutputStream(new FileOutputStream(this.nombre, true));
            }
            else{
                archivo = new AddObjectOutputStream(new FileOutputStream(this.nombre, true));
            }
            archivo.writeObject(emp);
            System.out.println("se logro adicioonar...");
        }
        catch(Exception e){
            System.out.println("No se logro adicionar");
        }
        finally{
            archivo.close();
        }
    }   
    
    public Object[][] listar()throws ClassNotFoundException, IOException{
        Object[][] mat=new Object[100][4];
        ObjectInputStream archivo = null;
        int n = 0;
        try{
            archivo =  new ObjectInputStream(new FileInputStream(this.nombre));
            while(true){
                 Empleado emp = new Empleado();
                 emp = (Empleado) archivo.readObject();
                 mat[n][0]= emp.getItem();
                 mat[n][1]= emp.getPaterno();
                 mat[n][2]= emp.getMaterno();
                 mat[n][3]= emp.getNombre();
                 n++;
            }
        }
        catch(Exception e){
            System.out.println("Fin del listado");
        }
        finally{
            archivo.close();
        }
        return mat;
    }
    public void eliminar(int item) throws IOException, ClassNotFoundException{
        ObjectInputStream archivo = null;
        ObjectOutputStream copia = null;
        try{
            archivo = new ObjectInputStream(new FileInputStream(this.nombre));
            copia = new ObjectOutputStream(new FileOutputStream("src/persistencia/copia.dat", true));
            while(true){
                Empleado emp=new Empleado();
                emp = (Empleado) archivo.readObject();
                if(emp.getItem() != item){
                    copia.writeObject(emp);
                }
            }
        }
        catch(Exception e){
            System.out.println("fin del proceso de eliminacion");
        }
        finally{
            copia.close();
            archivo.close();
            File f1 = new File(this.nombre);
            File f2 = new File ("src/persistencia/copia.dat");
            f1.delete();
            f2.renameTo(f1);
        }
    }
    public void editar(int item, Empleado nuevoEmpleado) throws IOException, ClassNotFoundException {
        ObjectInputStream archivo = null;
        ObjectOutputStream copia = null;
        try {
            archivo = new ObjectInputStream(new FileInputStream(this.nombre));
            copia = new ObjectOutputStream(new FileOutputStream("src/persistencia/copia.dat", true));
            while (true) {
                Empleado emp = (Empleado) archivo.readObject();
                if (emp.getItem() == item) {
                    copia.writeObject(nuevoEmpleado);
                } else {
                    copia.writeObject(emp);
                }
            }
        } catch (Exception e) {
            System.out.println("Fin del proceso de edicion.");
        } finally {
            if (archivo != null) archivo.close();
            if (copia != null) copia.close();
            // Reemplazamos el archivo original
            File original = new File(this.nombre);
            File temp = new File("src/persistencia/copia.dat");
            original.delete();
            temp.renameTo(original);
        }
    }
}
