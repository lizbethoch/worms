Worms - Project Requirements

1. Project Overview: 
Worms is a full-stack web application designed for avid readers to organize and manage their personal reading library. 
The application allows user to keep track of books they want to read, are currently reading, and have completed. Users can monitor their reading progress, search and filter their library, rate completed books, and use a TBR (To Be Read) randomizer to help decide what to read next.
Worms will represent a user's broader reading life rather than only the physical books they own. A user's TBR may include physical books they own, books they plan to purchase or borrow, and books they plan to read digitally. Reading status and book access/ownership will be treated as separate information.
The application will initially focus on providing an individual reading management experience, with social features planned for future development.

2. Problem Statement
Readers can discover books through multiple sources, including socile media, recommendations from peers, online communities, physical bookstores, and personal notes. As a result, it can become difficult to remember which books they plan on reading, are currently reading, how much they have read, and which books have been completed.

Worms aims to provide a centralized platform where readers can organize their reading library, track their progress, and discover what to read next.

3. Project Goals
The primary goals of Worms are to:
Provide users with a centralized personal reading library.
Allow users to organize books based on their reading status.
Allow users to track their progress through books.
Help users decide what to read next through a TBR randomizer.
Allow users to record ratings and reviews for completed books.
Provide a clean, responsive, and enjoyable reading-focused user experience.
Demonstrate practical full-stack engineering skills.

4.Target Users
The primary target users are:
Avid readers
Casual readers who want to read more consistently
Readers who maintain large TBR lists
Users who want to track their reading progress
Users who enjoy rating and reviewing books
Users or Creators who are a part of communities like #BookTok, #BookTube, etc.

5.Minimum Viable Product (MVP)
The first version of Worms will include the following functionality.

User Accounts
1. Users can create an account.
2. Users can log in to their account.
3. Users can log out of their account.

Book Library
4. Users can add books to their personal library.
5. Users can view books in their library.
6. Users can edit book information.
7. Users can delete books from their library.
8. Users can record how they own or access a book, such as:
Physical
Digital
Borrowed
Library
Subscription
Wishlist/ Do Not Currently Own
9. Users can update how they own or access a book.

Reading Status
10. User can assign a reading status to each book:
Want to Read
Currently Reading
Read
11. Users can update a book's reading status as their reading acitivty changes.

Reading Progress
12. Users can track their reading progress.
13. Users can update their current page or percentage completed.
14. Users can mark a book as completed.

Library Organization
15. Users can search their personal library.
16. Users can filter their library by reading status.

TBR Randomizer
17. Users can view books in their Want To Read list.
18. Users can use a randomizer/wheel to select a book from their TBR list.
19. The randomizer can provide prompts to help users choose their next book.

Ratings and Reviews
20. Users can rate books they have completed.
21. Users can write a personal review of a completed book.
22. Users can edit or delete their reviews

6.Future Features
The following features are outside the initial MVP but may be developed in future versions.

Social Features
Users can connect with friends.
Users can see what their friends are currently reading.
Users can see friends’ reading statuses.
Users can view friends’ ratings and reviews.
Users can discover books through their friends.

Book Discovery
Future versions may allow users to discover books outside of their personal library.
Potential features include
Search books by title or author.
Search books using an ISBN.
Brows books by genre.
View trending books.
View bestseller lists such as the New York Times Best Sellers.
Discover award-winning books.
View new releases.
Add discovered books directly to their personal library or TBR.

ISBN and BArcode
Users may eventually be able to add using an ISBN or by scanning a physical book's barcode using their device camera.
The application could use book metadata services to automatically retrive information such as:
Title
Author
Cover
Description
ISBN
Page count
Genres

Digital Reading Services
Future versions may allow users to record or connect access to digital reading servicces such as Kindle, Libby, or orther supported platforms

The feasibility of these intergrations will depend on available APIs and the technical limitaitons of external services.

Additional Features
Potential future features include:
Reading goals
Reading challenges (seasonal, monthly)
Reading statistics
Yearly reading summaries
Book recommendations catered to user.
AI-powered recommendations
Tags and genres
Favorite books
Reading streaks
Notifications
Public/private profiles
All user monthly favorites

7.Non-Functional Requirements
Worms should:
Be responsive on desktop, tablet, and mobile devices.
Provide a simple and intuitive user interface.
Protect user authentication information.
Prevent users from accessing another user’s private library.
Validate user input.
Handle errors.
Be tested before deployment.
Be documented sufficiently for future development.
Be deployed and accessible through the web.

8.Success Criteria
The MVP will be considered successful when a user can:
Create an account.
Log in.
Add books to their library.
Organize books by reading status.
Track reading progress.
Search and filter their library.
Use the TBR randomizer.
Complete a book.
Rate and review a completed book.
Log out securely.

The application should be deployed and usable by someone other than the developer.

9.Project Scope
The initial project will focus on building a reliable individual reading-management application. 
Social networking functionality will be excluded from the MVP to keep the initial scope manageable. The architecture should, however, allow social functionality to be added in a future version.

10.Project Identity
The application will be called “Worms”, comes from the term “bookworm” which is a figurative meaning to describe a person devoted to reading. The name also reflects people who prefer to spend their time with their head in a book.
The visual identity should communicate:
Reading
Books
Organization
Personality
Warmth
The design should avoid looking like a generic productivity dashboard and should instead feel like it is catered and designed specifically to readers.
The library should feel like a personalized digital bookshelf rather than a generic database or productivity dashboard.