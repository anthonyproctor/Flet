""" Flet Expense/Money Concept """

# modules
from flet import flet, UserContorl, Page, Column, Row, Container, Text, padding, alignment

# main class
class Expense(UserControl):

    def build(delf):
        return Column(
            controls=[]
        )

def start(page: Page):
    page.title='Flet Expense Concept'
    page.horizontal_alignment='center'
    page.vertical_alignment='center'

    app = Expense()
    page.add(app)
    page.update()

if __name__ == "__main__":
    flet.app(target=start)