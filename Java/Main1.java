public class Main1 {
    String name;

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
        System.out.println("Hallo Welt");
        Main1 m = new Main1();
        m.setName("test");
        
    }
}