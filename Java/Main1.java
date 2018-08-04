import java.net.ConnectException;
import java.sql.DriverManager;
import java.sql.Connection;

public class Main1 {
    String name="test";

    public Main1() {
    }

    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @param name the name to set
     */ 
    public void setName(String name) {
        this.name = name;
    }

    public static void main(String[] args) {
        System.out.println("Hallo Welt!");
        Main1 m = new Main1();
        m.setName("test");


        
        Connection myConnection;
        try {
            myConnection = (Connection)DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","");
            System.out.println("My Connection is:"+myConnection);
            myConnection.close();
            int  a=5;
            System.out.println("a="+a);
            a++;
            System.out.println("a="+a);
        } catch (Exception e) {
            System.out.println("Exceptoin:"+e);
        }
        
    }
}