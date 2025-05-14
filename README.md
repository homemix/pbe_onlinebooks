# Case Study: Designing a Database for an Online Bookstore
## Background
LitShelf, an expanding online bookstore, seeks to enhance its platform to compete with major e-commerce players. The platform supports the sale of physical books, e-books, and audiobooks, and introduces advanced features like subscription-based access, promotional campaigns, and multilingual support. LitShelf also aims to integrate with third-party logistics providers and offer a robust recommendation engine. To achieve this, LitShelf requires a sophisticated relational database to manage its complex operations while ensuring scalability and performance.
## Objective
Design a comprehensive relational database schema for LitShelf that supports its expanded operations and challenges learners to apply advanced database design principles, including normalization, complex relationships, indexing, and query optimization. The case study tests understanding of real-world database challenges, such as handling multilingual data, temporal data, and integration with external systems.

## Requirements
* Book management
* Customer management
* Order Processing
* Reviews and Ratings
* Recommendations and Analytics
* Promotions and Discounts
* Multilingual Support  
* Business Roles

### Task 1: Seed Books from CSV Using Generators
**Concept: Generators** <br>
**Description:** Write a generator function to read books.csv and seed the Books and PriceHistory tables. If the CSV has fewer than 100 books, supplement with generated data.
<br>
**Requirements:**
Create csv_book_generator(csv_file) to yield book records (dicts with Title, Language, Price, Genre, StartDate).
Insert records into Books and PriceHistory using the generator.
Set StartDate to “2025-01-01” for PriceHistory.
Review code as a group to ensure correct data types (e.g., float for Price).


