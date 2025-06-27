# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import joblib as jb

# # Load the trained model
# model = jb.load('disease/trained_model')

# class CheckDiseaseAPIView(APIView):
#     def post(self, request):
#         inputno = int(request.data.get("noofsym", 0))  
#         if inputno == 0:
#             return Response({'predicteddisease': "none", 'confidencescore': 0}, status=status.HTTP_200_OK)

#         psymptoms = request.data.get("symptoms", [])
#         if not psymptoms:
#             return Response({'error': "'symptoms' key is missing or empty"}, status=status.HTTP_400_BAD_REQUEST)

#         # Define symptoms list
#         symptomslist = [
#             'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
#             'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination',
#             'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
#             'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
#             'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
#             'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
#             'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
#             'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
#             'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
#             'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
#             'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
#             'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
#             'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
#             'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
#             'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
#             'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
#             'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
#             'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
#             'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
#             'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
#             'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
#             'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
#             'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
#             'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
#             'yellow_crust_ooze'
#         ]

#         # Prepare input for the model
#         testingsymptoms = []
#         for symptom in symptomslist:
#             if symptom in psymptoms:
#                 testingsymptoms.append(1)
#             else:
#                 testingsymptoms.append(0)

#         inputtest = [testingsymptoms]
#         print(inputtest)
#         # Predict disease
#         predicted = model.predict(inputtest)
#         y_pred_2 = model.predict_proba(inputtest)
#         confidencescore = y_pred_2.max() * 100
#         confidencescore = format(confidencescore, '.0f')
#         predicted_disease = predicted[0]

#         # Doctor specialization mapping
#         doctor_mapping = {
#             "Rheumatologist": ['Osteoarthristis', 'Arthritis'],
#             "Cardiologist": ['Heart attack', 'Bronchial Asthma', 'Hypertension '],
#             "ENT specialist": ['(vertigo) Paroymsal  Positional Vertigo', 'Hypothyroidism'],
#             "Neurologist": ['Varicose veins', 'Paralysis (brain hemorrhage)', 'Migraine', 'Cervical spondylosis'],
#             "Allergist/Immunologist": ['Allergy', 'Pneumonia', 'AIDS', 'Common Cold', 'Tuberculosis', 'Malaria', 'Dengue', 'Typhoid'],
#             "Urologist": ['Urinary tract infection', 'Dimorphic hemmorhoids(piles)'],
#             "Dermatologist": ['Acne', 'Chicken pox', 'Fungal infection', 'Psoriasis', 'Impetigo'],
#             "Gastroenterologist": ['Peptic ulcer diseae', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Gastroenteritis', 'Hepatitis E',
#                                    'Alcoholic hepatitis', 'Jaundice', 'hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Diabetes ', 'Hypoglycemia']
#         }

#         consultdoctor = "other"
#         for doctor, diseases in doctor_mapping.items():
#             if predicted_disease in diseases:
#                 consultdoctor = doctor
#                 break

#         # Return the response
#         return Response({'predicteddisease': predicted_disease, 'confidencescore': confidencescore, "consultdoctor": consultdoctor}, status=status.HTTP_200_OK)
severity_mapping = {
    "low": [
        'Allergy', 'Common Cold', 'Acne', 'Chicken pox', 'Eczema', 'Food allergies', 'Hay fever', 'Sinusitis', 'Tonsillitis',
        'Bronchitis', 'Conjunctivitis', 'Dry eye syndrome', 'Tendonitis', 'Carpal tunnel syndrome'
    ],
    "Medium": [
        'Asthma', 'Psoriasis', 'Vitiligo', 'GERD', 'Peptic ulcer disease', 'Irritable bowel syndrome (IBS)', 'Crohn\'s disease',
        'Ulcerative colitis', 'Kidney stones', 'Hypothyroidism', 'Hyperthyroidism', 'Diabetes', 'Anemia', 'Personality disorders',
        'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Tuberculosis', 'Malaria', 'Dengue', 'Typhoid',
    ],
    "High": [
        'Heart attack', 'Stroke', 'Cancer', 'Leukemia', 'Lymphoma', 'Pulmonary embolism', 'Renal failure', 'Parkinson\'s disease',
        'Alzheimer\'s disease', 'Brain tumor', 'Liver cirrhosis', 'Pancreatic cancer', 'Ovarian cancer', 'Testicular cancer',
        'Multiple sclerosis', 'Epilepsy', 'Sickle cell anemia', 'Deep vein thrombosis (DVT)', 'Post-traumatic stress disorder (PTSD)'
    ]
}

def detect_severity(disease):
    for severity, diseases in severity_mapping.items():
        if disease in diseases:
            return severity
    return "unknown"

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib as jb
import spacy

