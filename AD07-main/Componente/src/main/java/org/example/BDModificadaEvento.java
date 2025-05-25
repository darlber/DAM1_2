package org.example;

import java.util.EventObject;

public class BDModificadaEvento extends EventObject {
    private final boolean modo;
    // Constructor que recibe el objeto fuente del evento
    public BDModificadaEvento(Object source, boolean modo) {
        super(source);
        this.modo = modo;
    }

    public boolean isModo() {
        return modo;
    }
}
