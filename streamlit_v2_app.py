import streamlit as st
from PIL import Image
from ultralytics import YOLO # type: ignore
import numpy as np

# Load the YOLO model
model = YOLO('best.pt')  # Ensure this path is correct


# Disease information dictionary
disease_info = {
    "Healthy": {
        "Introduction": "No treatment needed.",
        "Managment": "The plant is healthy with no signs of disease.",
        "Prevention": "Continue regular care and monitoring to maintain plant health.",

    },
    "Iron Deficiency": {
        "Introduction": "Caused by insufficient iron in the soil, often due to high soil pH.",
        "Mananagement": "Apply iron chelates to the soil or as a foliar spray.",
        "Prevention": "Maintain proper soil pH, avoid over-watering, and use balanced fertilizers.",
       
    },

    "Leaf Miner": {
        "Introduction": "Caused by larvae of various leaf-mining insects.",
        "Management": "Use insecticides like spinosad or neem oil. Remove affected leaves.",
        "Prevention": "Use row covers to prevent adult insects from laying eggs, and remove infested leaves.",
       
    },
    
     "Bacterial Spot": {
        "Introduction": "Bacterial spot is a disease that affects tomatoes and peppers in particularly hot, humid conditions. Multiple bacteria are known to cause this disease, which results in spotty, pitted fruits.",
        "Symptoms": "Tomato plant leaves will develop small spots that are brown with a yellow ring around them. These spots often fall away and leave holes behind. Fruits may have scabby spots as well.",
        "Management": "Do not eat infected tomatoes, which can be host to secondary pathogens. Remove infected plants and rotate crops.",
        "Prevention": "Choose resistant varieties, water in the morning, and space out plants properly.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
    "Early Blight": {
        "Introduction": "Early blight, caused by Alternaria fungus, is the most common type of leaf spot disease on tomatoes. Early blight is more prevalent in hot, humid regions and remains in the soil for one year. Wet weather can bring on an attack. In areas impacted by early blight, choose disease-resistant cultivars with Resistant to EB (Early Blight) labels.",
        "Symptoms": "Dark brown spots encircled with rings start on the lowest leaves and move up, eventually causing foliage to shrivel, dry up, and fall. Lesions develop on stems and fruits. The defoliation causes sunscald.",
        "Management": "Remove lower leaves, including up to a third of the infected foliage. Apply a tomato fungicide at the first sign of infection or when weather conditions are favorable for the disease to develop. Do not compost affected plants. ",
        "Prevention": "Prevent early blight by watering at the soil level and mulching. Keep adequate space between plants and rows; use stakes and practice good weed control. Prune bottom leaves from plants and rotate tomato plants and other night shades every two years. Copper and/or sulfur sprays can prevent further development of the fungus.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
    "Late Blight": {
        "Introduction": "Late blight is a mold disease affecting tomato leaves, stems, and fruit. It develops in cool, wet weather and spreads rapidly. Late blight is caused by the oomycete Phytophthora infestans, which is not a true fungus but still causes devastation as it did during the Irish potato famine in the 1840s. If you suspect you have late blight, contact your local extension service for specific identification because there are many strains of late blight.",
        "Symptoms": "Greasy-looking, irregularly shaped dark brown blotches with green-gray edges appear on leaves. A ring of white mold develops around the spots, especially in wet weather. The spots eventually turn dry and papery. Blackened areas may appear on the stems. The fruit also develops large, irregularly shaped, greasy gray spots and can turn mushy from a secondary bacterial infection.",
        "Management": "Copper sprays offer some control. The fungicide Serenade works best as a deterrent rather than a cure. Late blight can overwinter in soil, tomato debris, and seeds, even in colder areas. Remove all the debris. Rotate crops to prevent infections the following year.",
        "Prevention": "Rotate crops each year, plant blight-resistant varieties, promote air circulation between plants by spacing them out properly and pruning leaves that touch.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
     "Leaf Mold": {
        "Introduction": "Leaf mold is a fungus caused by Passalora fulva and it occurs most frequently in humid conditions.",
        "Symptoms": "Leaf mold appears as pale green or yellowish spots on the upper leaves. When it's very humid, the spots occur on the bottom surfaces of the leaves and then become covered in a gray, velvety growth of fungal spores. Fruits can have a leathery, blackish rot near the stem.",
        "Management": "Increase air circulation by pruning, spacing, and staking tomato plants to control the disease. Avoid watering overhead to keep leaves dry.",
        "Prevention": "Crop rotation can make a critical difference in preventing leaf mold, and you can also use a preventive fungicide.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
         
      "Spider Mites": {
        "Introduction": "The two-spotted spider mite (Tetranychus urticae) is a common pest of vegetable and fruit crops, particularly in New England, affecting crops like tomatoes, eggplants, and melons. These mites thrive in hot, dry, and dusty conditions and can reproduce quickly, with up to 20 generations per year. They feed on plant leaves, causing blotchy yellow to reddish-brown spots and eventually leading to leaf drop. Infestations often go unnoticed until webbing becomes visible, which makes control difficult.",
         "Symptoms": "The symptoms of a two-spotted spider mite infestation include blotchy, pale yellow to reddish-brown spots on the leaves, giving them a mottled or speckled, dull appearance. As the infestation progresses, leaves turn yellow and eventually drop off. In large populations, visible webbing can cover the leaves, and mites may also move onto fruit. The plants may exhibit distorted leaves, yellowing, and overall loss of vigor, even with adequate moisture and nutrition.",
        "Management": "Management of two-spotted spider mites involves regular monitoring, particularly by inspecting the undersides of leaves with a magnifier. Look for tiny adult mites (about 1/50 inch) or webs. Chemical control options include selective miticides like bifenazate, abamectin, and spirotetramat, as well as organic products such as insecticidal soap, neem oil, and soybean oil. It's important to apply miticides in two rounds, spaced 5-7 days apart, and alternate products to prevent resistance. Biological control with predatory mites like Phytoseiulus persimilis and Amblyseius fallicis can help suppress mite populations, especially in greenhouses and fields.",
        "Prevention": "Prevention strategies include avoiding over-fertilizing with nitrogen, as excess fertilizer can worsen mite outbreaks. Crop rotation and careful planning to avoid planting eggplants near legume forage crops can reduce the risk of infestations. Using overhead irrigation or ensuring regular rainfall can also help limit mite populations. Avoid planting in weedy fields and eliminate host plants that may harbor mites. Lastly, avoid broad-spectrum insecticides early in the season, as they can harm the natural predators that help keep spider mite populations in check.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
      
        "Bacterial Spot": {
        "Introduction": "Bacterial leaf spot caused by Xanthomonas campestris pv. vesicatoria is the most prevalent foliar disease of pepper, Capsicum spp. The disease may cause early defoliation, yield losses, and poor fruit quality.",
        "Symptoms": "The first symptoms are small, yellow-green lesions on young leaves, which usually appear deformed and twisted. On older foliage, lesions are rather angular, dark-green, and greasy in appearance, often surrounded by yellow circles. They are often more numerous on leaf margins or tips. Eventually, the spots look like shot holes because the center dries up and disintegrates. ",
        "Management": "Consider destroying crops if disease is early. Use copper-containing bactericides.",
        "Prevention": "To prevent disease, use certified seeds, resistant varieties, and inspect fields regularly. Remove and burn infected plants, clear weeds, and mulch to prevent contamination. Clean tools, avoid wet foliage, and use drip irrigation. After harvest, plow debris deep or burn it, and practice 2–3-year crop rotation with non-susceptible plants.",
        "Reference": "GmbH, PEAT. “Bacterial Spot of Pepper: Pests & Diseases.” Plantix. Accessed November 20, 2024. https://plantix.net/en/library/plant-diseases/300003/bacterial-spot-of-pepper/   ",
    },
   
        "Mosaic Virus": {
        "Introduction": "The tomato mosaic virus is a plant pathogenic virus that causes the greatest harm to tomatoes, although its host range includes many other plants such as peppers, potatoes, apples, pears, cherries, and a number of weeds. ",
         "Management": "Management involves monitoring plants regularly and removing infected ones to prevent virus spread. Insect vectors, like aphids and thrips, must be controlled as they can transmit the virus. Resistant tomato varieties should be selected. Certified disease-free seeds and transplants should be used, and tools must be disinfected regularly.",
         "Symptoms": "Yellowing, stunting, and mottled leaves that may curl, become malformed, or reduce in size. Fruits may ripen unevenly, show raised or depressed off-color circles and develop internal browning (brownwall). Other signs include distorted fruit, shriveled leaves, and dark spots on the foliage.",
        "Prevention": "Prevention includes starting with uninfected, disease-free transplants and seeds. Crop rotation is vital to prevent soil-borne viruses, and using hot water or chemical treatments on seeds can help reduce virus spread. Sanitation is essential; disinfect tools between plants and avoid using tobacco products near tomatoes, as they can spread viruses. Infected plants should be bagged, removed, and either burned or buried, and all equipment should be disinfected between seasons.",
        "Reference": "Schuh, Authors: Marissa. “Tomato Viruses.” UMN Extension. Accessed November 26, 2024. https://extension.umn.edu/disease-management/tomato-viruses.  ",
    },
        "Septoria": {
        "Introduction": "The Septoria fungus causes septoria leaf spot. The fungal infection affects leaves but not the fruit. It is sometimes mistaken for late blight. Insects, tools, and water spread fungus spores which remain in the soil for up to two years. This fungus thrives in warm, wet weather so watch for symptoms and act immediately.",
        "Symptoms": "Symptoms are similar to early blight, but septoria more often appears at the first fruit set. This fungus appears on leaves as multiple small, dark, circles that enlarge to 1/3 to 1/4-inch in diameter. The spots develop a tan or gray center, and the leaves eventually wilt and fall off. It spreads rapidly causing loss of older leaves first, then infects new foliage, and can quickly move through an entire crop. Early leaf drop leads to fruit loss and sunscald.",
        "Management": "The most effective treatment is repeated applications with a tomato fungicide or biofungicide for the entire tomato crop. Copper sprays and Serenade fungicide are somewhat effective at halting the spread of symptoms. Remove infected leaves to prevent the spread of spores to other leaves, as water splashing on the leaves helps transmit the disease.",
        "Prevention": "Good garden sanitation is critical for preventing septoria leaf spot. Remove fallen leaves and debris from the garden immediately. Clean tools before and after working with plants, water at ground level, and control insect pests. Rotate your tomato crops every three years.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
   
    "Yellow Leaf Curl Virus": {
        "Introduction": "Yellow leaf curl virus causes yellow leaf curl disease, causing leaves to yellow and curl. The leaves may be smaller than expected and will curl upward. Flowers are more likely to fall off, resulting in less fruit.",
        "Symptoms": "Small, Yellow leaves will curl upward, blossoms may fall off, and less fruit will be produced.",
        "Management": "Remove infected plants and practice aggressive weed control.",
        "Prevention": "Serious crop rotation, avoiding fields where tomatoes with yellow leaf curl virus have been present. Practice pest prevention, as the virus is often spread through whiteflies.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
        
    
}

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# Set a specific width for both images to be the same
image_width = 520  # Define the image width here

# Main Page
if app_mode == "Home":
    st.header("Machine Learning-Based Detection and Differentiation of Diseases in Tomato and Pepper Plants")

    # Display the first image
    image_path1 = "https://raw.githubusercontent.com/khemrajr/Tomato-Disease-Recognition/main/home_page.jpg"  # Ensure the file extension is correct
    st.image(image_path1, width=image_width)

    # Display the second image
    image_path2 = "https://raw.githubusercontent.com/khemrajr/Tomato-Disease-Recognition/main/bell_pepper.jpg"  # Ensure the file extension is correct
    st.image(image_path2, width=image_width)

    st.markdown(""" 
        Welcome to the Plant Disease Recognition System! 🌿🔍
        
        Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

        ### How It Works
        1. *Upload Image:* Go to the *Disease Recognition* page and upload an image of a plant with suspected diseases.
        2. *Analysis:* Our system will process the image using advanced algorithms to identify potential diseases.
        3. *Results:* View the results and recommendations for further action.

        ### Why Choose Us?
        - *Accuracy:* Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
        - *User-Friendly:* Simple and intuitive interface for seamless user experience.
        - *Fast and Efficient:* Receive results in seconds, allowing for quick decision-making.

        ### Get Started
        Click on the *Disease Recognition* page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

        ### About Us
        Learn more about the project, our team, and our goals on the *About* page.
    """)

# About Project
elif app_mode == "About":
    st.header("About")
    st.markdown(""" 
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset. The original dataset can be found on this GitHub repo.
                This dataset consists of about 87K RGB images of healthy and diseased crop leaves which are categorized into 12 different classes. The total dataset is divided into an 80/20 ratio of training and validation sets, preserving the directory structure.
                A new directory containing 1145 test images is created later for prediction purposes.
                #### Content
                1. Train (9167 images)
                2. Test (1145 images)
                3. Validation (1145 images)
                """)



def display_disease_info(detected_class):
    if detected_class in disease_info:
        st.sidebar.subheader(f"Disease Detected: {detected_class}")
        st.sidebar.markdown(f"**Introduction:** {disease_info[detected_class]['Introduction']}")
        st.sidebar.markdown(f"**Symptoms:** {disease_info[detected_class]['Symptoms']}")
        st.sidebar.markdown(f"**Management:** {disease_info[detected_class]['Management']}")
        st.sidebar.markdown(f"**Prevention:** {disease_info[detected_class]['Prevention']}")
        st.sidebar.markdown(f"**Reference:** {disease_info[detected_class]['Reference']}")
    else:
        st.sidebar.subheader(f"Disease Detected: {detected_class}")
        st.sidebar.markdown("No information available for this disease.")

# Upload file
uploaded_file = st.file_uploader("Choose a tomato leaf image", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Predict classes
    results = model.predict(image)
    
    # Convert results to a format suitable for Streamlit display
    for result in results:
        im_array = result.plot()  # Plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # Convert BGR to RGB
        
        # Show the predicted image with a larger size
        st.image(im, caption='Model Prediction', width=500)  # Adjust the width as needed

        # Extract and display disease information
        if len(result.boxes) > 0:
            detected_class_index = int(result.boxes[0].cls[0])  # Extract the index of the predicted class
            detected_class = result.names.get(detected_class_index, "Unknown")  # Safely get the class name
            display_disease_info(detected_class)
        else:
            st.subheader("No disease detected.")
        
        # Save the predicted image
        im.save('results.jpg')

    # Success message
    st.success("Image processed successfully!")

    # Download processed image option
    with open("results.jpg", "rb") as file:
        btn = st.download_button(
            label="Download Processed Image",
            data=file,
            file_name="processed_image.jpg",
            mime="image/jpeg"
        )
