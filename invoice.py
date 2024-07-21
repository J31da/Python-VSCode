import streamlit as st
from fpdf import FPDF #python module to generate pdf's
import base64 #python module to convert binary data (code), to printable character, e.g: pdf

cl,cl2,cl3 = st.columns([2,1,1])
with cl3:
    st.header(':blue[**INVOICE**]')

with cl:
    img,img2,img3 = st.columns(3)
    with img:
        st.image('fb.png',use_column_width=True) 
    
    st.write('')
    st.write(':blue[FaceBook]')
    st.write(':blue[1 Hacker Way, Menlo Park, CA 94025]')
    st.write(':blue[California, USA]')

st.header('')
st.header('')

ft,ft2,ft3 = st.columns([2,0.7,1])

with ft:
    name = st.text_input(':blue[**Bill To:**]',placeholder='Customer Full Name')
    email = st.text_input('Enter address',placeholder='Enter Email Address',label_visibility='collapsed')

with ft2:
    st.write(':blue[**Invoice #**]')
    st.write('')
    st.write(':blue[**Invoice Date**]')
    st.write('')
    st.write(':blue[**Due Date**]')

with ft3:
   inv = st.text_input('invoice',label_visibility='collapsed')
   invdt = st.date_input('invoice date',label_visibility='collapsed')
   duedt = st.date_input('due date',label_visibility='collapsed')

st.header('')


st.divider()
st.header('')

c,c2,c3,c4 = st.columns([3,3,3,3])

with c:
    desc = st.text_input(':blue[**Description**]',placeholder='Enter Description')
with c2:
    qua = st.number_input(':blue[**Quantity**]',value=0,step=1)
with c3:
    pri = st.number_input(':blue[**Price | Item**]',value=0,step=1)
with c4:
    total = qua * pri
    tot = st.text_input(':blue[**Total**]',placeholder=0, disabled=True, value=total)



st.header('')
st.divider()

py,py2 = st.columns([2,2])

with py:
    st.write(':blue[**Payment Info**]')
    st.write('Account Name: FaceBook')
    st.write('Account Number: 00919900001')
    st.write('Bank Name: Meta Pay')

with py2:
    ppy,ppy2 = st.columns([1,5])
    with ppy2:
     st.write(':blue[**Payment Due:**]')

     st.subheader(f'{total:,} USD')


#------------------PDF------------------

