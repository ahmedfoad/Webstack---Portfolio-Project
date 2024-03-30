# School Video Lectures App

## Introduction
Welcome to the School Video Lectures App! This repository contains the technical documentation for our web-based platform designed for creating and sharing hall-of-fame videos among users.

## Team Introduction
**Team:** Ahmed Fouad  
**Roles:**  
- Ahmed Fouad: Project Lead & Developer  
- [Other team members and their roles]

## Architecture Overview
The School Video Lectures App is built with a modern architecture:
- **Frontend:** HTML/CSS/JavaScript
- **Backend:** Python with Django framework
- **Database:** PostgreSQL
- **External API:** YouTube API

## Database Schema
### Hall Table
| Field Name | Data Type | Description |
|------------|-----------|-------------|
| id         | Integer   | Primary key for the hall |
| title      | CharField | Maximum 255 characters |
| user_id    | Integer   | Foreign key referencing User table |

### Video Table
| Field Name | Data Type | Description |
|------------|-----------|-------------|
| id         | Integer   | Primary key for the video |
| title      | CharField | Maximum 255 characters |
| URL        | URLField  | URL for the video |
| youtube_id | CharField | YouTube ID for the video |
| hall_id    | Integer   | Foreign key referencing Hall table |

## Key Features
- Pipenv Integration
- Pre-made Authentication Views
- Class-Based Views
- Django Forms
- Integration with External APIs (YouTube API)
- AJAX Techniques
- Seed Data
- Heroku Deployment

## Technologies Used
- Python
- Django
- Pipenv
- HTML/CSS/JavaScript
- YouTube API
- AJAX
- Heroku

## Development Report
**Successes:**  
- Successful integration of Pipenv and deployment on Heroku.
- Implementation of pre-made authentication views for user management.

**Challenges:**  
- Overcoming integration issues with external APIs, particularly the YouTube API.
- Resolving compatibility issues with different versions of Django libraries.

**Areas for Improvement:**  
- Enhancing user interface for better user experience.
- Implementing more robust error handling mechanisms.

**Lessons Learned:**  
- Importance of thorough testing during API integration.
- Effective collaboration and communication within the team.

**Next Steps:**  
- Implementing additional features such as user profile customization.
- Optimizing application performance for scalability.

## Demo
Live demonstration of the School Video Lectures App showcasing key functionalities and features.

## Conclusion
The School Video Lectures App offers a comprehensive platform for creating and sharing educational videos. We thank the audience for their attention and participation.

## Q&A
Open the floor for questions from the audience.

## Contact Information
For further inquiries or collaborations, please contact us:
- Email: eng.ahmedfoad@gmail.com
- GitHub Repository: https://github.com/ahmedfoad/Webstack---Portfolio-Project

## Thank You
Thank you for your time and attention.


## End
Thank you once again for your closing remarks. End the presentation on a positive note.