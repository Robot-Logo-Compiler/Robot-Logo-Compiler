import lejos.nxt.*;

public class Main {

    public static void main(String[] args) {

        init();

        // insert generated code here


    }

    private static void init(int speed) {

        Motor.A.setSpeed(speed);
        Motor.B.setSpeed(speed);
    }

    private static void init() {

        Motor.A.setSpeed(100);
        Motor.B.setSpeed(100);

    }

    private static void moveForward(int amount) {

        Motor.A.forward();
        Motor.B.forward();
        Delay.msDelay(500 * amount);
        Motor.A.stop();
        Motor.B.stop();

    }

    private static void moveBackward(int amount) throws InterruptedException {

        Motor.A.backward();
        Motor.B.backward();
        Delay.msDelay(500 * amount);
        Motor.A.stop();
        Motor.B.stop();
        
    }

    private static void rotate(int angle) {

        Motor.A.rotate(angle);
        Motor.B.rotate(-1 * angle);
    }

    private static void printToLCD(String text) {
        
        LCD.drawString(text, 0, 0);
    }


}