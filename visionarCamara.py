import cv2
import mediapipe as mp

# Inicializa MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

# Función para procesar los frames y detectar las manos
def process_frame(image):
    # Convierte la imagen de BGR a RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Procesa la imagen para detectar las manos
    results = hands.process(image)
    # Convierte de vuelta a BGR para mostrarla
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Dibuja las manos detectadas
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return image

def main():
    # Inicia la captura de video
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            # Procesa cada frame
            processed_frame = process_frame(frame)

            # Muestra el frame procesado
            cv2.imshow('MediaPipe Hands', processed_frame)

            # Rompe el bucle si se presiona 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Libera la captura de video y cierra las ventanas abiertas
        cap.release()
        cv2.destroyAllWindows()
        hands.close()  # Asegúrate de cerrar el objeto de manos de MediaPipe

if __name__ == "__main__":
    main()
