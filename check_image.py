from cv2 import cv2
import numpy as np

import functions


def load_and_resize(image_path, image_width, image_height):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (image_width, image_height))
    return img


def find_contours(img2):
    img = img2.copy()
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_grey, (5, 5), 1)
    img_canny = cv2.Canny(img_blur, 10, 50)

    contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    return contours


def find_three_biggest_contours(contours):
    cont = []
    rect_contours = functions.find_rect_contour(contours)
    for i in range(3):
        cont.append(functions.get_corner_point(rect_contours[i]))
    return cont


def reorder_corners(contours):
    cont = []
    for i in range(3):
        cont.append(functions.reorder_cores(contours[i]))
    return cont


def warp_field(img2, contour, image_width, image_height, field_number):
    img = img2.copy()
    corners = np.float32(contour[field_number])
    img_corners = np.float32([[0, 0], [image_width, 0], [0, image_height], [image_width, image_height]])
    matrix = cv2.getPerspectiveTransform(corners, img_corners)
    img_warp_field = cv2.warpPerspective(img, matrix, (image_width, image_height))
    return img_warp_field


def binary_and_split(img, questions, choices):
    warp = img.copy()
    img_warp_grey = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
    img_warp_thresh = cv2.threshold(img_warp_grey, 170, 255, cv2.THRESH_BINARY_INV)[1]
    boxes = functions.split_boxes(img_warp_thresh, questions, choices)
    return boxes


def check_line(boxes, questions, choices, reverse):
    pixel_value = np.zeros((questions, choices))
    count_for_col = 0
    count_for_rows = 0
    # liczymy piksele( im wiecej białych tym wiekszy wynik)
    for i in boxes:
        total_pixels = cv2.countNonZero(i)
        pixel_value[count_for_rows][count_for_col] = total_pixels
        count_for_col += 1
        if count_for_col == choices:
            count_for_rows += 1
            count_for_col = 0
    if reverse:
        pixel_value = pixel_value.T
    print(pixel_value)
    return pixel_value


def find_idexes_of_marked_boxes(questions, choices, pixel_value, rotate):
    marked_indexes = []
    if rotate:
        n = choices
    else:
        n = questions

    for x in range(n):
        row_px_values = pixel_value[x] # mamy każdy rząd osobno
        index_max_px_value = np.where(row_px_values == np.amax(row_px_values))
        marked_indexes.append(index_max_px_value[0][0])
    print(marked_indexes)
    return marked_indexes


def check_if_correct(marked_indexes, correct_answers, questions):
    verified_answers = []
    for x in range(questions):
        if correct_answers[x] == marked_indexes[x]:
            verified_answers.append(1)
        else:
            verified_answers.append(0)
    print(verified_answers)
    percent_grade = (sum(verified_answers) / len(verified_answers)) * 100
    return verified_answers, percent_grade
    # print("procent to %0.2f" % percent_grade)


def save_colors_on_blank(img_answers_warp_colored, marked_indexes, verified_answers, correct_answers, questions,
                         choices, rotate):
    img_marks_on_blank = np.zeros_like(img_answers_warp_colored)
    img_marks_on_blank = functions.show_answers(img_marks_on_blank, marked_indexes, verified_answers, correct_answers,
                                                questions, choices, rotate)
    return img_marks_on_blank


def inverse_warp(img_marks_on_blank, contour, image_width, image_height, field_number):
    corners = np.float32(contour[field_number])
    img_corners = np.float32([[0, 0], [image_width, 0], [0, image_height], [image_width, image_height]])
    inverse_matrix = cv2.getPerspectiveTransform(img_corners, corners)
    img_inverse_warp = cv2.warpPerspective(img_marks_on_blank, inverse_matrix, (420, 600))
    return img_inverse_warp


def put_grade_on_blank(img_warp_colored, percent_grade):
    img_grade_on_blank = np.zeros_like(img_warp_colored)
    cv2.putText(img_grade_on_blank, str(int(percent_grade)) + "%", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255), 3)
    return img_grade_on_blank


def final_img_join(img_final, img_inverse_warp):
    img_final = cv2.addWeighted(img_final, 1, img_inverse_warp, 1, 0)
    return img_final


class CheckImage:
    def __init__(self, image_path, correct_answers):
        self.indexes = None
        self.img = None
        self.image_path = image_path
        self.correct_answers = correct_answers
        self.image_width = 420
        self.image_height = 600
        self.percentage = None

    def check_image(self):
        self.img = load_and_resize(self.image_path, self.image_width, self.image_height)
        img = self.img

        contours = find_contours(img)
        rect_contours = find_three_biggest_contours(contours)
        contours_reordered_corners = reorder_corners(rect_contours)
        answer = CheckField(img, contours_reordered_corners, self.image_width, self.image_height, 0, 12, 4,
                            self.correct_answers, False)
        student_id = CheckField(img, contours_reordered_corners, self.image_width, self.image_height, 1, 10, 5, None, True)
        # grade = CheckField(img, contours_reordered_corners, 300, 150, 2, 0, 0, None)
        answer.check_field()
        student_id.check_field()
        grade_wrap = warp_field(img, contours_reordered_corners, 300, 150, 2)

        grade_on_blank_warp = put_grade_on_blank(grade_wrap, answer.percent_grade)

        self.percentage = answer.percent_grade
        grade_on_blank = inverse_warp(grade_on_blank_warp, contours_reordered_corners, 300,
                                      150, 2)

        self.img = final_img_join(self.img, answer.img_colored_marks)
        self.img = final_img_join(self.img, student_id.img_colored_marks)
        self.img = final_img_join(self.img, grade_on_blank)

        self.indexes = student_id.indexes


class CheckField:
    def __init__(self, img, contour, image_width, image_height, field_number, questions, choices, correct_answers,
                 rotated_field):
        self.indexes = None
        self.rotated_field = rotated_field
        self.correct_answers = correct_answers
        self.choices = choices
        self.questions = questions
        self.field_number = field_number
        self.image_height = image_height
        self.contour = contour
        self.img = img
        self.image_width = image_width
        self.percent_grade = None
        self.img_colored_marks = None

    def check_field(self):
        field_wrap = warp_field(self.img, self.contour, self.image_width, self.image_height, self.field_number)
        if self.field_number < 2:
            splited_boxes = binary_and_split(field_wrap, self.questions, self.choices)
            pixels_value = check_line(splited_boxes, self.questions, self.choices, self.rotated_field)
            marked_indexes = find_idexes_of_marked_boxes(self.questions, self.choices, pixels_value, self.rotated_field)
            self.indexes = marked_indexes
            if self.field_number == 0:
                verified_answers, self.percent_grade = check_if_correct(marked_indexes, self.correct_answers,
                                                                        self.questions)
            else:
                verified_answers = [1, 1, 1, 1, 1]
            img_marks_on_blank = save_colors_on_blank(field_wrap, marked_indexes, verified_answers,
                                                      self.correct_answers, self.questions, self.choices,
                                                      self.rotated_field)
            self.img_colored_marks = inverse_warp(img_marks_on_blank, self.contour, self.image_width, self.image_height,
                                                  self.field_number)

