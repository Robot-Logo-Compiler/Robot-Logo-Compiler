import java.io.FileInputStream;
import java.util.Properties;
import lejos.nxt.*;
import lejos.robotics.navigation.DifferentialPilot;

public class Main {

    public static void main(String[] args) {
        
        DifferentialPilot pilot = init();
        
        try {
            Properties prop = new Properties();
            prop.load(new FileInputStream("config.properties"));
            float wheelDiameter = Float.valueOf(prop.getProperty("wheelDiameter")) * 0.393700787f;
            float trackWidth = Float.valueOf(prop.getProperty("trackWidth")) * 0.393700787f;
            double travelSpeed = Double.valueOf(prop.getProperty("travelSpeed"));
            double rotatingSpeed = Double.valueOf(prop.getProperty("rotatingSpeed"));
            pilot = init(wheelDiameter, trackWidth);
            setTravelSpeed(pilot, travelSpeed);
            setRotatingSpeed(pilot, rotatingSpeed);
            
        } catch (Exception e) {
            // use default values
            setTravelSpeed(pilot, 5.0);
            setRotatingSpeed(pilot, 30.0);
        }


        // insert generated code here


    }

    private static DifferentialPilot init(float wheelDiameter, float trackWidth) {

        return new DifferentialPilot(wheelDiameter, 0.5*trackWidth, Motor.A, Motor.B);
    }

    private static DifferentialPilot init() {

        return new DifferentialPilot(2.165f, 0.5*8.46f, Motor.A, Motor.B); // default values in inches

    }

    private static void travel(DifferentialPilot plt, float distance) {
        
        plt.travel(distance);
    }

    private static void rotate(DifferentialPilot plt, double angle) {

        plt.rotate(angle);
    }

    private static void printToLCD(String text) {
        
        LCD.drawString(text, 0, 0);
    }
    
    private static void setTravelSpeed(DifferentialPilot plt, double travelSpeed) {
        plt.setLinearSpeed(travelSpeed);
    }
    
    private static void setRotatingSpeed(DifferentialPilot plt, double angularSpeed) {
        plt.setAngularSpeed(angularSpeed);
    }
}
