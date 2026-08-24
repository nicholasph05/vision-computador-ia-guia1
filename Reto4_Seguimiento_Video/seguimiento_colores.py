import cv2
import numpy as np

# Abrir la cámara
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

print("Cámara abierta correctamente.")
print("Presiona Q para cerrar.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo leer el frame.")
        break

    # Convertir de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # =========================================================
    # COLOR ROJO
    # =========================================================

    rojo_bajo1 = np.array([0, 120, 70])
    rojo_alto1 = np.array([10, 255, 255])

    rojo_bajo2 = np.array([170, 120, 70])
    rojo_alto2 = np.array([180, 255, 255])

    mascara_rojo1 = cv2.inRange(hsv, rojo_bajo1, rojo_alto1)
    mascara_rojo2 = cv2.inRange(hsv, rojo_bajo2, rojo_alto2)

    mascara_rojo = cv2.bitwise_or(
        mascara_rojo1,
        mascara_rojo2
    )

    # Buscar contornos rojos
    contornos_rojos, _ = cv2.findContours(
        mascara_rojo,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contorno in contornos_rojos:

        area = cv2.contourArea(contorno)

        if area > 500:

            x, y, w, h = cv2.boundingRect(contorno)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                2
            )

            cv2.putText(
                frame,
                "ROJO",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

    # =========================================================
    # COLOR VERDE
    # =========================================================

    verde_bajo = np.array([35, 80, 50])
    verde_alto = np.array([85, 255, 255])

    mascara_verde = cv2.inRange(
        hsv,
        verde_bajo,
        verde_alto
    )

    contornos_verdes, _ = cv2.findContours(
        mascara_verde,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contorno in contornos_verdes:

        area = cv2.contourArea(contorno)

        if area > 500:

            x, y, w, h = cv2.boundingRect(contorno)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "VERDE",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    # =========================================================
    # COLOR AZUL
    # =========================================================

    azul_bajo = np.array([90, 80, 50])
    azul_alto = np.array([130, 255, 255])

    mascara_azul = cv2.inRange(
        hsv,
        azul_bajo,
        azul_alto
    )

    contornos_azules, _ = cv2.findContours(
        mascara_azul,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contorno in contornos_azules:

        area = cv2.contourArea(contorno)

        if area > 500:

            x, y, w, h = cv2.boundingRect(contorno)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            cv2.putText(
                frame,
                "AZUL",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

    # =========================================================
    # MOSTRAR RESULTADOS
    # =========================================================

    cv2.imshow(
        "Seguimiento de figuras por color",
        frame
    )

    cv2.imshow(
        "Mascara roja",
        mascara_rojo
    )

    cv2.imshow(
        "Mascara verde",
        mascara_verde
    )

    cv2.imshow(
        "Mascara azul",
        mascara_azul
    )

    # Presionar Q para cerrar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()