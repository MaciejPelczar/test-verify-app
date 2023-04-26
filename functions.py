import cv2
import numpy as np


# odszukuje tylko prostokątne kontury
def find_rect_contour(contours):

    rectangle_contours = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            # obwód konturu zamkniętego
            perimeter = cv2.arcLength(i, True)
            # punkty w których prawdopodobnie są wierzchołki konturu
            corners = cv2.approxPolyDP(i, 0.02 * perimeter, True)
            # print("corner points ", len(corners))
            if len(corners) == 4:
                rectangle_contours.append(i)
    # print(rectangle_contours)
    rectangle_contours = sorted(rectangle_contours, key=cv2.contourArea, reverse=True)

    return rectangle_contours


# szukanie rogów prostokąta
def get_corner_point(contour):
    # obwód konturu zamkniętego
    perimeter = cv2.arcLength(contour, True)
    # punkty w których prawdopodobnie są wierzchołki prostokąta
    corners = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    return corners


# uporządkowanie wierzchołków
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


# dzielenie pola odpowiedzi na osobne kwadraty
def split_boxes(img, q, ch):
    boxes = []
    rows = np.vsplit(img, q)
    for r in rows:
        cols = np.hsplit(r, ch)
        for box in cols:
            boxes.append(box)
            # cv2.imshow("split", box)

    return boxes


# pokolorowanie pola odpowiedzi, zielony dobra dopowiedz, czerwony zła
def show_answers(img, user_answer_indexes, verified_answers, correct_answers, questions, choices, rotate):
    # określenie wysokości i szerokości kratki
    section_width = int(img.shape[1]/choices)
    section_higth = int(img.shape[0]/questions)

    if rotate:
        n = choices
    else:
        n = questions
    # zaznaczenie kratek z odpowiedziami wypełniającego karte
    for x in range(n):
        if rotate:
            ans_temp = user_answer_indexes[x]
            centre_y = (ans_temp * section_higth) + (section_higth // 2)
            centre_x = (x * section_width) + (section_width // 2)
        else:
            ans_temp = user_answer_indexes[x]
            centre_x = (ans_temp * section_width) + (section_width // 2)
            centre_y = (x * section_higth) + (section_higth // 2)

        # kolor zaznaczenia jeśli grading jest 0  to kolor zaznaczenia na czerwono
        if verified_answers[x] == 1:
            rect_color = (0, 255, 0)
        else:
            # jesli zła odpowiedz to zaznaczmy ją na czerwono, a prawidłową na zielono, według correct_answers
            rect_color = (0, 0, 255)
            correct_answer = correct_answers[x]
            cv2.rectangle(img, (((correct_answer * section_width) + (section_width // 2)-65), centre_y-25),
                          (((correct_answer * section_width) + (section_width // 2)+65), centre_y+25),
                          (0, 255, 0), cv2.FILLED)

        # zaznaczenie na zdjeciu
        cv2.rectangle(img, (centre_x-65, centre_y-25), (centre_x+65, centre_y+25), rect_color, cv2.FILLED)

    return img

# def show_answers(img, user_answer_indexes, verified_answers, correct_answers, questions, choices):
#     # określenie wysokości i szerokości kratki
#     section_width = int(img.shape[1]/choices)
#     section_higth = int(img.shape[0]/questions)
#
#     # zaznaczenie kratek z odpowiedziami wypełniającego karte
#     for x in range(choices):
#         ans_temp = user_answer_indexes[x]
#         centre_y = (ans_temp * section_higth) + (section_higth // 2)
#         centre_x = (x * section_width) + (section_width // 2)
#
#         # kolor zaznaczenia jeśli grading jest 0  to kolor zaznaczenia na czerwono
#         if verified_answers[x] == 1:
#             rect_color = (0, 255, 0)
#         else:
#             # jesli zła odpowiedz to zaznaczmy ją na czerwono, a prawidłową na zielono, według correct_answers
#             rect_color = (0, 0, 255)
#             correct_answer = correct_answers[x]
#             cv2.rectangle(img, (((correct_answer * section_width) + (section_width // 2)-65), centre_y-25),
#                           (((correct_answer * section_width) + (section_width // 2)+65), centre_y+25),
#                           (0, 255, 0), cv2.FILLED)
#
#         # zaznaczenie na zdjeciu
#         cv2.rectangle(img, (centre_x-65, centre_y-25), (centre_x+65, centre_y+25), rect_color, cv2.FILLED)
#
#     return img

