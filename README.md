# Project: StockifyPro

### Distinctiveness and Complexity:
StockifyPro is a Django-based web application that combines stock market information with the latest business news. The project satisfies the distinctiveness and complexity requirements through the following features:

1. Stock Tracking: At the core of StockifyPro is its robust stock tracking functionality. Unlike basic stock applications, StockifyPro leverages the IEX Cloud API to fetch real-time data for each stock in the user's portfolio. The application doesn't merely display stock prices; it provides a comprehensive set of information, including company name, stock symbol, latest price, previous close, market cap, volume, PE ratio, percent change, YTD change, 52-week high and low, open, high, low, and close prices. This intricate level of detail sets StockifyPro apart, catering to users who demand more than just basic stock quotes.

2. News Aggregation: Another layer of complexity is added through the integration of the News API. StockifyPro doesn't limit itself to static stock data; it keeps users informed with the latest business news. Users can effortlessly access a stream of relevant articles or search for news based on specific keywords. This dual integration of stock and news data enhances the application's functionality, making it a one-stop-shop for users looking to stay updated on both market trends and business developments.

3. User-Friendly Interface: The frontend is designed using Bootstrap, ensuring a responsive and visually appealing interface. The application allows users to navigate easily between different sections such as stock search, stock addition, and news.

* The complexity of StockifyPro is not merely a result of integrating APIs but is deeply rooted in the thoughtful consideration of user needs. The application transforms raw stock and news data into a user-friendly interface, making complex financial information accessible to users of all levels of expertise. The intricacy lies in the harmonious integration of diverse datasets, real-time updates, and an elegant frontend – a fusion that required careful planning and implementation.

### Files Created:
1. views.py: Defines the core functionalities of the application, including stock search, stock addition, stock deletion, and news retrieval.

2. models.py: Contains the Stock model, which represents the stock ticker added by users. Includes the StockForm, a Django ModelForm for handling user input related to stock addition.

3. search_stock.html: Provides the template for displaying stock search results.

4. add_stock.html: Renders the page for adding and managing stock tickers in the user's portfolio.

5. news.html: Displays the top business news fetched from the News API.

6. search_news.html: Presents search results for news articles based on user queries.

7. base.html: Serves as the base template for other HTML files, providing a consistent layout and navigation.

### How to Run the Application:
1. Clone the repository to your local machine.

2. Create a virtual environment and install the required dependencies using pip install -r requirements.txt.

3. Apply migrations using python manage.py migrate.

4. Run the development server with python manage.py runserver.

5. Access the application in your web browser at http://127.0.0.1:8000/.

### Additional Information:
* Ensure you have a valid API key for the IEX Cloud API and the News API. Update the API keys in the requests.get calls in views.py accordingly.
* The application uses Bootstrap 5 for styling, and static files are included for default images.
* The project structure follows Django best practices, and the code is organized for readability and maintainability.
