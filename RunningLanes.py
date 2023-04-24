import cv2

lane_positions = [100, 200, 300, 400]

finish_line = 500

fgbg = cv2.createBackgroundSubtractorMOG2()


timers = {lane: 0 for lane in range(len(lane_positions))}
results = {}


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break


    fgmask = fgbg.apply(frame)


    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)


    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for i, y in enumerate(lane_positions):
        cv2.line(frame, (0, y), (frame.shape[1], y), (0, 255, 0), 2)
    cv2.line(frame, (finish_line, 0), (finish_line, frame.shape[0]), (255, 0, 0), 2)


    for contour in contours:

        x, y, w, h = cv2.boundingRect(contour)


        lane = None
        for i, y in enumerate(lane_positions):
            if y <= (y + h // 2) <= (y + h):
                lane = i
                break

        if lane is not None and x + w >= finish_line:
            if lane not in results:
                results[lane] = []
            results[lane].append(cap.get(cv2.CAP_PROP_POS_MSEC))
            timers[lane] += 1


        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        if lane is not None:
            cv2.putText(frame, str(lane), (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)


    cv2.imshow('frame', frame)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


for lane, times in results.items():
    print(f"Lane {lane+1} times: {times}")
