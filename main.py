from pyexpat import model
import streamlit as st
import tensorflow as tf
import numpy as np

# TensorFlow Model Prediction
def model_prediction(test_image):
    # Specify the correct path to your model file in the Downloads folder
    model_path = "C:/Users/rajhi/Downloads/Model_v2/model_version_1.keras"  # Updated with the new model's full path
    model = tf.keras.models.load_model(model_path)  # Load the model from the specified path

    # Load the image from the uploaded file
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
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
            st.snow()  # Display snow animation while predicting
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
            
            st.success(f"Model predicts: {class_name[result_index]}")
