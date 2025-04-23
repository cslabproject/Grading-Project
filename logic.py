from PyQt6.QtWidgets import *
from gui import Ui_MainWindow
import csv

class Logic(QMainWindow, Ui_MainWindow):
    '''
    A class controlling the logic for the GUI application.
    '''
    def __init__(self) -> None:
        '''
        Method to initialize a Logic class and connect GUI buttons to functions.
        '''
        super().__init__()
        self.setupUi(self)

        #Trying out releaseKeyboard to see if that will make the stuff pop up when you click off
        #Trying editingFinished, textChanged, textEdited
        self.attempt_input.textChanged.connect(lambda:self.display_text())
        self.submit_button.clicked.connect(lambda:self.submit())

    def clear_text(self) -> None:
        '''
        Method to clear the score labels, score inputs, and feedback messages by setting all of the widths to 0, making them 
        invisible.
        '''
        self.submit_success_label.resize(0,60)
        self.submit_namefail_label.resize(0,60)
        self.submit_attemptfail_label.resize(0,60)
        self.submit_scorefail_label.resize(0,60)

        self.score_one_label.resize(0,40)
        self.score_two_label.resize(0,40)
        self.score_three_label.resize(0,40)
        self.score_four_label.resize(0,40)

        self.score_one_input.resize(0,30)
        self.score_two_input.resize(0,30)
        self.score_three_input.resize(0,30)
        self.score_four_input.resize(0,30)

    def clear_score_text(self) -> None:
        '''
        Method to clear score labels and score inputs by setting all of the widths to 0, making them invisible.
        '''
        self.score_one_label.resize(0,40)
        self.score_two_label.resize(0,40)
        self.score_three_label.resize(0,40)
        self.score_four_label.resize(0,40)

        self.score_one_input.resize(0,30)
        self.score_two_input.resize(0,30)
        self.score_three_input.resize(0,30)
        self.score_four_input.resize(0,30)

    def display_text(self) -> None:
        """
        Method to display score labels and score inputs.
        """
        attempts = self.attempt_input.text()

        try:
            if attempts == '1':
                self.clear_score_text()
                self.score_one_label.resize(90,40)
                self.score_one_input.resize(170,30)
            elif attempts == '2':
                self.clear_score_text()
                self.score_one_label.resize(90,40)
                self.score_one_input.resize(170,30)
                self.score_two_label.resize(90,40)
                self.score_two_input.resize(170,30)
            elif attempts == '3':
                self.clear_score_text()
                self.score_one_label.resize(90,40)
                self.score_one_input.resize(170,30)
                self.score_two_label.resize(90,40)
                self.score_two_input.resize(170,30)
                self.score_three_label.resize(90,40)
                self.score_three_input.resize(170,30)
            elif attempts == '4':
                self.clear_score_text()
                self.score_one_label.resize(90,40)
                self.score_one_input.resize(170,30)
                self.score_two_label.resize(90,40)
                self.score_two_input.resize(170,30)
                self.score_three_label.resize(90,40)
                self.score_three_input.resize(170,30)
                self.score_four_label.resize(90,40)
                self.score_four_input.resize(170,30)
            elif attempts == '':
                self.clear_score_text()
                # Still allows user to click on input box and not enter anything without receiving an error
            else:
                raise ValueError
        except ValueError:
            self.submit_attemptfail_label.resize(280,60)

    def data_submission(name:str,score_one:int, score_two:int, score_three:int, score_four:int) -> None:

        with open('grade_data.csv','a+', newline='') as my_csv:
            csv_writer = csv.writer(my_csv)

            my_csv.seek(0)
            lines = my_csv.readlines()

            if len(lines) == 0:
                csv_writer.writerow(['Name', 'Score 1', 'Score 2', 'Score 3','Score 4','Final'])
    
            my_csv.seek(0,2)
            maximum = max([score_one, score_two, score_three, score_four])
            csv_writer.writerow([name,score_one,score_two,score_three,score_four, maximum])

    def submit(self) -> None:
        
        name = self.name_input.text()
        attempts = self.attempt_input.text()

        try:
            if name == '':
                raise ValueError
        except ValueError:
            self.clear_text()
            self.submit_namefail_label.resize(280,60)
            return

        try:
            if attempts == '1':
                score_one = int(self.score_one_input.text())
                score_two = 0
                score_three = 0
                score_four = 0
                if 0 <= score_one <= 100 == False:
                    raise ValueError
            elif attempts == '2':
                score_one = int(self.score_one_input.text())
                score_two = int(self.score_two_input.text())
                score_three = 0
                score_four =0
                if 0 <= score_one <= 100 == False or 0 <= score_two <= 100 == False:
                    raise ValueError
            elif attempts == '3':
                score_one = int(self.score_one_input.text())
                score_two = int(self.score_two_input.text())
                score_three = int(self.score_three_input.text())
                score_four = 0
                if 0 <= score_one <= 100 == False or 0 <= score_two <= 100 == False or 0 <= score_three <= 100 == False:
                    raise ValueError
            elif attempts == '4':
                score_one = int(self.score_one_input.text())
                score_two = int(self.score_two_input.text())
                score_three = int(self.score_three_input.text())
                score_four = int(self.score_four_input.text())
                if 0 <= score_one <= 100 == False or 0 <= score_two <= 100 == False or 0 <= score_three <= 100 == False or 0 <= score_four <= 100 == False:
                    raise ValueError
            else:
                raise TypeError
        except ValueError:
            self.clear_text()
            self.submit_scorefail_label.resize(280,60)
            return
        except TypeError:
            self.clear_text()
            self.submit_attemptfail_label.resize(280,60)
            return
    
        self.clear_text()

        self.data_submission(name,score_one,score_two,score_three,score_four)

        self.submit_success_label.resize(280,60)
        self.name_input.clear()
        self.attempt_input.clear() # could cause issues depending on how attempt input clears??
        self.name_input.setFocus()
