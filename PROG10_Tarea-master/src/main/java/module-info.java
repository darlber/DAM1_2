module org.example.prog10_tarea2 {
    requires javafx.controls;
    requires javafx.fxml;

    requires com.dlsc.formsfx;

    opens org.example.prog10_tarea to javafx.fxml;
    exports org.example.prog10_tarea;
}