# Load the trained model
model = jb.load('disease/trained_model')

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

class NLPBased(APIView):
    def post(self, request):
        # Extract the input string from the request
        input_string = request.data.get("input_string", "").lower()  # Convert to lowercase for case-insensitive matching
        if not input_string:
            return Response({'error': "'input_string' key is missing or empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Preprocess the input string using spaCy
        doc = nlp(input_string)
        processed_words = [token.lemma_ for token in doc if not token.is_stop]  # Lemmatize and remove stop words

        # Define symptoms list
        # symptomslist = [
        #     'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
        #     'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_urination',
        #     'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
        #     'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
        #     'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
        #     'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
        #     'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
        #     'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
        #     'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
        #     'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
        #     'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
        #     'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
        #     'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
        #     'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
        #     'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
        #     'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine',
        #     'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
        #     'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
        #     'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
        #     'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion'
        # ]

        symptomslist = [
            'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
            'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination',
            'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
            'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
            'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
            'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
            'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
            'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
            'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
            'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
            'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
            'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
            'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
            'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
            'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
            'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
            'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
            'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
            'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
            'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
            'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
            'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
            'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
            'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
            'yellow_crust_ooze'
        ]

        # Match symptoms using NLP-processed words
        print("Processed words:", processed_words)
        print("Symtoms List",len(symptomslist))
        matched_symptoms = [symptom for symptom in symptomslist if any(word in symptom for word in processed_words)]
        print(matched_symptoms)
        if not matched_symptoms:
            return Response({'error': "No matching symptoms found in the input string"}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare input for the model
        # for i in range(len(symptomslist)):
        #     if symptomslist[i] in matched_symptoms:
        #         matched_symptoms[i] = 1
        # testingsymptoms = [1 if symptom in matched_symptoms else 0 for symptom in symptomslist]
        # inputtest = [testingsymptoms]
        # testingsymptoms = [1 if symptom in psymptoms else 0 for symptom in symptomslist]

        # testingsymptoms = [1 if symptom in matched_symptoms else 0 for symptom in symptomslist]
        # inputtest = [testingsymptoms]

        testingsymptoms = []
        for symptom in symptomslist:
            if symptom in matched_symptoms:
                testingsymptoms.append(1)
            else:
                testingsymptoms.append(0)
        print("Test symptoms:", len(testingsymptoms))
        inputtest = [testingsymptoms]


        print(inputtest)

        # Predict disease
        predicted = model.predict(inputtest)
        y_pred_2 = model.predict_proba(inputtest)
        confidencescore = y_pred_2.max() * 100
        confidencescore = format(confidencescore, '.0f')
        predicted_disease = predicted[0]

        # Doctor specialization mapping
        # doctor_mapping = {
        #     "Rheumatologist": ['Osteoarthristis', 'Arthritis'],
        #     "Cardiologist": ['Heart attack', 'Bronchial Asthma', 'Hypertension '],
        #     "ENT specialist": ['(vertigo) Paroymsal  Positional Vertigo', 'Hypothyroidism'],
        #     "Neurologist": ['Varicose veins', 'Paralysis (brain hemorrhage)', 'Migraine', 'Cervical spondylosis'],
        #     "Allergist/Immunologist": ['Allergy', 'Pneumonia', 'AIDS', 'Common Cold', 'Tuberculosis', 'Malaria', 'Dengue', 'Typhoid'],
        #     "Urologist": ['Urinary tract infection', 'Dimorphic hemmorhoids(piles)'],
        #     "Dermatologist": ['Acne', 'Chicken pox', 'Fungal infection', 'Psoriasis', 'Impetigo'],
        #     "Gastroenterologist": ['Peptic ulcer diseae', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Gastroenteritis', 'Hepatitis E',
        #                            'Alcoholic hepatitis', 'Jaundice', 'hepatitis A', 'hepatitis B', 'hepatitis C', 'hepatitis D', 'Diabetes ', 'Hypoglycemia']
        # }

        severity = detect_severity(predicted_disease)


        doctor_mapping = {
    "Rheumatologist": [
        'Osteoarthristis', 'Arthritis', 'Rheumatoid arthritis', 'Gout', 'Lupus', 'Scleroderma', 'Fibromyalgia'
    ],
    "Cardiologist": [
        'Heart attack', 'Bronchial Asthma', 'Hypertension', 'Arrhythmia', 'Coronary artery disease', 'Congestive heart failure',
        'Pulmonary hypertension', 'Atrial fibrillation', 'Cardiomyopathy', 'Endocarditis'
    ],
    "ENT specialist": [
        '(vertigo) Paroymsal Positional Vertigo', 'Hypothyroidism', 'Sinusitis', 'Tonsillitis', 'Otitis media', 'Hearing loss',
        'Nasal polyps', 'Laryngitis', 'Tinnitus', 'Sleep apnea'
    ],
    "Neurologist": [
        'Varicose veins', 'Paralysis (brain hemorrhage)', 'Migraine', 'Cervical spondylosis', 'Epilepsy', 'Parkinson\'s disease',
        'Multiple sclerosis', 'Stroke', 'Alzheimer\'s disease', 'Neuropathy', 'Brain tumor'
    ],
    "Allergist/Immunologist": [
        'Allergy', 'Pneumonia', 'AIDS', 'Common Cold', 'Tuberculosis', 'Malaria', 'Dengue', 'Typhoid', 'Asthma', 'Eczema',
        'Food allergies', 'Hay fever', 'Anaphylaxis', 'Autoimmune diseases'
    ],
    "Urologist": [
        'Urinary tract infection', 'Dimorphic hemorrhoids (piles)', 'Kidney stones', 'Prostate cancer', 'Bladder cancer',
        'Erectile dysfunction', 'Urinary incontinence', 'Hydronephrosis', 'Interstitial cystitis'
    ],
    "Dermatologist": [
        'Acne', 'Chicken pox', 'Fungal infection', 'Psoriasis', 'Impetigo', 'Eczema', 'Rosacea', 'Vitiligo', 'Melanoma',
        'Contact dermatitis', 'Warts', 'Skin cancer'
    ],
    "Gastroenterologist": [
        'Peptic ulcer disease', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Gastroenteritis', 'Hepatitis E',
        'Alcoholic hepatitis', 'Jaundice', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Diabetes',
        'Hypoglycemia', 'Irritable bowel syndrome (IBS)', 'Crohn\'s disease', 'Ulcerative colitis', 'Pancreatitis',
        'Celiac disease', 'Gallstones', 'Liver cirrhosis'
    ],
    "Endocrinologist": [
        'Diabetes', 'Hypoglycemia', 'Hyperthyroidism', 'Hypothyroidism', 'Cushing\'s syndrome', 'Addison\'s disease',
        'Polycystic ovary syndrome (PCOS)', 'Acromegaly', 'Growth hormone deficiency', 'Osteoporosis'
    ],
    "Oncologist": [
        'Lung cancer', 'Breast cancer', 'Prostate cancer', 'Colorectal cancer', 'Leukemia', 'Lymphoma', 'Skin cancer',
        'Brain tumor', 'Pancreatic cancer', 'Ovarian cancer', 'Testicular cancer'
    ],
    "Pulmonologist": [
        'Asthma', 'Chronic obstructive pulmonary disease (COPD)', 'Bronchitis', 'Pneumonia', 'Tuberculosis',
        'Pulmonary fibrosis', 'Lung cancer', 'Sleep apnea', 'Pulmonary embolism'
    ],
    "Nephrologist": [
        'Kidney stones', 'Chronic kidney disease', 'Acute kidney injury', 'Glomerulonephritis', 'Polycystic kidney disease',
        'Nephrotic syndrome', 'Renal failure', 'Hypertension-related kidney disease'
    ],
    "Hematologist": [
        'Anemia', 'Leukemia', 'Lymphoma', 'Hemophilia', 'Thrombocytopenia', 'Sickle cell anemia', 'Iron deficiency anemia',
        'Multiple myeloma', 'Deep vein thrombosis (DVT)', 'Pulmonary embolism'
    ],
    "Psychiatrist": [
        'Depression', 'Anxiety disorders', 'Bipolar disorder', 'Schizophrenia', 'Obsessive-compulsive disorder (OCD)',
        'Post-traumatic stress disorder (PTSD)', 'Eating disorders', 'Sleep disorders', 'Personality disorders'
    ],
    "Orthopedic Surgeon": [
        'Fractures', 'Osteoarthritis', 'Rheumatoid arthritis', 'Bone tumors', 'Spinal cord injuries', 'Carpal tunnel syndrome',
        'Tendonitis', 'Rotator cuff injuries', 'Hip dysplasia', 'Scoliosis'
    ],
    "Ophthalmologist": [
        'Cataracts', 'Glaucoma', 'Macular degeneration', 'Diabetic retinopathy', 'Conjunctivitis', 'Dry eye syndrome',
        'Retinal detachment', 'Eye infections', 'Corneal ulcers', 'Strabismus'
    ]
}

        consultdoctor = "other"
        for doctor, diseases in doctor_mapping.items():
            if predicted_disease in diseases:
                consultdoctor = doctor
                break

        # Return the response
        return Response({
            'severity': severity,
            'predicteddisease': predicted_disease,
            'confidencescore': confidencescore,
            'consultdoctor': consultdoctor,
        }, status=status.HTTP_200_OK)