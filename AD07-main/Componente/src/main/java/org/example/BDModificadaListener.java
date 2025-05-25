package org.example;

import java.util.EventListener;

// Interfaz para los oyentes de eventos de base de datos modificada
public interface BDModificadaListener extends EventListener {
    // Método que se invoca cuando ocurre una modificación en la base de datos
    void capturarBDModificada(BDModificadaEvento ev);
}
