import org.opencv.core.*;
import org.opencv.highgui.Highgui;
import org.opencv.highgui.VideoCapture;


public class Test {
    public static void main(String[] args) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        VideoCapture camera = new VideoCapture(0);

        Mat frame = new Mat();
        camera.read(frame);
        Imshow im=new Imshow("title");

        if (!camera.isOpened()) {
            System.out.println("Error");
        } else {
            while (true) {
                if (camera.read(frame)) {
                    im.showImage(frame);
                }
            }
        }
        camera.release();
    }

}
