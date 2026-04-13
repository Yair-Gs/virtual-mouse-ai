# 🖐️ Control de Cursor por Gestos de la Mano

## 🧠 Descripción del Proyecto
Aplicación desarrollada en Python que permite controlar el cursor del computador mediante movimientos de la mano en tiempo real. Utiliza visión artificial para detectar gestos a través de una cámara, reemplazando completamente el uso del mouse tradicional.

---

## ⚙️ Tecnologías utilizadas
- Python  
- OpenCV (procesamiento de imágenes)  
- MediaPipe (detección de manos y gestos)  
- PyAutoGUI (control del cursor)  

---

## 🚀 Funcionalidades
- Detección de la mano en tiempo real mediante cámara  
- Seguimiento de los movimientos de la mano  
- Control del cursor en pantalla  
- Simulación de clic izquierdo y derecho  
- Función de arrastrar y seleccionar  
- Interacción sin necesidad de dispositivos físicos  

---

## 🔧 Instalación
Instalar las dependencias necesarias:

```bash
pip install opencv-python mediapipe pyautogui
```
## ▶️ Ejecución

Ejecutar el programa con:

```bash
python main.py
```
## 🧩 Cómo funciona

El sistema utiliza la librería **MediaPipe** para detectar puntos clave de la mano en tiempo real a través de la cámara.  

Luego, con **OpenCV**, se procesan las imágenes capturadas para interpretar los movimientos.  

Estos movimientos se traducen en acciones del cursor mediante **PyAutoGUI**, permitiendo mover el puntero, hacer clic y realizar otras funciones básicas.  

El sistema está optimizado para trabajar en tiempo real, brindando una interacción fluida entre el usuario y el computador.

---

## 💡 Valor del proyecto

Este proyecto ofrece una alternativa innovadora de interacción humano-computadora, mejorando la accesibilidad para personas con limitaciones físicas y eliminando la dependencia de dispositivos tradicionales como el mouse.  

Además, aporta al desarrollo de interfaces más naturales e intuitivas basadas en visión artificial.
