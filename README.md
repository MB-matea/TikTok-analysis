# TikTok Analysis Application

## Content

- [Overview](#overview)
- [Purpose and Scope](#purpose-and-scope)
- [Key Features](#key-features)
- [Technological Foundation](#technological-foundation)
- [Significance in National Security](#significance-in-national-security)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Contact](#contact)

## Overview

The TikTok Analysis Application is a sophisticated tool developed as part of a master's thesis titled "Integration of Artificial Intelligence into National Security Systems: Perspectives, Challenges, and Applications in the Prevention of Terrorism" by Matea Bešlić at the University of Split. This application leverages the power of Artificial Intelligence (AI) and advanced data analytics to detect and prevent the dissemination of terrorist content on TikTok, a popular social media platform known for its rapid spread of viral content.

### Purpose and Scope

The primary goal of this application is to enhance national security measures by providing a robust platform for monitoring and analyzing social media content. By focusing on TikTok, the application addresses a critical need for real-time analysis of user-generated content that could be associated with extremist ideologies or terrorist activities. This project aligns with broader security efforts to utilize AI for proactive threat detection, data-driven decision-making, and strategic response planning in combating terrorism.

### Key Features

- **Hashtag-Based Analysis:** Users can input any TikTok hashtag to analyze associated content and engagement metrics. This feature is crucial for identifying trending topics and potential propaganda tools used by extremist groups.
- **Data Collection and Processing:** The application integrates with the TikTok API to collect comprehensive data, including views, likes, comments, shares, and geolocation information. This data is processed to provide insightful analytics and visualizations.
- **Advanced Visualizations:** The platform uses interactive visualizations to display data, such as scatter plots for engagement statistics and bar charts for regional engagement distribution. These visual tools help in understanding the spread and impact of specific content across different regions.
- **Top Hashtags Identification:** A specialized algorithm identifies the top 10 hashtags related to the searched content, excluding the main hashtag. This function helps uncover hidden networks and connections between various content types.

### Technological Foundation

Built on the Streamlit platform, the TikTok Analysis Application utilizes a combination of Python libraries and frameworks, including Pandas for data manipulation, Plotly for interactive visualizations, and various machine learning algorithms for predictive analytics. The application's backend is designed to efficiently handle large datasets and perform real-time analysis, making it a powerful tool for security agencies and researchers.

### Significance in National Security

The application demonstrates the potential of AI in enhancing national security frameworks by integrating advanced data analytics and machine learning. It specifically focuses on identifying and mitigating the spread of terrorist content on social media, which has become a significant threat in recent years due to the increased use of platforms like TikTok for radicalization and recruitment.

## Installation

To run the application, follow these steps:

1. **Install Python:**
   Ensure Python is installed on your system. If not, you can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/MB-matea/TikTok-analysis.git
   cd TikTok-analysis
   ```

3. **Install Dependencies:**  
   Use the following command to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**  
   Launch the Streamlit app with the following command:

   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter a Hashtag:**  
   Enter the desired hashtag for analysis in the sidebar input field (e.g., `#dance`).

2. **Start the Analysis:**  
   Click the "Search" button to begin data retrieval and analysis.

3. **Explore the Results:**
   - **Video Data Table:** Provides a table of TikTok video data, including clickable video links.
   - **Engagement Visualization:** Examine the scatter plot for video engagement levels.
   - **Regional Engagement:** View a bar chart showing engagement metrics by region.
   - **Top Hashtags:** Another bar chart shows the top 10 hashtags related to your search.

## Code Structure

- **`app.py`:** The main application file containing the Streamlit app logic.
- **`api.py`:** Includes the `get_data` function to fetch data from the TikTok API.
- **`requirements.txt`:** Lists all required Python packages.
- **`helpers.py`:** Contains helper functions for data processing.

## Customization

- **Styling:** Customize the CSS styles within the `st.markdown` section to alter the app's look and feel.
- **Data Columns:** Adjust table and chart columns by modifying the `desired_order` list and renaming dictionary.
- **Visualizations:** Modify Plotly visualizations to include more data points or change their design.

## Dependencies

The application requires the following Python packages:

- **Streamlit:** For creating the interactive web app.
- **Pandas:** For data manipulation and analysis.
- **Plotly:** For interactive visualizations.

Full list of dependencies can be found in `requirements.txt`.

## Future Enhancements

Further development of this application could include the integration of advanced AI tools such as sentiment analysis to detect extremist rhetoric, weapon detection algorithms to identify dangerous objects in video content, and face recognition technology to track and identify known suspects. Additionally, implementing real-time alert systems for suspicious content would enable quicker responses to emerging threats. Expanding the application's capabilities to analyze other social media platforms, like Twitter, Facebook, and Instagram, would provide a more holistic surveillance tool, enhancing its utility for governments and security organizations worldwide. These enhancements would significantly bolster the capacity to monitor, detect, and respond to potential terrorist activities in a timely and effective manner.

## License

MIT License

Copyright (c) 2024 Matea Bešlić

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

For questions or suggestions, please contact Matea Bešlić at [mateabeslic1@gmail.com](mailto:mateabeslic1@gmail.com).
