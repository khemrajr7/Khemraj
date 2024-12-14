# Import libraries
from pyexpat import model
import streamlit as st
import tensorflow as tf
import numpy as np

# Set up disease details dictionary
disease_info = {
    "Tomato___Bacterial_spot": {
        "Introduction": "Bacterial spot is a disease that affects tomatoes and peppers in particularly hot, humid conditions. Multiple bacteria are known to cause this disease, which results in spotty, pitted fruits.",
        "Symptoms": "Tomato plant leaves will develop small spots that are brown with a yellow ring around them. These spots often fall away and leave holes behind. Fruits may have scabby spots as well.",
        "Management": "Do not eat infected tomatoes, which can be host to secondary pathogens. Remove infected plants and rotate crops.",
        "Prevention": "Choose resistant varieties, water in the morning, and space out plants properly.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
    "Tomato___Early_blight": {
        "Introduction": "Early blight, caused by Alternaria fungus, is the most common type of leaf spot disease on tomatoes. Early blight is more prevalent in hot, humid regions and remains in the soil for one year. Wet weather can bring on an attack. In areas impacted by early blight, choose disease-resistant cultivars with Resistant to EB (Early Blight) labels.",
        "Symptoms": "Dark brown spots encircled with rings start on the lowest leaves and move up, eventually causing foliage to shrivel, dry up, and fall. Lesions develop on stems and fruits. The defoliation causes sunscald.",
        "Management": "Remove lower leaves, including up to a third of the infected foliage. Apply a tomato fungicide at the first sign of infection or when weather conditions are favorable for the disease to develop. Do not compost affected plants. ",
        "Prevention": "Prevent early blight by watering at the soil level and mulching. Keep adequate space between plants and rows; use stakes and practice good weed control. Prune bottom leaves from plants and rotate tomato plants and other night shades every two years. Copper and/or sulfur sprays can prevent further development of the fungus.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
    "Tomato___Late_blight": {
        "Introduction": "Late blight is a mold disease affecting tomato leaves, stems, and fruit. It develops in cool, wet weather and spreads rapidly. Late blight is caused by the oomycete Phytophthora infestans, which is not a true fungus but still causes devastation as it did during the Irish potato famine in the 1840s. If you suspect you have late blight, contact your local extension service for specific identification because there are many strains of late blight.",
        "Symptoms": "Greasy-looking, irregularly shaped dark brown blotches with green-gray edges appear on leaves. A ring of white mold develops around the spots, especially in wet weather. The spots eventually turn dry and papery. Blackened areas may appear on the stems. The fruit also develops large, irregularly shaped, greasy gray spots and can turn mushy from a secondary bacterial infection.",
        "Management": "Copper sprays offer some control. The fungicide Serenade works best as a deterrent rather than a cure. Late blight can overwinter in soil, tomato debris, and seeds, even in colder areas. Remove all the debris. Rotate crops to prevent infections the following year.",
        "Prevention": "Rotate crops each year, plant blight-resistant varieties, promote air circulation between plants by spacing them out properly and pruning leaves that touch.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
     " Tomato___Leaf_Mold": {
        "Introduction": "Leaf mold is a fungus caused by Passalora fulva and it occurs most frequently in humid conditions. ",
        "Symptoms": "Leaf mold appears as pale green or yellowish spots on the upper leaves. When it's very humid, the spots occur on the bottom surfaces of the leaves and then become covered in a gray, velvety growth of fungal spores. Fruits can have a leathery, blackish rot near the stem.",
        "Management": "Increase air circulation by pruning, spacing, and staking tomato plants to control the disease. Avoid watering overhead to keep leaves dry.",
        "Prevention": "Crop rotation can make a critical difference in preventing leaf mold, and you can also use a preventive fungicide.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
      " Tomato___Septoria_leaf_spot": {
        "Introduction": "The Septoria fungus causes septoria leaf spot. The fungal infection affects leaves but not the fruit. It is sometimes mistaken for late blight. Insects, tools, and water spread fungus spores which remain in the soil for up to two years. This fungus thrives in warm, wet weather so watch for symptoms and act immediately. ",
        "Symptoms": "Symptoms are similar to early blight, but septoria more often appears at the first fruit set. This fungus appears on leaves as multiple small, dark, circles that enlarge to 1/3 to 1/4-inch in diameter. The spots develop a tan or gray center, and the leaves eventually wilt and fall off. It spreads rapidly causing loss of older leaves first, then infects new foliage, and can quickly move through an entire crop. Early leaf drop leads to fruit loss and sunscald.",
        "Management": "The most effective treatment is repeated applications with a tomato fungicide or biofungicide for the entire tomato crop. Copper sprays and Serenade fungicide are somewhat effective at halting the spread of symptoms. Remove infected leaves to prevent the spread of spores to other leaves, as water splashing on the leaves helps transmit the disease.",
        "Prevention": "Good garden sanitation is critical for preventing septoria leaf spot. Remove fallen leaves and debris from the garden immediately. Clean tools before and after working with plants, water at ground level, and control insect pests. Rotate your tomato crops every three years.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
      
      " Tomato___Spider_mites_Two-spotted_spider_mite": {
        "Introduction": "The two-spotted spider mite (Tetranychus urticae) is a common pest of vegetable and fruit crops, particularly in New England, affecting crops like tomatoes, eggplants, and melons. These mites thrive in hot, dry, and dusty conditions and can reproduce quickly, with up to 20 generations per year. They feed on plant leaves, causing blotchy yellow to reddish-brown spots and eventually leading to leaf drop. Infestations often go unnoticed until webbing becomes visible, which makes control difficult.",
        "Symptoms": "The symptoms of a two-spotted spider mite infestation include blotchy, pale yellow to reddish-brown spots on the leaves, giving them a mottled or speckled, dull appearance. As the infestation progresses, leaves turn yellow and eventually drop off. In large populations, visible webbing can cover the leaves, and mites may also move onto fruit. The plants may exhibit distorted leaves, yellowing, and overall loss of vigor, even with adequate moisture and nutrition.",
        "Management": "Management of two-spotted spider mites involves regular monitoring, particularly by inspecting the undersides of leaves with a magnifier. Look for tiny adult mites (about 1/50 inch) or webs. Chemical control options include selective miticides like bifenazate, abamectin, and spirotetramat, as well as organic products such as insecticidal soap, neem oil, and soybean oil. It's important to apply miticides in two rounds, spaced 5-7 days apart, and alternate products to prevent resistance. Biological control with predatory mites like Phytoseiulus persimilis and Amblyseius fallicis can help suppress mite populations, especially in greenhouses and fields.",
        "Prevention": "Prevention strategies include avoiding over-fertilizing with nitrogen, as excess fertilizer can worsen mite outbreaks. Crop rotation and careful planning to avoid planting eggplants near legume forage crops can reduce the risk of infestations. Using overhead irrigation or ensuring regular rainfall can also help limit mite populations. Avoid planting in weedy fields and eliminate host plants that may harbor mites. Lastly, avoid broad-spectrum insecticides early in the season, as they can harm the natural predators that help keep spider mite populations in check.",
        "Reference": "Gillette, Barbara. “22 Tomato Diseases: Identification, Treatment and Prevention.” The Spruce. Accessed November 13, 2024. https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094.",
    },
      
        " Tomato___Target_Spot": {
        "Introduction": "Target Spot is a fungal disease that affects tomatoes, as well as other crops like papayas, cucumbers, and legumes. It begins with small, yellow-margined spots on leaves that expand and develop a ring pattern, eventually causing leaf yellowing, collapse, and death. The disease spreads rapidly in wet, windy conditions, leading to significant leaf loss and reduced yields, especially if infection occurs before fruit development.",
        "Symptoms": "The disease causes severe leaf loss, resulting in low yields. It is a major concern for tomato farmers, as it can severely impact crop health and productivity.",
        "Management": "Before planting, avoid planting new crops near infected ones and ensure good seedling inspection to discard any with spots. During plant growth, prune lower branches for better airflow, remove and burn infected lower leaves, and control weeds that may host the fungus. Overhead irrigation should be avoided to reduce spore production. After harvest, it is crucial to collect and burn crop remains and practice crop rotation, leaving at least three years before replanting tomatoes on the same land.",
        "Prevention": "Prevention includes proper plant spacing, diligent seedling inspection, pruning, and managing weeds. Fungicides may be needed in wet conditions that favor disease spread. ",
        "Reference": "Target spot of tomato. Accessed November 26, 2024. https://www.vegetables.bayer.com/ca/en-ca/resources/agronomic-spotlights/target-spot-of-tomato.html. ",
    },
   
   
        "Tomato___Tomato_mosaic_virus": {
        "Introduction": "The tomato mosaic virus is a plant pathogenic virus that causes the greatest harm to tomatoes, although its host range includes many other plants such as peppers, potatoes, apples, pears, cherries, and a number of weeds. ",
         "Management": "Management involves monitoring plants regularly and removing infected ones to prevent virus spread. Insect vectors, like aphids and thrips, must be controlled as they can transmit the virus. Resistant tomato varieties should be selected. Certified disease-free seeds and transplants should be used, and tools must be disinfected regularly.",
         "Symptoms": "Yellowing, stunting, and mottled leaves that may curl, become malformed, or reduce in size. Fruits may ripen unevenly, show raised or depressed off-color circles and develop internal browning (brownwall). Other signs include distorted fruit, shriveled leaves, and dark spots on the foliage.",
        "Prevention": "Prevention includes starting with uninfected, disease-free transplants and seeds. Crop rotation is vital to prevent soil-borne viruses, and using hot water or chemical treatments on seeds can help reduce virus spread. Sanitation is essential; disinfect tools between plants and avoid using tobacco products near tomatoes, as they can spread viruses. Infected plants should be bagged, removed, and either burned or buried, and all equipment should be disinfected between seasons.",
        "Reference": "Schuh, Authors: Marissa. “Tomato Viruses.” UMN Extension. Accessed November 26, 2024. https://extension.umn.edu/disease-management/tomato-viruses.  ",
    },
         " Tomato___Target_Spot": {
        "Introduction": "Target Spot is a fungal disease that affects tomatoes, as well as other crops like papayas, cucumbers, and legumes. It begins with small, yellow-margined spots on leaves that expand and develop a ring pattern, eventually causing leaf yellowing, collapse, and death. The disease spreads rapidly in wet, windy conditions, leading to significant leaf loss and reduced yields, especially if infection occurs before fruit development.",
        "Symptoms": "The disease causes severe leaf loss, resulting in low yields. It is a major concern for tomato farmers, as it can severely impact crop health and productivity.",
        "Management": "Before planting, avoid planting new crops near infected ones and ensure good seedling inspection to discard any with spots. During plant growth, prune lower branches for better airflow, remove and burn infected lower leaves, and control weeds that may host the fungus. Overhead irrigation should be avoided to reduce spore production. After harvest, it is crucial to collect and burn crop remains and practice crop rotation, leaving at least three years before replanting tomatoes on the same land.",
        "Prevention": "Prevention includes proper plant spacing, diligent seedling inspection, pruning, and managing weeds. Fungicides may be needed in wet conditions that favor disease spread. ",
        "Reference": "Target spot of tomato. Accessed November 26, 2024. https://www.vegetables.bayer.com/ca/en-ca/resources/agronomic-spotlights/target-spot-of-tomato.html. ",
    },
        
    "Pepper__bell___Bacterial_spot": {
        "Introduction": "Bacterial leaf spot caused by Xanthomonas campestris pv. vesicatoria is the most prevalent foliar disease of pepper, Capsicum spp. The disease may cause early defoliation, yield losses, and poor fruit quality.",
        "Symptoms": "The first symptoms are small, yellow-green lesions on young leaves, which usually appear deformed and twisted. On older foliage, lesions are rather angular, dark-green, and greasy in appearance, often surrounded by yellow circles. They are often more numerous on leaf margins or tips. Eventually, the spots look like shot holes because the center dries up and disintegrates. ",
        "Management": "Consider destroying crops if disease is early. Use copper-containing bactericides.",
        "Prevention": "To prevent disease, use certified seeds, resistant varieties, and inspect fields regularly. Remove and burn infected plants, clear weeds, and mulch to prevent contamination. Clean tools, avoid wet foliage, and use drip irrigation. After harvest, plow debris deep or burn it, and practice 2–3-year crop rotation with non-susceptible plants.",
        "Reference": "GmbH, PEAT. “Bacterial Spot of Pepper: Pests & Diseases.” Plantix. Accessed November 20, 2024. https://plantix.net/en/library/plant-diseases/300003/bacterial-spot-of-pepper/   ",
    },

}

# TensorFlow Model Prediction
def model_prediction(test_image):
    model_path = os.path.abspath(os.path.join(os.getcwd(),  "Plant_disease.h5"))
#loading the model
    model= tf.keras.models.load_model(model_path)


    # Load the image from the uploaded file
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(224, 224))  # Update target size to 224x224
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    result_index = np.argmax(predictions)  # Return index of max element
    return result_index

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# Set a specific width for both images to be the same
image_width = 520  # Define the image width here

# Main Page
if app_mode == "Home":
    st.header("Machine Learning-Based Detection and Differentiation of Diseases in Tomato and Pepper Plants")

    # Display the first image
    image_path1 = "C:/Users/rajhi/Downloads/home_page.jpg"  # Ensure the file extension is correct
    st.image(image_path1, width=image_width)

    # Display the second image
    image_path2 = "C:/Users/rajhi/Downloads/bell_pepper.jpg"  # Ensure the file extension is correct
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
                This dataset consists of about 87K RGB images of healthy and diseased crop leaves which are categorized into 38 different classes. The total dataset is divided into an 80/20 ratio of training and validation sets, preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purposes.
                #### Content
                1. Train (70,295 images)
                2. Test (33 images)
                3. Validation (17,572 images)
                """)

# Prediction Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:", type=["jpg", "png", "jpeg"])
    
    if test_image is not None:
        # Show the uploaded image
        st.image(test_image, width=300, use_column_width=True)
        
        # Predict button
        if st.button("Predict"):
            st.write("Our Prediction")
            # Perform prediction
            result_index = model_prediction(test_image)

            # Class labels
            class_name = [
                'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
                'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
                'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
                'Tomato___Spider_mites_Two-spotted_spider_mite', 'Tomato___Target_Spot',
                'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
            ]
            
            predicted_class = class_name[result_index]
            st.success(f"Model predicts: {predicted_class}")
            
            # Fetch and display the recommendation
            recommendation = disease_info.get(predicted_class, "No recommendation available for this class.")
            if recommendation != "No recommendation available for this class.":
                introduction = disease_info[predicted_class].get("Introduction", "No introduction provided.")
                symptoms = disease_info[predicted_class].get("Symptoms", "No symptoms provided.")
                management = disease_info[predicted_class].get("Management", "No management instructions provided.")
                prevention = disease_info[predicted_class].get("Prevention", "No prevention instructions provided.")
                reference = disease_info[predicted_class].get("Reference", "No reference provided.")
                
                st.markdown(f"### Introduction:\n{introduction}")
                st.markdown(f"### Symptoms:\n{symptoms}")
                st.markdown(f"### Management:\n{management}")
                st.markdown(f"### Prevention:\n{prevention}")
                st.markdown(f"### Reference:\n{reference}")
            else:
                st.info(f"**Recommendation:** {recommendation}")
