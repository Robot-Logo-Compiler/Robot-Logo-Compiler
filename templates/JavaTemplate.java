import lejos.nxt.*;
import lejos.robotics.navigation.DifferentialPilot;

public class Main {

    public static void main(String[] args) {

        DifferentialPilot pilot = init();
        pilot.setTravelSpeed(5.0);
        pilot.setRotateSpeed(30.0);

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
}
