import cv2
import numpy as np


def find_rect_contour(contours):

    rectangle_contours = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            perimeter = cv2.arcLength(i, True)
            corners = cv2.approxPolyDP(i, 0.02 * perimeter, True)
            if len(corners) == 4:
                rectangle_contours.append(i)
    rectangle_contours = sorted(rectangle_contours, key=cv2.contourArea, reverse=True)

    return rectangle_contours


def get_corner_point(contour):
    perimeter = cv2.arcLength(contour, True)
    corners = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    return corners


def reorder_cores(points):
    points = points.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), np.int32)
    add = points.sum(1)
    new_points[0] = points[np.argmin(add)]  # [0, 0]
    new_points[3] = points[np.argmax(add)]  # [w, h]
    diff = np.diff(points, axis=1)
    new_points[1] = points[np.argmin(diff)]  # szerokość i zero [w, 0]
    new_points[2] = points[np.argmax(diff)]  # zero i wysokość [0, h]

    return new_points


def split_boxes(img, q, ch):
    boxes = []
    rows = np.vsplit(img, q)
    for r in rows:
        cols = np.hsplit(r, ch)
        for box in cols:
            boxes.append(box)

    return boxes


def show_answers(img, user_answer_indexes, verified_answers, correct_answers, questions, choices, rotate):
    section_width = int(img.shape[1]/choices)
    section_high = int(img.shape[0]/questions)

    if rotate:
        n = choices
    else:
        n = questions

    for x in range(n):
        if rotate:
            ans_temp = user_answer_indexes[x]
            centre_y = (ans_temp * section_high) + (section_high // 2)
            centre_x = (x * section_width) + (section_width // 2)
        else:
            ans_temp = user_answer_indexes[x]
            centre_x = (ans_temp * section_width) + (section_width // 2)
            centre_y = (x * section_high) + (section_high // 2)

        if verified_answers[x] == 1:
            rect_color = (0, 255, 0)
        else:
            rect_color = (0, 0, 255)
            correct_answer = correct_answers[x]
            cv2.rectangle(img, (((correct_answer * section_width) + (section_width // 2)-65), centre_y-25),
                          (((correct_answer * section_width) + (section_width // 2)+65), centre_y+25),
                          (0, 255, 0), cv2.FILLED)

        cv2.rectangle(img, (centre_x-65, centre_y-25), (centre_x+65, centre_y+25), rect_color, cv2.FILLED)

    return img
