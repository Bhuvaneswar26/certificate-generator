from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 150)  # Adjust font size here
FONT_COLOR = '#000000'

template = Image.open(r'aiml_template.jpg')
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r'aiml_template.jpg')
    draw = ImageDraw.Draw(image_source)

    # Finding the bounding box of the text
    text_bbox = draw.textbbox((0, 0), name, font=FONT_FILE)

    # Extracting width and height from the bounding box
    name_width = text_bbox[2] - text_bbox[0]
    name_height = text_bbox[3] - text_bbox[1]

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2  ), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":

    names = ['Madki Sai Charan', 'Sohom Laha', 'Chintabattina Urmitha', 'Shruthipoosa', 'Vyshnavi P', 'Duba Upagna ', 'L.Varshini', 'Simeen Ali', 'Bagathi Navyasri ', 'K Sai Tejaswini', 'Kamatham Soujanya', 'Tatiparti Pavani ', 'Molige Sai Charan ', 'N.Jahnavi', 'Deepika', 'M.Harshitha', 'Kolluri Prashanth', 'Mohammad Azaruddin ', 'Shaik Nabi Mansoor ', 'Md.Taha Sohail', 'Sandeep Kumar Reddy ', 'Qurratul Ain Aqsa ', 'G . Harsha Vardhan ', 'Sri Nithya ', 'Eda Gayathri', 'Sraghvi.A', 'S Premchandar Reddy ', 'Srirag Chowdary ', 'Kundela Raju Yadav ', 'Dhanush Bonagiri ', 'Rakesh Kandhi ', 'Mohammad Saabir', 'Manaswitha Sunkara ', 'Rohit', 'Deepesh Ahuja', 'N.Nandanaa', 'Valaboju Anil Kumar ', 'G Revanth Teja']
    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")
