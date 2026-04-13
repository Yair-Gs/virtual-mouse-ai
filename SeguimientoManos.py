import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Inicializar Mediapipe para la detección de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Inicializar OpenCV para la captura de video
cap = cv2.VideoCapture(0)

# Obtener las dimensiones de la pantalla
screen_width, screen_height = pyautogui.size()

# Variables para rastrear el estado del clic, arrastre y la posición del cursor
is_clicking = False
is_dragging = False
last_x, last_y = None, None

# Factor de suavizado para el movimiento del cursor
smooth_factor = 0.2

# Distancia mínima para el arrastre entre el pulgar y el meñique
drag_threshold = 0.1  # Ajusta esta distancia según lo que necesites

# Distancia mínima para el clic derecho entre el pulgar y el dedo medio
right_click_threshold = 0.05  # Ajusta esta distancia según lo que necesites

while True:
    success, image = cap.read()
    if not success:
        break

    # Convertir la imagen a RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    # Dibujar los puntos de la mano y controlar el mouse
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        # Dimensiones de la imagen de la cámara
        h, w, _ = image.shape

        # Coordenadas del índice (Landmark 8), pulgar (Landmark 4), meñique (Landmark 20), y medio (Landmark 12)
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
        middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

        # Escalar coordenadas de la cámara a la pantalla
        x_screen = int(np.interp(index_tip.x, [0, 1], [0, screen_width]))
        y_screen = int(np.interp(index_tip.y, [0, 1], [0, screen_height]))

        # Suavizar el movimiento del cursor
        if last_x is not None and last_y is not None:
            x_screen = int(last_x + (x_screen - last_x) * smooth_factor)
            y_screen = int(last_y + (y_screen - last_y) * smooth_factor)

        # Mover el cursor
        pyautogui.moveTo(screen_width - x_screen, y_screen)  # Invertir eje X

        # Actualizar la última posición conocida
        last_x, last_y = x_screen, y_screen

        # Calcular la distancia entre el pulgar y el meñique
        distance_thumb_pinky = np.sqrt((thumb_tip.x - pinky_tip.x) ** 2 + (thumb_tip.y - pinky_tip.y) ** 2)

        # Detectar clic izquierdo si la distancia entre el índice y el pulgar es pequeña
        distance_index_thumb = np.sqrt((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2)
        if distance_index_thumb < 0.05:
            if not is_clicking:
                pyautogui.click()
                is_clicking = True
        else:
            is_clicking = False

        # Verificar si la distancia entre el pulgar y el meñique es menor que el umbral para activar el arrastre
        if distance_thumb_pinky < drag_threshold:
            if not is_dragging:
                pyautogui.mouseDown(button='left')  # Iniciar el arrastre
                is_dragging = True
        else:
            if is_dragging:
                pyautogui.mouseUp(button='left')  # Soltar el arrastre
                is_dragging = False

        # Calcular la distancia entre el pulgar y el dedo medio
        distance_thumb_middle = np.sqrt((thumb_tip.x - middle_tip.x) ** 2 + (thumb_tip.y - middle_tip.y) ** 2)

        # Detectar clic derecho si la distancia entre el pulgar y el medio es pequeña
        if distance_thumb_middle < right_click_threshold:
            pyautogui.rightClick()  # Realizar clic derecho

        # Dibujar los puntos en la imagen
        mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    else:
        # Restablecer la posición del cursor si la mano no es detectada
        last_x, last_y = None, None

    # Mostrar la imagen
    cv2.imshow("Hand Tracking", image)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()


