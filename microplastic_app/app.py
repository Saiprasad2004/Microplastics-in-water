import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image
import streamlit as st
from PIL import Image
import numpy as np

# Load model
model = YOLO("microplastic_model.pt")

st.title("Microplastic Detection & Water Quality Analysis")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    '''image = Image.open(uploaded_file)
    image_np = np.array(image)'''

    image = Image.open(uploaded_file)

#  FIX: convert to RGB (removes 4th channel)
    image = image.convert("RGB")

    image_np = np.array(image)


    st.image(image, caption="Uploaded Image", use_column_width=True)

    results = model.predict(source=image_np, conf=0.25)

    counts = {"fiber":0, "fragment":0, "film":0, "pellet":0}

    for r in results:
        for cls in r.boxes.cls:
            label = model.names[int(cls)].lower()
            if label in counts:
                counts[label] += 1

    total = sum(counts.values())
    risk_percentage = min(100, total * 8)

    if risk_percentage < 30:
        contamination = "Low contamination"
        drinking = "Safe with filtration"
        irrigation = "Safe"
        aquatic = "Low risk"
    elif risk_percentage < 70:
        contamination = "Moderate contamination"
        drinking = "Not recommended"
        irrigation = "Acceptable with filtration"
        aquatic = "Moderate risk"
    else:
        contamination = "High contamination"
        drinking = "Unsafe"
        irrigation = "Unsafe without treatment"
        aquatic = "High risk"

    for r in results:
        st.image(r.plot(), caption="Detected Image", use_column_width=True)

    st.subheader("Microplastic Analysis Report")

    st.write(f"Fiber: {counts['fiber']}")
    st.write(f"Fragment: {counts['fragment']}")
    st.write(f"Film: {counts['film']}")
    st.write(f"Pellet: {counts['pellet']}")
    st.write(f"Total particles: {total}")

    st.write(f"Contamination Level: {contamination}")
    st.write(f"Risk Percentage: {risk_percentage}%")

    st.subheader("Water Usage Recommendation")
    st.write(f"Drinking: {drinking}")
    st.write(f"Irrigation: {irrigation}")
    st.write(f"Aquatic Life: {aquatic}")

    st.subheader("Recommended Treatment")
    st.write("- Membrane filtration")
    st.write("- Activated carbon filtration")
    st.write("- Ultrafiltration")
    st.write("- Advanced oxidation process")