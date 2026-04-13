# 🖐️ Control de Cursor por Gestos de la Mano

## 🧠 Descripción del Proyecto
Aplicación desarrollada en Python que permite controlar el cursor del computador mediante movimientos de la mano en tiempo real. Utiliza visión artificial para detectar gestos a través de una cámara, reemplazando completamente el uso del mouse tradicional.

---

## ⚙️ Tecnologías utilizadas
- Python  
- OpenCV  
- MediaPipe  
- PyAutoGUI  

---

## 🐍 Versión de Python recomendada
- **Python 3.10 ✅**

---

## 🚀 Funcionalidades
- Detección de la mano en tiempo real  
- Control del cursor con movimientos  
- Clic izquierdo y derecho  
- Arrastrar y seleccionar  
- Interacción sin mouse físico  

---

## 🔧 Instalación

Instalar dependencias necesarias:

```bash
pip install opencv-python pyautogui
pip uninstall mediapipe
pip install mediapipe==0.10.8
```
## ▶️ Ejecución

Ejecutar el programa con:

```bash
python SeguimientoManos.py
```
## 🧩 Cómo funciona

Se detectan los puntos clave de la mano en tiempo real usando MediaPipe.

OpenCV procesa la imagen de la cámara y calcula posiciones.

Los movimientos se convierten en acciones del mouse mediante PyAutoGUI.

---

## 💡 Valor del proyecto

Permite controlar el computador sin mouse físico, mejorando la accesibilidad e introduciendo interacción basada en gestos.
