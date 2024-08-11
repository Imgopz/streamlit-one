import streamlit as st


st.title("Hierarchical Data Viewer")

st.header("This is a header..!")

st.subheader("subheader")

st.caption("caption")

st.write("this is write")

st.text("fixed text")

python_code = '''
from datetime import datetime, timedelta

# Define the start date and number of commits
start_date = datetime(2024, 8, 11)
commit_dates = []

# Define the pattern of the smiley face
pattern = [
    start_date,                # First eye
    start_date + timedelta(days=2), # Second eye
    start_date + timedelta(days=4), # Start of mouth
    start_date + timedelta(days=5),
    start_date + timedelta(days=6),
    start_date + timedelta(days=7),
    start_date + timedelta(days=8), # End of mouth
]

# Generate commit dates based on the pattern
for date in pattern:
    commit_dates.append(date.strftime('%Y-%m-%d'))

print("Commit dates for smiley face pattern:")
for date in commit_dates:
    print(date)
'''

st.code(python_code, language='python')

# JavaScript code snippet
javascript_code = '''
const startDate = new Date('2024-08-11');
const commitDates = [];

// Define the pattern of the smiley face
// Example pattern: 2 eyes and a mouth
const pattern = [
    0,   // First eye
    2,   // Second eye
    4,   // Start of mouth
    5,
    6,
    7,
    8,   // End of mouth
];

// Generate commit dates based on the pattern
pattern.forEach(dayOffset => {
    let commitDate = new Date(startDate);
    commitDate.setDate(startDate.getDate() + dayOffset);
    commitDates.push(commitDate.toISOString().split('T')[0]);
});

console.log("Commit dates for smiley face pattern:");
commitDates.forEach(date => console.log(date));
'''

st.code(javascript_code, language='javascript')

# Markdown text with simple lorem ipsum content
lorem_markdown = '''
# Lorem Ipsum Example

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum. 

## Subheading

- Item 1
- Item 2
- Item 3

**Bold text** and *italic text* can be used for emphasis.

[Link to Streamlit](https://streamlit.io)

> Blockquote example
'''

st.markdown(lorem_markdown)

st.divider()

# LaTeX formula
st.latex(r''' e^{i\pi} + 1 = 0''')

# Error message
st.error("This is an error message. Something went wrong!")

# Info message
st.info("This is an informational message. Here is some useful information.")

# Warning message
st.warning("This is a warning message. Be cautious!")

# Success message
st.success("This is a success message. Everything worked as expected")

# st.balloons()

# st.snow()