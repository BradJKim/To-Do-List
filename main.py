import PySimpleGUI as sg

def create_row(row_counter, row_number_view):
    row = [
        sg.pin(
            sg.Col([
                [
                    sg.Button('X', border_width=0, 
                    button_color=(sg.theme_text_color(), sg.theme_background_color()),
                    key =('-DEL-', row_counter)),
                    sg.Input(size=21, key =('-VAL', row_counter)),
                    sg.Text(f'Row {row_number_view}', key=('-ROW_NO-', row_counter))
                ]
            ], 
            key=('-ROW-', row_counter)
            )
        )
    ]
    return row

sg.theme('Light Blue 6')


# custom layout
layout = [
    [sg.Text("To Do List")],
    [sg.Column([create_row(0,1)], key='-ROW_PANEL-')],
    [sg.Button("QUIT", key='-EXIT-'),
    sg.Button("+", key='-ADD_ROW-')]
]

# window with custom layout
window = sg.Window("Demo", layout, margins=(250,250))


# event loop, waits for something to happen

row_counter =0
row_number_view =1

while True:
    event, values = window.read()
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        break
    if event == '-ADD_ROW-':
        row_counter +=1
        row_number_view +=1
        window.extend_layout(window['-ROW_PANEL-'], [create_row(row_counter, row_number_view)])
    elif event[0] == '-DEL-':
        row_number_view -= 1
        window[('-ROW-', event[1])].update(visible=False)

window.close()