def generate_pdf():
    pdf = FPDF()

    pdf.add_page()
    pdf.set_font('Arial', size=12)

    cl1x = 10
    cl1y = 25
    
    #column width
    clw = 90
    clh = 10

    #logo
    pdf.image('fb.png', x=cl1x+8, y=cl1y+10, w=35)

    #invoice
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=30,style='B')
    pdf.set_xy(cl1x+140,cl1y+17)
    pdf.cell(clw,clh,txt = 'INVOICE',ln=True,align='L')
    
    
    # #name of place
    # pdf.set_text_color(0, 0, 0)
    # pdf.set_font(family='Times',size=12,style='B')
    # pdf.set_xy(cl1x+17,cl1y+50)
    # pdf.cell(clw,clh,txt = 'FaceBook',ln=True,align='L')
    
    # #address
    # pdf.set_text_color(0, 0, 0)
    # pdf.set_font(family='Times',size=12,style='B')
    # pdf.set_xy(cl1x+17,cl1y+60)
    # pdf.cell(clw,clh,txt = '1 Hacker Way, Menlo Park, CA 94025',ln=True,align='L')

    # #address 2
    # pdf.set_text_color(0, 0, 0)
    # pdf.set_font(family='Times',size=12,style='B')
    # pdf.set_xy(cl1x+17,cl1y+70)
    # pdf.cell(clw,clh,txt = 'California, USA',ln=True,align='L')
   

    #inv no.
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+153,cl1y+48)
    pdf.cell(clw,clh,txt = f'Invoice No: {inv}',ln=True,align='L')

    #inv dt.
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+153,cl1y+58)
    pdf.cell(clw,clh,txt = f'Date: {invdt}',ln=True,align='L')

    #bill to
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+17,cl1y+50)
    pdf.cell(clw,clh,txt = 'Bill To:',ln=True,align='L')

    #name
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+17,cl1y+60)
    pdf.cell(clw,clh,txt = f'{name}',ln=True,align='L')
    
    #mail
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+17,cl1y+70)
    pdf.cell(clw,clh,txt = f'{email}',ln=True,align='L')
    
    #line
    pdf.set_line_width(0.5) #line width
    pdf.line(cl1x+20,cl1y+100,cl1x+190,cl1y+100) #start & stop of line

    #item
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+18,cl1y+110)
    pdf.cell(clw,clh,txt = 'Item',ln=True,align='L')
    
    #item stuff1
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,)
    pdf.set_xy(cl1x+18,cl1y+130)
    pdf.cell(clw,clh,txt = f'{desc}',ln=True,align='L')

    #quantity
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+115,cl1y+110)
    pdf.cell(clw,clh,txt = 'Quantity',ln=True,align='L')

    #quantity stuff1
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,)
    pdf.set_xy(cl1x+120,cl1y+130)
    pdf.cell(clw,clh,txt = f'{qua:,}',ln=True,align='L')

    #price
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+143,cl1y+110)
    pdf.cell(clw,clh,txt = 'Price | Item',ln=True,align='L')

    #price stuff1
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,)
    pdf.set_xy(cl1x+148,cl1y+130)
    pdf.cell(clw,clh,txt = f'${pri:,}',ln=True,align='L')

    #subtt
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12)
    pdf.set_xy(cl1x+148,cl1y+150)
    pdf.cell(clw,clh,txt = f'Subtotal',ln=True,align='L')
    
    #tt
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12)
    pdf.set_xy(cl1x+174,cl1y+150)
    pdf.cell(clw,clh,txt = f'${total:,}',ln=True,align='L')

    #tax
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,)
    pdf.set_xy(cl1x+148,cl1y+162)
    pdf.cell(clw,clh,txt = f'Tax (0%)',ln=True,align='L')

    #tx
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,)
    pdf.set_xy(cl1x+177,cl1y+162)
    pdf.cell(clw,clh,txt = f'$0',ln=True,align='L')

    #total
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,style='B')
    pdf.set_xy(cl1x+174,cl1y+110)
    pdf.cell(clw,clh,txt = 'Total',ln=True,align='L')

    #total stuff1
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12,)
    pdf.set_xy(cl1x+174,cl1y+130)
    pdf.cell(clw,clh,txt = f'${total:,}',ln=True,align='L')

    #line2
    pdf.set_line_width(0.5) #line width
    pdf.line(cl1x+20,cl1y+125,cl1x+190,cl1y+125) #start & stop of line

    #line3
    pdf.set_line_width(0.5) #line width
    pdf.line(cl1x+20,cl1y+145,cl1x+190,cl1y+145) #start & stop of line

    #thx
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=25)
    pdf.set_xy(cl1x+18,cl1y+180)
    pdf.cell(clw,clh,txt = 'Thank You!',ln=True,align='L')

    #payment info
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=13,style='B')
    pdf.set_xy(cl1x+18,cl1y+210)
    pdf.cell(clw,clh,txt = 'PAYMENT INFORMATION',ln=True,align='L')

    #bank
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12)
    pdf.set_xy(cl1x+18,cl1y+220)
    pdf.cell(clw,clh,txt = 'Meta Pay',ln=True,align='L')
    
    #acc name
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12)
    pdf.set_xy(cl1x+18,cl1y+227)
    pdf.cell(clw,clh,txt = 'Account Name: FaceBook',ln=True,align='L')

    #acc no
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12)
    pdf.set_xy(cl1x+18,cl1y+234)
    pdf.cell(clw,clh,txt = 'Account Number: 00919900001',ln=True,align='L')

    #pay by
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=12)
    pdf.set_xy(cl1x+18,cl1y+241)
    pdf.cell(clw,clh,txt = f'Pay by: {duedt}',ln=True,align='L')

    #facebook
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=25)
    pdf.set_xy(cl1x+139,cl1y+227)
    pdf.cell(clw,clh,txt = 'FaceBook',ln=True,align='L')

    #facebook address
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family='Times',size=14)
    pdf.set_xy(cl1x+97,cl1y+237)
    pdf.cell(clw,clh,txt = '1 Hacker Way, Menlo Park, CA 94025',ln=True,align='L')
    
    #save pdf
    pdf_file = 'invoice.pdf' #creates file name
    pdf.output(pdf_file)
    return pdf_file



#stores the function in a variable
pdf_func = generate_pdf()

#read the pdf function as binary data
with open(pdf_func, 'rb')as binary:
    pdf_data = binary.read()

st.header('')

if st.button(':blue[**View Invoice**]'):
    #write the pdf using base64
    pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

    #generate HTML to embed pdf
    pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type = "application/pdf" width="70%" height="600px" />'

    #display embeded pdf (markdown)
    st.markdown(pdf_embed,unsafe_allow_html=True)