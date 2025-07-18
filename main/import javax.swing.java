import javax.swing.JFrame;

public class SimpleWindow {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Simple Window");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
