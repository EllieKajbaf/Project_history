# Project_history
In this project I am going to analysis a dataset.
About Dataset:
The Sustainable Development Report 2023 dataset includes thorough information about sustainability and advancements
 made in relation to the Sustainable Development Goals (SDGs) for a number of nations.
 The dataset's entries each include statistics on a country's sustainability rankings,
 regional placement, and SDG performance. This dataset offers insightful information about
 international sustainability initiatives and enables a nuanced evaluation of nations' development
 towards sustainability.

Dataset:
 The dataset includes the following columns:
 country_code (A unique identifier that links to the primary dataset),
 country (The name of the country.), year (The year of the data entry.),
 sdg_index_score (The overall SDG (Sustainable Development Goals) index score of the country.),
 goal_1_score (No Poverty.),
 goal_2_score (Zero Hunger), 
 goal_3_score (Good Health and Wellbeing),
 goal_4_score (Quality Education),
 goal_5_score (Gender Equality),
 goal_6_score (Clean Water and Sanitation),
 goal_7_score (Affordable and Clean Energy.),
 goal_8_score (Decent Work and Economic Growth.),
 goal_9_score (Industry, Innovation and Infrastructure.),
 goal_10_score (Reduced Inequalities.),
 goal_11_score (Sustainable Cities and Communities.), 
 goal_12_score (Responsible Consumption and Production.),
 goal_13_score( Climate Action.), 
 goal_14_score (Life Below Water.),
 goal_15_score (Life on Land.),
 goal_16_score (Peace, Justice and Strong Institutions.),
 goal_17_score (Partnerships for the Goals.).

Objectives:
1.	Considering every index, which countries have the minimum score, and which countries have the maximum score?
2.	Considering every index, which countries are above, and which countries are below the mean score?
3.	Considering the overall score, comparing developed and developing countries from various continents.
4.	What countries are in the top or bottom 10% than the absolute maximum and minimums?

Instructions to produce the figures:
1- Figure 1. Mean and Standard division for each goal score
  To produce this figure, I used code : Mean_tsd.ipynb
  To test that : mean_std_analysis_function.py, 
                and : test_mean_std_analysis_function.py

2- Figure 2. Minimum value for each goal.
  To produce this figure, I used code : Min_goal_scores.ipynb
  To test that: min_countries.py 
               and : test_min_countries.py

3- Figure 3. Maximum values for each goal.
 To produce this figure, I used code : max_countries.ipynb
 To test that: max_countries_function.py
               and : test_max_countries_function.py

4- Figure 4. The number of countries above mean for each goal.
 To produce this figure, I used code :  above_mean_countries.ipynb
 To test that: above_mean_countries_function.py
              and: test_above_mean_countries_function.py

5- Figure 5. The number of countries below the mean value for each goal.
 To produce this figure, I used code : below_mean_countries.ipynb
 To test that: below_mean_countries_function.py
              and:  test_below_mean_countries_function.py

6- Figure 6. Right: The number of countries above quantile 90. Left: Distribution of countries.
 To produce this figure, I used code : quantile_90_countries.ipynb
 To test that: quantile_90_countries_function.py
              and:  test_quantile_90_countries_function.py

7- Figure 7. Right: Distribution of countries. Left: The number of countries below quantile 10.
To produce this figure, I used code : quantile_10_countries.ipynb
 To test that: quantile_10_countries_function.py
              and:  test_quantile_10_countries_function.py

8- Figure 8. Comparing the 'No Poverty Goal Score’ with the 'Good Health and Wellbeing Score’.
To produce this figure, I used code : relationship_between_NoPoverty_GoodHealth.ipynb 

9- Figure 9. Comparing the ‘Quality Education’ with the ‘Gender Equality’.
To produce this figure, I used code : relationship_between_QualityEducation_GenderEquality.ipynb

10- Figure 10, 5 specific countries, including developed and developing countries from 5 different continents.
To produce this figure, I used code : countries_various_continents.ipynb
               
