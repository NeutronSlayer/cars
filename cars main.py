from classes.car import Cars
from classes.bcolors import BColors
from classes.search_option import SearchOption

running = True

colors = ['Blue', 'Green', 'Yellow', 'Red']
model = ['BMW I8', 'BMW 64']
manu_date = ['2021', '2020']
option = ['BY MODEL', 'BY COLOR', 'EXIT']

search = SearchOption(option)
bmw = Cars(colors, model, manu_date)


def model_call(m_selection_index):

    run = True

    while run:
        print("You want to know about our", bmw.get_model(m_selection_index))
        print('This car was remodeled one time.\nSo we have two types of',
              bmw.get_model(m_selection_index))
        print(bmw.show_manufacturing_date())

        m_date = int(input(BColors.Underlined +
                           "Please make your decision:" + BColors.ResetAll)) - 1

        if m_date == 0:
            print('The', bmw.get_model(m_selection_index), ' ',
                  bmw.get_manufacturing_date(m_date), ' is available in')
            print(bmw.show_color())
            run = False

        elif m_date == 1:
            print('The', bmw.get_model(m_selection_index), ' ',
                  bmw.get_manufacturing_date(m_date), ' is available in')
            print(bmw.show_color())
            run = False

        else:
            print(BColors.Red + 'INVALID' + BColors.ResetAll)
            continue


def color_call(color):

    run = True

    while run:
        print('In color ', bmw.get_colors(color), ' we have this cars:')
        print(bmw.show_model())
        model_selection = int(input(BColors.Underlined +
                                    "Please make your decision:" + BColors.ResetAll)) - 1

        if model_selection == 0:
            print('We offer two types of ', bmw.get_colors(color), ' ',
                  bmw.get_model(model_selection), ':')
            print(bmw.show_manufacturing_date())
            run = False

        elif model_selection == 1:
            print('We offer two types of ', bmw.get_colors(color), ' ',
                  bmw.get_model(model_selection), ':')
            print(bmw.show_manufacturing_date())
            run = False

        else:
            print(BColors.Red + 'INVALID' + BColors.ResetAll)
            continue


while running:
    print('|===========|' +
          BColors.Bold + BColors.BackgroundWhite + BColors.Blue +
          'BMW' +
          BColors.ResetAll +
          '|===========|')
    print(BColors.Bold +
          'Welcome.\nThis is a BMW search engine.\n' + BColors.Underlined +
          'Here are your search terms:' + BColors.ResetAll)
    print(search.get_search_o(1))

    search_selection_index = int(input(BColors.Underlined +
                                       "Please make your decision:" + BColors.ResetAll)) - 1

    if search_selection_index == 0:
        print(bmw.show_model())
        model_selection = int(input(BColors.Underlined +
                                    "Please make your decision:" + BColors.ResetAll)) - 1

        if model_selection == 0:
            model_call(model_selection)

        elif model_selection == 1:
            model_call(model_selection)

    elif search_selection_index == 1:
        print('There are four colors that BMW offers:')
        print(bmw.show_color())
        color_selection = int(input(BColors.Underlined +
                                    "Please make your decision:" + BColors.ResetAll)) - 1
        if color_selection == 0:
            color_call(color_selection)
        elif color_selection == 1:
            color_call(color_selection)
        elif color_selection == 2:
            color_call(color_selection)
        elif color_selection == 3:
            color_call(color_selection)

    elif search_selection_index == 2:
        print(BColors.Bold + BColors.BackgroundWhite + BColors.Blue +
              'THANK YPU!' +
              BColors.ResetAll)
        running = False

    else:
        print(BColors.Bold + BColors.Red + BColors. Underlined + BColors.BackgroundBlack +
              'INVALID' +
              BColors.ResetAll)
        continue
