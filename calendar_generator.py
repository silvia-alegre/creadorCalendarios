from PIL import Image, ImageDraw, ImageFont
import calendar
import os

def create_calendar(year, month, output_folder):
    '''
    Dado un año y mes, genera el calendario correspondiente y lo guarda
    en la carpeta
    '''
    # crear 'folio' en blanco
    img = Image.new('RGB', (600, 400), 'white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype('arial.ttf', 40)
    except:
        font = ImageFont.load_default()

    title = f'{calendar.month_name[month]} {year}'
    draw.text((250, 50), title, fill = 'black', font = font)

    cal_text = calendar.month(year, month)
    draw.text((100, 150), cal_text, fill="black", font=font)

    # Guardar imagen
    filename = f"calendar_{year}_{month}.png"
    filepath = os.path.join(output_folder, filename)
    img.save(filepath)
    
    return filename