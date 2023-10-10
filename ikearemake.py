import streamlit as st
st.set_page_config(layout='wide')
bill = 0
st.title("Ikea Off-Brand")
st.divider()
st.image("https://www.ikea.com/us/en/images/products/kallax-shelf-unit-white__1051351_pe845166_s5.jpg?f=s")
st.divider()
st.subheader("Choose A Category")
st.divider()


st.subheader("Home")
home1,home2,home3,home4 = st.columns(4)


with home1:
    st.image("https://www.ikea.com/eg/en/images/products/kallax-shelving-unit-white__1113779_pe871547_s5.jpg")
    if st.checkbox("Shelving Unit; $50"):
        bill +=50
        st.success("Added to Shopping Cart")

with home2:
    st.image("https://www.ikea.com/ae/en/images/products/hemnes-day-bed-frame-with-3-drawers-white__1078996_pe857423_s5.jpg")
    if st.checkbox("Day-Bed Frame; $55"):
        bill +=55
        st.success("Added to Shopping Cart")

with home3:
    st.image("https://www.ikea.com/us/en/images/products/brimnes-bed-frame-with-storage-white__1101953_pe866879_s5.jpg")
    if st.checkbox("Bed Frame With Storage; $65"):
        bill +=60
        st.success("Added to Shopping Cart")

with home4:
    st.image("https://www.ikea.com/ae/en/images/products/kivik-3-seat-sofa-tibbleby-beige-grey__1056143_pe848278_s5.jpg")
    if st.checkbox("3 Seat Sofa; $57"):
        bill +=57
        st.success("Added to Shopping Cart")

st.divider()


st.subheader("Office")
office1,office2,office3,office4 = st.columns(4)


with office1:
    st.image("https://www.ikea.com/ae/en/images/products/lagkapten-adils-desk-white__1028412_pe835341_s5.jpg?f=s")
    if st.checkbox("Office Chair; $44"):
        bill +=44
        st.success("Added to Shopping Cart")

with office2:
    st.image("https://www.ikea.com/ae/en/images/products/bekant-desk-combination-black-stained-ash-veneer-black__0853330_pe714813_s5.jpg?f=s")
    if st.checkbox("Team Desk; $62"):
        bill +=62
        st.success("Added to Shopping Cart")

with office3:
    st.image("https://www.ikea.com/my/en/images/products/bekant-corner-desk-right-linoleum-blue-black__0852813_pe714738_s5.jpg")
    if st.checkbox("Corner Right Desk; $50"):
        bill +=50
        st.success("Added to Shopping Cart")

with office4:
    st.image("https://www.ikea.com/ae/en/images/products/trotten-desk-white__1192595_pe901174_s5.jpg?f=s")
    if st.checkbox("Storage Inclined Desk; $56"):
        bill +=56
        st.success("Added to Shopping Cart")

st.divider()


st.subheader("School")
school1,school2,school3,school4 = st.columns(4)


with school1:
    st.image("https://www.ikea.com/ae/en/images/products/pahl-desk-white-turquoise__1032059_pe836752_s5.jpg")
    if st.checkbox("Single Desk; $50"):
        bill +=50
        st.success("Added to Shopping Cart")

with school2:
    st.image("https://www.ikea.com/images/a-black-office-chair-and-a-helmer-drawer-unit-by-a-grey-whit-5fc0cd0e86ae362754ae9e358297bc0b.jpg?f=s")
    if st.checkbox("Teacher's Desk; $64"):
        bill +=64
        st.success("Added to Shopping Cart")

with school3:
    st.image("https://www.ikea.com/ae/en/images/products/jonaxel-storage-combination-white__0703659_pe732279_s5.jpg")
    if st.checkbox("Supplies Cart; $56"):
        bill +=56
        st.success("Added to Shopping Cart")

with school4:
    st.image("https://www.ikea.com/gb/en/images/products/jonaxel-open-storage-combination-white__0703646_pe732270_s5.jpg")
    if st.checkbox("Large Storage; $66"):
        bill +=66
        st.success("Added to Shopping Cart")

st.divider()


if st.button("See Bill"):
     st.success(f"The price is $ {bill} ")