# Quantium Retail Analytics Project

## Overview
This project, completed as part of the Quantium Virtual Experience Program on Theforage.com, focuses on analyzing retail transaction data for the chips and crisps category. The analysis aims to provide actionable insights to the category manager for optimizing product performance and customer targeting.

Constructive feedback are most welcome !

## Project Objectives
- Examine and clean transaction and customer data to ensure data quality
- Identify distinct customer segments based on purchasing behavior
- Analyze sales drivers and develop key performance metrics
- Create data visualizations to effectively communicate insights
- Provide strategic recommendations based on the analysis

## Technologies Used
- Programming language: Python
- Libraries: pandas, matplotlib, numpy
## Dataset
The analysis is based on retail transaction data containing:
- Customer purchase information
- Product details for chips and crisps category
- Transaction timestamps and amounts
- Store location data

## Analysis Components
1. **Data Cleaning and Preparation** : this step was done manually beforehand. 
   - Transaction data examination
   - Anomaly detection and handling
   - Data standardization

2. **Customer Segmentation**
   - Behavioral analysis
   - Purchase pattern identification
   - Segment profiling

3. **Sales Analysis**
   - Trend identification
   - Sales driver analysis
   - Performance metrics development

4. **Visualization and Reporting**
   - Creation of informative charts and graphs
   - Key findings presentation
   - Strategic recommendations


## How to Run
1. Clone this repository
2. Install required dependencies:
   ```
   pip install pandas numpy matplotlib
   ```
3. Navigate to the notebooks directory to view the analysis

## Key Insights and Recommendations

### Task 1 : Sales and customer segmentation analysis
To go directly to the concerned graph :
   -  copy the selected title below
   - go to notebook
   - press ctrl+f, paste. This will lead you directly to the concerned section.
1. **Sales Drivers :**
   - 4 primary brands drive the sales, by quantity and by total sales : Kettle, Smiths, Doritos and Pringles  
   - 4 primary pack sizes drive the sales, by quantity and by total sales : 175G, 150G, 134G, 110G 
   - __**Interesting point**__ : As unique products, some 380G, 330G and 175G belong in the top 10 most profitables products, could be an interesting wave to ride. Was it the last marketing campaign effect ? Product layout in store ? Discuss this with stakeholder

2. **Customer segmentation deep dive :**
   - I should put side by side the "Total Sales" and the "Sales Distribution" graphs. Sames with "Total Quantity" and "Quantity Distribution". This allows more intuitive insights 
   - New families don't buy much chips, possible campaign targets ? Define which premium type to deliver 
   - Analyze product-market fit for each lifestage, and select most pertinent premium category to market. Need stakeholder expertise on this
   - Older and Midage Singles/Couples drivers of premium products, ride that wave

3. **Sales trends :**
   - Sales hit low point on week 20 and week ~32. **This low point is felt mostly by budget and mainstream, but not by premium products**, look into it 
   - Plotting weekly sales by lifestage gives an intuitive visualization of profitable segments ;

4. **Most profitable shops and cumulative gross sales :**
   - ~ 1/3rd of the shops make up 50% of cumulative gross sales. To be confirmed

   ### Task 2 : Product layout effect on sales 

   The category manager experimented with a product layout on stores 77, 86 and 88 during a trial period.
   We have to determine whether the product layout had indeed an effect on driving sales by making the customer make more transactions (since he walks through the product aisles, likes what he sees, and spends more).

   **Key insights :**
   - Trial period did not affect sales at all in store 77 ; 
   - Sales noticed an increase in store 86. After further analysis, it was due to the increase in number of customers, not the increase in the number of transactions per customer ;
   - Trial period did affect sales in store 88, and the main reason was the increase in the number of transaction per customer.

   **Recommandations :**
   - Confirm this trend with a statistical significance test (Z-test) (halfway done) ;
   - Once we have confirmation, expand the product layout of store 88 to all the stores, sit, ???, profit. 


## Acknowledgments
- Quantium for providing the dataset
- Theforage.com for hosting the virtual experience program
